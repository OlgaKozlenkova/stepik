d = int(input())
words = {input().lower() for _ in range(d)}
num_str = int(input())
lines = []
new_words = set()
for i in range(num_str):
    a = input().lower().split()
    lines.append(a)
for i in range(len(lines)):
    new_words.update(lines[i])
a = new_words - words
print(*a, sep="\n")
