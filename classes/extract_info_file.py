def read_file(file_path):
    """
    This function reads a file and returns its lines as a list.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    list: A list of lines in the file.

    Raises:
    IOError: If the file cannot be opened.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except IOError:
        print(f"Error opening file: {file_path}")
        return []

def process_line(line):
    """
    This function processes a line from the file and returns a dictionary of key-value pairs.

    Parameters:
    line (str): The line to be processed.

    Returns:
    dict: A dictionary where the keys are the identifiers before the '=' character and the values are the corresponding
    values after the '=' character.
    """
    line_data = {}
    parts = line.strip().split('|')

    for part in parts:
        key, value = part.split('=', 1)
        key = key.strip()
        value = value.strip()

        if value.startswith('[') and value.endswith(']'):
            value = parse_list(value)
        elif '.' in value:
            value = float(value)
        else:
            value = int(value)

        line_data[key] = value

    return line_data

def parse_list(value):
    """
    This function parses a string representation of a list and returns a list of integers or floats.

    Parameters:
    value (str): The string representation of a list.

    Returns:
    list: A list of integers or floats.
    """
    value = value[1:-1].split(',')
    return [float(v) if '.' in v else int(v) for v in value]

def process_file(file_path):
    """
    This function processes a file and returns a list of dictionaries. Each dictionary represents a line in the file.

    Parameters:
    file_path (str): The path to the file to be processed.

    Returns:
    list: A list of dictionaries. Each dictionary represents a line in the file.
    """
    lines = read_file(file_path)
    data = [process_line(line) for line in lines]
    return data

# Exemplo de uso
file_path = '../output/dados.txt'  # Caminho para o arquivo de dados
dados = process_file(file_path)

# Exibir os dados lidos do arquivo
for dado in dados:
    print(dado)
    # Acessar valores individuais, como lat e long
    lat = dado.get('lat')
    long = dado.get('long')
    print(f"Latitude: {lat}, Longitude: {long}")
    print("--------------------------------------------------------------\n")
