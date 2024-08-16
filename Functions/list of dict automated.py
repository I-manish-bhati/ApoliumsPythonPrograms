def inp(movies):
    #input
    for j in range(len(movies)):
        x={}
        print("\nEnter no of keys in iteration ",j+1," : ",end="")
        i=int(input(""))
        for i in range(i):
            if i==3:
                k=input("Enter key : ")
                l=int(input("Enter the length of array : "))
                v=[]
                for m in range(l):
                    v.append(input("Enter the actor : "))
            else:
                k=input("Enter key : ")
                v=input("Enter Value : ")
            x[k]=v
        movies[j]=x 
    return movies
    
def op(movies):
    #printing all the movies
    print("\nPrinting whole dataset : ")
    for i in movies:
        print(i)
    return movies

def ops(movies):
    #selective movie details
    choice=int(input("\n1 Name \n2 Year \n3 Director \n4 Actor \nSelect key to search : "))
    if choice==1:
        name=input("Enter name : ")
        for i in range(len(movies)):
            if name in movies[i]["Name"]:
                print(movies[i])
    elif choice==2:
        year=input("Enter year : ")
        for i in range(len(movies)):
            if year in movies[i]["Year"]:
                print(movies[i])
    elif choice==3:
        director=input("Enter director name : ")
        for i in range(len(movies)):
            if director in movies[i]["director"]:
                print(movies[i])
    elif choice==4:
        actor=input("Enter actor name : ")
        for i in range(len(movies)):
            if actor in movies[i]["Actor"]:
                print(movies[i])
    else:
        print("\nInvalid choice!!!!\n")
    return movies
    
def delete(movies):
    #delete specific movie
    choice=int(input("\n1 Via  Key Value \n2 Via Index \nEnter your choice : "))
    if choice==1:
        k=input("Enter Key : ")
        v=input("Enter Value : ")
        for i in range(len(movies)):
            if v in movies[i][k]:
                del movies[i]
    if choice==2:
        index=int(input("Enter index no : "))
        del movies[index]
    return movies

#main code    
movies=[]
while True:
    print("\n1 Insert\n2 Print Whole Dataset\n3 Print Specific\n4 Delete Specific Movies \nSelect Action to be performed : ",end="")
    ch=int(input(""))
    if ch==1:
        num=int(input("\nEnter the number of movies you want to enter : "))
        for i in range(num):
            movies.append({})
        inp(movies)
    elif ch==2:
        op(movies)
    elif ch==3:
        ops(movies)
    elif ch==4:
        delete(movies)
    else:
        print("Enter valid choice")
    
        
    
    
