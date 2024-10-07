### Lecture notes

#### Importance of Data Structures


- **Efficient Retrieval of Data**
- **Optimized Storage Utilization**
- **Enhanced Algorithmic Performance**


#### Data Structures:
With the primary function of data structures being to store information, each data structure has it's own unique features that lend it to being useful in specific scenarios

##### Lists:
Lists are ordered collections of items, allowing for sequential storage and retrieval
```python
# Example of a list in the library
fiction_books = ["Dune", "1984", "Brave New World", "Neuromancer"]
```

##### Dictionaries:
Dictionaries are key-value pairs, providing a fast and flexible way to retrieve information.

```python
# Example of a dictionary in the library
book_locations = {
    "Dune": "Fiction Section, Shelf 1",
    "1984": "Fiction Section, Shelf 2",
    "Brave New World": "Fiction Section, Shelf 3",
    "Neuromancer": "Fiction Section, Shelf 4"
}
```

##### Linked Lists:
Are products of OOP constisting of a Node Class, and a List Class. Node objects carry a value or "data", and also have an attribute "next" which points to the next node in the chain. You build your list by starting with a Head node and continually adding the next node

![Linked List](https://media.geeksforgeeks.org/wp-content/uploads/20220829110944/LLdrawio.png)

```python
# Example of a linked list in the library
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a linked list
head = Node("Book1")
head.next = Node("Book2")
head.next.next = Node("Book3")

# Resulting linked list:
#   Book1 -> Book2 -> Book3
```

#### Others we will talk more about:
- **Stacks:** Collections that follow the LIFO order (Last in First out) *(stack of pancakes)*
- **Queues:** Collections that follow the FIFO order (First in First out) *(song queue)*
- **Binary Trees:** Similar to linked lists we create TreeNode objects that have data, but instead of a "next" attribute they have a left and right attributes that point to other TreeNodes, creating a Node Heirarchy commonly used to store categories with sub-categories
- **Graphs:** Just wait and see :)

#### Time and Space Complexity

**Time Complexity**: How we denote/ measure the execution time of our code as it scales with input size

**Space Complexity**: Measures the memory usage of our algo, also taking into account how it will scale with input.

#### Big O Notation
https://www.bigocalc.com/
Big O notation is the measurement scale we use to lable the execution time of the code, O representing the number of operations we do, and n the size of our input.

|| Big O | Efficiency | 
|-----|-------|--------|
| Best/Fastest|O(1)| Constant|
||O(Log n)| Logrithmic|
||O(n)| Linear|
||O(n logn)| Linear Logrithmic|
|Worst/Slowest..|O(n^2)| Quadratic

![Big O Graph](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

**Constant**: Assignment operations, math operations, and comparison operations.
**Logrithmic**: Binary Search (we'll learn this later)
**Linear**: for loops, many built-in methods(count,index,replace,etc.) (any time you need to perform an operation FOR every item in the input)
**Linear Logrithmic**: Sorting functions (.sort(), sorted())
**Quadractic**: Whenever you have nested Linear operations you (Nested for loops, .count() inside a for loop)

### Time and Space Complexity of Python Lists

**Accessing Elements**: Indexing into a list happens in constant time
```python
treasures = ['gold', 'gems', 'diamonds']
print(treasures[1])  # Accessing the second stone
```

**Adding Elements**
- **.append()**: happens in constant time O(1), becuase this process doesn't involve moving/rearranging the items already in the list.
- **.insert()**: Requires the rearrangement for pre-existing elements to accomodate the incoming element, which makes it O(n) linear

**Removing Elements**: 
.remove() is also Linear, becuase once the item is removed, the other items have to slide over to fill in the gaps.
**Sorting Elements**: 
.sort(), is based off of the Timsort algorith which is O(n logn)

**Membership Checks**:
When checking if an element is **IN** a list, python works through each element comparing it to the one we are looking for. This makes list membership checks O(n) Linear

### Time and Space Complexity of Python Dictionaries

**Adding Elements**
Because Dictionaries are unordered, there is no 'insert' in the middle or 'append' to the end. We simply add it to the collection and this happens in constant time

**Accessing Elements**
We unlock values stored in our dictionaries with keys, and when we key into the dictionary this also happens in constant time O(1).

**Deleting Elements**
Again, because there is no order to dictionaries, when we remove items, there is no space to be filled causing other items to have to move. So deleting is also constant.

**Membership Checks**:
Because all keys of a dictionary are unique, when we go to see if a key exists in our dictionary, it is just as quick as trying to access this value. Therefor membership checks also happen in constant time O(1)
