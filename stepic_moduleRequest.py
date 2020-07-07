import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.2/854.txt")
lines = 0
for i in r.text.splitlines():  # считаем строки в файле
    lines += 1
print(lines)
