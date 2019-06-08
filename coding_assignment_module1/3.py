def binarySearch(arr, beg, end, pos):
    while(beg<=end):
        mid = (beg+end)//2

        if (arr[mid] == pos):
            return mid
        elif (arr[mid] < pos):
            beg = mid+1
        else:
            end = mid-1
    return -1


arr = input("Enter a list of numbers separated by commas").split(",")
arr = [int(x) for x in arr]
arr.sort()

pos = int(input("Enter number to be searched for "))

ans = binarySearch(arr, 0, len(arr)-1, pos)

if (ans != -1):
	print("Element is present at index", arr.index(pos))
else:
	print("Element is not present in array")
