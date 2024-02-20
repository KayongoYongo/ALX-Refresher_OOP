# 0x06. Python - Classes and Objects

## 0. My first square
Write an empty class `Square` that defines a square:

* You are not allowed to import any module

```Shell
vagrant@ubuntu-focal:~/ALX-Refresher_OOP$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
vagrant@ubuntu-focal:~/ALX-Refresher_OOP$ ./0-main.py
<class '0-square.Square'>
{}
vagrant@ubuntu-focal:~/ALX-Refresher_OOP$
```

## 1. Square with size
Write a class Square that defines a square by: (based on 0-square.py)

* Private instance attribute: size
* Instantiation with size (no type/value verification)
* You are not allowed to import any module

```Shell
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$
```

## 2. Size validation
Write a class Square that defines a square by: (based on 1-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
  * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* You are not allowed to import any module

```Shell
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```

# 3. Area of a square

Write a class Square that defines a square by: (based on 2-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
 * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
 * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Public instance method: def area(self): that returns the current square area
* You are not allowed to import any module

```Shell
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
vagrant@ubuntu-focal:~/ALX-Refresher_OOP/0x06-python-classes$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```
