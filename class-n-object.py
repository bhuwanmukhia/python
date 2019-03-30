# creating class objects taking user inputs

class Student:
    name = ""
    std = ""
    roll_no = ""

    def detail(self):
        student = ("{}, studing in standard: {}, Roll.No: {}".format(self.name, self.std, self.roll_no))
        return student


no_obj = int(input("How many students to enter ?: "))
string = 'student'

obj_list = [string+str(i) for i in range(0, no_obj)]

for i in range(0, no_obj):
    obj_list[i] = Student()
    obj_list[i].name = input("\nEnter Name of the Student {}: ".format(i))
    obj_list[i].std = input("Enter Standard of the Student {}: ".format(i))
    obj_list[i].roll_no = input("Enter Roll no of the Student {}: ".format(i))

for i in range(0, no_obj):
    print("\n",obj_list[i].detail())
