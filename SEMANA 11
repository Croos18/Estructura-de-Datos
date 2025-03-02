using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static Dictionary<string, string> diccionario = new Dictionary<string, string>()
    {
        {"time", "tiempo"}, {"person", "persona"}, {"year", "año"}, {"way", "camino"},
        {"day", "día"}, {"thing", "cosa"}, {"man", "hombre"}, {"world", "mundo"},
        {"life", "vida"}, {"hand", "mano"}, {"part", "parte"}, {"child", "niño"},
        {"eye", "ojo"}, {"woman", "mujer"}, {"place", "lugar"}, {"work", "trabajo"},
        {"week", "semana"}, {"case", "caso"}, {"point", "punto"}, {"government", "gobierno"},
        {"company", "empresa"}
    };

    static void Main()
    {
        int opcion;
        do
        {
            Console.WriteLine("\nMENU");
            Console.WriteLine("=======================================================");
            Console.WriteLine("1. Traducir una frase");
            Console.WriteLine("2. Ingresar más palabras al diccionario");
            Console.WriteLine("0. Salir");
            Console.Write("Seleccione una opción: ");
            opcion = Convert.ToInt32(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    TraducirFrase();
                    break;
                case 2:
                    AgregarPalabra();
                    break;
                case 0:
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Intente de nuevo.");
                    break;
            }
        } while (opcion != 0);
    }

    static void TraducirFrase()
    {
        Console.Write("Ingrese la frase: ");
        string frase = Console.ReadLine();
        string[] palabras = frase.Split(' ');
        for (int i = 0; i < palabras.Length; i++)
        {
            string palabraLimpia = palabras[i].ToLower().Trim(',', '.', '!', '?'); // Eliminar puntuación
            if (diccionario.ContainsKey(palabraLimpia))
            {
                palabras[i] = diccionario[palabraLimpia]; // Traducción inglés -> español
            }
            else if (diccionario.ContainsValue(palabraLimpia))
            {
                palabras[i] = diccionario.FirstOrDefault(x => x.Value == palabraLimpia).Key; // Traducción español -> inglés
            }
        }
        Console.WriteLine("Su frase traducida es: " + string.Join(" ", palabras));
    }

    static void AgregarPalabra()
    {
        Console.Write("Ingrese la palabra en inglés: ");
        string ingles = Console.ReadLine().ToLower();
        Console.Write("Ingrese la traducción en español: ");
        string español = Console.ReadLine().ToLower();

        if (!diccionario.ContainsKey(ingles))
        {
            diccionario.Add(ingles, español);
            Console.WriteLine("Palabra agregada con éxito.");
        }
        else
        {
            Console.WriteLine("La palabra ya existe en el diccionario.");
        }
    }
}
