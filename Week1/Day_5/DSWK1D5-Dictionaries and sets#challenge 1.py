#challenge
#dict
friends={
    "Jolapinio":"Gns",
    "tiny":"Maths",
    "quaterback":"biology"
}

friends["eniola"]="chemistry"
del friends["quaterback"]

for key,value in friends.items():
    print(f"{key} : {value}")
    
print(friends.keys())
print(friends.values())

    #set
favSubjects=set(friends.values())
print(favSubjects)