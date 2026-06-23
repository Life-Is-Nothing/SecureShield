#!/usr/bin/env python3
# SecureShield - Dashboard securite Linux - ibramoha2
import psutil, subprocess, time, os
from datetime import datetime

def bar(pct, width=20):
    filled = int(width * pct / 100)
    return '#' * filled + '.' * (width - filled)

def get_ssh_failures():
    try:
        result = subprocess.run(
            ['grep', 'Failed password', '/var/log/auth.log'],
            capture_output=True, text=True
        )
        lines = result.stdout.strip().split('\n')
        return len([l for l in lines if l])
    except:
        return 0

def get_connections():
    try:
        conns = psutil.net_connections(kind='inet')
        return len([c for c in conns if c.status == 'ESTABLISHED'])
    except:
        return 0

def display():
    os.system('clear')
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ssh_fails = get_ssh_failures()
    conns = get_connections()

    print(f'\n  SecureShield - {datetime.now():%Y-%m-%d %H:%M:%S}')
    print('  ' + '='*46)
    print(f'  CPU    : {cpu:5.1f}%  [{bar(cpu)}]')
    print(f'  RAM    : {ram:5.1f}%  [{bar(ram)}]')
    print(f'  Disque : {disk:5.1f}%  [{bar(disk)}]')
    print('  ' + '-'*46)
    status = 'CRITIQUE' if ssh_fails > 20 else 'ALERTE' if ssh_fails > 5 else 'OK'
    print(f'  SSH    : {ssh_fails} echecs  [{status}]')
    print(f'  Reseau : {conns} connexions etablies')
    print('  ' + '='*46)

if __name__ == '__main__':
    print('[*] SecureShield demarre... (Ctrl+C pour arreter)')
    while True:
        try:
            display()
            time.sleep(5)
        except KeyboardInterrupt:
            print('\n[*] Arret SecureShield.')
            break
