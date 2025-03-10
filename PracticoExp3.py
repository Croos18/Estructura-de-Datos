using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int opcion;
        do
        {
            Console.WriteLine("\nSeleccione una aplicación:");
            Console.WriteLine("1. Registro de jugadores y equipos en un torneo de fútbol");
            Console.WriteLine("2. Premiación de deportistas de varias disciplinas");
            Console.WriteLine("3. Registro de libros en una biblioteca");
            Console.WriteLine("0. Salir");
            Console.Write("Ingrese su opción: ");
            
            if (!int.TryParse(Console.ReadLine(), out opcion))
            {
                Console.WriteLine("Opción no válida. Intente nuevamente.");
                continue;
            }

            switch (opcion)
            {
                case 1:
                    TorneoFutbol.Iniciar();
                    break;
                case 2:
                    PremiacionDeportistas.Iniciar();
                    break;
                case 3:
                    Biblioteca.Iniciar();
                    break;
                case 0:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Intente nuevamente.");
                    break;
            }
        } while (opcion != 0);
    }
}

class TorneoFutbol
{
    static Dictionary<string, List<string>> equipos = new Dictionary<string, List<string>>();
    
    public static void Iniciar()
    {
        Console.WriteLine("\n=== Registro de Torneo de Fútbol ===");
        Console.Write("Ingrese el nombre del equipo: ");
        string equipo = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(equipo))
        {
            Console.WriteLine("El nombre del equipo no puede estar vacío.");
            return;
        }
        
        if (!equipos.ContainsKey(equipo))
        {
            equipos[equipo] = new List<string>();
        }
        
        Console.Write("Ingrese el nombre del jugador: ");
        string jugador = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(jugador))
        {
            Console.WriteLine("El nombre del jugador no puede estar vacío.");
            return;
        }
        
        equipos[equipo].Add(jugador);
        
        Console.WriteLine($"Jugador {jugador} registrado en el equipo {equipo}.");
    }
}

class PremiacionDeportistas
{
    static Dictionary<string, List<string>> premios = new Dictionary<string, List<string>>();
    
    public static void Iniciar()
    {
        Console.WriteLine("\n=== Premiación de Deportistas ===");
        Console.Write("Ingrese el nombre del deportista: ");
        string deportista = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(deportista))
        {
            Console.WriteLine("El nombre del deportista no puede estar vacío.");
            return;
        }
        
        Console.Write("Ingrese el premio otorgado: ");
        string premio = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(premio))
        {
            Console.WriteLine("El premio no puede estar vacío.");
            return;
        }
        
        if (!premios.ContainsKey(deportista))
        {
            premios[deportista] = new List<string>();
        }
        premios[deportista].Add(premio);
        
        Console.WriteLine($"Premio {premio} otorgado a {deportista}.");
    }
}

class Biblioteca
{
    static Dictionary<string, string> libros = new Dictionary<string, string>();
    
    public static void Iniciar()
    {
        Console.WriteLine("\n=== Registro de Libros en la Biblioteca ===");
        Console.Write("Ingrese el título del libro: ");
        string titulo = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(titulo))
        {
            Console.WriteLine("El título del libro no puede estar vacío.");
            return;
        }
        
        Console.Write("Ingrese el autor del libro: ");
        string autor = Console.ReadLine()?.Trim();
        
        if (string.IsNullOrEmpty(autor))
        {
            Console.WriteLine("El nombre del autor no puede estar vacío.");
            return;
        }
        
        libros[titulo] = autor;
        
