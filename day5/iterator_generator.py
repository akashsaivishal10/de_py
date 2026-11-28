# 1. What is an Iterator?
# An iterator is an object that allows you to access elements one at a time.

# Python uses two important methods:
# - iter() – converts an iterable into an iterator.
# - next() – retrieves the next element from an iterator.

# Example 1: Basic iterator
import csv

numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Traceback (most recent call last):
#   File "D:\DE\de_py\day5\iterator_generator.py", line 17, in <module>
#     print(next(iterator))
#           ~~~~^^^^^^^^^^
# Example 2: StopIteration
# What happens when there are no more elements?

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
numbers = [10, 20]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
    except StopIteration:
        break


def countDown(n):
    print("starting")
    while n > 0:
        print("about to yield", n)
        yield n
        print("resumed after ", n)
        n = n - 1
        print("done")


gen = countDown(2)
print("created, nothing printed yet")
print("got", next(gen))
print("got", next(gen))


# 6. Generator Expressions
# Similar to list comprehensions, Python supports generator expressions.
# List comprehension:
numbers = [x * x for x in range(1, 6)]
print(numbers)
# Generator expression:
numbers = (x * x for x in range(1, 9))
print(numbers)
for number in numbers:
    print(number)


# Real time examples :
def read_customers(file_path):

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


customers = read_customers("customers.csv")
for customer in customers:
    print(customer)
