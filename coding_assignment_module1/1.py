num_list = input("Enter a sequence of numbers separated by commas").split(",")
num_list = [int(x) for x in num_list] #Converting the strings into integer values
print("List: ", num_list)
print("Tuple: ", tuple(num_list))
