#Program to check whether two matrix are equal or not 
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,7],[7,8,9]]
if len(A)==len(B):
    if len(A[0])==len(B[0]):
        abc:
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]!=B[i][j]:
                    print("Matrices are not equal")
                    break
        else:
            print("Both of the matrices are equal")
    else:
        print("Matrices are not equal")
else:
    print("Matrices are not equal")