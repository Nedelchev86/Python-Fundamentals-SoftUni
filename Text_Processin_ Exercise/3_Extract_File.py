# text = input().split("\\")
# selected_last_index = text[-1].split(".")
# name , extension = selected_last_index
#
# print(F"File name: {name}")
# print(F"File extension: {extension}")


text = input().split("\\")
name , extension = text[-1].split(".")

print(F"File name: {name}\nFile extension: {extension}")



