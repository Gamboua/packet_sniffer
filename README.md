# Packet Sniffer com MongoDB

Este projeto é uma aplicação Python que captura pacotes de rede, armazena os dados no MongoDB e exibe estatísticas sobre o tráfego.

## Funcionalidades:
- Captura pacotes de uma interface de rede especificada.
- Armazena os seguintes campos dos pacotes no MongoDB: IP de origem, IP de destino, protocolo e tamanho.
- Exibe estatísticas como o número total de pacotes capturados, pacotes por protocolo e os 5 principais IPs de origem e destino com mais tráfego.
- Executa continuamente até ser interrompido pelo usuário.

## Requisitos:
- Docker
- Docker Compose

## Como executar o projeto:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/packet-sniffer.git
   cd packet-sniffer
    ```
2. Construa e inicie os containers usando Docker Compose:
```bash
    docker-compose up --build
```
3. A aplicação começará a capturar pacotes de rede. Pressione Ctrl+C para interromper e ver as estatísticas.

4. Os pacotes capturados serão armazenados no MongoDB, que está disponível na porta 27017 do host.

