class Student:
    #here name, id ... are the parameters, this is the constructor function. This constructs the object. init means intialize
    def __init__(self,name,id,email,gpa):
        self.name = name,
        self.id = id,
        self.email = email,
        self.gpa = gpa

#These functions are not necessary to work with OOPS btw....
##STR function
    def __str__(self):
        current_object_data= (f"\nName: {self.name}"
                              f"\nID: {self.id}"
                              f"\nEmail: {self.email}"
                              f"\nGPA: {self.gpa}")
        return current_object_data

    '''   ##Getter function: it returns values
    def get_name(self):
        return self.name, self.id, self.email, self.gpa
    #Setter function: no return, it always has parameters.
    def set_name(self,name,id,email,gpa):
        self.name=name,
        self.id=id,
        self.email= email,
        self.gpa=gpa,
'''
    def get_id(self):
        id=self.id
        return id
def main():
    print("WEEk 14")

    my_first_student= Student('Arshroop Saini',4589,'something@maimi.edu',3.5)
    my_second_student=Student("unknown",5748,'sfjsf@gmail.com',3.0)
    print(my_first_student)

    my_first_student.gpa=4.0 #this is how you update the object without using a setter function
    print(my_first_student.name) #this is how you get something from the object without using a getter function
    print(my_first_student)
    print('------------------------')
    #creating a dictionary
    student_dictionary={}
    student_dictionary[my_first_student.get_id()]=my_first_student
    student_dictionary[my_second_student.id]=my_second_student
    print(student_dictionary.keys())

    for current_key in student_dictionary:
        print(student_dictionary.get(current_key))

if __name__ =='__main__':
    main()