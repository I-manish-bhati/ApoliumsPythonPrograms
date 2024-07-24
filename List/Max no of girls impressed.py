def func(n,k,g,tst):
    for i in range(len(n)):
        sm,a,m=0,0,0
        gap=round(n[i]/len(g[i]))
        for j in range(0,k[i]):
            sm=sum(g[i][:k[i]])
        for l in range(k[i],len(g[i])):
            if l==len(g[i]):
                break
            else:
                if sm>m:
                    m=sm
                sm+=g[i][l]-g[i][a]
        if k[i]==len(g[i]):
            m=sm
        if m==tst[i]:
            print("Test ",i+1," Passed sucessfully")
        else:
            print("Test ",i+1,"Failed")

n=[7,5,6,4]
k=[2,3,2,4]
g=[[2,4,8,1,2,1,8],[5,3,9,2,4],[1,1,1,1,1,1],[10,20,30,40]]
tst=[12,17,2,100]
func(n,k,g,tst)

