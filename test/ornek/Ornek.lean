/-!
Küçük sınama projesi / Small test project.
`ana_teorem`: tam ispatlı. `eksik_teorem`: bilerek `sorry` içerir; künye bunu yakalamalı.
`ana_teorem` is fully proved; `eksik_teorem` deliberately uses `sorry` and the passport must flag it.
-/
namespace Ornek

/-- Bir sayı çifttir: iki katı olarak yazılabilir. / A number is even if it is twice something. -/
def Cift (n : Nat) : Prop := ∃ k, n = 2 * k

theorem ana_teorem (n : Nat) : Cift (2 * n) := ⟨n, rfl⟩

theorem eksik_teorem (n : Nat) : Cift (n + n) := by sorry

end Ornek
