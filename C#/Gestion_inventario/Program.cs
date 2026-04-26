using System;
using SistemaInventario.Models;
using SistemaInventario.Services;

namespace SistemaInventario
{
    class Program
    {
        static void Main(string[] args)
        {
            InventarioService service = new InventarioService();
            LoggerSistema.Registrar("Aplicación iniciada por el usuario.");

            Console.WriteLine("=== GESTIÓN DE INVENTARIO C# (IFCT0609) ===");

            // Ejemplo de inserción funcional
            Console.Write("Introduce nombre del producto: ");
            string nombre = Console.ReadLine();

            service.AgregarProducto(new Producto
            {
                Id = new Random().Next(1, 1000),
                Nombre = nombre,
                Stock = 10,
                Precio = 25.50m
            });

            Console.WriteLine("\nInventario Actual:");
            service.ListarTodo().ForEach(p => Console.WriteLine(p.ToString()));

            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
            LoggerSistema.Registrar("Aplicación cerrada.");
        }
    }
}