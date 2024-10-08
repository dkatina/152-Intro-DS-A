#============ Constants O(1)

#Assignment
x = 7
y = 9

#Math operations
a = x + y 
b = x - y

#comparison
a == b
a > b

#============ Logrithmic O(logn)

#Binary Search


#============ Linear O(n)

def double_evens_and_odds(alist):

    output = []
    odds = []

    for num in alist: #For loop indicates linear
        if num % 2 == 0: #Constants Math and Comparison ops
            output.append(num*2) #adding is constant

    for num in alist:
        if num % 2 == 1:
            odds.append(num*2)

#Measure time complexity based on worst case scenario
def search(alist, target):

    for item in alist:
        if item == target:
            return f"Found {item}"
        

alist = [1,2,3,4]
target = 5

# .count()

def my_count(alist, target):

    count= 0
    for item in alist:
        if item == target:
            count += 1

#============ Linear Log O(n Logn)

#.sort()
#sorted()

#Create a solution that turns in the highest score given a list of scores

def highest(scores):
    scores.sort() #sort() increases the timecomplexity to O(n logn)
    return scores[-1]

def highest2(scores):
    current_highest = 0
    for score in scores: #linear
        if score > current_highest:
            current_highest = score
    return score

def highest3(scores):
    highest = max(scores) #sneaky linear
    return highest


#====== Quadratic O(n^2)

#Nested linear operations

def quad(alist):

    for num in alist:
        print("Outter:", num)
        for num2 in alist:
            print("Inner:", num2)

alist = [1,2,3,4,5]
quad(alist)


def highest_count(alist):
    highest_counter = 0
    highest_num = 0

    for num in alist: #Linear

        if alist.count(num) > highest_counter: #sneaky linear
            highest_num = num
            highest_counter = alist.count(num)
    return (highest_counter, highest_num)



