while True:
    try:
        a = int(input())
    except:
        break

    b = 1
    while True:
        if b % a == 0:
            print(len(str(b)))
            break
        else:
            b = b * 10 + 1