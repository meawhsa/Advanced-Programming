import numpy as np

def merge(left, right, key):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if getattr(left[i], key) < getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(L, key):
    if len(L) < 2:
        return L[:]

    middle = len(L) // 2

    left = merge_sort(L[:middle], key)
    right = merge_sort(L[middle:], key)

    return merge(left, right, key)

class person():
    def __init__(self,name):
        self.name = name 
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value
    
    def show_info(self):
        print(f'person name is {self.name}')

class student(person):
    def __init__(self,name,grades,curiculum):
        super().__init__(name)
        self.grades = grades
        self.curiculum = curiculum
    @property
    def grades(self):
        return self._grades
    @property
    def curiculum(self):
        return self._curiculum
    @grades.setter
    def grades(self,value):
        if isinstance(value , dict):
            self._grades = value
        else:
            raise TypeError("Grades must be a dictionary.")
    @curiculum.setter
    def curiculum(self,value):
        if isinstance(value , list):
            self._curiculum = value
        else:
              raise TypeError("curiculum must be a list.")
    @property
    def gpa(self):
        if len(self.grades) == 0:
           return 0
        return np.mean(list(self.grades.values()))
    @property
    def unit(self):
        total = 0
        if len(self.curiculum) == 0 :
            return 0
        else :
            for i in self.curiculum:
                total += i.unit
        return total
    def show_info(self):
        print(f'name : {self.name} gpa : {self.gpa} courses number : {len(self.curiculum)}')
        
    
class lesson():
    def __init__(self,name,unit):
        self.name = name
        self.unit = unit
    @property
    def name(self):
        return self._name
    @property
    def unit(self):
        return self._unit
    @name.setter
    def name(self,value):
        if isinstance(value , str):
            self._name = value
        else:
            raise TypeError("Name must be a string.")
    @unit.setter
    def unit(self,value):
        if isinstance(value , int) and value > 0:
            self._unit = value
        else:
            raise TypeError("unit number must an integer greater than 0.")
    def __str__(self):
        return f'lesson name : {self.name} , unit number : {self.unit}'
    
class EducationSystem:
    student_count = 0
    lesson_count = 0
    def __init__(self):
        self.students = []
        self.courses = []
        
    def add_stu(self,name):
        if isinstance(name,student):
           self.students.append(name)
           student_count += 1
        else:
            raise ValueError('enter the right value')
    def del_stu(self,name):
        if name in self.students :
            self.students.remove(name)
            student_score -= 1
        else :
            raise ValueError('student is not in here!')
        
    def add_course(self,name):
        if isinstance(name,lesson):
           self.courses.append(name)
           lesson_count += 1
        else:
            raise ValueError('course name must be a string')
            
    def del_course(self,name):
        if name in self.courses :
            self.courses.remove(name)
            lesson_count -= 1
        else :
            raise ValueError('course is not in here!')
    @staticmethod
    def valid_score(num):
        if num>= 0 and num=<20 and isinstance(num ,(int,float)):
            return True
        else :
            return False
    def stu_score(self,name,lesson,score):
        if isinstance(name,student) and isinstance(lesson,str) and EducationSystem.valid_score(score):
            name.grades[lesson] = score
        else :
            raise ValueError
    def stu_report(self,name):
        name.show_info()
    def sorted_gpa(self):
        sorted_students = merge_sort(self.students,'gpa')
        return sorted_students
    def sorted_unit(self):
        sorted_students = merge_sort(self.students,'unit')
        return sorted_students
    def sorted_name(self):
        sorted_students = merge_sort(self.students,'name')
        return sorted_students
    
    def statistics(self):
        l = [i.gpa for i in self.students]
        if len(l)>0 :
           return f' class avg = {np.mean(l)} min gpa = {np.min(l)} max gpa = {np.max(l)} std = {np.std(l)}'
        else :
            raise ValueError 'no score found'
    def acc_fail(self):
        acc = 0
        fail = 0
        l = [i.gpa for i in self.students]
        if len(l)>0 :
         for j in l :
            if j >= 12 :
                acc += 1
            else:
                fail += 1
        else :
            raise ValueError 'no score found'
        return f' accepted : {acc} fsiled : {fail}'
    
    
    
    