class SuperClass:
    def greeting(self):
        print('Hello!')


class ChildClass(SuperClass):
    pass


class YoungClass(ChildClass):
    pass



child = ChildClass()
young = YoungClass()
child.greeting()
young.greeting()