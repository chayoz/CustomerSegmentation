using CustomerSegmentation.Data;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CustomerSegmentation.Controllers
{
    public class Statistics : Controller
    {
        private readonly CustomerContext _context;

        public Statistics(CustomerContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            return View();
        }
    }
}
