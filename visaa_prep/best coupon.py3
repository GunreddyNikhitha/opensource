bill_price=int(input())
discount_1=bill_price*0.1
discount_2=100
if discount_1>=discount_2:
    final_price = bill_price-discount_1
else:
    final_price=bill_price-discount_2
print(int(final_price))
