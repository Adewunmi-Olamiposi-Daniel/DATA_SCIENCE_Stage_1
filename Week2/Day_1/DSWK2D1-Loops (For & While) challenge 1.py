#challenge 1

num=int(input("Please, enter a number to start countdown: "))

while num >0:
    print(num)
    num-=1
print("Times up!")

#challenge 2
#multiplication table generator
number=int(input("Enter your number for multiplication: "))

for i in range(1,13):
    print(f"{number} x {i} = {number* i}")