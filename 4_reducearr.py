
arr = []
n_elements = int (input ("Enter no of elements: "))
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