# convert two lists into dictionaries
# Merge two dictionaries into one
# Print the value of key of any selected value
# Check if a value exist in a dictionary or not
# Rename a given key of any word of your choice. 
# Get the minimum value from the following dictionary

# Convert two lists into dictionary

keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty']
values = [10,20,30,40,50]

def combine1():
    print(keys)
    print(values)
    print(keys, values)
    numbers_dictionary = dict(zip(keys, values))
    print(numbers_dictionary)
combine1()
def combine2():
    num_dict = {}
    for i in range(len(keys)):
        num_dict.update({keys[i]:values[i]})
    print(num_dict)
combine2()
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}
dict2 = {'Sixty': 60, 'Seventy': 70, 'Eighty': 80, 'Ninety': 90, 'hundred': 100}

# Merge two dictionaries into one
def merger():
    print(dict1.update(dict2))
merger()