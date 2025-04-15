def find_first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None

nums = [10, 20, 30, 40, 50, 30, 20, 10]
first_duplicate = find_first_duplicate(nums)

if first_duplicate:
    print("First duplicate is:", first_duplicate)
else:
    print("No duplicates found.")
