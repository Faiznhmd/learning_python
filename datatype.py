# A data type tells Python what kind of value a variable is storing.


# 1. str = str("Hlo world")
# 2. int = int(5)
# 3. float = float(5.5)
# 4. complex = complex(1, 2)
# 5. list = list[1, 2, 3]
# 6. tuple = tuple((1, 2, 3))
# 7. range = range(1, 10)
# 8. dict = dict({"name": "Faizan", "age": 21})
# 9. set = set([1, 2, 3])
# 10. frozenset = frozenset([1, 2, 3])
# 11. bool = bool(True)
# 12. bytes = bytes(b"Hello")
# 13. bytearray = bytearray(b"Hello")
# 14. memoryview = memoryview(bytes(5))
# 15. NoneType = None : no value

#  lets go into deeper into data types in python

# Lists: Lists are used to store multiple items in a single variable
fruits = ["apple", "banana", "mango"]
print(fruits[0])

# 1. Mutable : we can change it.
fruits[1] = "orange"
print(fruits)

# 2. Allow duplicates
fruits.append("apple")
print(fruits)

# 3. index start from zero
# 4. syntax [  ]

# Tuples: Tuples are used to store multiple items in a single variable

# 1. Immutable : we can not change it.
# 2. Allow Duplicates
# 3. index start from zero
# 4. Tuples are faster than lists
# 4.Representation: Tuples are represented by parentheses ().

# Sets: A set stores multiple unique values.
numbers = {1, 2, 3, 3, 4}
print(numbers)

# 1. no duplicates allowed
# 2.  Mutable can add remove items
# 3. Sets are unordered, so you cannot be sure in which order the items will appear.
# 4. syntax  {  }


# dict: It stores data in key-value pairs.
user = {
    "name": "Zeeshan",
    "age": 25,
    "city": "Mithapur"
}
print(user["name"])