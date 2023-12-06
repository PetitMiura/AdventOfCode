def sum_all_v2(filename):
    # Mapeo de palabras a dígitos
    word_to_digit = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Función para encontrar el primer dígito (número o palabra)
    def find_first_digit(line):
        for i, char in enumerate(line):
            if char.isdigit():
                return char
            for word, digit in word_to_digit.items():
                if line[i:].startswith(word):
                    return digit
        return None

    # Función para encontrar el último dígito (número o palabra)
    def find_last_digit(line):
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                return line[i]
            for word, digit in word_to_digit.items():
                if line[i-len(word)+1:i+1] == word:
                    return digit
        return None

    # Calcula la suma total de todos los valores de calibración
    with open(filename, 'r') as file:
        total_sum = 0
        for line in file:
            line = line.strip()
            first_digit = find_first_digit(line)
            last_digit = find_last_digit(line)
            if first_digit and last_digit:
                total_sum += int(first_digit + last_digit)
                print(first_digit + last_digit)
        return total_sum
result = sum_all_v2('dataDay1.txt')
print(result)