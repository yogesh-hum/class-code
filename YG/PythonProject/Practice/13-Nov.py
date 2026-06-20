'''2️⃣ Student Grading System with Subjects
Input marks for 3 subjects: Math, Science, English.
Calculate total and average.
Print grade based on average:
90+ → A
80–89 → B
70–79 → C
<70 → Fail
Also print “Pass/Fail” for each subject individually (pass >= 40).'''

Maths=int(input('enter your Maths numeber: '))
Science=int(input('enter your Science numeber: '))
English=int(input('enter your English number: '))

Total=(Maths+Science+English)
print(Total)
Average=(Total/3)
print(Average)

if Average > 90:
    print("Grad A")
elif Average > 80:
    print('Grade B')
elif Average > 70:
    print('Grade C')
else:
    print('Fail')
