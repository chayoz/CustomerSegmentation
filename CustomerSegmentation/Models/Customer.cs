using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace CustomerSegmentation.Models
{
    public class Customer
    {
        public int CustomerID { get; set; }
        public string Gender { get; set; }
        public int Age { get; set; }
        public int AnnualIncome { get; set; }
        public int SpendingScore { get; set; }
    }
}
