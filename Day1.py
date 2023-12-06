def sum_all(filename):
    with open(filename, 'r') as file:
        total_sum = 0

        for line in file:
            line = line.strip()
            if line:
                # Encuentra el primer dígito
                first_digit = next((char for char in line if char.isdigit()), None)
                # Encuentra el último dígito
                last_digit = next((char for char in reversed(line) if char.isdigit()), None)

                if first_digit is not None and last_digit is not None:
                    new_number = first_digit + last_digit
                    total_sum += int(new_number)
        
        return total_sum

result = sum_all('dataDay1.txt')
print(result)