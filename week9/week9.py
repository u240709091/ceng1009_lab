def is_odd(n):
    return n % 2 != 0


print(is_odd(5))
print(is_odd(4))
### Example 2

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2023))
### Example 2

def print_triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(f"{i} {total}")
### Example 3
print_triangular_numbers(5)
def print_triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(f"{i} {total}")


print_triangular_numbers(5)

### Example 4

def reverse(s):
    result=""
    for ch in s:
        result= ch+ result
    return result
print(reverse("hello world"))
### Example 5

def reverse_slice(s):
    s[::-1]

print(reverse_slice("hello world"))
### Example 6

def remove_all_occurrences(sub, s):
    return s.replace(sub, " ")
print(remove_all_occurrences("l", "hello world"))

####7
def substution(message, key):
    alphabet = "abcçdefghıijklmnoöprsştuüvyz"
    result = ""
    for ch in message:
        index = alphabet.find(ch.lower())
        if index == -1:
            result = result + ch
        elif ch.isupper():
            result = result + key[index].upper()  # Parantez yerine köşeli parantez []
        else:
            result = result + key[index].lower()  # Parantez yerine köşeli parantez []

    return result

key = "qtgjungtsşplnvbzçxlşıkjhydrg"
print(substution("hello, world", key))


def remove_dups(s):
    result = ""
    for ch in s:
        if ch not in result:
         result = result + ch

    return result
print(remove_dups("hello, world"))

