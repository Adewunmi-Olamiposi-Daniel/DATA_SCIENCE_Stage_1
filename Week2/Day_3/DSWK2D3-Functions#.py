def cgpa_checker():
    subject_count=5
    tgp=float(input("Enter your Total grade point here: "))
    avg=tgp/ subject_count
    if avg >=4.5:
      rat= "Excellent"
    elif avg >=3.5 and avg <= 4.49:
      rat= "Very Good"
    elif avg >=2.5 and avg <=3.49:
      rat="Good"
    elif avg >=1.5 and avg <=2.49:
      rat="Need Improvement"
    else:
      rat="Poor.Need to do more!"
    print(f"Your CGPA is {avg}. {rat} ")
    return

cgpa_checker()
