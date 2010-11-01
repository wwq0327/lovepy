import random, string
a = " "*100+string.printable
while True:
    print a[random.randint(0,len(a)-1)],
