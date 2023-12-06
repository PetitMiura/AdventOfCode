numbers = ['one', 'two', 'three','four','five', 'six', 'seven', 'eight', 'nine']

def sum_all(filename):
    with open(filename, 'r') as file:
        total_sum = 0

        for line in file:
            line = line.strip()
            if line:
                # Encuentra el primer dígito
                first_digit = next((char for char in line if char.isdigit()), None)
                # Encuentra la primera palabra en numbers
                first_num = next((char for char in line if char in numbers), None)
                # Encuentra el último dígito
                last_digit = next((char for char in reversed(line) if char.isdigit()), None)
                # Encuentra la ultima palabra en numbers
                last_num = next((char for char in reversed(line) if char in numbers), None)



                if first_digit is not None and last_digit is not None:
                    new_number = first_digit + last_digit
                    total_sum += int(new_number)
        
        return total_sum

result = sum_all('dataDay1.txt')
print(result)