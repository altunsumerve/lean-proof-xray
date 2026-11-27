/-
Dök / Dump — bir modüldeki her bildirimin tipini (ve tanımlarda gövdesini) ağaç olarak JSON'a yazar.
TR: Sözel çevirici (arac/sozel.py) bu dökümü okur; böylece doğal dile çeviri Lean'in okunur yazımına değil,
    çekirdek terimine dayanır: hiçbir argüman, tip ya da üs türü gizlenmez. Ayrıca kullanılan her sabitin
    bağlayıcı türleri (açık / örtük / tip sınıfı) yazılır ki çevirici hangi argümanın gösterileceğini bilsin.
EN: Dumps the type (and for definitions the value) of every declaration of a module as a JSON tree, plus the
    binder kinds of every constant used. The verbaliser works from these kernel terms, not from pretty-printing.

Düğümler / nodes: ["b",i] bvar · ["c",ad] sabit · ["a",f,x…] uygulama · ["l",ad,tür,tip,gövde] lambda ·
  ["p",ad,tür,tip,gövde] ∀/→ · ["z",ad,tip,değer,gövde] let · ["s","Prop"|"Type"] · ["n",sayı] · ["t",metin] ·
  ["j",yapı,i,x] izdüşüm · "…" (bütçe bitti)

Kullanım / usage:  dok <Modul> <cikti.jsonl> [dugum_butcesi] [ek_adlar.txt] [yalniz]
-/
import Lean
open Lean

def bk : BinderInfo → String
  | .default => "e"
  | .implicit => "i"
  | .strictImplicit => "i"
  | .instImplicit => "c"

partial def baglayicilar : Expr → String
  | .forallE _ _ b bi => bk bi ++ baglayicilar b
  | .mdata _ b => baglayicilar b
  | _ => ""

partial def yaz (e : Expr) : StateM Nat Json := do
  let n ← get
  if n == 0 then return Json.str "…"
  set (n - 1)
  match e with
  | .bvar i => return Json.arr #[Json.str "b", toJson i]
  | .const c _ => return Json.arr #[Json.str "c", toJson c.toString]
  | .app .. => do
    let fn := e.getAppFn
    let args := e.getAppArgs
    let jf ← yaz fn
    let mut ja : Array Json := #[Json.str "a", jf]
    for x in args do
      let jx ← yaz x
      ja := ja.push jx
    return Json.arr ja
  | .lam x t b bi => do
    let jt ← yaz t
    let jb ← yaz b
    return Json.arr #[Json.str "l", toJson x.toString, toJson (bk bi), jt, jb]
  | .forallE x t b bi => do
    let jt ← yaz t
    let jb ← yaz b
    return Json.arr #[Json.str "p", toJson x.toString, toJson (bk bi), jt, jb]
  | .letE x t v b _ => do
    let jt ← yaz t
    let jv ← yaz v
    let jb ← yaz b
    return Json.arr #[Json.str "z", toJson x.toString, jt, jv, jb]
  | .sort l => return Json.arr #[Json.str "s", Json.str (match l with | .zero => "Prop" | _ => "Type")]
  | .lit (.natVal k) => return Json.arr #[Json.str "n", toJson k]
  | .lit (.strVal s) => return Json.arr #[Json.str "t", toJson s]
  | .proj s i x => do
    let jx ← yaz x
    return Json.arr #[Json.str "j", toJson s.toString, toJson i, jx]
  | .mdata _ x => yaz x
  | _ => return Json.str "?"

def turAd : ConstantInfo → String
  | .thmInfo _ => "teorem"
  | .defnInfo _ => "tanim"
  | .axiomInfo _ => "aksiyom"
  | .opaqueInfo _ => "opak"
  | .inductInfo _ => "tip"
  | .ctorInfo _ => "kurucu"
  | .recInfo _ => "ozyineleyici"
  | .quotInfo _ => "bolum"

/-- Bir bildirimin döküm satırı ve kullandığı sabitler. -/
def satir (n : Name) (ci : ConstantInfo) (butce : Nat) : Json × Array Name := Id.run do
  let (jt, kalanT) := (yaz ci.type).run butce
  let mut alanlar : List (String × Json) :=
    [("ad", toJson n.toString), ("tur", toJson (turAd ci)), ("b", toJson (baglayicilar ci.type)),
     ("tip", jt), ("tipTam", toJson (kalanT != 0))]
  let mut kul : Array Name := ci.type.getUsedConstants
  match ci with
  | .defnInfo v =>
    let (jv, kalanV) := (yaz v.value).run butce
    alanlar := alanlar ++ [("govde", jv), ("govdeTam", toJson (kalanV != 0))]
    kul := kul ++ v.value.getUsedConstants
  | .inductInfo v =>
    alanlar := alanlar ++ [("kurucular", toJson (v.ctors.map (·.toString)).toArray), ("parametre", toJson v.numParams)]
  | _ => pure ()
  return (Json.mkObj alanlar, kul)

def main (args : List String) : IO UInt32 := do
  let modul := args[0]!.toName
  let cikti := args[1]!
  let butce : Nat := match args[2]? with
    | some s => s.toNat!
    | none => 4000
  initSearchPath (← findSysroot)
  let env ← importModules #[{ module := modul }] {} (trustLevel := 1024)
  let some idx := env.getModuleIdx? modul | throw (IO.userError s!"modül yok: {modul}")
  let mut adlar := (env.header.moduleData[idx.toNat]!).constNames
  -- ek adlar (modül dışından): dördüncü argümandaki dosyada satır başına bir ad.
  -- Beşinci argüman "yalniz" ise modülün kendi bildirimleri dökülmez, yalnızca ek adlar dökülür.
  let ek : Option String := args[3]?
  let yalniz : Option String := args[4]?
  if yalniz == some "yalniz" then
    adlar := #[]
  match ek with
  | some ekYol =>
    let satirlar ← IO.FS.lines (System.FilePath.mk ekYol)
    for s in satirlar do
      let ad := s.toName
      if s != "" && (env.find? ad).isSome && !adlar.contains ad then
        adlar := adlar.push ad
  | none => pure ()
  let h ← IO.FS.Handle.mk cikti .write
  let mut kullanilan : Std.HashSet Name := {}
  let mut dokulen : Std.HashSet Name := {}
  let mut say : Nat := 0
  for n in adlar do
    let some ci := env.find? n | continue
    let (j, kul) := satir n ci butce
    for c in kul do
      kullanilan := kullanilan.insert c
    h.putStrLn j.compress
    dokulen := dokulen.insert n
    say := say + 1
  -- bir tur kapanış: önermelerde adı geçen, tipi Prop olan sabitler (adlandırılmış önermeler) de dökülür
  let mut ekSay : Nat := 0
  for c in kullanilan.toList do
    if dokulen.contains c then continue
    let some ci := env.find? c | continue
    if !ci.type.isProp then continue
    match ci with
    | .defnInfo _ | .inductInfo _ =>
      let (j, kul) := satir c ci butce
      for k in kul do
        kullanilan := kullanilan.insert k
      h.putStrLn j.compress
      dokulen := dokulen.insert c
      ekSay := ekSay + 1
    | _ => pure ()
  -- kullanılan her sabitin bağlayıcı türleri (modül dışındakiler dahil)
  let mut tablo : List (String × Json) := []
  let mut onerme : Array Json := #[]
  for c in kullanilan.toList do
    match env.find? c with
    | some ci =>
      tablo := (c.toString, toJson (baglayicilar ci.type)) :: tablo
      -- tipi sonunda Prop'a varan sabitler (önerme ya da yüklem): cümleye çevirirken → ile fonksiyon tipini ayırmak için
      if ci.type.getForallBody.isProp then
        onerme := onerme.push (toJson c.toString)
    | none => pure ()
  h.putStrLn (Json.mkObj [("baglayici", Json.mkObj tablo), ("onerme", Json.arr onerme)]).compress
  IO.println s!"dökülen {say} + {ekSay} / {adlar.size}, sabit {tablo.length}"
  return 0
