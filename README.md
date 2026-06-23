# SecureShield

> Dashboard de securite Linux en temps reel — surveillance systeme, alertes et rapports.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)
![Author](https://img.shields.io/badge/Author-ibramoha2-CC0000?style=flat-square)

## Fonctionnalites
- Surveillance CPU, RAM, disque en temps reel
- Detection des connexions reseau suspectes
- Alertes sur les tentatives SSH echouees
- Surveillance des processus anormaux
- Rapport HTML genere automatiquement

## Installation
```bash
git clone https://github.com/ibramoha2/SecureShield
cd SecureShield
pip install -r requirements.txt
python shield.py
```

## Screenshot
```
============ SecureShield Dashboard ============
CPU    : 23%   [####..................]
RAM    : 61%   [############..........]
Disque : 44%   [########..............]
SSH    : 3 tentatives echouees (derniere: 192.168.1.105)
Reseau : 12 connexions actives
================================================
```

**Auteur :** [@ibramoha2](https://github.com/ibramoha2) | Niger