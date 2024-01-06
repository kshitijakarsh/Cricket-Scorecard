balls = int(input("Enter number of balls "))
over = 0
run = 0
i = 0
while balls>i:
    input1 = input("What happened on this ball ")

    if input1 == 'wide':
        run = run + 1
        extra = int(input("Extras > "))
        
        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")
        
        
        if extra != 0:
            run = run + extra
        continue

    elif input1 == 'no ball':
        run = run + 1
        extra = int(input("Extras > "))
        if extra != 0:
            run = run + extra

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")    
        
        continue

    elif input1 == '1':
        run = run + 1
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '2':
        run = run + 2
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '3':
        run = run + 3
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '4':
        run = run + 4
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '6':
        run = run + 6
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

print(run)
