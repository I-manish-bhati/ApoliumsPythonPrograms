#Program to check whether two matrix are equal or not 
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,7],[7,8,9]]
count=0
if len(A)==len(B) and len(A[0])==len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]!=B[i][j]:
                    count+=1
if count==0:
    print("Both of the matrices are equal")
else:
    print("Matrices are not equal")