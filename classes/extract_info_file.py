# Função para ler o arquivo e processar as linhas
def process_file(file_path):
    # Abrir o arquivo no modo de leitura
    with open(file_path, 'r') as file:
        # Ler todas as linhas do arquivo
        lines = file.readlines()

    # Lista para armazenar os dados processados
    data = []

    # Processar cada linha do arquivo
    for line in lines:
        # Remover possíveis espaços em branco nas extremidades da linha
        line = line.strip()

        # Dividir a linha pelos delimitadores "|"
        parts = line.split('|')

        # Dicionário para armazenar os dados da linha
        line_data = {}

        # Processar cada parte da linha
        for part in parts:
            # Dividir a parte pela primeira ocorrência do caractere "="
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()

            # Tratar valores especiais como listas ou floats
            if value.startswith('[') and value.endswith(']'):
                value = eval(value)  # Avaliar a string como uma lista
            elif '.' in value:
                value = float(value)  # Converter para float
            else:
                value = int(value)  # Converter para int

            # Adicionar o par chave-valor ao dicionário
            line_data[key] = value

        # Adicionar o dicionário da linha à lista de dados
        data.append(line_data)

    return data




# Exemplo de uso
file_path = 'dados.txt'  # Caminho para o arquivo de dados
dados = process_file("../output/dados.txt")

# Exibir os dados lidos do arquivo
for dado in dados:
    print(dado)

    # Acessar valores individuais, como lat e long
    lat = dado.get('lat')
    long = dado.get('long')
    print(f"Latitude: {lat}, Longitude: {long}")
