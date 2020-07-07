import re

with open("dataset_3363_2.txt", "r+") as file_in, open("out.txt", "w") as file_out:
    a = re.split(r"(\d+)", file_in.readline())[
        :-1
    ]  # Разделяет по цифрам в список и присваивает все элементы кроме последнего
    result = "".join([y * int(x) for x, y in zip(a[1::2], a[::2])])
    file_out.write(result)
