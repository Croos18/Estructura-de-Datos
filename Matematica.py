using System;
using System.Collections.Generic;

class Program
{
    /// <summary>
    /// Verifica si una expresión matemática tiene paréntesis balanceados.
    /// </summary>
    /// <param name="expression">Expresión matemática a evaluar.</param>
    /// <returns>True si está balanceada, False en caso contrario.</returns>
    static bool EstaBalanceada(string expression)
    {
        Stack<char> stack = new Stack<char>();
        foreach (char ch in expression)
        {
            if (ch == '(' || ch == '{' || ch == '[')
            {
                stack.Push(ch);
            }
            else if (ch == ')' || ch == '}' || ch == ']')
            {
                if (stack.Count == 0) return false;

                char top = stack.Pop();
                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '['))
                {
                    return false;
                }
            }
        }
        return stack.Count == 0;
    }

    static void Main()
    {
        string formula = "{7+(8*5)-[(9-7)+(4+1)]}";
        Console.WriteLine($"La expresión \"{formula}\" está balanceada: {EstaBalanceada(formula)}");
    }
}
