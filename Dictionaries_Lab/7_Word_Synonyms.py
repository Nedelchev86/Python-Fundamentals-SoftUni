number = int(input())
my_dict = {}

for i in range(number):
    word = input()
    synonym = input()
    if word not in my_dict.keys():
        my_dict[word] = []
    my_dict[word].append(synonym)

for i in my_dict:
    print(F"{i} - {', '.join(my_dict[i])}")
