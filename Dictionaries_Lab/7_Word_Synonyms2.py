number = int(input())
my_dict = {}

for i in range(number):
    word, synonym = input(), input()
    if word not in my_dict.keys():
        my_dict[word] = []
    my_dict[word].append(synonym)

print('\n'.join([F"{key} - {', '.join(value)}" for key, value in my_dict.items()]))