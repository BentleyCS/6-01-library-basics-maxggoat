#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


import analytics

# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    newPrices = []
    for x in rawPrices:
        y=analytics.apply_markup(x, 0.15)
        newPrices.append(y)
    rawPrices = newPrices
    return rawPrices

x=[10,20,30,40,50,60,70,80,90]
print(process_expenses(x))

# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    x=analytics.get_average(n)
    y=analytics.get_highest(n)
    return x, y

analyze_scores(x)
print(analyze_scores(x))

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(n):
    x=analytics.clean_text(n)
    return x

x=["   Dogs Are Cool","  Max will play division 1 football        "]
print(sanitize_usernames(x))


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(n):
    x=analytics.filter_threshold(n,100)
    return x
x=[10,110,20,300,999,23]
print(identify_outliers(x))

def binarySearch(items:list, target):
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

    L=0
    H=len(items)-1
    i=1
    F=0
    while L<=H:

        M=(L+H)//2
        if H-L==1:
            M=L
        if items[M] == target:
            F=1
            break
        if items[M] < target:
            L=M+1
        if items[M] > target:
            H=M-1
        i+=1

    if F == 1:
        return M
    else:
        return -1

# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case words with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(list1, list2):
    list3=list1.copy()
    list3=analytics.clean_text(list3)
    M = binarySearch(list3,list2)
    return M

x=["  Apple", "Banana ", "  CHERRY  ", " date "]
print(search_and_report(x,"date"))




