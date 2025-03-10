using System;
using System.Collections.Generic;
 
class Program
{
   static void Main()
   {
      // Creación de un HashSet vacío
      HashSet<int> miConjunto = new HashSet<int>();
 
      // Creación de un HashSet con valores iniciales
      HashSet<int> numeros = new HashSet<int> { 1, 2, 3 };
 
      // Mostrar el conjunto inicial
      Console.WriteLine("Conjunto inicial:");
      MostrarConjunto(numeros);
 
      // Adición de elementos al HashSet
      Console.WriteLine("\nAgregando elementos...");
      numeros.Add(4); // Se agrega el número 4 al conjunto
      numeros.Add(2); // Intento de agregar un número duplicado (no se añadirá)
 
      // Mostrar el conjunto después de la adición
      Console.WriteLine("Conjunto después de agregar elementos:");
      MostrarConjunto(numeros);
 
       // Verificación de pertenencia (Contains)
      Console.WriteLine("\nVerificando si el número 3 está en el conjunto:");
      bool contiene = numeros.Contains(3); // Devuelve true si el número 3 está en el conjunto
      Console.WriteLine("¿El conjunto contiene el número 3? " + contiene);
 
      // Eliminación de elementos del HashSet
      Console.WriteLine("\nEliminando el número 2...");
      numeros.Remove(2); // Se elimina el número 2 del conjunto
 
      // Mostrar el conjunto después de la eliminación
      Console.WriteLine("Conjunto después de eliminar el número 2:");
      MostrarConjunto(numeros);
   }
 
  // Método auxiliar para mostrar los elementos del HashSet en consola
  static void MostrarConjunto(HashSet<int> conjunto)
   {
      Console.Write("{ ");
      foreach (var elemento in conjunto)
      {
          Console.Write(elemento + " ");
      }
      Console.WriteLine("}");
   }
}
