# with open("dataset_3363_4.txt", "r", encoding="utf8") as list_of_names, open(
#     "out.txt", "w", encoding="utf8"
# ) as outFile:
#     sum = 0
#     sum2 = 0
#     marks = []
#     result_avg = []
#     for line in list_of_names:
#         one_line = line.strip().split(";")
#         one_line = one_line[1:]
#         marks.append(one_line)
#         for i in range(len(one_line)):
#             sum += int(one_line[i])
#             avg = sum / len(one_line)
#         outFile.write(str(avg) + "\n")
#         sum = 0
#         avg = 0
#     for j in range(len(marks[0])):
#         for i in range(len(marks)):
#             sum2 += int(marks[i][j])
#         avg2 = sum2 / len(marks[0])
#         result_avg.append(avg2)
#         sum2 = 0
#         avg2 = 0
#     outFile.write(str(result_avg))

averages = []
marks_math = []
marks_phys = []
marks_rus = []
counter = 0
value01 = 0
value02 = 0
value03 = 0

with open("dataset_3363_4.txt") as in_f_obj:

    for line in in_f_obj:
        line = line.rstrip().split(";")
        student_average = (int(line[1]) + int(line[2]) + int(line[3])) / 3
        averages.append(student_average)
        marks_math.append(int(line[1]))
        marks_phys.append(int(line[2]))
        marks_rus.append(int(line[3]))
        counter += 1

with open("out.txt", "w") as out_f_obj:

    for _ in averages:
        out_f_obj.write(str(_) + "\n")

    for _ in marks_math:
        value01 += int(_)
    for _ in marks_phys:
        value02 += int(_)
    for _ in marks_rus:
        value03 += int(_)
    average_math = value01 / counter
    average_phys = value02 / counter
    average_rus = value03 / counter

    out_f_obj.write(
        str(average_math) + " " + str(average_phys) + " " + str(average_rus)
    )
