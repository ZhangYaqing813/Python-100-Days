def is_palindrome(num):
    tmp = num
    total=0
    while tmp >0:
        total = total*10 + tmp % 10
        tmp //= 10
    
    return total == num


def main():
    s = is_palindrome(121)
    print(s)


if __name__ == "__main__":
    main()
    
    