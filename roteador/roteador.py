import threading
import socket
import time
import sys
import json

print("[ROTEADOR R1] INÍCIO DO SCRIPT")
sys.stdout.flush()
time.sleep(1)

lsdb = {}
lsdb_lock = threading.Lock()

def receber():
    print("[THREAD RECEBER R1] Iniciada.")
    sys.stdout.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind(("0.0.0.0", 5000))
        print("[RECEBER R1] Escutando na porta 5000 (UDP)")
        sys.stdout.flush()
        while True:
            try:
                dados, addr = sock.recvfrom(1024)
                mensagem = dados.decode()
                pacote = json.loads(mensagem)
                print(f"[RECEBER R1] De {addr}: ID={pacote['id']} | Vizinhos={pacote['vizinhos']} | Custos={pacote['custos']}")
                sys.stdout.flush()

                with lsdb_lock:
                    lsdb[pacote["id"]] = {
                        "vizinhos": pacote["vizinhos"],
                        "custos": pacote["custos"]
                    }
                    print(f"[LSDB R1] Atualizada: {json.dumps(lsdb, indent=2)}")
                    sys.stdout.flush()
                    executar_dijkstra("R1", lsdb)

            except Exception as e:
                print(f"[ERRO RECEBER R1] Durante recebimento: {e}")
                sys.stdout.flush()
            time.sleep(1)
    except OSError as e:
        print(f"[ERRO RECEBER R1] Falha ao abrir porta 5000: {e}")
        sys.stdout.flush()

def enviar():
    print("[THREAD ENVIAR R1] Iniciada.")
    sys.stdout.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destinos = [("roteador2", 5000), ("roteador3", 5000)]  # Conectado a R2 e R3
    print(f"[DEBUG R1] Enviando para {destinos}")
    sys.stdout.flush()
    time.sleep(5)

    while True:
        try:
            pacote = {
                "id": "R1",
                "vizinhos": ["R2", "R3"],
                "custos": {"R2": 1, "R3": 1}
            }
            mensagem = json.dumps(pacote)
            for destino in destinos:
                sock.sendto(mensagem.encode(), destino)
                print(f"[ENVIAR R1] Enviado para {destino}: {mensagem}")
                sys.stdout.flush()
        except Exception as e:
            print(f"[ERRO ENVIAR R1] {e}")
            sys.stdout.flush()
        time.sleep(5)

def executar_dijkstra(origem, lsdb):
    distancias = {no: float("inf") for no in lsdb}
    anteriores = {}
    visitados = set()
    distancias[origem] = 0

    while len(visitados) < len(lsdb):
        atual = min((no for no in lsdb if no not in visitados), key=lambda n: distancias[n], default=None)
        if atual is None:
            break

        visitados.add(atual)
        for vizinho in lsdb[atual]["vizinhos"]:
            if vizinho not in lsdb:
                continue
            custo = lsdb[atual]["custos"].get(vizinho, float("inf"))
            if distancias[atual] + custo < distancias[vizinho]:
                distancias[vizinho] = distancias[atual] + custo
                anteriores[vizinho] = atual

    caminhos = {}
    for destino in lsdb:
        if destino == origem:
            continue
        caminho = []
        atual = destino
        while atual in anteriores:
            caminho.insert(0, atual)
            atual = anteriores[atual]
        if caminho:
            caminho.insert(0, origem)
            caminhos[destino] = caminho

    print(f"\n[DIJKSTRA R1] Caminhos calculados a partir de {origem}:")
    for destino, caminho in caminhos.items():
        print(f" - {origem} → {destino}: {' → '.join(caminho)} (Custo: {distancias[destino]})")
    sys.stdout.flush()

print("\n[ROTEADOR R1] Script roteador.py foi iniciado com sucesso!\n")
sys.stdout.flush()

thread_receber = threading.Thread(target=receber)
thread_enviar = threading.Thread(target=enviar)

thread_receber.start()
thread_enviar.start()

while True:
    time.sleep(1)