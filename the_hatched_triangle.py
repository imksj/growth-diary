def the_hatched_triangle():
    a, b = map(int, input().split(' '))
    c = 0
    for i in range(a):
        for j in range(a):
            if i == 0 or i == a-1 or j == 0 or j == a-1:
                print('*', end = '')
            else:
                d = b-1
                if (i+j)%d==0:
                    c = (i+j)//d
                    if i + j == d*c:
                        print(' ', end = '')
                else:
                    print('*', end = '')
        print()

def find_missing_number():
    a = int(input())
    b = 0
    d = 0
    for i in range(a+1):
        b += i
    for j in range(a-1):
        c = int(input())
        d += c
    print(b - d)