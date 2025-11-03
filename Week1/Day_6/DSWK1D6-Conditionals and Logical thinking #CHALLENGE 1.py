#CHALLENGE 1

#ACCEPTING INPUT

Python=int(input("Enter your python skill level from 1 to 10: "))
Statistics=int(input("Enter your statistics skill level from 1 to 10: "))
Communication=int(input("Enter your communication skill level from 1 to 10: "))

#USING CONDITIONAL STATEMENT

if (Python<0 or Python>10) or (Statistics<0 or Statistics>10) or (Communication<0 or Communication>10):
    print("Invalid input. Scorws must be between 0 and 10❌")
elif Python>=8 and Statistics>=8 and Communication>=8:
    print("Excellent! You're Internship ready👌.")
elif (Python>=7 and Statistics>=7) or (Python>=7 and Communication>=7) or (Statistics>=7 and Communication>=7):
    print("Almost there! Keep sharpening your weaker areas🙌.")
elif Python>=7  or Statistics>=7 or Communication>=7:
    print("You're getting started,stay consistent👍.")
else:
    print("You need more practice! Stay hungry and keep learning")


print(f"NO MATTER WHERE YOU'RE AT, DON'T GIVE UP, WHEN YOU DO IS WHEN YOU LOSE. STAY STRONG💪.")