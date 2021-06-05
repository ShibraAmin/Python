for  num in range(1, 11, 3): #starting, to n-1, steps size
    print(num)

total=0
for number in range(1,101):
    total +=number
print(total)

#sum of all even numbers
sum=0
for n in range(2,101,2):
    sum+=n
print(sum)

#or

sum2=0
for n in range(1,101):
    if n%2==0:
        sum2+=n

print(sum2)
