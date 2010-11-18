def k(num):
    debug = True
    print num
    while debug:
        if num%2 == 0:
            num = num/2
            print num
        else:
           
            num = num+3
            print num

        if num == 1:
            debug = False

k(17)
