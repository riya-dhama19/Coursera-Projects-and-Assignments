def computepay(h,r):
    if h<=40:
        pay = r
    else:
        pay = h*r
        over = (h-40.0)*(0.5*r)
        pay = pay+over
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)
