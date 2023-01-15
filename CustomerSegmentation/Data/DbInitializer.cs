using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using CsvHelper;
using CustomerSegmentation.Models;

namespace CustomerSegmentation.Data
{
    public class DbInitializer
    {
        public static void Initialize(CustomerContext context)
        {
            context.Database.EnsureCreated();
            //Look for customers
            if (context.Customers.Any())
            {
                return; //DB has data
            }

            List<CustomerDataImport> cdata;

            //Read csv file
            var reader = new StreamReader(@"..\Customer_Data.csv");
            var csv = new CsvReader(reader, CultureInfo.CurrentCulture);

            cdata = csv.GetRecords<CustomerDataImport>().ToList();

            //Import data into database
            foreach (CustomerDataImport c in cdata)
            {
                context.Customers.Add(new Customer {Gender = c.Gender, Age = c.Age, AnnualIncome = c.AnnualIncome, SpendingScore = c.SpendingScore });
            }
            context.SaveChanges();
        }
    }
}
