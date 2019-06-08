num_list = input("Enter a set of numbers(separated by commas)").split(",")
flag = 0
i = 0

num_list = [int(x) for x in num_list] #Converting the strings into integer values

i = 0
while(i<len(num_list)):
    if (num_list[i]>237):
        break
    elif (num_list[i]%2 == 0):
        print(num_list[i])
    i = i+1
