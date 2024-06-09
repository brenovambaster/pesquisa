
# Extratores de características

<!-- TOC -->
* [Extratores de características](#extratores-de-características)
  * [Description](#description)
  * [Installation](#installation)
  * [Dependencies](#dependencies)
  * [DATA-SETS](#data-sets)
  * [TODO](#todo)
  * [License](#license)
  * [Contact](#contact)
<!-- TOC -->

| Anotações       | Arquivo                                 |
|-----------------|-----------------------------------------|
| Notas da branch | [o quem sido feito](./refat-2_NOTAS.md) |
| To-do list      |                                         |


## Description

Extratores implementados para extração de características de imagens:

- [x] **Color Structure Descriptor (CSD)**
- [x] **Color Layout Descriptor (CLD)**
- [x] **Homogeneous Texture Descriptor (HTD)**
- [x] **Scalable Color Descriptor (SCD)**
- [x] **Dominant Color Descriptor (DCD)** 

It's recommended to use IntelliJ IDEA to run the project, but you can use any IDE that supports Python.

## Installation

To install this project, follow these steps:

1. Clone the repository.
2. Run the setup script.
3. Install the required dependencies. `pip install -r requirements.txt`

## Dependencies
* Phython 3.11.0b4
* OpenCV 4.9.0.80
* Numpy  1.26.4
* pip 24.0

## DATA-SETS
- https://www.kaggle.com/datasets/sachinpatel21/pothole-image-dataset?resource=download
- https://datasetninja.com/cracks-and-potholes-in-road

## TODO
- [ ] Fazer a extração para todas a images e gravar em um arquivo (.csv ou não), 
        depois medir a distância entre cada uma das imagens.

## License

This project is licensed under the MIT License. See the LICENSE.md file for more details.

## Contact

bvcl@aluno.ifnmg.edu.br



