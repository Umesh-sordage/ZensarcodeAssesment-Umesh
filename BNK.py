from BankPackage import BankInfo as BNK

acct1 = BNK.Account(5000, "Sachin")

acct1.Deposit(1000)
acct1.Withdrawal(2000)

print(acct1)
print(f"acct1:{type(acct1)}")


acct2 = BNK.Account(3000, "Ali")
acct2.Deposit(500)
acct2.Withdrawal(250)
print(acct2)

if(acct1 == acct2):

    print("Thay have equal balance")
else:
    print("Thay have different balance")

if(acct1 != acct2):
    print("Oops!!! they are not equal")

else:
    print("wow!!! they are equal")

if (acct2.balance > acct1.balance):
    print("acct2 should pay more tax")
else:
    print("acct1 should pay normal tax")

if (acct1.balance < acct2.balance):
    print("Sponsor for two children")

else:
    print("Start an Orphanage")

if (acct2.balance >= acct1.balance):
    print("Go On Europe Trip")
else:
    print("Go for an excursion")

if (acct1.balance <= acct2.balance):
    print("we can have coffee")
else:
    print('we can have meal')

acct1.AddNominee("Ranjini")
acct1.AddNominee("Rajini")
acct1.AddNominee("Malini")
acct1.AddNominee("Rukmini")

print(len((acct1.nominee)))
print(len(acct1))

for nom in acct1:
    print(nom)