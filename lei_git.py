"""表示学生和管理员的类"""

class Student():
    """表示学生的类"""
    def __init__(self, name, number, sex, age, home):
        """初始化属性值"""
        self.name = name
        self.number = number
        self.sex = sex
        self.age = age
        self.home = home
        self.privilege = ''
        
    def show_infos(self):
        """显示学生信息"""
        self.infos = self.name + "\t" + self.number + "\t" + self.sex + "\t"
        self.infos += str(self.age) + "\t" + self.home + "\t" + self.privilege
        if self.privilege:
            print("姓名\t学号\t性别\t年龄\t籍贯\t权限")
        else:
            print("姓名\t学号\t性别\t年龄\t籍贯")
        print(self.infos)
    
    def show_grades(self):
        """显示成绩"""
        print(self.name.title() + "的数学成绩为90分。")
        
        
class Admin(Student):
    """表示管理员：班长、团支书的类"""
    def __init__(self, name, number, sex, age, home, privilege):
        """初始化父类属性，和子类特有属性"""
        super().__init__(name, number, sex, age, home)
        self.privilege = privilege
        
    def show_privilege(self):
        """显示权限"""
        print(self.name.title() + "的权限为" + self.privilege + "。")

