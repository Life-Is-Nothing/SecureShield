#!/usr/bin/env python3
"""
SecureShield — Real-time Security Dashboard
Author: Mohamed Adoungouss Ibrahim (@ibramoha2)
"""

import subprocess
import json
import datetime
import os
import socket
import platform

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
    except:
        return "N/A"

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "uptime": run("uptime -p"),
        "kernel": run("uname -r"),
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_users():
    return run("who").split('\n') if run("who") else []

def get_failed_logins():
    return run("grep 'Failed password' /var/log/auth.log 2>/dev/null | tail -10")

def get_open_ports():
    return run("ss -tlnp | grep LISTEN")

def get_processes():
    return run("ps aux --sort=-%cpu | head -10")

def get_disk():
    return run("df -h /")

def get_memory():
    return run("free -h")

def get_network():
    return run("ss -s")

def check_services():
    services = ["ufw", "fail2ban", "ssh", "crowdsec", "auditd"]
    results = {}
    for svc in services:
        status = run(f"systemctl is-active {svc} 2>/dev/null")
        results[svc] = "✅ active" if status == "active" else "❌ " + status
    return results

def generate_html_report():
    info = get_system_info()
    services = check_services()
    
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="30">
<title>SecureShield Dashboard</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#0a0a0a; color:#00ff41; font-family:'Courier New',monospace; padding:20px; }}
  h1 {{ color:#ff0000; font-size:2em; text-align:center; margin-bottom:10px; text-shadow: 0 0 10px #ff0000; }}
  .subtitle {{ text-align:center; color:#666; margin-bottom:30px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(350px,1fr)); gap:20px; }}
  .card {{ background:#111; border:1px solid #00ff41; border-radius:8px; padding:20px; }}
  .card h2 {{ color:#ff0000; margin-bottom:15px; border-bottom:1px solid #333; padding-bottom:8px; }}
  .card pre {{ font-size:0.8em; white-space:pre-wrap; color:#ccc; }}
  .ok {{ color:#00ff41; }} .err {{ color:#ff0000; }} .warn {{ color:#ffaa00; }}
  .stat {{ display:flex; justify-content:space-between; padding:5px 0; border-bottom:1px solid #1a1a1a; }}
  .badge {{ padding:2px 8px; border-radius:4px; font-size:0.8em; }}
  .badge-ok {{ background:#003300; color:#00ff41; }} .badge-err {{ background:#330000; color:#ff0000; }}
  footer {{ text-align:center; margin-top:30px; color:#333; }}
</style>
</head>
<body>
<h1>🛡️ SecureShield Dashboard</h1>
<p class="subtitle">Généré le {info['date']} | {info['hostname']}</p>
<div class="grid">

<div class="card">
  <h2>🖥️ Système</h2>
  <div class="stat"><span>Hostname</span><span class="ok">{info['hostname']}</span></div>
  <div class="stat"><span>OS</span><span>{info['os'][:40]}</span></div>
  <div class="stat"><span>Uptime</span><span class="ok">{info['uptime']}</span></div>
  <div class="stat"><span>Kernel</span><span>{info['kernel']}</span></div>
</div>

<div class="card">
  <h2>🔒 Services de Sécurité</h2>
  {"".join(f'<div class="stat"><span>{k}</span><span class="{"ok" if "active" in v else "err"}">{v}</span></div>' for k,v in services.items())}
</div>

<div class="card">
  <h2>💾 Mémoire & Disque</h2>
  <pre>{get_memory()}</pre>
  <br><pre>{get_disk()}</pre>
</div>

<div class="card">
  <h2>🌐 Ports ouverts</h2>
  <pre>{get_open_ports() or 'Aucun port détecté'}</pre>
</div>

<div class="card">
  <h2>⚠️ Dernières tentatives échouées</h2>
  <pre class="err">{get_failed_logins() or 'Aucune tentative récente'}</pre>
</div>

<div class="card">
  <h2>👤 Utilisateurs connectés</h2>
  <pre>{"chr(10).join(get_users()) or 'Aucun utilisateur connecté'}</pre>
</div>

</div>
<footer>SecureShield v1.0 — Mohamed Adoungouss Ibrahim | Niger 🇳🇪</footer>
</body>
</html>"""
    
    with open("dashboard.html", "w") as f:
        f.write(html)
    print("[+] Dashboard généré : dashboard.html")

def cli_report():
    print("\n" + "="*60)
    print("  🛡️  SECURESHIELD — Security Dashboard")
    print("="*60)
    info = get_system_info()
    for k, v in info.items():
        print(f"  {k:12} : {v}")
    print("\n[🔒 Services]")
    for k, v in check_services().items():
        print(f"  {k:12} : {v}")
    print("\n[🌐 Ports ouverts]")
    print(get_open_ports())
    print("\n[💾 Mémoire]")
    print(get_memory())
    print("="*60)

if __name__ == "__main__":
    import sys
    if "--html" in sys.argv:
        generate_html_report()
    else:
        cli_report()
