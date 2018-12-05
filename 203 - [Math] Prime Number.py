def prime(num):
    for k in range(2, num+1):
        if k != num:
            k = num % k
            if k == 0:
                print("This number isn't a prime number.")
                break
        else:
            print("This number is a prime number.")
            break

num = int(input('Number: '))
prime(num)