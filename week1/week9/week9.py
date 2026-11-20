my_list = [55, 76, "hello", True, 98.6]

my_list.append("apple")
my_list.append(76)

my_list.insert(3, "cat")

my_list.insert(0, 99)

hello_index = my_list.index("hello")

count_76 = my_list.count(76)

my_list.remove(76)

my_list.pop(my_list.index(True))


def sum_evens(number_list):
    total = 0
    for number in number_list:
        if number % 2 == 0:
            total += number
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def count_five_letter(words):
    counter = 0
    for word in words:
        if len(word) == 5:
            counter += 1
    return counter

mylist = ["hahaa", "catat", "datat", "aasdasd"]



def newnew_list(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            break
        total += number
    return total


nums = [1, 3, 5, 8, 2, 7]



def count_up_to_sam(words):
    newtotal = 0
    for word in words:
        newtotal += 1
        if word == "sam":
            break
    return newtotal


words = ["merhaba", "dünya", "saam", "selam", "python"]



def replace(s, old,new):
    pieces = s.split(old)
    return new.join(pieces)

def test(actual, expected):
    if actual == expected:
        print("PASSED")
    else:
        print("FAILED")

test(replace('Mississippi','i','I'),expected='MIssIssIppI')


def max(numbers):
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max

print(max([4, 19, -2, 19, 7]))  # 19
print(max([-8, -2, -15]))       # -2
print(max([42]))                # 42