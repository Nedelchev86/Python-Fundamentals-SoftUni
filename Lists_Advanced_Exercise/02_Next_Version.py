# version_list = [int(x) for x in input().split(".")]
# version_list[-1] += 1
# for i in range(len(version_list) - 1 , -1, -1):
#     if version_list[i] == 10:
#         version_list[i] = 0
#         version_list[i-1] += 1
#
#     else:
#         break
# version_list = [str(x) for x in version_list]
# print(".".join(version_list))

version = "".join(input().split("."))
next_version = int(version) + 1
print(".".join(str(next_version)))
