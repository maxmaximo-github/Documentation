<span style="color: blue">Question 1</span>
***

The following expression

` 2 ** 3 ** 2 ** 1`

is:

A. invalid
B. equal to `16`
C. equal to `16.0`
<span style="color: red">D. equal to `512` </span>
E. equal to `64`
F. equal to `128.0`   




<span style="color: blue">Question 2</span>
***

If you want to build a string that reads:

`Peter's sister's name's "Anna"`

which of the following literrals would you use? (Sellect all that apply)

<span style="color: red">A. `"Peter's sister's name's \"Anna\""`</span>
<span style="color: red">B. `'Peter\'s sister\'s name\'s \"Anna\"'` </span>  
C. `"Peter's sister's name's "Anna""`
D. `'Peter's sister's name's "Anna"'`


<span style="color: blue">Question 3</span>
***

What is the expected output of the following snippet?

``` python
i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2
print(i)
```


<span style="color: red">A. 125</span>
B. 250
C. 72
D. 500

* `/` Division. The result always has type `float`.
* `//` Floor Division (also called integer Division). Return an integer.
* `**` Exponentiation. `a` raised to the power of `b`.


<span style="color: blue">Question 4</span>
***

What snippet would you insert in the line indicated below:


``` python
n = 0
    while n < 4:
        n += 1
        # insert your code here.
```

to print the following string to the monitor after the loop finishes its execution:

``` python
1 2 3 4
```

A. `print(n)`
B. `print(n, sep=" ")`
<span style="color: red">C. `print(n, end="")`</span>
D. `print(n, " ")`



<span style="color: blue">Question 5</span>
***

What is the value type returned after executing the following snippet?

``` python
x = 0
y = 2
z = len("Python")
x = y > z

print(x)

```

A. `int`
B. `float`
C. `str`
<span style="color: red">D. `bool`</span>
E. `NoneType`


<span style="color: blue">Question 6</span>
***

What will the final value of the `Val` variable be when the following snippet finishes its execution?


``` python
Val = 1
Val2 = 0

Val = Val ^ Val2

Val2 = Val ^ Val2

Val = Val ^ Val2

print(Val)
```

<span style="color: red">A. `0`</span>
B. `1`
C. `2`
D. `4`
E. The code is erroneous

* Bitwise Operators
  * ^ `a ^ b` bitwise XOR (exclusive OR) Each bit position in the result is the logical XOR of he bits in the corresponding possition of the operands. (`1` if the bits in the operands are different, `0` if they are the same).
