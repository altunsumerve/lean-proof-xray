/-
Kütüphane adları / Library names — verilen modülün ortamındaki bildirimlerden, projeye ait OLMAYANLARIN
adlarını yazar (arac/koni.cpp'nin kayıttan okuduğu yazımla). "Projeye ait" = bildirimin tanımlandığı
modülün adı verilen öneklerden biriyle başlıyor. Önek verilmezse bütün bildirimler kütüphane sayılır
(ör. yalnızca Mathlib'i içe aktarıp bir kayıttaki Mathlib bildirimlerini ayırmak için).
EN: Writes the names of the declarations that do NOT belong to the project (i.e. whose defining module does
    not start with one of the given prefixes), in the spelling arac/koni.cpp reads from the export.

Kullanım / usage (Lake projesinin içinde):
  lake env lean --run kutuphane_adlari.lean cikti.txt Modul [ProjeOneki ...]
-/
import Lean
open Lean

/-- Ad parçası, JSON kaçışlı (kayıttaki yazımıyla aynı). -/
def parca (s : String) : String :=
  let j := (Json.str s).compress
  ((j.toList.drop 1).dropLast).foldl (fun a c => a.push c) ""

def adYaz : Name → String
  | .anonymous => ""
  | .str .anonymous s => parca s
  | .num .anonymous n => "#" ++ toString n
  | .str p s => adYaz p ++ "." ++ parca s
  | .num p n => adYaz p ++ ".#" ++ toString n

def main (args : List String) : IO UInt32 := do
  let cikti := args[0]!
  let modul := args[1]!.toName
  let onekler := (args.drop 2).map String.toName
  initSearchPath (← findSysroot)
  let env ← importModules #[{ module := modul }] {} (trustLevel := 1024)
  let moduller := env.header.moduleNames
  let h ← IO.FS.Handle.mk cikti .write
  let adlar := env.constants.fold (fun a n _ => a.push n) (#[] : Array Name)
  let mut kut := 0
  for n in adlar do
    let projede := match env.getModuleIdxFor? n with
      | some i => onekler.any (fun p => p.isPrefixOf moduller[i.toNat]!)
      | none => false
    if !projede then
      h.putStrLn (adYaz n)
      kut := kut + 1
  IO.println s!"bildirim {adlar.size}, kütüphane {kut}, proje {adlar.size - kut}"
  return 0
