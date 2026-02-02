total = int(input("The total is: "))
paid = int(input("The amount paid is: "))
change = paid - total
temp = change

w=0
y=0
z=0

if paid > 10000 or total > 10000:
    print("The value paid or the total value can't be over 10.000")

elif change < 0:
    print("The value paid is inferior to the total")

else:

    if temp > 99:
        for a in range(100):
            if temp > 99:
                temp= temp-100
                w += 1
            else:
                continue

    if temp<100 and temp>9:
        for b in range(10):
            if temp<100 and temp>9:
                temp= temp-10
                y +=1 
            else:
                continue
            
    if temp<10 and temp >0:
        for c in range(10):
            if temp<10 and temp>0:
                temp= temp-1
                z +=1
            else:
                continue

    print("The change is: ",change)
    print(f"\n{w} 100$ bills\n{y} 10$ bills\n{z} 1$ bills")