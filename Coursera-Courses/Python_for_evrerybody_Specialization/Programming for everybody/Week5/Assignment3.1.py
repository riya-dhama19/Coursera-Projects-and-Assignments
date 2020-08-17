hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs<=40 :
    pay = rate*hrs
    print(pay)
else:
    pay = hrs*rate
    over = (hrs-40.0) * (rate*0.5)
    pay = pay + over
    print(pay)
