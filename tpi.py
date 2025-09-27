import random
import threading
from rich.console import Console

console = Console()

random_integer = random.randint(1, 100)
random_binary = bin(random_integer)[2:]

def decimal_a_binario(n):
    decimal_counter = n
    correct_bin = []

    while decimal_counter > 0:
        remainder = decimal_counter % 2
        decimal_counter = decimal_counter // 2
        correct_bin.append(str(remainder))

    correct_bin.reverse()
    correct_bin = ''.join(correct_bin)

    return correct_bin

def binario_a_decimal(n):
    binary_str = str(n)
    decimal_value = 0
    console.print(f'Binario random: {binary_str}')
    reversed_binary = list(binary_str)
    reversed_binary.reverse()
    console.print(f'Binario reverse: {reversed_binary}')

    for i in range(0, len(binary_str)):
        bit = int(reversed_binary[i])
        decimal_value += bit * (2 ** i)
        console.print(f'Decimal: {decimal_value}')

    return decimal_value


def juego_decimal_a_binario():   
    console.print("[blue]>> Ejecutando juego Decimal a Binario...[/blue]")
    console.print("[bold cyan]=== Juego: Decimal a Binario ===[/bold cyan]")
    console.print("Convierte el siguiente número decimal a binario:\n")
    console.print(f"[bold yellow]Número: {random_integer}[/bold yellow]\n")
    bin_user = input("Ingresa el resultado en binario:")
    console.print("[bold cyan]=== Calculando... ===[/bold cyan]")

    # Calculamos el binario del numero random

    correct_bin = decimal_a_binario(random_integer)
    
    # Mostramos el resultado

    if(bin_user == correct_bin):
        console.print(f"\n[green]✅ Correcto![/green]El decimal {random_integer} es igual al binario [bold green]{correct_bin}[/bold green]")
    else:
        console.print(f"\n[red]❌ Incorrecto[/red]. La respuesta correcta era [bold green]{correct_bin}[/bold green]")
     
    

def juego_binario_a_decimal():        
    console.print("[bold cyan]=== Juego: Binario a Decimal ===[/bold cyan]")
    console.print("Convierte el siguiente número binario a decimal:")
    console.print(f"[bold yellow]Número: {random_binary}[/bold yellow]\n")
    decimal_user = input("Ingresa el resultado en decimal:")

    console.print("[bold cyan]=== Calculando... ===[/bold cyan]")

    correct_decimal = binario_a_decimal(random_binary)

    if(decimal_user == str(correct_decimal)):
        console.print(f"\n[green]✅ Correcto![/green]. El numero binario {random_binary} es el decimal [bold green]{correct_decimal}[/bold green]")
    else:
        console.print(f"\n[red]❌ Incorrecto[/red]. La respuesta correcta era [bold green]{correct_decimal}[/bold green]")


def desafio_contrarreloj():        
    # dummy screen 
    console.print("[bold cyan]=== Desafío Contrarreloj ===[/bold cyan]")

    # TODO: habilitar la opcion de elegir entre decimal a binario y viceversa

    decimals = []
    binaries = []
    success_count = 0

    for i in range(0, 5):
        r_decimal = random.randint(1,100)
        r_binaries = decimal_a_binario(r_decimal)

        decimals.append(r_decimal)
        binaries.append(r_binaries)

    console.print("Responde [bold magenta]5 preguntas en un minuto[/bold magenta], ¿te crees capaz?.")
    start_or_menu = console.input("[green]El tiempo empieza al ingresar 1, ingresa 0 para volver al menu:[/green].")

    if(start_or_menu == "1"):
        game_on = True  
        console.print("[bold red]¡Tiempo iniciado![/bold red] Tienes 60 segundos para responder 5 preguntas.\n")
    else:
        console.print("[bold yellow]Volviendo al menú...[/bold yellow]")
        return

    def timeout():
        nonlocal game_on
        game_on = False
        console.print("\n[bold red]¡Tiempo terminado![/bold red]")
        console.print("\n[bold green]¡Fin del desafío![/bold green]")
        console.print(f"Aciertos: [bold blue]{success_count}/5[/bold blue]")
        console.print("[bold yellow]Apreta enter Enter para volver al menú...[/bold yellow]")
    
    timer = threading.Timer(60, timeout)
    timer.start()

    while game_on == True and timer.is_alive() == True:

     for i in range(0, 5):
        if game_on == False:
            break
        console.print(f"[bold]Pregunta {i+1} de 5:[/bold]")
        console.print(f"Convierte {decimals[i]} → binario")
        bin_user = input("Tu respuesta: ")
        if game_on == False:
            break
        if(int(bin_user) == int(binaries[i])):
            console.print(f"[green]✅ Correcto![/green]El decimal {decimals[i]} es igual al binario [bold green]{binaries[i]}[/bold green]\n")
            success_count += 1
        else:
            console.print(f"[red]❌ Incorrecto[/red]. La respuesta correcta era [bold green]{binaries[i]}[/bold green]\n")
    
    timer.cancel()
    console.print("\n[bold green]¡Fin del desafío![/bold green]")
    console.print(f"Aciertos: [bold blue]{success_count}/5[/bold blue]")
    return


def tutorial_decimal_a_binario():        
    # dummy screen
    console.print("[bold cyan]=== Tutorial: Decimal a Binario ===[/bold cyan]")
    console.print("Número a convertir: [bold yellow]23[/bold yellow]\n")

    console.print("Paso 1: 23 ÷ 2 → Cociente: 11, Resto: 1")
    console.print("Paso 2: 11 ÷ 2 → Cociente: 5, Resto: 1")
    console.print("Paso 3: 5 ÷ 2 → Cociente: 2, Resto: 1")
    console.print("Paso 4: 2 ÷ 2 → Cociente: 1, Resto: 0")
    console.print("Paso 5: 1 ÷ 2 → Cociente: 0, Resto: 1\n")

    console.print("Lee los restos de abajo hacia arriba → [bold green]10111₂[/bold green]\n")
    console.print("Presiona [green]Enter[/green] para probar otro número.")

    # si la multiplataforma no lo complica, agregar un pause entre cada paso
    # para hacerlo un oco mas interactivo y facil de seguir


def tutorial_binario_a_decimal():        
    # dummy screen
    console.print("[bold cyan]=== Tutorial: Binario a Decimal ===[/bold cyan]")
    console.print("Número a convertir: [bold yellow]10101[/bold yellow]\n")

    console.print("Expansión paso a paso:")
    console.print("1*(2^4) + 0*(2^3) + 1*(2^2) + 0*(2^1) + 1*(2^0)")
    console.print("= 16 + 0 + 4 + 0 + 1")
    console.print("= [bold green]21[/bold green]\n")

    console.print("Presiona [green]Enter[/green] para probar otro número.")

    # si la multiplataforma no lo complica, agregar un pause entre cada paso
    # para hacerlo un oco mas interactivo y facil de seguir


def menu():
    while True:
        console.print("\n[bold cyan]=== MENÚ PRINCIPAL ===[/bold cyan]")
        console.print("[bold green]1[/bold green]. [white]Juego: convertir número decimal a binario[/white]")
        console.print("[bold green]2[/bold green]. [white]Juego: convertir número binario a decimal[/white]")
        console.print("[bold green]3[/bold green]. [white]Desafío contrarreloj: responde X conversiones en el menor tiempo posible[/white]")
        console.print("[bold green]4[/bold green]. [white]Tutorial interactivo: aprender conversión de decimal a binario[/white]")
        console.print("[bold green]5[/bold green]. [white]Tutorial interactivo: aprender conversión de binario a decimal[/white]")
        console.print("[bold green]0[/bold green]. [white]Salir[/white]")

        opcion = console.input("[yellow]Elige una opción: [/yellow]")

        if opcion == "1":
            juego_decimal_a_binario()
        elif opcion == "2":
            juego_binario_a_decimal()
        elif opcion == "3":
            desafio_contrarreloj()
        elif opcion == "4":
            tutorial_decimal_a_binario()
        elif opcion == "5":
            tutorial_binario_a_decimal()
        elif opcion == "0":
            console.print("[bold red]Saliendo...[/bold red]")
            break
        else:
            console.print("[bold red]Opción inválida, intenta de nuevo.[/bold red]")

if __name__ == "__main__":
    menu()
