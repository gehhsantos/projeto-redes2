# Projeto de Redes de Computadores 2

Este projeto simula uma rede de computadores utilizando **Docker** e **Docker Compose**, composta por **três roteadores interligados** e **quatro hosts**, divididos em **duas subredes**. O objetivo principal é aplicar conceitos de **roteamento, troca de mensagens via UDP**, e **cálculo de rotas com o algoritmo de Dijkstra**.

---

## Estrutura da Rede

![Diagrama da Rede](imgs/diagrama.png)


## Tecnologias Utilizadas

- Docker
- Docker Compose
- Python 3.9
- Redes Virtuais Bridge
- UDP
- Algoritmo de Dijkstra (em Python)

---

##  Topologia da Rede

A rede é composta por:

- **Subrede 1** (`192.168.10.0/24`)
  - Host1
  - Host2
  - Roteador1

- **Subrede 2** (`192.168.20.0/24`)
  - Host3
  - Host4
  - Roteador2

- **Rede Backbone** (`172.77.0.0/24`)
  - Roteador1
  - Roteador2
  - Roteador3

**Conexões entre roteadores:**
- R1 ↔ R2
- R2 ↔ R3
- R3 ↔ R1

---

## Como Executar o Projeto

1. Clone o repositório:

   ```bash```
   git clone https://github.com/gehhsantos/projeto-redes2.git
   cd projeto-redes2 

2. Construa e execute os containers com Docker Compose:

 ```bash```
docker-compose up --build

3. Para interromper a simulação, pressione Ctrl + C no terminal onde o Docker está rodando ou execute:

``` bash```

docker-compose down


---

## Licença

Este projeto é apenas para fins acadêmicos da disciplina **Redes de Computadores 2**.

---

> Projeto desenvolvido por Geovana Santos — UFPI – Sistemas de Informação

