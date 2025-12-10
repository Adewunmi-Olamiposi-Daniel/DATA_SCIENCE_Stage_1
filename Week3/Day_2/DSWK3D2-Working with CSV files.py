import csv

with open("updated_grade.csv", "w", newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["Name", "Score","Grade"])
    writer.writerow(["Alice", "85","B"])
    writer.writerow(["Bob", "92","A"])
    writer.writerow(["Shaun", "78","C"])


with open("updated_grade.csv", "r") as read1:
    print(read1.read())

    #using dictionaries instead of lists
with open("updated_company_list.csv", "w", newline="") as files:
    field_names=(["Name", "Sex","Wages"])
    writer= csv.DictWriter(files,fieldnames=field_names)
    writer.writeheader()
    writer.writerow({"Name":"A.Alice", "Sex":"F","Wages":"$124,000"})
    writer.writerow({"Name":"S.Bob", "Sex":"M","Wages":"$112,000"})
    writer.writerow({"Name":"M.Shaun", "Sex":"M","Wages":"$109,420"})
    writer.writerow({"Name":"T.Malia", "Sex":"F","Wages":"$104,532"})
    writer.writerow({"Name":"E.Adebayo", "Sex":"M","Wages":"$101,201"})
    writer.writerow({"Name":"T.Alexander", "Sex":"M","Wages":"$98,020"})
    writer.writerow({"Name":"B.Claude", "Sex":"M","Wages":"$92,999"})
    writer.writerow({"Name":"S.Adams", "Sex":"F","Wages":"$85,660"})
    writer.writerow({"Name":"M.Penelope", "Sex":"F","Wages":"$78,650"})

with open("updated_company_list.csv", "r") as read2:
    print(read2.read())
    

        #MINI PROJECT
with open("Expenses.csv", "w", newline="") as data:
    expenses=(["Date", "Categories","Amount"])
    writer= csv.DictWriter(data,fieldnames=expenses)
    writer.writeheader()
    writer.writerow({"Date":"2025-11-11", "Categories":"Food","Amount":"$1,500"})
    writer.writerow({"Date":"2025-11-12", "Categories":"Transport","Amount":"$500"})
    writer.writerow({"Date":"2025-11-26", "Categories":"Books","Amount":"$2,000"})
    writer.writerow({"Date":"2025-12-17", "Categories":"Clothes","Amount":"$3,000"})
    writer.writerow({"Date":"2025-12-25", "Categories":"Entertainment","Amount":"$1,000"})

with open("Expenses.csv", "r") as read3:
    print (read3.read())