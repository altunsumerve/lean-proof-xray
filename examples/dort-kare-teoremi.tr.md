# İspat künyesi: `Nat.sum_four_squares`

> Deneysel araç. Bu rapor Lean'in kendi dışa aktarım kaydından üretilir; ispatı yeniden doğrulamaz.

## Özet

| | |
|---|---:|
| Tam ispat zinciri (dayandığı her şey) | 12,704 bildirim |
| Önermeyi anlamak için gereken | 214 bildirim (1.7%) |
| Bunlardan okunacaklar (otomatik yardımcılar hariç) | 168 |
| Kullanılan aksiyomlar | 3 |
| Teoremin parmak izi | `f3907f44bbad59b1` |

## Aksiyomlar

- `Classical.choice`
- `Quot.sound`
- `propext`

Yalnızca Lean'in üç standart aksiyomu kullanılıyor (ya da hiçbiri).

## Önermede doğrudan geçenler

Okumaya buradan başlayın; aşağıdaki liste bunların dayandığı her şeyi içerir.

`Eq`, `Exists`, `HAdd.hAdd`, `HPow.hPow`, `Monoid.toNPow`, `NPow.toPow`, `Nat`, `Nat.instMonoid`, `OfNat.ofNat`, `instAddNat`, `instHAdd`, `instHPow`, `instOfNatNat`


## Önermeyi anlamak için okunması gerekenler (tamamı)

### Tanım (106)

`Add.add`, `Array.empty`, `Array.emptyWithCapacity`, `Array.push`, `Array.toList`, `BitVec.ofNat`, `BitVec.toFin`, `BitVec.toNat`, `Bool.decEq`, `ByteArray.empty`, `ByteArray.emptyWithCapacity`, `ByteArray.push`, `Char.val`, `CommMonoid.toMonoid`, `DecidableEq`, `Div.div`, `Eq.ndrec`, `False.elim`, `Fin.Internal.ofNat`, `Fin.val`, `HAdd.hAdd`, `HDiv.hDiv`, `HMod.hMod`, `HMul.hMul`, `HPow.hPow`, `HSub.hSub`, `LE.le`, `LT.lt`, `Lean.Name.mkStr1`, `Lean.Name.mkStr4`, `Lean.SyntaxNodeKind`, `Lean.mkAtom`, `List.append`, `List.brecOn.go`, `List.concat`, `List.flatMap`, `List.flatten`, `List.map`, `List.toByteArray`, `List.toByteArray.loop`, `List.utf8Encode`, `Mod.mod`, `Monoid.toNPow`, `Monoid.toSemigroup`, `Mul.mul`, `NPow.npow`, `NPow.toPow`, `Nat.add`, `Nat.beq`, `Nat.ble`, `Nat.brecOn.go`, `Nat.decLe`, `Nat.decLt`, `Nat.div`, `Nat.div.go`, `Nat.instCommMonoid`, `Nat.instDiv`, `Nat.instMod`, `Nat.instMonoid`, `Nat.isValidChar`, `Nat.lt`, `Nat.mod`, `Nat.modCore`, `Nat.modCore.go`, `Nat.mul`, `Nat.pow`, `Nat.pred`, `Nat.sub`, `NatPow.pow`, `Not`, `OfNat.ofNat`, `One.one`, `One.toOfNat1`, `Pow.pow`, `Semigroup.toMul`, `String.utf8EncodeChar`, `Sub.sub`, `UInt32.isValidChar`, `UInt32.toBitVec`, `UInt32.toNat`, `UInt8.ofNat`, `Unit`, `Unit.unit`, `autoParam`, `dite`, `inferInstance`, `instAddNat`, `instDecidableEqBool`, `instHAdd`, `instHDiv`, `instHMod`, `instHMul`, `instHPow`, `instHSub`, `instLENat`, `instLTNat`, `instMulNat`, `instNatPowNat`, `instOfNatNat`, `instPowNat`, `instSubNat`, `ite`, `namedPattern`, `optParam`, `outParam`, `rfl`

### Tip / yapı (49)

`Add.mk`, `And.intro`, `Array.mk`, `BitVec.ofFin`, `Bool.false`, `ByteArray.IsValidUTF8.intro`, `ByteArray.mk`, `Char.mk`, `CommMonoid.mk`, `Decidable.isFalse`, `Div.mk`, `Eq.refl`, `Exists.intro`, `Fin.mk`, `HAdd.mk`, `HDiv.mk`, `HEq.refl`, `HMod.mk`, `HMul.mk`, `HPow.mk`, `HSub.mk`, `LE.mk`, `LT.mk`, `Lean.Name.anonymous`, `Lean.SourceInfo.original`, `Lean.Syntax.Preresolved.namespace`, `Lean.Syntax.missing`, `List.nil`, `Mod.mk`, `Monoid.mk`, `Mul.mk`, `NPow.mk`, `Nat.le.refl`, `Nat.zero`, `NatPow.mk`, `OfNat.mk`, `One.mk`, `Or.inl`, `PProd.mk`, `PUnit.unit`, `Pow.mk`, `Semigroup.mk`, `String.Pos.Raw.mk`, `String.ofByteArray`, `Sub.mk`, `Substring.Raw.mk`, `True.intro`, `UInt32.ofBitVec`, `UInt8.ofBitVec`

### Teorem (13)

`Nat.div_rec_fuel_lemma`, `Nat.le_of_ble_eq_true`, `Nat.lt_succ_self`, `Nat.mod_lt`, `Nat.mul_assoc`, `Nat.mul_comm`, `Nat.mul_one`, `Nat.not_le_of_not_ble_eq_true`, `Nat.one_mul`, `Nat.pow_pos`, `Nat.pow_zero`, `Nat.zero_lt_succ`, `noConfusion_of_Nat`

## Parmak izleri

Aynı bildirim, aynı kaynaktan üretilen her kayıtta aynı izi verir. Başkasının "doğruladık" dediği kaydın izleriyle karşılaştırarak elinizdeki kodun aynı olduğunu denetleyebilirsiniz.

| bildirim | tür | önerme izi | tanım izi |
|---|---|---|---|
| `Nat.sum_four_squares` | thm | `f3907f44bbad59b1` | `-` |
| `Add.add` | def | `f31ed7f0b616ab77` | `f4ee1a92c38e5c9b` |
| `Add.mk` | ctor | `8e88db86150d3f7f` | `-` |
| `And.intro` | ctor | `3ca040d9e40aabb3` | `-` |
| `Array.empty` | def | `bcd190238d2b2faa` | `3b27fbef808d40ac` |
| `Array.emptyWithCapacity` | def | `f40f078a90343556` | `148443f59980294e` |
| `Array.mk` | ctor | `73910e22fef87d5a` | `-` |
| `Array.push` | def | `fdc01471a16e8006` | `04acb13dc2146cc1` |
| `Array.toList` | def | `e760e998060c8bff` | `4aad983c86194926` |
| `BitVec.ofFin` | ctor | `6126ab360ec1e2cb` | `-` |
| `BitVec.ofNat` | def | `cb2ed839094baa73` | `f8305be2591a13bd` |
| `BitVec.toFin` | def | `f032b864f324be88` | `a905596a650268de` |
| `BitVec.toNat` | def | `1598cd883a6c2ca0` | `17f88c997042b61b` |
| `Bool.decEq` | def | `17043fa5b252bb0d` | `88bda83f8537df7f` |
| `Bool.false` | ctor | `9053fbfb20ed4c50` | `-` |
| `ByteArray.IsValidUTF8.intro` | ctor | `23a1b75b4d76e1dd` | `-` |
| `ByteArray.empty` | def | `1ace6af7f06f6e20` | `63ed999ed8ba706d` |
| `ByteArray.emptyWithCapacity` | def | `23dcd732cad2eb2b` | `2a84e356004ddc5c` |
| `ByteArray.mk` | ctor | `761cf52237e8bf9f` | `-` |
| `ByteArray.push` | def | `5d17a40d1463bd96` | `5942f536eb6d4fc9` |
| `Char.mk` | ctor | `4474d828d2542ac5` | `-` |
| `Char.val` | def | `42d12e4b3c25dee2` | `5afdee69866445c9` |
| `CommMonoid.mk` | ctor | `9adef4f609c0f1bb` | `-` |
| `CommMonoid.toMonoid` | def | `b8e96bee7c559caf` | `4642d5d041dd91b3` |
| `Decidable.isFalse` | ctor | `425917dafceea8ce` | `-` |
| `DecidableEq` | def | `5c2a8c29b2748cda` | `fa843f185d2bffce` |
| `Div.div` | def | `81008e41dc8e8430` | `997f052f9aeca014` |
| `Div.mk` | ctor | `d2f45327cf237b47` | `-` |
| `Eq.ndrec` | def | `05e212166f2e4df4` | `e03519b7b524a7cc` |
| `Eq.refl` | ctor | `e299d10a76c8ddc7` | `-` |
| `Exists.intro` | ctor | `6c60a78e1da1daff` | `-` |
| `False.elim` | def | `84dc3b0f52bbd009` | `a11e357c2dc9a447` |
| `Fin.Internal.ofNat` | def | `75e95febfc1a710d` | `932b34b8879b0af7` |
| `Fin.mk` | ctor | `10855fc006b5977e` | `-` |
| `Fin.val` | def | `74943ec71c25b8ff` | `672426a13ecb2749` |
| `HAdd.hAdd` | def | `057c4618deb53f57` | `7963a46b08694ecf` |
| `HAdd.mk` | ctor | `354f6eac0eab074d` | `-` |
| `HDiv.hDiv` | def | `2cb743c795bac3f4` | `c458a0afdaef1cc8` |
| `HDiv.mk` | ctor | `c0fe526cdbf34a3d` | `-` |
| `HEq.refl` | ctor | `97ef0403c4fb58ff` | `-` |
| `HMod.hMod` | def | `ae5a8031744c7d54` | `21d8e7b4f38c821a` |
| `HMod.mk` | ctor | `4b3658157f2dcfac` | `-` |
| `HMul.hMul` | def | `73e6ecff4d98bbac` | `14e924fc678ae063` |
| `HMul.mk` | ctor | `fd3510d1dddfe2ab` | `-` |
| `HPow.hPow` | def | `417151e0357363b5` | `57871f149cdf545f` |
| `HPow.mk` | ctor | `0c0b2c7e611197da` | `-` |
| `HSub.hSub` | def | `4a281661bd804590` | `d7122140b95b6ff8` |
| `HSub.mk` | ctor | `e8e8d31361a583ba` | `-` |
| `LE.le` | def | `05a50d55392d44d6` | `317992e218a4176c` |
| `LE.mk` | ctor | `aa46f53812c508c3` | `-` |
| `LT.lt` | def | `774cf4c917aad0b0` | `38db73040628d572` |
| `LT.mk` | ctor | `bfce994f20f75a98` | `-` |
| `Lean.Name.anonymous` | ctor | `aa04a200720a508c` | `-` |
| `Lean.Name.mkStr1` | def | `eef91eb1d914ba53` | `dc8bf80299802c1c` |
| `Lean.Name.mkStr4` | def | `1a5299b12854c028` | `bcf7ea8801f27b40` |
| `Lean.SourceInfo.original` | ctor | `8f952bde58ea81cd` | `-` |
| `Lean.Syntax.Preresolved.namespace` | ctor | `c5974bd3d237931f` | `-` |
| `Lean.Syntax.missing` | ctor | `d38f63b802d872b0` | `-` |
| `Lean.SyntaxNodeKind` | def | `36b3566cba0b3215` | `743b996f28a3c556` |
| `Lean.mkAtom` | def | `e0e695d79d08284e` | `151a836e94d4b18e` |
| `List.append` | def | `7eb3758bbca9aeb5` | `7cb3c360e94a2aac` |
| `List.brecOn.go` | def | `eb871bc292c89b8e` | `063d2bc5b151d96d` |
| `List.concat` | def | `5a61e69343b0b815` | `72a7a696ccdb534a` |
| `List.flatMap` | def | `9a73fc39a9d307f3` | `176e1fae117b88ca` |
| `List.flatten` | def | `52072c9ea2937060` | `3e0a0c86f56683db` |
| `List.map` | def | `8a934be32dd9a95d` | `094b2722804141c3` |
| `List.nil` | ctor | `482aeca93c56465a` | `-` |
| `List.toByteArray` | def | `c4c7754775fbabc6` | `779752d63d1554e3` |
| `List.toByteArray.loop` | def | `fa7c2fe1641db63c` | `684cb3d4afa89d00` |
| `List.utf8Encode` | def | `64eb92803b033f84` | `c946a31741665eaf` |
| `Mod.mk` | ctor | `c0ffbeed95ce0198` | `-` |
| `Mod.mod` | def | `58c45acee1de3ab6` | `0a57961cbea7cc54` |
| `Monoid.mk` | ctor | `b5b8e0317a7f0546` | `-` |
| `Monoid.toNPow` | def | `2246d27313689231` | `92fb5cddae2dc4c7` |
| `Monoid.toSemigroup` | def | `8d7a38d981e2d55a` | `a850486e2108b68e` |
| `Mul.mk` | ctor | `aea500773d80ae5f` | `-` |
| `Mul.mul` | def | `a328411d6b246053` | `ecd6bab52a71bd72` |
| `NPow.mk` | ctor | `501827f88f20bdf9` | `-` |
| `NPow.npow` | def | `0f05a5b315366b78` | `70e7e04467643d0a` |
| `NPow.toPow` | def | `6e07d72e2c299f1f` | `1d184f187cc87f55` |
| `Nat.add` | def | `c7d99daff6608d31` | `f796c54c9fe945ca` |
| `Nat.beq` | def | `9046df0b24894e77` | `d91347fc8c744fb0` |
| `Nat.ble` | def | `9046df0b24894e77` | `e3655d94b449156d` |
| `Nat.brecOn.go` | def | `0752578dd097ba54` | `71463fce2144f229` |
| `Nat.decLe` | def | `ab2c38f551434461` | `778ec9a134053d6a` |
| `Nat.decLt` | def | `c0f9d43541a446f4` | `9e63642b957cbdcf` |
| `Nat.div` | def | `c7d99daff6608d31` | `615d35676dfdc885` |
| `Nat.div.go` | def | `e4eb7f5a486941d0` | `6a794e50d2160bd7` |
| `Nat.div_rec_fuel_lemma` | thm | `ec3d3a91f16fc5ce` | `-` |
| `Nat.instCommMonoid` | def | `9efa455ef1ae8789` | `e02121f1ac65fc8d` |
| `Nat.instDiv` | def | `e0223b735791d22c` | `3dfbfff89593a48d` |
| `Nat.instMod` | def | `6e4e33d9d993bb51` | `5b15cdc378b5334d` |
| `Nat.instMonoid` | def | `317784543ea86ab3` | `9d5cd90a7d8e9d5c` |
| `Nat.isValidChar` | def | `19369973e10d845f` | `ce2654b34e896ede` |
| `Nat.le.refl` | ctor | `6045dfd3916140a6` | `-` |
| `Nat.le_of_ble_eq_true` | thm | `41e4e56153e15ded` | `-` |
| `Nat.lt` | def | `0ea2bd1a994b5185` | `800c5308473271bb` |
| `Nat.lt_succ_self` | thm | `bb8a4d833cb1d9e6` | `-` |
| `Nat.mod` | def | `c7d99daff6608d31` | `9969d7293dfc896e` |
| `Nat.modCore` | def | `c7d99daff6608d31` | `6b236d26d38b89ef` |
| `Nat.modCore.go` | def | `e4eb7f5a486941d0` | `799213b01e50e2ab` |
| `Nat.mod_lt` | thm | `10f0ed63531c7248` | `-` |
| `Nat.mul` | def | `c7d99daff6608d31` | `7c1cbf620c2d1083` |
| `Nat.mul_assoc` | thm | `6d8010ce1c6a8670` | `-` |
| `Nat.mul_comm` | thm | `a886f23747ad86e0` | `-` |
| `Nat.mul_one` | thm | `ebd45d629e84e0d8` | `-` |
| `Nat.not_le_of_not_ble_eq_true` | thm | `4a3169923ed46254` | `-` |
| `Nat.one_mul` | thm | `40db331ca1329822` | `-` |
| `Nat.pow` | def | `c7d99daff6608d31` | `7fbb4c36f74b6b39` |
| `Nat.pow_pos` | thm | `305732cb9e41739a` | `-` |
| `Nat.pow_zero` | thm | `d5c5fdcede00304c` | `-` |
| `Nat.pred` | def | `7cc95a8d2bc28183` | `b1e85d91b6de7cb7` |
| `Nat.sub` | def | `c7d99daff6608d31` | `6caeab050a95c6c0` |
| `Nat.zero` | ctor | `ba582b761acb3e64` | `-` |
| `Nat.zero_lt_succ` | thm | `6fc891c463decc78` | `-` |
| `NatPow.mk` | ctor | `50a69381d51ac92a` | `-` |
| `NatPow.pow` | def | `dea119acc9f4bb54` | `e792167a3d449d17` |
| `Not` | def | `af52bf68e0fcc9a1` | `4d2c1f8beef730b7` |
| `OfNat.mk` | ctor | `02dc5bb76cae307b` | `-` |
| `OfNat.ofNat` | def | `0952fce854adee73` | `75a34549d8266184` |
| `One.mk` | ctor | `5c179e47b2cd6e29` | `-` |
| `One.one` | def | `be5069001be5fd2d` | `d515546d2626b88e` |
| `One.toOfNat1` | def | `088b594cf346088a` | `cf084147dea4a964` |
| `Or.inl` | ctor | `16b85aefbf24a520` | `-` |
| `PProd.mk` | ctor | `ebbd630e4ff1f80e` | `-` |
| `PUnit.unit` | ctor | `91d731f00d202102` | `-` |
| `Pow.mk` | ctor | `87c195414f3bb143` | `-` |
| `Pow.pow` | def | `a874e200de434cee` | `4804b8240bd8a56b` |
| `Semigroup.mk` | ctor | `860d61b0fb0a83dc` | `-` |
| `Semigroup.toMul` | def | `f0699533e0c6cf7b` | `f73b38e6e1c07d7b` |
| `String.Pos.Raw.mk` | ctor | `3dd76bdf56223bbc` | `-` |
| `String.ofByteArray` | ctor | `8d7f0f82c0c871d7` | `-` |
| `String.utf8EncodeChar` | def | `f14c21c34ff17ffc` | `f8cdcbe22bc40d4f` |
| `Sub.mk` | ctor | `e461fdd1a30366be` | `-` |
| `Sub.sub` | def | `6de166b873baf3a1` | `81a3064f2cfb648c` |
| `Substring.Raw.mk` | ctor | `606135ab632ce055` | `-` |
| `True.intro` | ctor | `c85f5b3d0164e5e9` | `-` |
| `UInt32.isValidChar` | def | `63af1cabc492b3f1` | `1d84e5c2a0558747` |
| `UInt32.ofBitVec` | ctor | `51a21c1222c53772` | `-` |
| `UInt32.toBitVec` | def | `3c4efdddc52188ed` | `0bbc6320fd1ef857` |
| `UInt32.toNat` | def | `13336ddbd292f1bf` | `4a79aa8519c36999` |
| `UInt8.ofBitVec` | ctor | `e6896d6d1eceeb1c` | `-` |
| `UInt8.ofNat` | def | `d0d071bd4a8e8af1` | `825628236810d794` |
| `Unit` | def | `36b3566cba0b3215` | `c5b811f0a6d6f1c3` |
| `Unit.unit` | def | `d19171799396e6a6` | `ab02b6e2d0341b28` |
| `autoParam` | def | `724dc65a211f861c` | `768f378a4e7b4df3` |
| `dite` | def | `8236f9570d38d3da` | `6f75b0165575c2bf` |
| `inferInstance` | def | `52cb78377ad8ad33` | `50ae945320322d16` |
| `instAddNat` | def | `21839be0a10b07f4` | `9a1f9079739bc134` |
| `instDecidableEqBool` | def | `17e68d7442e038f0` | `331ad7225c1a1265` |
| `instHAdd` | def | `3d9eb82e2981b2e2` | `5a00fe0158ca317c` |
| `instHDiv` | def | `32c59d7b26655bbd` | `1c7a7037177805f9` |
| `instHMod` | def | `207aee3f8c581426` | `826d475f38ce2c3b` |
| `instHMul` | def | `3fc1d84569c17f64` | `6fc9f66a7c1b7082` |
| `instHPow` | def | `21d2931176fc4a3c` | `297a5c1a2e881cae` |
| `instHSub` | def | `8ea23234822b64e5` | `a4c831aa7ee8ba86` |
| `instLENat` | def | `b2e9cbbb5e3cf5d7` | `5aa3ae3faddd55c9` |
| `instLTNat` | def | `b22fb73522afe2e8` | `63a4b1c6e05ec321` |
| `instMulNat` | def | `1a340a410cdab173` | `7f459f1c503c1d51` |
| `instNatPowNat` | def | `3b8e94323c32b05e` | `bcd854a6de17f8ef` |
| `instOfNatNat` | def | `3a47c327b5cc7084` | `ed925866f901ddd8` |
| `instPowNat` | def | `ed31d247b4619c17` | `a0bdaef9bfccd91d` |
| `instSubNat` | def | `3d8be27ff0a29594` | `f8483620dc396af4` |
| `ite` | def | `8a24659d042e3089` | `cfa92c14a30c43f3` |
| `namedPattern` | def | `c4ef2d441ac93f65` | `d1c00bd236fdc6d7` |
| `noConfusion_of_Nat` | thm | `b9c8a22090f42db5` | `-` |
| `optParam` | def | `03c2ef5caa5f8fd8` | `a4436603ffd3cf49` |
| `outParam` | def | `3e438ebdefc3369b` | `dc3c341b691d253c` |
| `rfl` | def | `d4f2038b0e11fad3` | `46fbff2eef527852` |
