a=int(input('ukuran: '))
x=1
y=1

while x<a+1:
    if x%2!=0:
        while y<a*x+1:
            print(y,end='\t')
            y=y+1
    elif x%2==0:
        b=a*x
        while b>y-1:
            print(b,end='\t')
            b=b-1
        y=a*x+1
    print()
    x=x+1
