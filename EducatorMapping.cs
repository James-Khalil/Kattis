using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
using CsvHelper;
using CsvHelper.Configuration;
using Newtonsoft.Json.Linq;

public class EducatorMap : ClassMap<Educator>
{
    public EducatorMap()
    {
        Map(m => m.ProgramType).Name("Program Type");
        Map(m => m.EstablishmentName).Name("Facility Name");
        Map(m => m.StreetAddress).Name("Address");
        Map(m => m.City).Name("City");
        Map(m => m.Province).Name("Province");
        Map(m => m.PostalCode).Name("Postal Code");
        Map(m => m.GoogleMapsLink).Name("Google Maps Link");
        Map(m => m.PhoneNumber).Name("Phone Number");
        Map(m => m.Capacity).Name("Capacity");
        // Skipping columns that we don't have data for.
    }
}


public class EducatorService
{
    private static async Task<(decimal Latitude, decimal Longitude)> GetCoordinatesFromPostalCode(string postalCode)
    {
        // Replace with your actual geocoding API endpoint and API key
        string apiKey = "YOUR_API_KEY";
        string url = $"https://maps.googleapis.com/maps/api/geocode/json?address={postalCode}&key={apiKey}";

        using (HttpClient client = new HttpClient())
        {
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();
            string responseBody = await response.Content.ReadAsStringAsync();

            JObject json = JObject.Parse(responseBody);
            JToken location = json["results"]?[0]?["geometry"]?["location"];
            if (location != null)
            {
                decimal latitude = location.Value<decimal>("lat");
                decimal longitude = location.Value<decimal>("lng");
                return (latitude, longitude);
            }

            throw new Exception("Failed to get coordinates.");
        }
    }

    public static async Task<List<Educator>> ConvertCsvToEducators(string csvFilePath)
    {
        List<Educator> educators = new List<Educator>();

        using (var reader = new StreamReader(csvFilePath))
        using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
        {
            csv.Configuration.RegisterClassMap<EducatorMap>();
            var records = csv.GetRecords<Educator>();

            foreach (var educator in records)
            {
                var coordinates = await GetCoordinatesFromPostalCode(educator.PostalCode);

                educator.Latitude = coordinates.Latitude;
                educator.Longitude = coordinates.Longitude;

                educators.Add(educator);
            }
        }

        return educators;
    }
}
