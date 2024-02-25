from rich.console import Console

console = Console()

def es_float(valor):
    while True:
        try:
            numero = float(valor)
            return numero
        except ValueError:
            console.print("[italic magenta]Error: La entrada debe ser un número real.[/italic magenta]")
            valor = console.input("[italic magenta]Por favor, ingrese un número real: [/italic magenta]")

def es_int(valor):
    while True:
        try:
            numero = int(valor)
            return numero
        except ValueError:
            console.print("[italic red]Error: La entrada debe ser un número entero.[/italic red]")
            valor = console.input("[italic magenta]Por favor, ingrese un número entero: [/italic magenta]")
