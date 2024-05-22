# refat-2 O QUE VAI MUDAR ?

Em reunião do dia 20/05 foi acordado: 

- [ ] retirar a função de distância de cada classe e criar um nova classe para distâncias
- [ ] criar classe  `Descritor` => Link ou agregado de extrator com distância
- [ ] classe operador de busca => dado um objeto, consultar com base em um critéro
  - knn, wide-join, raio de _abrangência (r)_ e quantos _(k)_ devem ser escolhidos

___

Responsabilidade de cada classe extratora: 
- Método para extrair características 
- construtor padrão
- NÃO TEM responsabilidade de medir distância 
- NÃO TEM responsabilidade de abrir imagem ou manipular. 