class SingleTon(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


o1 = SingleTon()
print("Object - 1 ==>", o1)
o1.data = 10
print("Object - 1 ==>", o1.data)

o2 = SingleTon()
print("Object - 2 ==>", o2)
print("Object - 2 data ==>", o2.data)
o2.data = 5

print("Object - 1 data ==>", o1.data)
print(o1==o2)