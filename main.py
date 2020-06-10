def find_numbers(numbers):
    result = []
    for index, item in enumerate(numbers):
        if index == len(numbers) - 1:
            break
        next_number = numbers[index+1]
        numbers_sum = item + next_number
        if numbers_sum in numbers:
            pair_set = {item, next_number}
            if pair_set in result:
                continue
            result.append(pair_set)
    return result

