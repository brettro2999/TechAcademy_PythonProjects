

class User:
    id_num = ""
    full_name = ""
    password = ""

    def checkGrade(self):
        enter_id = input("Enter ID: ")
        enter_fullName = input("Enter Full Name: ")
        enter_password = input("Password: ")
        if (enter_id == self.id and enter_password == self.password):
            print("Grades for {}:".format(enter_fullName))
        else:
            print("Incorrect credentials.")

class Teacher(User):
        teach_id = ""
        full_name = ""
        password = ""

        def checkGrade(self):
            enterTeach_id = input("Enter Teacher ID: ")
            enter_fullName = input("Enter Full Name: ")
            enter_password = input("Password: ")
            if (enterTeach_id == self.id and enter_password == self.password):
                print("Grades for {}:".format(enter_fullName))
            else:
                print("Incorrect credentials.")

class Student(User):
        student_id = ""
        full_name = ""
        password = ""

        def checkGrade(self):
            enterStu_id = input("Enter Student ID: ")
            enter_fullName = input("Enter Full Name: ")
            enter_password = input("Password: ")
            if (enterStu_id == self.id and enter_password == self.password):
                print("Grades for {}:".format(enter_fullName))
            else:
                print("Incorrect credentials.")


parent = User()
parent.checkGrade()

teacher = Teacher()
teacher.checkGrade()

student = Student()
student.checkGrade()

    
