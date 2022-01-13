using CsvHelper.Configuration.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CustomerSegmentation.Models
{
    public class CustomerDataImport
    {
        [Name("CustomerID")]
        public int CustomerID { get; set; }
        [Name("Gender")]
        public string Gender { get; set; }
        [Name("Age")]
        public int Age { get; set; }
        [Name("Annual Income (k$)")]
        public int AnnualIncome { get; set; }
        [Name("Spending Score (1-100)")]
        public int SpendingScore { get; set; }
    }
}
