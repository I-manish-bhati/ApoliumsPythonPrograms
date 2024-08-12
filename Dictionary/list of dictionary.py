mainl=[{
        "Name": "DDLJ",
        "Year" : 2002,
        "Director":"Manish Bhati",
        "Actor":["Nikunj","Navmann","Ayush","Kiran",{
            "Name":"Don3",
            "Year":2025,
            "Director":"Navmann",
            "Actor":["SRK","Salman","Manish","Amitabh","Dhanush"]
            }]
       },
       {
        "Name":"Son of Sardar"  , 
        "Year": 2015,
        "Director":"Manish",
        "Actor":["Nikunj","Navmann",'Anil',"Sonakshi",{"Name":"Don4",
            "Year":2029,
            "Director":"Nikunj",
            "Actor":["SRK","Ayush","Manish","Salman","Kabir","Manthan"]}]
       },
       {
        "Name":"Good news"  , 
        "Year": 2013,
        "Director":"Nikunj",
        "Actor":["Nikunj","Navmann","Salman","Sonakshi",{"Name":"Don5",
            "Year":2029,
            "Director":"Sejal",
            "Actor":["SRK","Navmann","Manish","Akshay","Rajveer"]}]
       },
       {
        "Name":"Gangs of Wassepur"  , 
        "Year": 2013,
        "Director":"Anurag Kashyap",
        "Actor":["Faizan","Pankaj","Manish","Anil",{"Name":"Gangs of Wassepur 2",
            "Year":2015,
            "Director":"Anurag Kashyap",
            "Actor":["Faizan","Pankaj","Manish","Manoj","Salman"]}]
       },
       {
        "Name":"Taare Zameen par"  , 
        "Year": 2013,
        "Director":"Manish",
        "Actor":["Salman","Navmann","anil","Ishaan",{"Name":"Mars",
            "Year":2029,
            "Director":"Aamir khan",
            "Actor":["SRK","Ayush","Manish","Arav","Akshay"]}]
       }
       ]
flag=0
for i in range(len(mainl)):
    #mainl[i]["Actor"]
    #print(mainl[i]["Actor"][4]["Actor"][1])

    """if "Salman" in mainl[i]["Actor"] or "Salman" in mainl[i]["Actor"][4]["Actor"]:
        if mainl[i]["Year"]>2012 and mainl[i]["Year"]<=2015 or mainl[i]["Actor"][4]["Year"]>2012 and mainl[i]["Actor"][4]["Year"]<=2015:
            print(mainl[i]["Name"])"""
            

               
    if mainl[i]["Actor"]=="Salman" or mainl[i]["Actor"][4]["Actor"]:
        if mainl[i]["Year"]>2012 and mainl[i]["Year"]<2015 or mainl[i]["Actor"][4]["Year"]>2012 and mainl[i]["Actor"][4]["Year"]<2015:
            print(mainl[i]["Name"])
 
    