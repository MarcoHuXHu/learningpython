class Student(object):

    # attribute for all instance of 'Student' class
    class_name = 'Student'

    # unlike Java, Python can only have on '__init__' method
    # thus using constructor with default value to replace default constructor
    def __init__(self, name='', age=10, score=0):
        # private property, start with '__'
        # 注意: 双下划线开头的实例变量是不是一定不能从外部访问呢? 其实也不是.
        # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name,
        # 所以, 仍然可以通过_Student__name来访问__name变量:
        self.__name = name
        # protected property
        self._age = age
        self.score = score

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    # using properties and setter

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson',11, 59)
lisa = Student('Lisa Simpson',None, 87)
# lisa.age = None, cannot be default value

print('bart.name =', bart.get_name())
bart.set_name('Bart Simpson Junior')
print('bart.name =', bart.get_name())
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())

class GoodStudent(Student):

    def __init__(self, name='', age=12, score=100):
        self.__name = name
        self._age = age
        self.score = score


cathy = GoodStudent('Cathy Simpson')    # cathy._GoodStudent__name
# cathy.get_name() # AttributeError: 'GoodStudent' object has no attribute '_Student__name'
cathy.set_name('Cathy Simpson Junior')  # cathy._Student__name (not Private, new attribute)
print(cathy.get_name()) # Cathy Simpson Junior
print(cathy.get_age()) # 12

# type & isinstance
print(type(cathy))
print(isinstance(cathy, GoodStudent))
print(isinstance(cathy, Student))
print(isinstance(bart, GoodStudent))

print(hasattr(cathy, 'height'))
print(hasattr(cathy, '__name'))
setattr(cathy, 'height', 140)
print(hasattr(cathy, 'height'))
print(getattr(cathy, 'height'))
