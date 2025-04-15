# Como Utilizar o Repositório

Para fazer uso das ferramentas disponibilizadas neste repositório, recomenda-se seguir os passos abaixo:

1. **Clonar o repositório**: Utilize o comando `git clone` para baixar o repositório em sua máquina local.

2. **Configurar ambiente**: 
   - Crie um ambiente virtual Python: `python -m venv venv`
   - Ative o ambiente virtual:
     - Windows: `venv\Scripts\activate`
     - Linux/Mac: `source venv/bin/activate`
   - Instale as dependências: Execute o comando `pip install -r requirements.txt`

3. **Configurar diretório de imagens**:
   - Defina o diretório onde suas imagens para análise estão armazenadas `base_imgs_testes/` 
   - Verifique se as imagens estão em formatos suportados (JPG, PNG, etc.).

4. **Gerar vetores de características**:
   - Execute o script específico para extrair características das imagens no diretório configurado.`scripts/generate_all_databases.py` 
   - Os vetores gerados serão armazenados em arquivos que servirão como base para pesquisas posteriores.
   - Por exemplo: `python scripts/generate_all_databases.py `

5. **Realizar pesquisa por similaridade**:
   - Escolha uma imagem de consulta e selecione qual descritor deseja utilizar (CSD, CLD, HTD, SCD ou DCD).
   - Execute o script de busca, indicando a imagem de consulta e o descritor escolhido.
   - Por exemplo: `python mainHTD.py`
   - O sistema retornará as imagens mais semelhantes encontradas na base, ordenadas por similaridade.

6. **Explorar exemplos**: Acesse o diretório `raiz/` para executar demonstrações práticas e compreender o funcionamento dos extratores em diferentes contextos. Execute algum dos arquivos *main* para ver exemplos de uso completos.

Embora o uso do IntelliJ IDEA seja recomendado para uma experiência otimizada, qualquer IDE com suporte a Python pode ser utilizada para trabalhar com este repositório.
