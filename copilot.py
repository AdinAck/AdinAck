# a function that returns the fibonacci sequence at a given index
def fib(n):
    """This function returns the nth Fibonacci number."""
    i = 0
    j = 1
    n = n - 1

    while n >= 0:
        i, j = j, i + j
        n = n - 1
    return i


def binary_search(array, value):
    """This function searches for a value in an array using binary search"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def factorial(n):
    """This function returns the factorial of n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# create a taylor series of sinx
def taylor_series(x, n):
    """This function returns the nth value of the taylor series of sin(x)"""
    return sum(
        (((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))) for i in range(n)
    )


# open a file and read its contents
def read_file(filename):
    """This function reads the contents of a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # print("Sorry, the file " + filename + " does not exist.")
        pass
    else:
        print(contents)


# cross multiply two matrices
def matrix_multiply(A, B):
    """This function multiplies two matrices"""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


"""
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""


def format_number(number):
    """This function formats a number with commas"""
    number = str(number)
    if len(number) <= 3:
        return number
    else:
        return format_number(number[:-3]) + "," + number[-3:]


"""
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""


def consecutive_zeros(string):
    """This function returns the biggest number of consecutive zeros in a string"""
    biggest = 0
    current = 0
    for i in range(len(string)):
        if string[i] == "0":
            current += 1
        else:
            current = 0
        if current > biggest:
            biggest = current
    return biggest


"""
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""


def add_dots(string):
    """This function adds dots between each letter in a string"""
    new_string = ""
    for letter in string:
        new_string += letter + "."
    return new_string[:-1]


def remove_dots(string):
    """This function removes dots from a string"""
    return string.replace(".", "")


# fast forier tranform
def fft(x):
    import cmath

    """This function returns the fast forier transform of a list of numbers"""
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [
        even[k] - T[k] for k in range(N // 2)
    ]


# normalize vector
def norm(x):
    """This function returns the norm of a list of numbers"""
    return sum(i ** 2 for i in x) ** (1 / 2)


# implement a matrix camera look-at function
def look_at(pos, target, up):
    """This function returns a camera matrix that will look at a target position"""
    from math import cos, sin, pi

    f = target - pos
    f /= norm(f)
    s = cross(f, up)
    s /= norm(s)
    u = cross(s, f)
    u /= norm(u)
    return [
        [u[0], s[0], -f[0], 0],
        [u[1], s[1], -f[1], 0],
        [u[2], s[2], -f[2], 0],
        [0, 0, 0, 1],
    ]


# matrix camera perspective
def perspective(fov, aspect, near, far):
    """This function returns a camera matrix that will create a perspective projection"""
    from math import tan, pi

    f = 1 / tan(fov / 2)
    return [
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0],
    ]


# create an ecryption algorithm using sha256
def sha256(message):
    """This function returns a sha256 hash of a message"""
    import hashlib

    return hashlib.sha256(message.encode()).hexdigest()


# compute the longest common substring given two strings
def lcs(s1, s2):
    """This function returns the longest common substring of two strings"""
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest : x_longest]


# compute the longest common subsequence given two strings
def lcs_recursive(s1, s2):
    """This function returns the longest common subsequence of two strings"""
    if s1 == "" or s2 == "":
        return ""
    if s1[-1] == s2[-1]:
        return lcs_recursive(s1[:-1], s2[:-1]) + s1[-1]
    else:
        return max(lcs_recursive(s1, s2[:-1]), lcs_recursive(s1[:-1], s2), key=len)


if __name__ == "__main__":
    print(fib(9))
    print(taylor_series(2, 4))
    print(lcs("ABCDGH", "ACDGHR"))
    print(lcs_recursive("AGGTAB", "GXTXAYB"))
    print(consecutive_zeros("1001101000110"))
    print(add_dots("test"))
    print(remove_dots("t.e.s.t"))
    # print(look_at([0, 0, 0], [0, 0, 0], [0, 0, 0]))
    print(perspective(45, 1, 0.1, 1))
    print(sha256("hello world"))

