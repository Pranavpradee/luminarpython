class Teacher:
    college_name="JECC"
    def __init__(self,tname,subject,departmnt,tid):
        self.tname=tname
        self.subject=subject
        self.departmnt=departmnt
        self.tid=tid

    def printval(self):
        print("name",self.tname)
        print("subject",self.subject)
        print("department",self.departmnt)
        print("teacher is",self.tid)
        print("college_name",Teacher.college_name)
t=Teacher("PRANAV","MATHS","ECE",1060248)
t.printval()