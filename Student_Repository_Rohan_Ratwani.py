from typing import Dict, DefaultDict, List
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Rohan_Ratwani import file_reader
import os, sys

class Student:

    """Stores information about a single student with all of the relevant information including:
        cwid
        name
        major
        Container of courses and grades
    """
    def __init__(self, cwid: str, name: str, major: str) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict() #courses[course_name] = grade
        self.stu_course: List = []

    def store_course_grade(self, course: str, grade: str) -> None:
        """ this student took course and earned grades"""
        self._courses[course] = grade
        self.stu_course.append(course)

    def info(self):
        return[self._cwid, self._name, sorted(self.stu_course)]


class Instructor:
    """ Stores information about a single Instructor with all of the relevant information including:
    cwid
    name
    department
    Container of courses taught and the number of students in each course
    """

    def __init__(self, cwid: str, name: str, dept: str) -> None:
        self.cwid: str = cwid
        self.name: str = name
        self.dept: str = dept
        self.courses: DefaultDict[str, int] = defaultdict(int) #courses[course_name] = of students who have taken the course.
        self.stu_course: dict = {}


    def store_course_student(self, course: str):
        # instructor taught course more than one student
        self.courses[course] += 1

    # def info(self):
    #     # k=""
    #     # v=""
    #     # for k,v in self._courses.items():
    #     #     print(k,v)
    #     #     print(self._name)
    #     #     print(self._cwid)
    #     return[self.courses]


class Repository:
    """Store all students, instructors for a university and print pretty tables"""
    def __init__(self, path: str) -> None:
        """ init function of class repository"""
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()

        self._read_students(self._path)
        self._read_instructors(self._path)
        self._read_grades(self._path)

        self.student_pretty_table()
        self.instructor_pretty_table()

    def _read_students(self, path: str) -> None:
        """read each line from path/students.txt and create instance of class student"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._path, 'students.txt'), 3, "\t"):
                self._students[cwid] = Student(cwid, name, major)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_instructors(self, path: str) -> None:
        """read each line from file instructors.txt and create instance of class instructor"""
        try:
            for cwid, name, department in file_reader(os.path.join(self._path, 'instructors.txt'), 3, "\t"):
                self._instructors[cwid] = Instructor(cwid, name, department)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_grades(self, path: str) -> None:
        """ read student_cwid, course, grade, instructor_cwid """
        # tell the student about the course and the grade
        # look up student associated with student_cwid, reach inside and update the dictionary
        try:
            for student_cwid, course, grades, instructor_cwid in file_reader(os.path.join(self._path, 'grades.txt'), 4, "\t"):
                if student_cwid in self._students.keys():
                    stu: Student = self._students[student_cwid]
                    stu.store_course_grade(course, grades)
                else:
                    print(f"The Student with CWID : {student_cwid} is unknown.")
                if instructor_cwid in self._instructors.keys():
                    inst: Instructor = self._instructors[instructor_cwid]
                    inst.store_course_student(course)
                else:
                    print(f"The Instructor with CWID : {instructor_cwid} is unknown.")
        except (FileNotFoundError, ValueError) as e:
            if FileNotFoundError:
                print(e)
                sys.exit()

    #tell the instructor that she taught one more student in the course.
    def student_pretty_table(self) -> None:
        """Print pretty table for student data"""
        lst: List = []
        pt = PrettyTable(field_names= ['CWID', 'Name', 'Completed Courses'])
        for stu in self._students.values():
            pt.add_row(stu.info())
            lst.append(stu.info())
        print("Student Summary")
        print(pt, "\n")
        return lst

    def instructor_pretty_table(self) -> None:
        """Print pretty table for instructor data"""
        lst1: List = []
        pt = PrettyTable(field_names= ['CWID', 'Name', 'Department', 'Courses', 'Number of Students'])
        for inst in self._instructors.values():
            for k, v in inst.courses.items():
                pt.add_row([inst.cwid, inst.name, inst.dept, k, v])
                lst1.append([inst.cwid, inst.name, inst.dept, k, v])
        print("Instructor Summary")
        print(pt)
        return lst1

if __name__ == '__main__':
    stevens: Repository = Repository("R:\Stevens\Sem-2\SSW-810\HW_09_Rohan_Ratwani")
