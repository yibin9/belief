"""
步骤：
    （一）数据模型类：StudentModel
		    数据：姓名 name,年龄 age,成绩 score,编号 id
	     逻辑控制类：StudentManagerController
		    数据：学生列表 __stu_list
		    行为：获取列表 stu_list,  ---- 只读属性
		         添加学生 add_student(stu) --- 创建id 添加新学生
		            创建id:自增长
		测试：
		manager =  StudentManagerController()
		data01 = StudentModel("悟空",26,95)
		manager.add_student(data01)
		for item in manager.stu_list:
		    print(item.id,item.name)

	（二） 删除学生remove_student(sid)
	    测试：
		manager =  StudentManagerController()
		data01 = StudentModel("悟空",26,95)
		manager.add_student(data01)
		manager.add_student(StudentModel("八戒",27,91))
		manager.remove_student(1001)
		for item in manager.stu_list:
		    print(item.id,item.name)
	（三）修改学生信息
        在Controller类中： 修改学生update_student
        在View类中： 修改学生__modify_student
    (四) 按照成绩升序排列
        在View类中： __output_students_by_score
        在Controller类中： order_by_score
"""


class StudentModel:
    def __init__(self, name="None", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    # 初始编号
    __init_id = 1000

    @classmethod
    def __generate_id(cls, stu):
        stu.id = cls.__init_id
        cls.__init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    # 由于View调用
    def add_student(self, stu):
        StudentManagerController.__generate_id(stu)
        self.__stu_list.append(stu)

    def remove_student(self, stu_id):
        for item in self.stu_list:
            if item.id == stu_id:
                self.stu_list.remove(item)
                return True
        return False

    def update_student(self, stu):
        for item in self.stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False

    def order_by_score(self):
        for r in range(len(self.stu_list) - 1):
            for c in range(r + 1, len(self.stu_list)):
                if self.stu_list[r].score > self.stu_list[c].score:
                    self.stu_list[r], self.stu_list[c] = self.stu_list[c], self.stu_list[r]


# 测试
# manager = StudentManagerController()
# data01 = StudentModel("悟空", 26, 95)# 没有编号
# manager.add_student(data01)# 创建编号/存储
# manager.add_student(StudentModel("八戒", 27, 91))# 创建编号/存储
# manager.remove_student(1004)
# for item in manager.stu_list:
#     print(item.id,item.name)
class StudentManagerView:

    def __init__(self):
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("1）添加学生")
        print("2）显示学生")
        print("3）删除学生")
        print("4）修改学生")
        print("5）按照成绩升序显示")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_students_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))

        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print("编号是:%d,姓名是:%s,年龄是:%d,成绩是%d" % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        id = int(input("请输入学生编号："))
        if self.__controller.remove_student(id):
            print("删除成功！")
        else:
            print("删除失败！")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = int(input("请输入需要修改的学生年龄："))
        stu.score = int(input("请输入需要修改的学生成绩："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_students_by_score(self):
        self.__controller.order_by_score()
        self.__output_students()


view = StudentManagerView()
view.main()
