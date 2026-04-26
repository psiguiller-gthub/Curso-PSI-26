using System;

namespace SistemaInventario.Models
{
    public class Producto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public int Stock { get; set; }
        public decimal Precio { get; set; }

        public override string ToString() => $"[ID: {Id}] {Nombre} - Stock: {Stock} - Precio: {Precio:C}";
    }
}