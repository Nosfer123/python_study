class Sample:
    def _private(self):
        print("I'm private!")

    def __superprivate(self):
        print("I'super private!")

a = Sample()
a._private()
# a.__superprivate() doesn't work
a._Sample__superprivate()