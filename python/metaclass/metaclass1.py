"""metaclass
"""

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print(cls, name, bases, attrs, sep='\n')
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaClass):
    pass

l = MyList()
l.add(1)
print(l)
