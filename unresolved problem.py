def temperature_control(a, b):
    num = 0
    while a != b:
        if a == b:
            break
        else:
            num += 1
            if a > b:
                if a - b > 10:
                    a -= 10
                elif a - b > 5:
                    a -= 5
                elif a - b > 1:
                    a -= 1
            else:
                print()
    print(num)

def class_leaders_choice(a):
    b = []
    while 2**a == len(b)-1:
        break

def see_another_hair(n):
    h = [10, 3, 7, 4, 12, 2]
    # for i in range(n):
    #     a = int(input())
    #     h.append(a)

    a = 0
    b = 1
    n = 0
    while a != len(h)-1:
        if h[a] >= h[b]:
            n += 1
            b += 1
        else:
            a += 1
            b = a + 1
    print(n)

see_another_hair(6)
맨위로