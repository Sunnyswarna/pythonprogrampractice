amount=float(input('enetr the amount'))
if amount<=1000:
    discount= amount*10/100
elif amount>100 and amount>=5000:
    discount=amount *20/100
else:
    discount=amount*30/100
disc_amount= amount-discount
print('pay',disc_amount)
