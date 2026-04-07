name = input("Name: ")
dob = input("DOB: ")
reg = input("Reg No: ")
dept = input("Department: ")

m1 = int(input("Mark1: "))
m2 = int(input("Mark2: "))
m3 = int(input("Mark3: "))
m4 = int(input("Mark4: "))
m5 = int(input("Mark5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

print("\nStudent Details")
print("Name:", name)
print("DOB:", dob)
print("Reg No:", reg)
print("Dept:", dept)
print("Total:", total)
print("Percentage:", per)

if per >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
