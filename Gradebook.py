last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# My current classes
subjects = ["physics", "calculus", "poetry", "history"]

# My current grades for my classes
grades = [98, 97, 85, 88]

# Full classes and grades
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

print(gradebook) # test output

# Adding new grades with their score to the gradebook list
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

print(gradebook) # test output

# Updating grading score from a number to pass/fail for a single class
gradebook[2].remove(85)
gradebook[2].append("Pass")

print(gradebook) # test output

# Combing last semesters grades to this semesters in a new list
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)