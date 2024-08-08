d1={101:"Manish",102:"Nikunj",103:"Navmann"}
x=int(input("Enter the key to search : "))
if x in d1.keys():
    print(f"Yes {x} key already exist in the dictionary")
else:
    print(f"No {x} key does not exist in the dictionary")