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

