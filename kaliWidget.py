#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from colorama import Fore, Style
import os
import time


def banner():
    print('')
    os.system('clear')
    banner = '''
            ██╗  ██╗ █████╗ ██╗     ██╗
            ██║ ██╔╝██╔══██╗██║     ██║
            █████╔╝ ███████║██║     ██║
            ██╔═██╗ ██╔══██║██║     ██║
            ██║  ██╗██║  ██║███████╗██║
            ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
           '''
    banner1 = '''
    ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗
    ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝
    ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   
    ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   
    ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   
     ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝  (By onix) 
           '''
    print(banner + Fore.BLUE + banner1 + Fore.RESET)
    os.system('jp2a --color --width=40  kali-banner.png')


def main():

    # Instalación de jp2a
    os.system('clear')
    print(Fore.GREEN + Style.BRIGHT + '''
    ╔════════════════════════════════════╗
    ║ Se instalara jp2a antes de iniciar ║
    ╚════════════════════════════════════╝
    ''' + Style.RESET_ALL)
    time.sleep(1)
    os.system('sudo apt-get update')
    os.system('sudo apt-get install jp2a')
    time.sleep(1)

    while True:
        banner()

        time.sleep(1)
        print('\n' + Fore.YELLOW + Style.BRIGHT + '[!] Advetencia: ' + Style.RESET_ALL + 'El contenido de esta aplicación solo\n'
                                                                                        'funciona en el entorno de escritorio xfce - Kali Linux.')
        time.sleep(1)

        pregunta = input(Fore.BLUE + Style.BRIGHT + '\n[+] ' + Style.RESET_ALL + '¿Estas en xfce? - [S/N]\n' + Fore.GREEN + '» ' + Style.RESET_ALL)
        time.sleep(2)

        if pregunta.lower() == 's':
            break

        elif pregunta.lower() == 'n':
            print(Fore.RED + Style.BRIGHT + '\n[!] ' + Style.RESET_ALL + 'Saliendo del programa.')
            time.sleep(2)
            exit()

        else:
            print(Fore.RED + Style.BRIGHT + '\n[✗] ' + Style.RESET_ALL + 'Haz ingresado un dato no valido\n' + Style.BRIGHT + '    Vuelve a intentarlo' + Style.RESET_ALL)
            time.sleep(2)
            os.system('clear')

    os.system('clear')

    while True:
        print(Fore.YELLOW + '''
    ╔═══════════════════════════╗
    ║ Se instalara lo siguiente ║
    ╠═══════════════════════════╣
    ╠»      Targeted            ║
    ╠»      IP VPN              ║
    ╠»      IP Ethernet         ║
    ╚═══════════════════════════╝
      ¿Deseas continuar? [S/N]
        ''' + Fore.RESET)
        resp = input(Fore.GREEN + '» ' + Style.RESET_ALL)

        if resp.lower() == 's':

            # Copiando archivos
            time.sleep(1)
            print(Fore.BLUE + Style.BRIGHT + '\n[+] ' + Style.RESET_ALL + 'Copiando archivos.')
            os.system('cp -r Archivos/bin ~/.config')
            time.sleep(2)

            # Dando permidos de ejecucion
            time.sleep(1)
            print(Fore.BLUE + Style.BRIGHT + '\n[+] ' + Style.RESET_ALL + 'Dando permisos correspondientes de ejecución.')
            os.system('chmod +x ~/.config/bin/target.sh')
            os.system('chmod +x ~/.config/bin/ethernet.sh')
            os.system('chmod +x ~/.config/bin/vpnip.sh')
            time.sleep(2)

            # Integrando settarget a .zshrc
            time.sleep(1)
            print(Fore.BLUE + Style.BRIGHT + '\n[+] ' + Style.RESET_ALL + 'Integrando settarget a .zshrc')
            os.system("""echo '
# settargeted
function settarget(){
    ip_address=$1
    machine_name=$2
    echo "$ip_address $machine_name" > $HOME/.config/bin/target/target.txt
}' >> ~/.zshrc """)

            # Guia para el usuario
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n═════════════════════════════════════════════════════════════' + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n[→] ' + Style.RESET_ALL + 'Quedo todo listo, ahora es tu turno.\n')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n[1] ' + Style.RESET_ALL + 'Eliminina el' + Style.BRIGHT + ' motor generico ' + Style.RESET_ALL + 'que Kali tiene por defecto, guiate\n'
                                                                           '    del siguiente video: https://i.imgur.com/6jRe3jT.mp4\n')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n[2] ' + Style.RESET_ALL + 'Ahora toca activar' + Style.BRIGHT + ' Targeted ' + Style.RESET_ALL + 'guiate\n'
                                                                           '    del siguiente video: https://i.imgur.com/4Xuzdgi.mp4\n'
                                                                           '    Enlace: /home/tuusuario/.config/bin/target.sh\n')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n[3] ' + Style.RESET_ALL + 'El siguiente es' + Style.BRIGHT + ' IP VPN ' + Style.RESET_ALL + 'guiate\n'
                                                                           '    del siguiente video: https://i.imgur.com/BunV9M7.mp4\n'
                                                                           '    Enlace: /home/tuusuario/.config/bin/vpnip.sh \n')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n[4] ' + Style.RESET_ALL + 'Por ultimo' + Style.BRIGHT + ' IP Ethernet ' + Style.RESET_ALL + 'guiate\n'
                                                                           '    del siguiente video: https://i.imgur.com/IHKxldr.mp4\n'
                                                                           '    Enlace: /home/tuusuario/.config/bin/ethernet.sh')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n═════════════════════════════════════════════════════════════' + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.CYAN + Style.BRIGHT + '\n[?] ' + Style.RESET_ALL + 'Quiza al ejecutar el script el area de trabajo se haya disminuido a 1\n'
                                                                           '    guiate del video: https://i.imgur.com/nkoUR9q.mp4\n'
                                                                           '    si no es asi, omitir esto.')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + '\n═════════════════════════════════════════════════════════════' + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.BLUE + Style.BRIGHT + '\n[✔] ' + Style.RESET_ALL + 'Espero haber ayudado.')
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + '\n[✗] ' + Style.RESET_ALL + 'Saliendo del programa . . .')
            time.sleep(2)
            break

        elif pregunta.lower() == 'n':
            print(Fore.RED + Style.BRIGHT + '\n[!] ' + Style.RESET_ALL + 'Saliendo del programa.')
            time.sleep(2)
            exit()

        else:
            print(Fore.RED + Style.BRIGHT + '\n[✗] ' + Style.RESET_ALL + 'Haz ingresado un dato no valido\n' + Style.BRIGHT + '    Vuelve a intentarlo' + Style.RESET_ALL)
            time.sleep(2)
            os.system('clear')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + '\n\n[!] ' + Style.RESET_ALL + 'Script interrumpido, Saliendo del programa . . .')
        time.sleep(2)
        exit()
