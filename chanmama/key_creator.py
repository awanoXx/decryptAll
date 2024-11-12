#密钥生成器，v2版本是：Kj7pQr4Df8s6tXbW，v1版本是：cmmgfgehahweuuii
def to_base36(n):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if n == 0:
        return '0'
    sign = ''
    if n < 0:
        sign = '-'
        n = -n
    res = ''
    while n:
        n, i = divmod(n, 36)
        res = digits[i] + res
    return sign + res

# Function to simulate the anonymous function in JS
def transform(e, *args):
    t = list(args)
    t.reverse()
    return ''.join([chr(ti - e - 24 - ni) for ni, ti in enumerate(t)])


# Part 1
part1 = ''.join([chr(ord(c) - 39) for c in to_base36(27).lower()])  # 'K'

# Part 2
part2 = to_base36(24901).lower()  # 'j7p'

# Part 3
part3 = ''.join([chr(ord(c) - 39) for c in to_base36(33).lower()])  # 'Q'

# Part 4
part4 = to_base36(976).lower()  # 'r4'

# Part 5
part5 = ''.join([chr(ord(c) - 39) for c in to_base36(20).lower()])  # 'D'

# Part 6
part6 = transform(10, 127, 154, 91, 151, 91, 136)  # 'f8s6tX'

# Part 7
part7 = to_base36(11).lower()  # 'b'

# Part 8
part8 = ''.join([chr(ord(c) - 13) for c in to_base36(13).lower()])  # 'W'

final_string = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8  # 'Kj7pQr4Df8s6tXbW'


# Print the results
print("最终字符串:", final_string)         # 输出: Kj7pQr4Df8s6tXbW

