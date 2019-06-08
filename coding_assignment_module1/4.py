num = int(input("Enter a number: "))
rest = num
sum = 0

while (rest):
    sum += (rest%10)
    rest = (rest - (rest%10))/10

sum = int(sum)
print(sum)
