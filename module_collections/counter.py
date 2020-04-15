from collections import Counter

c = Counter(a=3, b=31)
d = Counter(a=1, b=2)
print(c+d)
print(c-d)
print(c & d)  # пересечение: min(c[x], d[x])
print(c | d)  # обьединение: max(c[x], d[x])

f = Counter()
f[92] = -10
f[92] += 1
f.update([92])
f.update(['Freedom'])
f.update(['Freedom'])
print(f)








