def reverseString (string):
    string = string [::-1]
    return string

string = input("Enter your String: ")
print ("Reversed string is: ",end="")
print (reverseString(string))  