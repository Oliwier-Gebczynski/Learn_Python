def rgb(r, g, b):
    r_hex = ''
    g_hex = ''
    b_hex = ''

    if r == '':
        r_hex = '00'
    elif r >= 255:
        r_hex = 'FF'
    elif (r < 255) and (r > 0):
        if r < 10:
            r_hex = hex(r)
            r_hex = f"0{r_hex[2].upper()}"
        else:
            r_hex = hex(r)
            r_hex = (r_hex[2] + r_hex[3]).upper()
    elif 0 >= r:
        r_hex = '00'

    if g == '':
        g_hex = '00'
    elif g >= 255:
        g_hex = 'FF'
    elif (g < 255) and (g > 0):
        if g < 10:
            g_hex = hex(g)
            g_hex = f"0{g_hex[2].upper()}"
        else:
            g_hex = hex(g)
            g_hex = (g_hex[2] + g_hex[3]).upper()
    elif 0 >= g:
        g_hex = '00'

    if b == '':
        b_hex = '00'
    elif b >= 255:
        b_hex = 'FF'
    elif (b < 255) and (b > 0):
        if b < 10:
            b_hex = hex(b)
            b_hex = f"0{b_hex[2].upper()}"
        else:
            b_hex = hex(b)
            b_hex = (b_hex[2] + b_hex[3]).upper()
    elif 0 >= b:
        b_hex = '00'

    result = r_hex + g_hex + b_hex
    print(f"R {r_hex}, G {g_hex}, B {b_hex} | Result: {result}")

    return result


rgb(254, 253, 252)
rgb(-20, 275, 125)
rgb(1,2,3)

