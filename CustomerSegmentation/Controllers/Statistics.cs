using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CustomerSegmentation.Controllers
{
    public class Statistics : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
