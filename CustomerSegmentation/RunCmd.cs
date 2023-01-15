using Microsoft.JSInterop;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Twilio.TwiML.Voice;

namespace CustomerSegmentation
{
    public class RunCmd
    {
        [JSInvokable]
        public static string Run(string args)
        {
            if(!(args == "test"))
            {
                string workingDirectory = @"..\python";
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

                if(result.IndexOf("high") != -1)
                {
                    result = "Customer is most likely to have an average or high spending score.";
                }
                else if(result.IndexOf("low") != -1)
                {
                    result = "Customer is most likely to have a low spending score.";
                }
                else
                {
                    result = "Uknown";
                }
                return result;
            }

            return args;
            
        }
    }
}
