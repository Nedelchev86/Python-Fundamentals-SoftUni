text = input()
result = ""
for i in range(len(text)-1):
    if text[i] != text[i+1]:
        result += text[i]

if text and result:
    if text[-1] != result[-1]:
        result += text[-1]
if not result and text:
    print(text[0])
else:
    print(result)
