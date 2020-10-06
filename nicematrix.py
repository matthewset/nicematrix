for i in range(int(input())):
    n,m=map(int,input().split(" "))
    array=[]
    for i in range(n):
        l=input().split(" ")
        lt=[]
        for j in range(m):
            lt.append(int(l[j]))
        array.append(lt)
        count=0
    for i in range(n//2):
        for j in range(m//2):
            new=sorted([array[i][j],array[i][m-1-j],array[n-1-i][j]])[1]
            count=count+abs(new-array[i][j])+abs(new-array[i][m-1-j])+abs(new-array[n-1-i][j])+abs(new-array[n-1-i][m-1-j])
    if n%2==1:
        for i in range(m//2):
            new=max(array[(n//2)][i],array[(n//2)][m-1-i])
            count=count+abs(new-array[(n//2)][i])+abs(new-array[(n//2)][m-1-i])
    if m%2==1:
        for i in range(n//2):
            new=max(array[i][(m//2)],array[n-1-i][(m//2)])
            count=count+abs(new-array[i][(m//2)])+abs(new-array[n-1-i][(m//2)])
    print(count)
            
    
