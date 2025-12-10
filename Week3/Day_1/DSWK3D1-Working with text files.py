file=open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "w")
file.write("My name is Adewunmi Olamiposi Daniel.")
file.close()

append=open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "a")
append.write(" I'm 20 years of age. And i aspire to be great.")
append.close()

#context manager
with open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "a") as append:
    append.write("\n I'm currently going through a data science course. And i aim to become a business analyst one day with a MBAN.")

    #to read
with open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "r") as read:
    print(read.read())

    #multiline
    multi_line="""
I'll love to work at the biggest companies because i embrace challenges and like a good pay.
 I also wish to go to UBC to aquire my MBAN.
 And i'm excited through the journey.
"""
with open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "a") as append:
    append.write(multi_line)
    
with open(r"C:\Users\awote\OneDrive\Documents\newtext.txt", "r") as read:
    print(read.read())