transactionAmount=float(input('Please enter how much you paid'))
amountPaid=float(input('Enter the amount that you paid'))
changeDue = amountPaid - transactionAmount
print("Change due is $" + str(changeDue))
print('You need', int(changeDue/20), "- $20")
changeDue = (changeDue%20)
print('You need', int(changeDue/10), "- $10")
changeDue = (changeDue%10)
print('You need', int(changeDue/5), "- $5")
changeDue = (changeDue%5)
print('You need', int(changeDue/1), "- $1")
changeDue = (changeDue%1)
print('You need', int(changeDue/0.25), "- $0.25")
changeDue = (changeDue%0.25)
print('You need', int(changeDue/0.10), "- $0.10")
changeDue = (changeDue%0.10)
print('You need', int(changeDue/0.05), "- $0.05")
changeDue = (changeDue%0.05)
print('You need', int(changeDue/0.01), "- $0.01")
changeDue = (changeDue%0.01)









