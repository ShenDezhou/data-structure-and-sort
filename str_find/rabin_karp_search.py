a = "1239391021933486774883912958"
b = "86774"

def rabin_karp_search(a, b):
    mod = 13
    na = len(a)
    nb = len(b)
    hb = int(b) % mod
    print(hb)
    # build a module list a_mod
    a_mod = []
    for i in range(na - nb):
        ha_part = int(a[i:i+nb]) % mod
        a_mod.append(ha_part)
    print(a_mod)
    for i in range(na - nb):
        if a_mod[i] == hb:
            if a[i:i+nb] == b:
                return i
    return -1

position = rabin_karp_search(a, b)
print("b index in a is:", position)
