while True:
    n=0
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
    # Time for scores
    score=n*m
    print "here's your score-",score
    status=raw_input("Type again to play again.")
    if status !=again:
        break


