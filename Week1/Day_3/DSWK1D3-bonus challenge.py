#ACCEPTING THE INPUT
name=input("ENTER YOUR NAME:\n").strip().upper()
cgpa=input("ENTER YOU CGPA:\n").strip()
#SPLITING NAMES
parts=name.split()
first=parts[0]
last=parts[-1]

#PRINTING OUT RESULTS
print(f"HELLO {name}")
print(f"Your Data Scientist ID is:{name[:3]+name[-3:]+cgpa} ")
print("Data is power and Data Scientists wield it!".upper())