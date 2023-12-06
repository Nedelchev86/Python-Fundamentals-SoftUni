# text = input()
#
# for i in range(0, len(text)):
#     if text[i] == ":" and  i < len(text) - 1:
#         print(text[i]+text[i+1])

#
text = input()

for i in range(0, len(text)):
    if text[i] == ":" and  i < len(text) - 1:
        print(text[i]+text[i+1])


# Test
text = input()
print("\n".join([ text[x]+text[x+1] for x in range(len(text)) if text[x] == ":" ]))