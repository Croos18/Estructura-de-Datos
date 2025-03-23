using System;

class Node
{
    public int Value;
    public Node Left, Right;
    public Node(int value)
    {
        Value = value;
        Left = Right = null;
    }
}

class BinaryTree
{
    public Node Root;

    public void Insert(int value)
    {
        Root = InsertRec(Root, value);
    }

    private Node InsertRec(Node root, int value)
    {
        if (root == null) return new Node(value);
        if (value < root.Value)
            root.Left = InsertRec(root.Left, value);
        else
            root.Right = InsertRec(root.Right, value);
        return root;
    }

    public Node Search(int value)
    {
        return SearchRec(Root, value);
    }

    private Node SearchRec(Node root, int value)
    {
        if (root == null || root.Value == value) return root;
        return value < root.Value ? SearchRec(root.Left, value) : SearchRec(root.Right, value);
    }

    public Node Delete(int value)
    {
        return DeleteRec(Root, value);
    }

    private Node DeleteRec(Node root, int value)
    {
        if (root == null) return null;
        if (value < root.Value)
            root.Left = DeleteRec(root.Left, value);
        else if (value > root.Value)
            root.Right = DeleteRec(root.Right, value);
        else
        {
            if (root.Left == null) return root.Right;
            else if (root.Right == null) return root.Left;

            root.Value = FindMin(root.Right).Value;
            root.Right = DeleteRec(root.Right, root.Value);
        }
        return root;
    }

    public void InOrder(Node node)
    {
        if (node != null)
        {
            InOrder(node.Left);
            Console.Write(node.Value + " ");
            InOrder(node.Right);
        }
    }

    public void PreOrder(Node node)
    {
        if (node != null)
        {
            Console.Write(node.Value + " ");
            PreOrder(node.Left);
            PreOrder(node.Right);
        }
    }

    public void PostOrder(Node node)
    {
        if (node != null)
        {
            PostOrder(node.Left);
            PostOrder(node.Right);
            Console.Write(node.Value + " ");
        }
    }

    public int Height(Node node)
    {
        if (node == null) return -1;
        return Math.Max(Height(node.Left), Height(node.Right)) + 1;
    }

    public int CountNodes(Node node)
    {
        if (node == null) return 0;
        return 1 + CountNodes(node.Left) + CountNodes(node.Right);
    }

    public int CountLeaves(Node node)
    {
        if (node == null) return 0;
        if (node.Left == null && node.Right == null) return 1;
        return CountLeaves(node.Left) + CountLeaves(node.Right);
    }

    public Node FindMin(Node node)
    {
        while (node.Left != null)
            node = node.Left;
        return node;
    }

    public Node FindMax(Node node)
    {
        while (node.Right != null)
            node = node.Right;
        return node;
    }

    public Node Invert(Node root)
    {
        if (root == null) return null;
        Node temp = root.Left;
        root.Left = Invert(root.Right);
        root.Right = Invert(temp);
        return root;
    }

    public void PrintTree(Node node, string indent = "", bool last = true)
    {
        if (node != null)
        {
            Console.Write(indent);
            Console.Write(last ? "└──" : "├──");
            Console.WriteLine(node.Value);
            indent += last ? "    " : "│   ";
            PrintTree(node.Left, indent, false);
            PrintTree(node.Right, indent, true);
        }
    }
}

class Program
{
    static void Main()
    {
        BinaryTree tree = new BinaryTree();
        int opcion;
        do
        {
            Console.WriteLine("\n--- MENÚ DE OPERACIONES ÁRBOL BINARIO ---");
            Console.WriteLine("1. Insertar nodo");
            Console.WriteLine("2. Eliminar nodo");
            Console.WriteLine("3. Buscar valor");
            Console.WriteLine("4. Recorrido InOrden");
            Console.WriteLine("5. Recorrido PreOrden");
            Console.WriteLine("6. Recorrido PostOrden");
            Console.WriteLine("7. Mostrar árbol");
            Console.WriteLine("8. Altura del árbol");
            Console.WriteLine("9. Contar nodos");
            Console.WriteLine("10. Contar hojas");
            Console.WriteLine("11. Valor mínimo");
            Console.WriteLine("12. Valor máximo");
            Console.WriteLine("13. Invertir árbol (espejo)");
            Console.WriteLine("0. Salir");
            Console.Write("Seleccione una opción: ");
            opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.Write("Ingrese valor a insertar: ");
                    int valIns = int.Parse(Console.ReadLine());
                    tree.Insert(valIns);
                    break;
                case 2:
                    Console.Write("Ingrese valor a eliminar: ");
                    int valDel = int.Parse(Console.ReadLine());
                    tree.Delete(valDel);
                    break;
                case 3:
                    Console.Write("Ingrese valor a buscar: ");
                    int valBus = int.Parse(Console.ReadLine());
                    var result = tree.Search(valBus);
                    Console.WriteLine(result != null ? "Valor encontrado" : "No encontrado");
                    break;
                case 4:
                    Console.Write("InOrden: ");
                    tree.InOrder(tree.Root);
                    Console.WriteLine();
                    break;
                case 5:
                    Console.Write("PreOrden: ");
                    tree.PreOrder(tree.Root);
                    Console.WriteLine();
                    break;
                case 6:
                    Console.Write("PostOrden: ");
                    tree.PostOrder(tree.Root);
                    Console.WriteLine();
                    break;
                case 7:
                    Console.WriteLine("Árbol:");
                    tree.PrintTree(tree.Root);
                    break;
                case 8:
                    Console.WriteLine("Altura: " + tree.Height(tree.Root));
                    break;
                case 9:
                    Console.WriteLine("Total de nodos: " + tree.CountNodes(tree.Root));
                    break;
                case 10:
                    Console.WriteLine("Total de hojas: " + tree.CountLeaves(tree.Root));
                    break;
                case 11:
                    var min = tree.FindMin(tree.Root);
                    Console.WriteLine("Mínimo: " + (min != null ? min.Value.ToString() : "Árbol vacío"));
                    break;
                case 12:
                    var max = tree.FindMax(tree.Root);
                    Console.WriteLine("Máximo: " + (max != null ? max.Value.ToString() : "Árbol vacío"));
                    break;
                case 13:
                    tree.Root = tree.Invert(tree.Root);
                    Console.WriteLine("Árbol invertido.");
                    break;
            }
        } while (opcion != 0);
    }
}
