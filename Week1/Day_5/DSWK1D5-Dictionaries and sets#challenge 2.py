#ACCEPTING INPUT
print("Kindly enter your name and favorite data science tool(e.g.Python,Sql,Excel)")
person1=input("Enter your name :").strip().title()
tool1=input("Enter your favorite tool :").strip().capitalize()

person2=input("Enter your name :").strip().title()
tool2=input("Enter your favorite tool :").strip().capitalize()

person3=input("Enter your name :").strip().title()
tool3=input("Enter your favorite tool :").strip().capitalize()

#dict
dictitem={
    person1:tool1,
    person2:tool2,
    person3:tool3
}
for key,value in dictitem.items():
    print(f"{key} likes {value}")

    #set
setitem={tool1,tool2,tool3}
print(f"Unique tools mentioned:{setitem}")
