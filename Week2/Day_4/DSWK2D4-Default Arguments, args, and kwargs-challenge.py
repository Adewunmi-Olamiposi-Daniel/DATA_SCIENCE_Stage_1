#args challenge
def numbers(*args):
   total =0
   for price in args:
      total += price
   return f"The total cost of items are {total}"
print(numbers(200, 500, 1000))
print(numbers(250, 450))

#kwargs challenge
def student_profile(**kwargs):
   print("STUDENT PROFILE:")
   for key, value in kwargs.items():
      print(f"{key.capitalize()}:{value}")
student_profile(name="Olamiposi Adewunmi",age="20",level="400l",cgpa="4.18")
student_profile(Name="Alex Freburg",age="20",level="300l",cgpa="2.15")