d1={101:"Manish",102:"Nikunj",103:"Navmann",104:"Ayush"}
print("Dictionary before removal : ",d1)
rmv=int(input("Enter the key you want to remove : "))
del d1[rmv]
print(f"Dictionary after the removal of {rmv} key : ",d1)