def is_valid(n):
    n = str(n)
    return ('5' in n and '7' not in n) or ('7' in n and '5' not in n)

def find_number():
    count = 0
    num = 0
    while count < 1000:
        num += 1
        if is_valid(num):
            count += 1
    return num

print(find_number())