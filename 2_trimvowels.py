import sys 
str = sys.argv[1]
str_len = len(str)
new_str=""
vowels = ["a","e","o","i","u","A","E","O","I","U"]
for i in range(str_len):
    if str[i] not in vowels:
        new_str=new_str+str[i]
print (new_str)


#new_str = (l for l in str if l not in vowels)
#new_str = ''.join(new_str)