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

<span style="color: blue">Question 7</span>
***

Which line can be used instead of the comment to cause the snippet to produce the following exepected output? (Select all that apply)

Code:

``` python
z, y, x = 2, 1, 0
x, z = z, y
y = y - z

# put line here

```
Excected output:
`0, 1, 2`

<span style="color: red">A. `x, y, z = y, z, x`</span>
<span style="color: red">B. `z, y, x = x, z, y`</span>
C. `y, z, x = x, y, z`
D. The code is erroneous

<span style="color: blue">Question 8</span>
***

What is the expected output of the following snippet?

``` python
a = 0
b = a ** 0
if b < a + 1:
    c = 10
elif b == 1:
    c = 2
else:
    c = 3

print(a + b + c)
```

A. `1`
B. `2`
<span style="color: red">C. `3`</span>
D. The code is erroneous

<span style="color: blue">Question 9</span>
***
How many stars (*) does the following snippet print?


``` python
i = 10

while i > 0:
    i -= 3
    print("*")

    if i <= 3:
        break

else:
    print("*")
```

<span style="color:red">A. three</span>
B. two
C. One
D. The code is erroneous


<span style="color: blue">Question 10</span>
***

How many lines does each of the followin code examples output when run separately?

``` python
# Example 1
for i in range(1, 4, 2):
    print("*")

# Example 2
for i in range(1, 4, 2):
    print("*", end="")

# Example 3
for i in range(1, 4, 2):
    print("*", end="**")

# Example 4
for i in range(1, 4, 2):
    print("*", end="***")
print("***")
```

<span style="color:red">A. Example 1: two, Example 2: one, Example 3: one, Example 4: one</span>
B. Example 1: two, Example 2: one, Example 3: one, Example 4: two
C. Example 1: two, Example 2: one, Example 3: two, Example 4: three
D. Example 1: one, Example 2: one, Example 3: one, Example 4: two


> ## Note:
The end parameter is used to append any string at the end of the output of the print statement in python
By default python’s print() function ends with a newline.
By default, the value of this parameter is '\n'.
