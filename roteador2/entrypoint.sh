#!/bin/bash
echo "[ENTRYPONT] Script entrypoint.sh foi executado!"

# Ativa o roteamento IP no sistema (essencial para funcionar como roteador)
echo 1 > /proc/sys/net/ipv4/ip_forward

# Adiciona regra de NAT para permitir tráfego entre redes conectadas ao roteador
iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE

# Inicia o script principal do roteador
python3 roteador.py

echo "[ENTRYPONT] roteador.py terminou."
