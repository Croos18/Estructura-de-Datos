using System;
using System.Collections.Generic;
using System.IO;
using iTextSharp.text;
using iTextSharp.text.pdf;

class Program
{
    static void Main()
    {
        // Generar ciudadanos
        HashSet<string> ciudadanos = GenerarCiudadanos(500);
        HashSet<string> vacunadosPfizer = GenerarCiudadanos(75, "Pfizer");
        HashSet<string> vacunadosAstraZeneca = GenerarCiudadanos(75, "AstraZeneca");
        
        // Listado de ciudadanos no vacunados
        HashSet<string> noVacunados = new HashSet<string>(ciudadanos);
        noVacunados.ExceptWith(vacunadosPfizer);
        noVacunados.ExceptWith(vacunadosAstraZeneca);
        
        // Listado de vacunados con ambas dosis
        HashSet<string> vacunadosAmbas = new HashSet<string>(vacunadosPfizer);
        vacunadosAmbas.IntersectWith(vacunadosAstraZeneca);
        
        // Solo vacunados con Pfizer
        HashSet<string> soloPfizer = new HashSet<string>(vacunadosPfizer);
        soloPfizer.ExceptWith(vacunadosAstraZeneca);
        
        // Solo vacunados con AstraZeneca
        HashSet<string> soloAstraZeneca = new HashSet<string>(vacunadosAstraZeneca);
        soloAstraZeneca.ExceptWith(vacunadosPfizer);
        
        // Generar PDF
        GenerarReportePDF(noVacunados, vacunadosAmbas, soloPfizer, soloAstraZeneca);
    }
    
    static HashSet<string> GenerarCiudadanos(int cantidad, string tipo = "")
    {
        HashSet<string> ciudadanos = new HashSet<string>();
        Random rnd = new Random();
        while (ciudadanos.Count < cantidad)
        {
            ciudadanos.Add($"Ciudadano_{rnd.Next(1, 10000)}_{tipo}");
        }
        return ciudadanos;
    }
    
    static void GenerarReportePDF(HashSet<string> noVacunados, HashSet<string> vacunadosAmbas, HashSet<string> soloPfizer, HashSet<string> soloAstraZeneca)
    {
        Document doc = new Document();
        PdfWriter.GetInstance(doc, new FileStream("ReporteVacunacion.pdf", FileMode.Create));
        doc.Open();
        doc.Add(new Paragraph("Reporte de Vacunación COVID-19"));
        doc.Add(new Paragraph("\n"));
        
        AgregarListaAlPDF(doc, "No vacunados", noVacunados);
        AgregarListaAlPDF(doc, "Vacunados con ambas dosis", vacunadosAmbas);
        AgregarListaAlPDF(doc, "Vacunados solo con Pfizer", soloPfizer);
        AgregarListaAlPDF(doc, "Vacunados solo con AstraZeneca", soloAstraZeneca);
        
        doc.Close();
        Console.WriteLine("Reporte PDF generado exitosamente.");
    }
    
    static void AgregarListaAlPDF(Document doc, string titulo, HashSet<string> lista)
    {
        doc.Add(new Paragraph(titulo));
        foreach (var item in lista)
        {
            doc.Add(new Paragraph(item));
        }
        doc.Add(new Paragraph("\n"));
    }
}
