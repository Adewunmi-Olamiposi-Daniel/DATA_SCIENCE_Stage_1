#defalut arguments
def greet(name="User", salutations="Welcome back!"):
    user_input=input("Enter your name here: ")

    if user_input:
        name=user_input

    print(f"Hello {name}. {salutations}")
    return
greet()

#*args
def example(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("args:", args)
    print("kwargs:", kwargs)

example(1, 2, 3, 4, 5, name="Posi", level="400L")

#kwargs
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Olamiposi", age=20, course="Computer Science")

