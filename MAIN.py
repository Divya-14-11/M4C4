num = input("enter a number:")
numofdigit = len(num)
print(f"the number of digit in {num} is {numofdigit}")
tempory=int(num)
sum=0
while tempory>0:
    digit=tempory%10
    sum+=digit**numofdigit
    tempory=tempory//10
if int(num)==sum:
    print("IT IS AN AMSTRUNG NUMBER ")
else:
    print("IT IS NOT AN AMSTRUNG NUMBER")