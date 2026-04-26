using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using SistemaInventario.Models;

namespace SistemaInventario.Services
{
    public class InventarioService
    {
        private List<Producto> _productos;
        private const string ArchivoDatos = "inventario.json";

        public InventarioService()
        {
            CargarDatos();
        }

        public void AgregarProducto(Producto p)
        {
            _productos.Add(p);
            GuardarDatos();
            LoggerSistema.Registrar($"Producto '{p.Nombre}' añadido correctamente.");
        }

        public List<Producto> ListarTodo() => _productos;

        public List<Producto> ObtenerAlertas(int minimo)
            => _productos.Where(p => p.Stock < minimo).ToList();

        private void GuardarDatos()
        {
            string json = JsonSerializer.Serialize(_productos);
            File.WriteAllText(ArchivoDatos, json);
        }

        private void CargarDatos()
        {
            if (File.Exists(ArchivoDatos))
            {
                string json = File.ReadAllText(ArchivoDatos);
                _productos = JsonSerializer.Deserialize<List<Producto>>(json) ?? new List<Producto>();
            }
            else
            {
                _productos = new List<Producto>();
            }
        }
    }
}