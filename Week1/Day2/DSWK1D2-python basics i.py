name=input("WHAT IS YOUR NAME?\n")
age=int(input("HOW OLD ARE YOU?\n"))
cgpa=float(input("WHAT IS YOUR CGPA?\n"))
if cgpa>=4.5:
    rating="excellent"
elif cgpa >= 3.5 and cgpa <= 4.49:
    rating="very good"
elif cgpa >=2.5 and cgpa <=3.49:
    rating="good"
elif cgpa >=1.5 and cgpa <2.49:
    rating="fair"
else:
    rating= "poor"
print(f"Hi{name},in the next five years,you'll be {age+5},and your CGPA IS{rating}")