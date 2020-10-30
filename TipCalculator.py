
bill = round(float(input("Input the bill(as a decimal number): ")), 2)
print("Your bill is ${:.2f}".format(bill))

tip = round(bill * .15, 2)
total = bill + tip
print("A 15 percent tip would be ${:.2f} for a total of ${:.2f}.".format(tip, total))

splitAmount = int(input("How many ways would you like to split the bill: "))
owedPerPerson = total/splitAmount
print("Split {} ways, each person owes ${:.2f}.".format(splitAmount, owedPerPerson))

billRoundedUp = int(total) + 1
forCharity = billRoundedUp - total
print("If you choose to round up for charity, your bill will be: ${} and there will be ${:.2f} given to charity."
      .format(billRoundedUp, forCharity))
      



