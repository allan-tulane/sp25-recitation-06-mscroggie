def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1


    if n <= 1:
        return n
    else:
        return fib_recursive(n-1,counts) + fib_recursive(n-2,counts)


    

    
def fib_top_down(n, fibs,count):
    #fib(n) = fib(n-1) + fib(n-2)
    #if fib[i] has been calculated, fib(n) = fib[i]
    #else, calculate
    count +=1
    print(count)
    i = n
    if i <=1:
        fibs[i]= i
    else:
        if fibs[i] == -1:
         fibs[i] = fib_top_down(n-1,fibs,count)+fib_top_down(n-2,fibs,count)


    return fibs[n]

print(fib_top_down(20, [-1] * (20+1),1))


def fib_bottom_up(n):
     fibs =  [0] * (n+1)
     for i in range(n+1):
         if i <= 1:
             fibs[i] = i
         else:
             fibs[i] = fibs[i-1]+fibs[i-2]



     return fibs[i]





