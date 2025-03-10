import sys

def main():
    while True:
        print("\nSeleccione una aplicación:")
        print("1. Registro de jugadores y equipos en un torneo de fútbol")
        print("2. Premiación de deportistas de varias disciplinas")
        print("3. Registro de libros en una biblioteca")
        print("0. Salir")
        
        opcion = input("Ingrese su opción: ")
        if not opcion.isdigit():
            print("Opción no válida. Intente nuevamente.")
            continue
        
        opcion = int(opcion)
        if opcion == 1:
            TorneoFutbol.iniciar()
        elif opcion == 2:
            PremiacionDeportistas.iniciar()
        elif opcion == 3:
            Biblioteca.iniciar()
        elif opcion == 0:
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción no válida. Intente nuevamente.")

class TorneoFutbol:
    equipos = {}
    
    @staticmethod
    def iniciar():
        print("\n=== Registro de Torneo de Fútbol ===")
        equipo = input("Ingrese el nombre del equipo: ").strip()
        
        if not equipo:
            print("El nombre del equipo no puede estar vacío.")
            return
        
        if equipo not in TorneoFutbol.equipos:
            TorneoFutbol.equipos[equipo] = []
        
        jugador = input("Ingrese el nombre del jugador: ").strip()
        
        if not jugador:
            print("El nombre del jugador no puede estar vacío.")
            return
        
        TorneoFutbol.equipos[equipo].append(jugador)
        print(f"Jugador {jugador} registrado en el equipo {equipo}.")

class PremiacionDeportistas:
    premios = {}
    
    @staticmethod
    def iniciar():
        print("\n=== Premiación de Deportistas ===")
        deportista = input("Ingrese el nombre del deportista: ").strip()
        
        if not deportista:
            print("El nombre del deportista no puede estar vacío.")
            return
        
        premio = input("Ingrese el premio otorgado: ").strip()
        
        if not premio:
            print("El premio no puede estar vacío.")
            return
        
        if deportista not in PremiacionDeportistas.premios:
            PremiacionDeportistas.premios[deportista] = []
        PremiacionDeportistas.premios[deportista].append(premio)
        print(f"Premio {premio} otorgado a {deportista}.")

class Biblioteca:
    libros = {}
    
    @staticmethod
    def iniciar():
        print("\n=== Registro de Libros en la Biblioteca ===")
        titulo = input("Ingrese el título del libro: ").strip()
        
        if not titulo:
            print("El título del libro no puede estar vacío.")
            return
        
        autor = input("Ingrese el autor del libro: ").strip()
        
        if not autor:
            print("El nombre del autor no puede estar vacío.")
            return
        
        Biblioteca.libros[titulo] = autor
        print(f"Libro '{titulo}' de {autor} registrado.")

if __name__ == "__main__":
    main()
