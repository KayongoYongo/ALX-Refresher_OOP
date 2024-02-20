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
