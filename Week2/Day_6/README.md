🧠 DSWK2D6 — Mini Project: Login System with Error Handling

— DAY 6 — SATURDAY, NOV 8

I built a complete login system that uses everything I have learned so far, from dictionaries to loops to exception handling. I worked with a real dataset containing usernames, passwords, roles, emails, and security questions, then created a system that behaves like an actual authentication flow.

I learned how to validate login attempts, detect wrong passwords, handle missing usernames, and even reset a user’s password through a security question. I also practiced activity logging to track every success and failure in the system.

📚 WHAT I LEARNED:

How to store user profiles using nested dictionaries.

How to validate usernames and passwords correctly.

How to use try and except to catch wrong input types and missing users.

How to count login attempts and block access after multiple failures.

How to reset a password safely through a security question.

How to log each event like a real system audit trail.

🧩 PRACTICE CHALLENGES:

1️⃣ LOGIN AUTHENTICATION

Create a login flow that:

Accepts a username and password.

Handles:

Username not found

Wrong password

Invalid input types

Allows 3 attempts before locking the user out.

2️⃣ PASSWORD RESET SYSTEM

After three failed logins:

Ask the user if they want to reset their password.

Validate them with their stored security question.

Allow them to create a new password if the answer is correct.

3️⃣ ACTIVITY TRACKER

Create a list that stores every event:

Login success

Login failure

Password reset success

Password reset failure

Print the log at the end of the program.

💭 REFLECTION

This mini project showed me how several concepts can merge into one powerful system. Error handling made the program safe, dictionaries made it structured, and loops made it flexible. I now understand how actual login systems think, how they defend against mistakes, and how they keep track of everything happening behind the scenes. It felt like building a small real-world application from scratch.

✅ Status: Completed
📅 Next Lesson: DSWK2D7 — Review and Reflection.
