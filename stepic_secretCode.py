# string = str(input())
# code = str(input())
# new_string = str(input())
# new_code = str(input())
# new_string_list = []
# new_code_list = []
# string_list = []
# code_list = []
# a_list = ""
# cd_list = ""
# for i in range(len(string)):
#     string_list.append(string[i])
# for j in range(len(code)):
#     code_list.append(code[j])
# crypt = dict(zip(string_list, code_list))
# print(crypt)
# for x in range(len(new_string)):
#     new_string_list.append(new_string[x])
# for y in range(len(new_string)):
#     new_code_list.append(new_code[y])
# for key, value in crypt.items():
#     for letter in new_string_list:
#         if crypt[key] == letter:
#             # a_list.append(crypt[value])
#             print("".join(crypt[value]), end="")
#     for cd in new_code_list:
#         if crypt[value] == cd:
#             # cd_list.append(crypt[key])
#             print("".join(crypt[key]))
#

key, value, str1, str2 = list(input()), list(input()), list(input()), list(input())
for i in str1:
    print(
        value[key.index(i)], end=""
    )  # Для каждой буквы списка str1, выводим то значение Value,которое соответствует Key
print()
for j in str2:
    print(
        key[value.index(j)], end=""
    )  # Для каждой буквы списка str2, выводим то значение Key,которое соответствует Value
print()
