lst = []
d = {}
with open("dataset_3363_3.txt", "r") as file_in:
    for line in file_in:
        lst.extend(line.lower().split())
    for i in lst:
        d.update({i: lst.count(i)})
    common_value = max(d.values())
    print(*min(i for i in d.items() if i[1] == common_value))
