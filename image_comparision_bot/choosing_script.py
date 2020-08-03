a = [0,1,2,3,4,5,6,7,8,9]
while len(a)!=1:
    if len(a)==2:
        print(a[0],a[1])
        choice = int(input("choose "))
        del a[0:1]
        a[0]=choice
        print(a)
    else:
        print(a[0], a[1])
        choice = int(input("choose "))
        del a[0:1]
        a[0] = choice
        print(a[len(a)-2],a[len(a)-1])
        choice2 = int(input("choose "))
        del a[len(a)-2:a[len(a)-1]]
        a.append(choice2)
        print(a)
