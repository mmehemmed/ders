# 1. Simple problem

def simple_problem(a, b):
    digits = list(str(a))
    return f"{digits[0]} {digits[1]}"

# 2. Digits

def sum_of_digits(n):
    return len(str(n))

# 10. Gardener

def gardener_days_skipped(N):
    skipped_days = 0
    remaining_water = 0.5  # Half a bucket of water
    for i in range(N, 0, -1):
        remaining_water -= 1 / i
        if remaining_water >= 0:
            skipped_days += 1
        else:
            break
    return skipped_days

# 14. The Ticket Chase

def passengers_to_prime(N, start_ticket):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for passengers in range(N):
        if is_prime(start_ticket + passengers):
            return passengers
    return -1

# 19. Degree of symmetry

def degree_of_symmetry(n):
    n = str(n)
    return sum(1 for i in range(len(n) // 2 + 1) if n[i] == n[-i - 1])

# 29. The level of palindrome

def palindrome_level(m):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    level = 0
    while not is_palindrome(m):
        m += int(str(m)[::-1])
        level += 1
    return level

# 31. Superstitious Santa Claus

def count_friday_13(K, years):
    import calendar

    unlucky_days = 0
    for start_year, end_year in years:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                if calendar.weekday(year, month, 13) == 4:  # Friday
                    unlucky_days += 1
    return unlucky_days

# 34. The word of sponsor

def count_sponsor_word_occurrences(word, sponsor):
    return sponsor.count(word)
