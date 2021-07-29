my_Number = int (input("Enter your Number: "))

def division (num):
    flag = 0
    ret_val = num
    if num % 3 == 0:
        flag += 1
        ret_val = "Fizz"
    if num % 5 == 0:
        flag += 1
        ret_val = "Buzz"
    if flag == 2:
        ret_val ="FizzBuzz"
    return ret_val

print (division(my_Number))