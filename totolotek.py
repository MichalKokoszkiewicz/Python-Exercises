wylosowane = [1, 11, 15, 23, 35, 47]
# import random
# wylosowane = random.sample(range(1, 50), 6)
# wylosowane.sort()
# print(wylosowane)

wybrane = []
for i in range(6):
    wybrane.append(int(input("\"Skreśl\" liczbę: ")))

trafione = []
for i in wybrane:
    if i in wylosowane:
        trafione.append(i)

print("trafiłeś", str(len(trafione)), "liczb:", str(trafione))
