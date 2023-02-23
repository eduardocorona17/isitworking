# age = 12
# if age < 4:
#     print("Free admission.")
# elif age < 18:
#     print("Admission is $25.")
# else:
#     print("Admission is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else: price = 40
print(f"Your admission cost is ${price}")