using CustomerSegmentation.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using System.Text.Json;
using Newtonsoft.Json.Linq;

namespace CustomerSegmentation.Controllers
{
    public class PredictionController : Controller
    {

        public IActionResult Index()
        {
            return View();
        }       

        [HttpPost]
        public ActionResult Run([FromBody]dynamic data1)
        {
            string args = Convert.ToString(data1);
            var data = JObject.Parse(args);
            args = "" + data["args"];
            if (!(args == "test"))
            {
                string workingDirectory = @"D:\uni\Contemporary problems analysis\Customer Segmentation\CustomerSegmentation\CustomerSegmentation\python";
                var process = new Process
                {
                    StartInfo = new ProcessStartInfo
                    {
                        FileName = "cmd.exe",
                        RedirectStandardInput = true,
                        UseShellExecute = false,
                        RedirectStandardOutput = true,
                        WorkingDirectory = workingDirectory
                    }

                };
                process.Start();


                using (var sw = process.StandardInput)
                {
                    if (sw.BaseStream.CanWrite)
                    {
                        // Batch script to activate Anaconda
                        sw.WriteLine(@"D:\Anaconda\Anaconda3\Scripts\activate.bat");
                        // Activate your environment
                        sw.WriteLine("conda activate base");
                        // run your script. You can also pass in arguments
                        sw.WriteLine("python kmeans.py {0}", args);
                    }
                }
                // read multiple output lines
                string result = process.StandardOutput.ReadToEnd();

                if (result.IndexOf("high") != -1)
                {
                    result = "Customer is most likely to have an average or high spending score.";
                }
                else if (result.IndexOf("low") != -1)
                {
                    result = "Customer is most likely to have a low spending score.";
                }
                else
                {
                    result = "Uknown";
                }
                return this.Json(new { success = result });
            }

            return this.Json(new { success = args });

        }
    }
}
