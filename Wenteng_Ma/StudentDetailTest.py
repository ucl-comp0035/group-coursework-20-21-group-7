import unittest
import StudentDetailClass

class MyTestCase(unittest.TestCase):
    def testInitRegisteredUser(self):
        student_detail = StudentDetailClass.StudentDetail(1005, 'College', 10012021)
        self.assertEqual(student_detail.__repr__(),
                         'StudentDetail(StudentID=1005,status=College,dateCreated=10012021)')

    def testUpdateDetail(self):
        student_detail = StudentDetailClass.StudentDetail(1005, 'College', 10012021)
        self.assertEqual(student_detail.__repr__(),
                         'StudentDetail(StudentID=1005,status=College,dateCreated=10012021)')
        student_detail.UpdateStudentDetail('Master')

        self.assertEqual(student_detail.__repr__(),
                         'StudentDetail(StudentID=1005,status=Master,dateCreated=10012021)')
if __name__ == '__main__':
    unittest.main()