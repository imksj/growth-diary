def Max_and_Min():
    count = int(input())
    blank = []

    for i in range(count):
        receive = int(input())
        blank.append(receive)

    max = blank[0]
    min = blank[0]

    for i in range(len(blank)):
        if max < blank[i]:
            max = blank[i]
        if min > blank[i]:
            min = blank[i]

    print(max, min)

def Max():
    max = 0
    where = 0
    for i in range(9):
        num = int(input())
        if max < num:
            max = num
            where = i+1

    print(max, where)

def How_Many():
    l = []
    for i in range(3):
        num = int(input())
        l.append(num)

    sum = l[0]*l[1]*l[2]
    sum = str(sum)
    length = len(sum)
    sum = int(sum)
    print(sum, length)
    one, two, thr, fowr, five, six, seven, eight, nine = 1, 2, 3, 4, 5, 6, 7, 8, 9
    zeroc, onec, twoc, thrc, fowrc, fivec, sixc, sevenc, eightc, ninec = 0,0,0,0,0,0,0,0,0,0
    multiple = 10**length
    print(multiple)
    for j in range(length):
        if sum % (nine * multiple) == 0:
            ninec += 1
        elif sum % (eight * multiple) == 0:
            eightc += 1
        elif sum % (seven * multiple) == 0:
            sevenc += 1
        elif sum % (six * multiple) == 0:
            sixc += 1
        elif sum % (five * multiple) == 0:
            fivec += 1
        elif sum % (fowr * multiple) == 0:
            fowrc += 1
        elif sum % (thr * multiple) == 0:
            thrc += 1
        elif sum % (two * multiple) == 0:
            twoc += 1
        elif sum % (one * multiple) == 0:
            onec += 1
        else:
            zeroc += 1
        multiple /= 10

    # print(sum)
    print(zeroc, onec, twoc, thrc, fowrc, fivec, sixc, sevenc, eightc, ninec)

def split():
    l = []
    count = 1
    for i in range(10):
        num = int(input())
        l.append(num)

    for i in range(len(l)):
        l[i] = l[i]%42
    l.sort()
    clone = l[0]
    for i in range(len(l)-1):
        if clone != l[i+1]:
            count += 1
            clone = l[i+1]
        else:
            clone = l[i+1]
    print(count)

def middle():
    input()
    a = input().split()
    a = [float(n) for n in a]
    max = 0
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
    count = 0
    for i in range(len(a)):
        a[i] = a[i]/max*100
    for i in range(len(a)):
        count += a[i]

    print(count/len(a))

def OX():
    n = int(input())
    l = []
    for i in range(n):
        OX = input()
        l.append(OX)

    score = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 'O':
                score += 1
            else:
                score += 0

    print(score)


