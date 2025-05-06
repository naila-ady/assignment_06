"""Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
that allows changing the bank name. Show that it affects all instances."""


class Bank:
    default_bank_name = "Standar Chartered Bank"
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
        return new_name
changed_name=Bank.change_bank_name("Meezan Bank")
changed_name1=Bank.change_bank_name("Faisal Bank")

acc1 = Bank()
acc2 = Bank()


print(f"Your Account1 was in {Bank.default_bank_name} and now shifted to {changed_name}")
print(f"Your Account1 was in {Bank.default_bank_name} and now shifted to {changed_name1}")

