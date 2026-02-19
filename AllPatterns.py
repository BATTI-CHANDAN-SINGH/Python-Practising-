n=5
for x in range(1,n+1):
    for y in range(1,n+1):
        print(x,end=' ')
    print()

print('-'*10)

for x in range(1,n+1):
    for y in range(1,n+1):
        print(y,end=' ')
    print()

print('-'*10)

for x in range(1,n+1):
    for y in range(1,n+1):
        print(x+y,end=' ')
    print()

print('-'*10)

for x in range(n,0,-1):
    for y in range(1,n+1):
        print(x,end=' ')
    print()
