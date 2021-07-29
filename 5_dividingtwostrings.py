import sys
a = sys.argv[1]
b = sys.argv[2]
def divide_strings(a, b):
    a_len = int(len(a)/2)
    b_len = int(len(b)/2)
    if len(a) % 2 == 0:
        a_front = a[0:a_len]
        a_back = a[a_len:]
    else:
        a_front = a[0:a_len + 1]
        a_back = a[a_len+ 1:]
    if len(b) % 2 == 0:
        b_front = b[0:b_len]
        b_back = b[b_len:]
    else:
        b_front = b[0:b_len + 1]
        b_back = b[b_len + 1:]
    return a_front + b_front + a_back + b_back

print (divide_strings(a,b))