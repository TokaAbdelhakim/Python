import sys
word = sys.argv[1]
char = sys.argv[2]
word_len = len(word)
result = []
for i in range(word_len):
    if char == word[i]:
        result.append(i)
        
print (result)
