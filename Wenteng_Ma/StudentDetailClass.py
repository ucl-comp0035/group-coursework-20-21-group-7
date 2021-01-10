'''
Name: Wenteng Ma
Purpose: (Record student details, shown in UML Class)
Instance variables: (StudentID, status, datecreated)
Methods: ( __repr__: display Student detail ,UpdateStudentDetail)
'''

class StudentDetail():
    def __init__(self, StudentID: int, status: str, dateCreated: int):
        self.dateCreated = dateCreated
        self.StudentID = StudentID
        self.status = status

    def UpdateStudentDetail(self, status: str):
        self.status = status

    def __repr__(self):
        return 'StudentDetail(StudentID={},status={},dateCreated={})' \
            .format(self.StudentID, self.status, self.dateCreated)