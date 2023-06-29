def Mitmorning():
    print("This is MIT Morning class")


Mitmorning()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(x - y)
    print(x / y)


calculate()


def Majina(myfirstname, mylastname, age):
    print("my name is ", myfirstname + " " + mylastname, "and my age is ", age)


Majina("Stacy", "Mula", 19)
Majina("Evans", "Ichalai", 34)
Majina("Ariana", "Mise", 9)
Majina("John", "Milton", 18)
Majina("Eunice", "Muliro", 34)


# calculate a function that is going to give an average [2.5,6,3,5]
def calculate_Average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = [3, 6, 8, 9, 2, 1, 8]
result = calculate_Average(data)
print("The average data is", result)
# create a function that will create a palandrome (the longest string)
