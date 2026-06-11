"""
## 3. Student Class with Marks List  *(Medium)*

=================================================
STUDENT CLASS WITH MARKS LIST
=================================================

Problem Statement:
Write a Python CLASS called `Student` that
stores a student's name, roll number, and a
LIST of subject marks. The class should be
able to compute statistics about the marks
and decide a grade.

This problem reinforces:
   - storing a LIST as an instance attribute
   - mutating that list through methods
   - calling one instance method from another
     using `self`

-------------------------------------------------
Instructions:
1. Define a class:
      class Student:
2. Constructor:
      def __init__(self, name, roll, marks=None):
          - if marks is None, set self.marks = []
            (do NOT use marks=[] as a default
             argument — it is a shared mutable
             default)
          - store self.name and self.roll
3. Instance methods:
      - add_mark(self, mark)
            * append a single mark to self.marks
            * reject negative marks or marks > 100
              with a message
      - total(self)          -> sum of marks
      - average(self)        -> total / count,
                                 0 if no marks
      - grade(self)          -> use self.average():
                                  >= 90 -> "A"
                                  >= 75 -> "B"
                                  >= 50 -> "C"
                                  else  -> "F"
      - report(self)         -> return a TUPLE:
              (name, roll, total, average, grade)
4. In the driver code:
      - create AT LEAST TWO students
      - add marks for each student using
        add_mark() in a for loop
      - print each student's report tuple
5. Do NOT use:
   - statistics / numpy modules
   - class attributes for marks (must be on
     each instance)

-------------------------------------------------
Input Example:
s1 = Student("Alice", 101)
for m in [90, 85, 95]:
    s1.add_mark(m)

s2 = Student("Bob", 102)
for m in [40, 55, 60]:
    s2.add_mark(m)

Output Example:
('Alice', 101, 270, 90.0, 'A')
('Bob',   102, 155, 51.666..., 'C')

-------------------------------------------------
Explanation:
- `self.marks` is a SEPARATE list for each
  student object, so Alice's marks do not mix
  with Bob's.
- `grade(self)` calls `self.average()`, which
  shows how one method can use another method
  on the SAME object through `self`.
=================================================

"""
def get_numeric_input(prompt, default_value=None):
    while True:
        user_input = input(prompt)
        if not user_input and default_value is not None:
            return default_value
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

class Student:
    def __init__(self, name, roll, marks=None):
        self.name = name
        self.roll = roll
        if marks is None:
            self.marks = []
        else:
            self.marks = list(marks)

    def add_mark(self, mark):
        if not (0 <= mark <= 100):
            print(f"Warning: Mark {mark} for {self.name} is out of valid range (0-100). Ignoring.")
        else:
            self.marks.append(mark)

    def total(self):
        return sum(self.marks)

    def average(self):
        if not self.marks:
            return 0.0
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def report(self):
        return (self.name, self.roll, self.total(), self.average(), self.grade())

students = []
num_students = int(get_numeric_input("Enter the number of students to create: "))

for i in range(num_students):
    print(f"\n--- Enter Details for Student {i+1} ---")
    name = input("Enter student's name: ")
    roll = int(get_numeric_input("Enter student's roll number: "))
    student = Student(name, roll)

    num_marks = int(get_numeric_input(f"How many marks for {name}?: "))
    for j in range(num_marks):
        mark = int(get_numeric_input(f"Enter mark {j+1} for {name}: "))
        student.add_mark(mark)
    students.append(student)

print("\n--- Student Reports ---")
for student in students:
    print(student.report())