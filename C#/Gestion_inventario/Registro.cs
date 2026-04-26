using System;
using System.IO;

namespace SistemaInventario.Services
{
    public static class LoggerSistema
    {
        private const string LogFile = "sistema_logs.txt";

        public static void Registrar(string mensaje, string nivel = "INFO")
        {
            try
            {
                string linea = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] [{nivel}] {mensaje}";
                File.AppendAllText(LogFile, linea + Environment.NewLine);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Fallo crítico al escribir log: " + ex.Message);
            }
        }
    }
}