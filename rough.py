import functools



def catch_exception(f):
    @functools.wraps(f)
    def func(self, *args, **kwargs):
        try:
            return f(self,*args, **kwargs)
        except Exception as e:
            print(" ******** :", self.val)
            print('Caught an exception in', f.__name__)
            raise
    return func

class Test(object):
    def __init__(self, val):
        self.val = val

    @catch_exception
    def calc():
        return self.val / 0

t = Test(3)
t.calc()


# def decorator(func):
#     def _decorator(self, *args, **kwargs):
#         # access a from TestSample
#         print 'self is %s' % self
#         return func(self, *args, **kwargs)
#     return _decorator
