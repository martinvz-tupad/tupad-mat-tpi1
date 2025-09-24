from rich.console import Console

console = Console()


def juego_decimal_a_binario():    
    # dummy screen
    console.print("[blue]>> Ejecutando juego Decimal a Binario...[/blue]")
    console.print("[bold cyan]=== Juego: Decimal a Binario ===[/bold cyan]")
    console.print("Convierte el siguiente número decimal a binario:\n")
    console.print("[bold yellow]Número: 25[/bold yellow]\n")
    console.print("Ingresa el resultado en binario: [white]_[/white]")
    console.print("\n[green]✅ Correcto![/green] 25 = 11001₂")
    

def juego_binario_a_decimal():        
    # dummy screen 
    console.print("[bold cyan]=== Juego: Binario a Decimal ===[/bold cyan]")
    console.print("Convierte el siguiente número binario a decimal:\n")
    console.print("[bold yellow]Número: 10110[/bold yellow]\n")
    console.print("Ingresa el resultado en decimal: [white]_[/white]")
    console.print("\n[red]❌ Incorrecto[/red]. La respuesta correcta era [bold green]22[/bold green]")


def desafio_contrarreloj():        
    # dummy screen 
    console.print("[bold cyan]=== Desafío Contrarreloj ===[/bold cyan]")
    console.print("Responde [bold magenta]5 preguntas[/bold magenta] lo más rápido posible.")
    console.print("El tiempo empieza al presionar [green]Enter[/green].\n")
    console.print("[bold]Pregunta 1 de 5:[/bold]")
    console.print("Convierte 13 → binario")
    console.print("Tu respuesta: [white]_[/white]")

    # TODO: agregar el listado de respuestas (correctas incorrectas) 
    # tal cual lo hace la plataforma de la UTN con las autoevaluaciones
    # usar listas para guardar las respuestas (lista de listas)

    console.print("\n[bold green]¡Fin del desafío![/bold green]")
    console.print("Aciertos: [bold blue]4/5[/bold blue]")
    console.print("Tiempo total: [bold yellow]42 segundos[/bold yellow]")


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
