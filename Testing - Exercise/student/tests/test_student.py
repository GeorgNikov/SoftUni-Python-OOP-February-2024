from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('Test')
        self.student_with_course = Student('Study', {'math': ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual('Test', self.student.name)
        self.assertEqual('Study', self.student_with_course.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ["x + y = z"]}, self.student_with_course.courses)

    def test_enroll__in_same_course_add_new_notes(self):
        result = self.student_with_course.enroll("math", ["1 + 2 = 3", "2 + 3 = 5"])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(["x + y = z", "1 + 2 = 3", "2 + 3 = 5"], self.student_with_course.courses["math"])

    def test_enroll__new_course_without_third_param_adds_note_to_course(self):
        result = self.student.enroll('math', ['x + y = z'])

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual({'math': ['x + y = z']}, self.student.courses)

    def test_enroll__new_course_with_third_param_adds_note_to_course(self):
        result = self.student.enroll('math', ['x + y = z'], 'Y')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual({'math': ['x + y = z']}, self.student.courses)

    def test_enroll__new_course_with_third_wrong_param_adds_note_to_course(self):
        result = self.student.enroll('math', ['x + y = z'], 'N')

        self.assertEqual('Course has been added.', result)
        self.assertEqual({'math': []}, self.student.courses)

    def test_add_notes__course_exist_expect_result(self):
        result = self.student_with_course.add_notes("math", '1 + 2 = 3')

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(["x + y = z", "1 + 2 = 3"], self.student_with_course.courses['math'])

    def test_add_notes__non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', '1 + 2 = 3')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_existing_course_expect_result(self):
        result = self.student_with_course.leave_course('math')

        self.assertEqual("Course has been removed", result)

    def test_leave_course_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
