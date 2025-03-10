using System;

class TorresDeHanoi
{
    /// <summary>
    /// Resuelve el problema de las Torres de Hanoi utilizando recursión.
    /// </summary>
    /// <param name="n">Número de discos.</param>
    /// <param name="origen">Torre de origen.</param>
    /// <param name="destino">Torre de destino.</param>
    /// <param name="auxiliar">Torre auxiliar.</param>
    static void ResolverHanoi(int n, char origen, char destino, char auxiliar)
    {
        if (n == 1)
        {
            Console.WriteLine($"Mover disco 1 de {origen} a {destino}");
            return;
        }
        
        // Mover n-1 discos de origen a auxiliar usando destino como auxiliar
        ResolverHanoi(n - 1, origen, auxiliar, destino);
        
        // Mover el disco restante de origen a destino
        Console.WriteLine($"Mover disco {n} de {origen} a {destino}");
        
        // Mover n-1 discos de auxiliar a destino usando origen como auxiliar
        ResolverHanoi(n - 1, auxiliar, destino, origen);
    }

    static void Main()
    {
        int numDiscos = 3; // Número de discos
        ResolverHanoi(numDiscos, 'A', 'C', 'B');
    }
}
