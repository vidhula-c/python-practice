# Eligibility Evaluation System

age = int(input("Enter your age: "))
score = float(input("Enter your score: "))

if age >= 18 and score >= 60:
    status = "Eligible"
elif age >= 18 and score < 60:
    status = "Not eligible - minimum score not met"
elif age < 18:
    status = "Not eligible - minimum age not met"
else:
    status = "Invalid input"

print(f"\nEligibility Status: {status}")