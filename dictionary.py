my_dict  ={}
my_dict={1: 'apple', 2: 'banana', 3: 'cherry'}
print(my_dict)

my_dict["4"]="orange"
print(my_dict)

my_dict={"name": "John", "age": 30, "city": "New York"}
print(my_dict)
my_dict["hobby"]="reading"
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.clear()
print(my_dict)


def test (lst):
    my_dict={}
    for i in lst:
        my_dict[i[0]]= i[1:]
    return my_dict
students=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print(students)
print(test(students))



