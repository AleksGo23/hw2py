# Aleks Gondek alg6177@psu.edu

grade1 = input("Enter your course 1 letter grade: ")
 
def getGradePoint(grade):
  gpa = 0.0
  if grade == "A" :
    gpa = 4.0
  elif grade == "A-" :
    gpa = 3.67
  elif grade == "B+" :
    gpa = 3.33
  elif grade == "B" :
    gpa = 3.0
  elif grade == "B-" :
    gpa = 2.67
  elif grade == "C+" :
    gpa = 2.33
  elif grade == "C" :
    gpa = 2.0
  elif grade == "D" :
    gpa = 1.0
  else :
    gpa = 0.0
  return gpa

credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)
gpa1 = getGradePoint(grade1)
print("Grade point for course 1 is:",gpa1)

grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)
gpa2 = getGradePoint(grade2)
print("Grade point for course 2 is:",gpa2)

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)
gpa3 = getGradePoint(grade3)
print("Grade point for course 3 is:",gpa3)

GPA = (gpa1*credit1 + gpa2*credit2 + gpa3*credit3)/(credit1+credit2+credit3)

print("Your GPA is:", GPA)
