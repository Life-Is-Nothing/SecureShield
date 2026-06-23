# 📊 SecureShield

> Real-time Security Monitoring Dashboard for Linux — by [@ibramoha2](https://github.com/ibramoha2)

## 🔧 Fonctionnalités

- 🖥️ Info système (hostname, uptime, kernel)
- 🔒 Statut services sécurité (UFW, fail2ban, CrowdSec, auditd)
- 🌐 Ports ouverts en écoute
- ⚠️ Tentatives de connexion échouées (auth.log)
- 👤 Utilisateurs connectés
- 💾 Mémoire & disque
- 🌍 Dashboard HTML auto-rafraîchi (30s)

## 🚀 Usage

```bash
# Mode CLI
python3 secureshield.py

# Mode HTML Dashboard
python3 secureshield.py --html
xdg-open dashboard.html
```

## 👤 Auteur
**Mohamed Adoungouss Ibrahim** | DUT Cybersécurité | Niger 🇳🇪
