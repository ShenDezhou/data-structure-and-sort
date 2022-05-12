a = "12340939453023876"
b = "93945"
char_set = {i for i in a+b}
print(char_set)

def create_state_machine(b, char_set):
    state_machine = {}
    n = len(b)
    for q in range(n):
        for char in char_set:
            s = b[0:q] + char
            s = s[::-1]
            state_machine[(q, char)] = 0
            for k in range(1, n+1):
                if k > len(s):
                    break
                prefix = b[0:k]
                prefix = prefix[::-1]
                count = 0
                for j in range(len(prefix)):
                    if prefix[j] == s[j]:
                        count += 1
                    else:
                        break
                if count == len(prefix):
                    state_machine[(q, char)] = j + 1
    return state_machine

def finite_state_machine_search(a, b):
    state_machine = create_state_machine(b, char_set)
    print(state_machine)
    finish_state = len(b)
    state = 0
    for i in range(len(a)):
        state = state_machine[(state, a[i])]
        print(i, state)
        if state == finish_state:
            return i - finish_state + 1
    return -1

position = finite_state_machine_search(a, b)
print("the position of b in string a:", position)

