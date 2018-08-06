while True:
    m=1
    i=1
    n=1
    t=1
    e=1
    print "During key counting..."
    print "-Press only enter to continue key counting"
    print "-Press 1 and enter to stop key counting"
    while True:
        i=raw_input()
        n=n+1
        if i=='1':
            break
        print n
    print "During multiplier time..."
    print "-Press only enter to continue multiplying"
    print "-Press 1 and enter to stop multiplying"
    while True: # multipliers
        i=raw_input()
        m=m+1
        if i=='1':
            break
        print m
    print "During triple multiplier time..."
    print "-Press only enter to continue triple multiplying"
    print "-Press 1 and enter to stop triple multiplying"
    while True: # triple multipliers
        i=raw_input()
        t=t+1
        if i=='1':
            break
        print t
    print "During exponentiation time..."
    print "-Press only enter to continue exponents"
    print "-Press 1 and enter to stop exponents"
    while True: # exponential bonuses
        i=raw_input()
        e=e+1
        if i=='1':
            break
        print e
    # Time for scores
    score=(n*m*t*t*t)^e
    print "here's your score-",score
    status=raw_input("Type again to play again.")
    if status !=again:
        break


