﻿using CustomerSegmentation.Data;
using CustomerSegmentation.Models;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace CustomerSegmentation.Controllers
{
    public class Statistics : Controller
    {
        private readonly CustomerContext _context;
        private List<Customer> customers;

        public Statistics(CustomerContext context)
        {
            _context = context;
            customers = _context.Customers.ToList();
        }

        public IActionResult Index()
        {
            ViewData["Age"] = ReturnData();

            return View();
        }

        private int[] ReturnData()
        {
            List<int> age = new List<int>();
            foreach (Customer x in customers)
            {
                age.Add(x.Age);
            }

            return age.ToArray();
        }

    }
}
