
length = int (input("Enter array length: "))
start = int (input("Enter array start: "))

def create_arr (start,length):
    arr = []
    i=1
    for i in range(length):
        arr.append(start)
        start +=1
    return arr

print (create_arr(start,length))