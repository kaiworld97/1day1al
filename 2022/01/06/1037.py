while True:
    try:
        a = int(input())
    except:
        break
    if a in range(1, 51):
        pass
    else:
        break
    try:
        b = list(set(input().split()))
    except:
        break
    if len(b) == a:
        pass
    else:
        break
    d = []
    for c in b:
        if int(c) in range(2, 1000001):
            d.append(int(c))
        else:
            break
    if len(d) == a:
        pass
    else:
        break
    e = max(d)*min(d)
    print(e)
    # if b in range(2, 1000001):
    #     print(b)
    # else:
    #     break