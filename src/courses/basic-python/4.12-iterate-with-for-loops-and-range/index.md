---
lesson_name: Iterate with For Loops and Range
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 250
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 249
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

### Iterate with for loops and range

In Python, there is a property of an object called **iterable**, which means it can be iterated or looped through. For example, with string data, we can iterate through each character, we can iterate through each item in a list, or iterate through each key-value pair in a dictionary. We can use a `for...loop` statement with these objects.

<div class="alert-info text-sm">
In Python, everything is considered an <b>object</b>, such as the number 1 is an object of the integer type, or the string "Hello World" is also an object.
</div>

In Python, the `range()` function is commonly used when creating loops. The `range()` function generates a sequence of numbers that can be used in loops or other operations.

For example:

```python
my_numbers = []
for i in range(5):
    my_numbers.append(i)
print(my_numbers) # [0, 1, 2, 3, 4]
```

The first line creates an empty list called `my_numbers`.

`for i in range(5)` is a `for...loop` that will run five times, as specified by the argument passed to the `range()` function. The range function generates a sequence of integers from 0 up to (but not including) the argument passed to it.

On each iteration of the loop, the variable `i` is assigned the next integer in the sequence generated by the `range()` function.

The `append` method is called on `my_numbers` for each value of `i` in the loop, adding the value to the end of the list.

After the loop has finished, the list `my_numbers` is printed using the `print()` function. The output shows the list of integers from 0 to 4, as generated by the range function and appended to the list.

---

### Exercise

<ul>
<li id="test-1">Use <code>for...loop</code> to make the list <code>my_numbers</code> contains the numbers from 0 to 10.</li>
</ul>