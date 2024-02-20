def bubble(x):
    n = len(x)

    for i in range(n):
        for j in range(0,n-i-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]

y = [12,36,58,445,229,55,26,48,99,41,33]
print("orginal list: ",y)

bubble(y)
print("sorted list: ",y)