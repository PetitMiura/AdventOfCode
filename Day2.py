def sum_possible_games(file_name):
    game_sum = 0  # Inicializa la variable para almacenar la suma de los números de juego posibles

    with open(file_name, 'r') as file:  # Abre el archivo en modo lectura
        for line in file:  # Itera sobre cada línea del archivo
            line = line.strip()  # Elimina espacios en blanco al principio y al final de la línea
            game_id, cube_info = line.split(': ')  # Divide la línea en el número de juego y la información de los cubos

            # Extrae solo el número del juego y conviértelo a entero
            game_id = int(game_id.replace('Game', '').strip())

            cube_info = cube_info.split(';')  # Divide la información de los cubos en subconjuntos

            is_possible = True  # Bandera para verificar si el juego es posible

            # Verifica cada subconjunto de cubos para cada juego
            for subset in cube_info:
                red_count = green_count = blue_count = 0  # Inicializa contadores para los cubos de cada color
                cubes = subset.split(', ')  # Divide el subconjunto en cubos individuales

                # Cuenta la cantidad de cubos de cada color en el subconjunto
                for cube in cubes:
                    count, color = cube.split()
                    count = int(count)

                    # Incrementa el contador del color correspondiente
                    if color == 'red':
                        red_count += count
                    elif color == 'green':
                        green_count += count
                    elif color == 'blue':
                        blue_count += count

                # Verifica si alguna cantidad supera el límite establecido
                if red_count > 12 or green_count > 13 or blue_count > 14:
                    is_possible = False  # Establece la bandera como False si los límites se exceden
                    break  # Sale del bucle actual

            # Si el juego es posible, agrega su número al total de la suma
            if is_possible:
                game_sum += game_id

    return game_sum  # Devuelve la suma total de los números de juego posibles

# Ejemplo de uso
result = sum_possible_games('dataDay2.txt')  # Llama a la función con el nombre del archivo
print(result)  # Imprime la suma de los números de juego posibles
