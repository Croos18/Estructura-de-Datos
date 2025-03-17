using System;

class CatalogoRevistas
{
    static void Main(string[] args)
    {
        string[] catalogo = new string[10];

        Console.WriteLine("Ingrese 10 títulos de revistas:");

        for (int i = 0; i < 10; i++)
        {
            Console.Write($"Título {i + 1}: ");
            catalogo[i] = Console.ReadLine();
        }

        int opcion;
        do
        {
            Console.Clear();
            Console.WriteLine("==== Catálogo de Revistas ====");
            Console.WriteLine("1. Búsqueda Iterativa");
            Console.WriteLine("2. Búsqueda Recursiva");
            Console.WriteLine("3. Salir");
            Console.Write("Elige una opción: ");
            opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    BusquedaIterativa(catalogo);
                    break;
                case 2:
                    Console.Write("Ingrese título a buscar (recursivo): ");
                    string tituloRec = Console.ReadLine();
                    bool encontrado = BusquedaRecursiva(catalogo, tituloRec, 0);
                    Console.WriteLine(encontrado ? "Título encontrado." : "Título no encontrado.");
                    Console.ReadKey();
                    break;
                case 3:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Presione cualquier tecla...");
                    Console.ReadKey();
                    break;
            }
        } while (opcion != 3);
    }

    static void BusquedaIterativa(string[] catalogo)
    {
        Console.Write("Ingrese título a buscar (iterativo): ");
        string titulo = Console.ReadLine();

        foreach (string t in catalogo)
        {
            if (t.Equals(titulo, StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Título encontrado.");
                Console.ReadKey();
                return;
            }
        }
        Console.WriteLine("Título no encontrado.");
        Console.ReadKey();
    }

    static bool BusquedaRecursiva(string[] catalogo, string titulo, int indice)
    {
        if (indice >= catalogo.Length)
            return false;

        if (catalogo[indice].Equals(titulo, StringComparison.OrdinalIgnoreCase))
            return true;

        return BusquedaRecursiva(catalogo, titulo, indice + 1);
    }
}
