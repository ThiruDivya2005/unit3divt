class student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(studenrt_list):
  # sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
                           key= lambda student: student.cgpa,
                           reverse=True)
  # syntax - lambda arg:exo
  return sorted_students
                           
                           