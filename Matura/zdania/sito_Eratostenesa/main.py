zbior_liczb = []

for item in range(199):
    zbior_liczb.append(item+2)

for item in zbior_liczb:
    pierwsza = item

    for element in zbior_liczb:
        if element is not pierwsza:
            if element%pierwsza == 0:
                zbior_liczb.remove(element)


print(zbior_liczb)
