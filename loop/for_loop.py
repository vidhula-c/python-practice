marks=[99,85,95,78]

t=0
h=marks[0]
l=marks[0]

for i in marks:
    t+=i
    if i>h:
        h=i
    if i<l:
        l=i

average = t / len(marks)

print("Student Marks Analysis")
print("----------------------")
print(f"Marks   : {marks}")
print(f"Total   : {t}")
print(f"Average : {average:.2f}")
print(f"Highest : {h}")
print(f"Lowest  : {l}")