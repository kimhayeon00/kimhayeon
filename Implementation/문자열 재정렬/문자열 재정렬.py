S = input()
a = 0
answer = [0]*len(S)
result = ""
for i in range(len(S)):
    if ord(S[i]) > 82:
        answer[i] = ord(S[i])  
    else:
        a += int(S[i])

answer.sort()
for i in range(len(answer)):
    result += chr(int(answer[i])) 

result += str(a)

print(result)
