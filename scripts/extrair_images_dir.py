import os
import shutil


# Função para extrair imagens de diretórios de 1 a 15 e copiá-las para o diretório raiz

def copiar_imagens(root_dir):
    __QUANTIDADE_DE_IMAGENS_NO_DIR = 12
    __QUANTIDADE_DE_CLASSES = 11  # Quantidade de pastas que tem dentro do diretório raiz

    # Percorrer todos os diretórios de 1 a N (Quantidade de classes, cada diretório representa uma classe)
    for i in range(1, __QUANTIDADE_DE_CLASSES + 1):
        # Caminho do diretório atual
        current_dir = os.path.join(root_dir, str(i))

        # Verifica se o diretório existe
        if os.path.exists(current_dir) and os.path.isdir(current_dir):
            # Lista todos os arquivos no diretório atual
            arquivos = os.listdir(current_dir)

            # Filtra apenas arquivos de imagem (extensões comuns)
            imagens = [f for f in arquivos if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

            # Copia cada imagem para o diretório raiz
            counter = 0
            for img in imagens:
                if counter == __QUANTIDADE_DE_IMAGENS_NO_DIR:
                    break
                source = os.path.join(current_dir, img)
                destination = os.path.join(root_dir, img)

                # Verifica se o arquivo já existe no destino para evitar sobreposição
                if not os.path.exists(destination):
                    shutil.copy(source, destination)
                    counter += 1
                else:
                    print(f"Arquivo {img} já existe no destino. Ignorando...")


# Chama a função
copiar_imagens('../database/')
