
arr = []
n_elements = int (input ("Enter number of array elements: "))
print ("Enter your elements")
for i in range(0,n_elements):
    ele=int(input())
    arr.append(ele)

def function_arr (arr):
    result = []
    for j in arr:
        if j not in result:
            result.append(j)
    return result

print (function_arr(arr))