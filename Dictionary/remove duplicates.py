d1={101:"Manish",102:"Nikunj",103:"Navmann",104:"Manish",105:"Ayush",106:"Nikunj"}
d2={}
for i in d1.keys():
    if d1[i] not in d2.values():
        d2[i]=d1[i]
print(d2)