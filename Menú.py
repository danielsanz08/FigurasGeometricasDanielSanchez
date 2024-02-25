from rich.console import Console
from rich.table import Table
from Validacion import es_float, es_int
from Circulo import Circulo
from Triangulo import Triangulo
from Rectangulo import Rectangulo

console = Console()

# Tabla de bienvenida
table_bienvenida = Table(show_header=True, header_style="italic blue")
table_bienvenida.add_column("Bienvenido a la calculadora de áreas de figuras geométricas", style="dim", width=33)
table_bienvenida.add_row("By: Daniel Sánchez")

# Tabla de figuras disponibles
table_figuras = Table(show_header=True, header_style="italic green", width=50)
table_figuras.add_column("Figuras disponibles", style="dim", width=20)
table_figuras.add_row("[italic red]1.[italic red]", "[italic red]● Círculo[italic red]")
table_figuras.add_row("[italic yellow]2.[italic yellow]", "[italic yellow]▲ Triángulo[italic yellow]")
table_figuras.add_row("[italic yellow]3.[italic blue]", "[italic blue]■ Rectángulo[italic blue]")
table_figuras.add_row("[italic magenta]4.[italic magenta]", "[italic magenta]⚠️ Salir[italic magenta]")

console.print(table_bienvenida, table_figuras)

while True:
    opcion = es_int(console.input("[bold green]Digite un número segun la tabla [bold green]\n"))

    if opcion == 1:
        radio = es_float(console.input("[bold red]Digite la medida del radio: [bold red]"))
        circulo = Circulo(radio)
        circulo.calcular_area()
        console.print("[bold red]...[bold red]")
        console.print(f"[bold red]El área del círculo es: {circulo.area}[bold red]")

    elif opcion == 2:
        base = es_float(console.input("[bold yellow]Digite la base del triángulo:[bold yellow]"))
        altura = es_float(console.input("[bold yellow]Digite la altura del triángulo: [bold yellow]"))
        triangulo = Triangulo(base, altura)
        triangulo.calcular_area()
        console.print("[bold yellow]...[bold yellow]")
        console.print(f"[bold yellow]El área del triángulo es: {triangulo.area}[bold yellow]")

    elif opcion == 3:
        base_r = es_float(console.input("[bold blue]Digite la base del rectángulo:[bold blue]"))
        altura_r = es_float(console.input("[bold blue]Digite la altura del rectángulo: [bold blue]"))
        rectangulo = Rectangulo(base_r, altura_r)
        rectangulo.calcular_area()
        console.print("[bold blue]...[bold blue]")
        console.print(f"[bold blue]El área del rectángulo es: {rectangulo.area}[bold blue]")

    elif opcion == 4:
        console.print("[bold magenta]Saliendo del programa.[bold magenta]")
        break

    else:
        console.print("[bold magenta]Opción inválida. Por favor, elija una opción válida.[bold magenta]")
