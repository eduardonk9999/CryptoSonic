# CryptoSonic

CryptoSonic é um projeto em Python que monitora o preço do Bitcoin e reproduz um som quando há uma variação significativa no preço.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/eduardonk9999/CryptoSonic.git
    cd CryptoSonic
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Coloque o arquivo de áudio `la-ele-manoel-gomes.mp3` no diretório do projeto.
2. Execute o script `cryptoSonic.bat`:
    ```sh
    ./cryptoSonic.bat
    ```

## Dependências

- Python 3.13
- pygame
- requests
