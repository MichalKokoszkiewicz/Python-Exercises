dane = bytearray(10)
for i in range(len(dane)):
    dane[i] = len(dane) - i
print(dane)
for i in dane:
    print(i)
