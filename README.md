- [Repositório de Extratores de Características para Busca por Similaridade de Imagens](#repositório-de-extratores-de-características-para-busca-por-similaridade-de-imagens)
- [Contexto do Projeto](#contexto-do-projeto)
- [Objetivo do Repositório](#objetivo-do-repositório)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Utilizar o Repositório](#como-utilizar-o-repositório)
- [Resultados e Aplicações](#resultados-e-aplicações)


# Repositório de Extratores de Características para Busca por Similaridade de Imagens
Este repositório foi desenvolvido como parte de um projeto de pesquisa dedicado à implementação de extratores de 
características de imagens para busca por similaridade. O objetivo principal é disponibilizar uma coleção de ferramentas
computacionais que permitem a extração de características visuais de imagens, como Color Structure Descriptor (CSD), 
Color Layout Descriptor (CLD), Homogeneous Texture Descriptor (HTD), Scalable Color Descriptor (SCD) e Dominant Color 
Descriptor (DCD), e sua subsequente utilização em sistemas de busca por similaridade em bancos de dados de imagens.

# Contexto do Projeto
A busca por similaridade de imagens constitui uma área de pesquisa essencial em diversas aplicações de visão computacional,
incluindo sistemas de recomendação, detecção de plágio, análise de conteúdo visual e organização de grandes coleções de 
imagens. Nesse contexto, os extratores de características desempenham um papel central ao transformar imagens em 
representações numéricas que capturam aspectos visuais específicos, como cor, textura e layout, possibilitando comparações
eficientes entre elas. Este projeto de pesquisa foi motivado pela necessidade de implementar e testar tais extratores em 
cenários práticos, contribuindo para o avanço de técnicas de recuperação de imagens baseadas em conteúdo.

# Objetivo do Repositório
O repositório tem como objetivo principal oferecer uma implementação robusta, modular e acessível dos extratores
de características mencionados, permitindo sua integração em sistemas de busca por similaridade. Através dessas 
ferramentas, é possível extrair características de imagens, armazená-las em um espaço de busca (como um banco de dados) 
e, posteriormente, realizar consultas para identificar imagens similares com base em uma ou mais dessas características. 
O foco é facilitar tanto a experimentação por pesquisadores quanto a aplicação prática por desenvolvedores em projetos de
visão computacional.

# Tecnologias Utilizadas
O desenvolvimento do repositório foi realizado utilizando a linguagem de programação Python (versão 3.11.0b4), 
escolhida por sua ampla adoção na comunidade científica e por sua rica ecosystema de bibliotecas para processamento de 
imagens. As principais bibliotecas empregadas incluem:

- OpenCV (versão 4.9.0.80): para manipulação e pré-processamento de imagens.
- NumPy (versão 1.26.4): para operações numéricas eficientes com arrays multidimensionais.

Essas tecnologias foram selecionadas por sua robustez e compatibilidade com os requisitos computacionais do projeto.

# Como Utilizar o Repositório
Para fazer uso das ferramentas disponibilizadas neste repositório, recomenda-se seguir os passos abaixo:

1. Clonar o repositório: Utilize o comando `git clone` para baixar o repositório em sua máquina local.
2. Criar um ambiente virtual e ativá-lo. 
3. Instalar as dependências: Execute o comando `pip install -r requirements.txt` em um ambiente Python compatível para instalar as bibliotecas necessárias.
4. Explorar os exemplos: Acesse o diretório raiz/ para executar demonstrações práticas e compreender o funcionamento dos extratores em diferentes contextos. Execute algum dos arquivos *main*
5. Embora o uso do IntelliJ IDEA seja recomendado para uma experiência otimizada, qualquer IDE com suporte a Python pode ser utilizada.

# Resultados e Aplicações

A avaliação dos extratores de características foi conduzida com base em conjuntos de dados públicos, incluindo o "Pothole Image Dataset", o "Cracks and Potholes in Road" (disponíveis em repositórios como Kaggle e DatasetNinja), e o ALOI (Amsterdam Library of Object Images).
O ALOI é uma coleção de imagens coloridas de mil pequenos objetos, registrada para fins científicos. Para capturar a variação sensorial nos registros de objetos, foram sistematicamente variados o ângulo de visão, o ângulo de iluminação e a cor da iluminação para cada objeto, além de capturadas imagens estéreo de linha de base ampla.
Os resultados indicaram que determinados extratores, como o Color Structure Descriptor (CSD) e o Homogeneous Texture Descriptor (HTD), exibiram desempenho superior em relação a outros métodos testados, particularmente em condições ideais, caracterizadas por imagens uniformes e com iluminação adequada. Especificamente, o HTD destacou-se em ambientes controlados, conseguindo recuperar com precisão todas as imagens similares da base ALOI. 
Contudo, foi constatada uma redução significativa na precisão desses extratores quando submetidos a variações nas imagens, tais como rotação, presença de sombras ou ruídos, o que destaca a sensibilidade inerente dessas técnicas a perturbações externas. Ao criar uma nova base com problemas reais, como imagens de buracos nas ruas para buscar por duplicatas, o resultado do HTD não foi tão satisfatório, apresentando imagens não correlatas já nas primeiras posições do array de distância, comprometendo a identificação das imagens mais semelhantes. 
Historicamente, métodos de extração de características, como os analisados neste estudo, foram amplamente empregados em tarefas de busca por similaridade de imagens. Apesar disso, sua eficácia mostrou-se limitada em situações nas quais as imagens sofrem transformações ou distorções, comprometendo a confiabilidade dos resultados. Os experimentos realizados corroboram que, para imagens uniformes e livres de ruídos expressivos, esses extratores tradicionais conseguem atingir desempenho satisfatório. Por outro lado, em cenários mais desafiadores, caracterizados por maior heterogeneidade ou complexidade visual, os resultados evidenciam a necessidade de explorar abordagens alternativas. 
Nesse contexto, técnicas baseadas em Redes Neurais Convolucionais (CNNs) emergem como uma solução promissora, dado seu maior potencial de robustez frente a variações nas imagens e sua capacidade de generalização em diferentes condições.
Portanto, os extratores avaliados demonstram aplicabilidade em domínios específicos, como a detecção de defeitos em superfícies ou a análise de imagens com padrões visuais consistentes. No entanto, sua utilização em contextos mais amplos e diversificados exige ponderação, sendo recomendável a integração de métodos avançados, como os baseados em aprendizado profundo, para superar as limitações observadas e aprimorar a precisão em tarefas de busca por similaridade. 


 



 
 
 


 
 
 
