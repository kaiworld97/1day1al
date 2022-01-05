def hi(a):
    b = 1
    while(True):
        if b % a == 0:
            print(len(str(b)))
            break
        else:
            b = b*10 + 1



hi(9901)