#string concatenation
first= "Adewunmi"
last="Olamiposi"
full=first+" "+last
print (full)

name="ADEWUNMI OLAMIPOSI"
print(name [0])    #first letter
print(name[-1])    #last letter
print(name[::-1])  #reversed
print(name[0:4])   #partial slicing

#f-string
cgpa=input("What is my CGPA: ").strip()
print(f"My CGPA IS {cgpa} AND I'M PROUD OF IT")

#COMMON STRING METHODS
print("hello".upper())
print("HELLO".lower())
print("Data Science rocks".split())
print("Hi  ".strip())
print("Data Science is so fun".replace("a","@"))