def prime():
    n=int(input("enter the number:"))
    for i in range(2,n//2):
        if n%i==0:
            print("number is not prime")
            break
    else:
        return print("number is prime")
    
    
k = prime()
print(k)