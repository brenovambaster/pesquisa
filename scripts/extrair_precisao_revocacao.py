class ExtraiPrecisaoRevocao:
    TAMANHO_DA_BASE = 4000

    def compute(self, array, classe, num_imgs_por_classe=20, dir_base_imgs='base_imgs_testes/'):
        """

        :param array: Saída da função all_knn, apenas o caminho das imagens
        :param classe: classe da imagem que está sendo analisada
        :param num_imgs_por_classe: Quantidade de imagens que cada classe na base
        :param dir_base_imgs: Diretório base das imagens para pesquisar
        :return:
        """
        size_of_array = len(array)
        count = 0
        recall = []
        precision = []
        k = 1
        for i in array:
            # pegar apenas a classe da imagem
            nome_img = i.replace(f'{dir_base_imgs}', '').replace('../', '').split('_')[0]

            if nome_img == classe:
                count += 1

            precision.append(float(format(count / (array.index(i) + 1), '.3f')))
            recall.append(float(format(k / self.TAMANHO_DA_BASE, '.6f')))
            k += 1

        return precision, recall
