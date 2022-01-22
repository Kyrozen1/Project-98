def swapContent():
    f1 = input("enter file 1 name:")
    f2 = input("enter file 2 name:")
    with open(f1,'r') as a:
        data_a = a.read()

    with open(f2,'r') as a:
        data_b = a.read()

    with open(f1,'w') as a:
        a.write(data_b)

    with open(f2,'w') as a:
        a.write(data_a)

swapContent()