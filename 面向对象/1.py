class Animal:
    # 所用的知识 Animal类的封装 -> Dog类，Cat类，Person类的继承->多态
    # 把所有的共同属性和方法封装在一个公有类里面让子类继承父类的方法来实现和数据
    # 在创建一个小狗实例的时候，给它设置几个属性
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        # print("名字是%s，年龄%d岁的小狗在吃饭"%(self.name,self.age))
        print("%s吃饭" % self)
        return self

    def play(self):
        print("%s玩" % self)
        return self

    def sleep(self):
        print("%s睡觉" % self)
        return self

    def work(self):
        pass


class Dog(Animal):

    def work(self):
        print("%s看家" % self)

    def __str__(self):
        # self对象本身对字符串的一个描述
        return "名字是%s，年龄%d岁的小狗在" % (self.name, self.age)


class Cat(Animal):
    def work(self):
        print("%s捉老鼠" % self)

    def __str__(self):
        # self对象本身对字符串的一个描述
        return "名字是%s，年龄%d岁的小猫在" % (self.name, self.age)


class Person(Animal):
    def __init__(self, name, pets, age=1):
        super(Person, self).__init__(name, age)
        self.pets = pets

    def feed_pets(self):
        # 所用的知识就是多态，养宠物，和让宠物工作也都是多态
        for pet in self.pets:
            pet.eat()
            pet.sleep()
            pet.play()

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()

    def __str__(self):
        # self对象本身对字符串的一个描述
        return "名字是%s，年龄%d岁的人在" % (self.name, self.age)


# d = Dog("小黑",18)
# c = Cat("小红",2)
# p = Person("BruceLong", [d, c], 24 )
# print(p.__dict__)

d = Dog("小黑", 18)  # self中谁调用就是谁 此处d 会去Animal中找到self和里的的属性和方法而Animal里的self就是Dog类
c = Cat("小红", 2)
p = Person("BruceLong", [d, c], 24)
p.feed_pets()
p.make_pets_work()
print(p.__str__())
