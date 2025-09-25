# TYPE ERROR
#a = 5 + '10'


#IMPORT ERROR
#import somemod


#NAME ERROR
#a = 5
#b = c

#FILE NOT FOUND ERROR
#f = open('somefile.txt')

#VALUE ERROR
#a = [1,2,3,4,5]
#a.remove(9)  9 not in list


# INDEX ERROR
#a = [1,2,3,4,5]
#value = a[7]

# KEY ERROR
#my_dict = {'haha' : 5}
#value = my_dict['hahaha']


# HOW TO RAISE EXCEPTION
#x = -5
#if x < 0:
#    raise Exception('x should be positive')


# ASSERT    
#x = -5
#assert (x > 0)


# TRY CATCH
try:
    a = 5 / 0
except Exception as e:
    print (f'errorrrrr {e}') # errorrrrr division by zero


try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up')



# DEFINE YOUR OWN EXCEPTION
    
class ValueToohighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_val(x):
    if x > 100:
        raise ValueToohighError('Value is too high', x)
    
try:
    test_val(200)
except ValueToohighError as e:
    print(e.message, e.value)


