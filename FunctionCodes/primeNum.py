def prime_num():
    min_num = int("enter your number")
    max_num = int("enter your number")
    while min_num<=max_num:
        j = 2
        if min_num%j==0:
            print "prime not"
        min_num = min_num+1
        print "prime number"