romannumber=input("enter a roman number")
roman={
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}
number=0
for i in range(0,len(romannumber)-1):
    if roman[romannumber[i]]<roman[romannumber[i+1]]:
        number-=roman[romannumber[i]]
    else:
        number+=roman[romannumber[i]]
print(f"THE NUMBERIC IS {number+roman[romannumber[-1]]}")