
## Customer Segmentation

The purpose of this project was to create the source code for a commercial web application 
which will be able to analyse given data, show statistics and predict the spending score 
of customers.

The project was created using ASP.NET Core MVC for the front-end and python for the 
back-end by implementing the K-means algorithm for predictions.​​​​​​​

For the examples below, a customer data set provided by kaggle was used.
## Features

The application provides the following features:
- Statistics Page: Here we can preview several graphs based on the customers data.
- Prediction Page: By inputing some customer features (Age, Gender, Annual Income) the algorithm can predict if the spending score of the customer is low/average/high.


## Screenshots
**Home Page:**

![Home](https://cdn.myportfolio.com/1a037fbd-dda5-453e-b988-037213e016ef/34734e92-bf57-4619-befe-d182e7e90df6_rw_600.png?h=2f6f28839c08d38f2e681d464f4509e1)
##
**Statistics Page:**

![Statistics](https://cdn.myportfolio.com/1a037fbd-dda5-453e-b988-037213e016ef/1f85dfa0-cbca-4744-93f2-f16e9060aafd_rw_600.png?h=09598d0ea6dfa31af39da563640548a9)
##
**Prediction Page:**

![Prediction](https://cdn.myportfolio.com/1a037fbd-dda5-453e-b988-037213e016ef/c2dfb3d1-b48c-4077-82c1-852a36921598_rw_600.PNG?h=52765b8f43c8dd1037ed89607726a17f)
## Installation
**Requirements:**
- Microsoft Visual Studio (Application has been tested on 2017/2022 versions)
- "ASP.NET and web development" Workload installed
- .NET 5.0
- The application uses Anaconda for the python environment.

Clone the project in your desired folder with:
```bash
  git clone https://github.com/chayoz/CustomerSegmentation.git
```
Finally import the project solution from Visual Studio:
```bash
  Go to: File > Open > Project/Solution and select CustomerSegmentation.sln
  Or simply run CustomerSegmantation.sln and open with Visual Studio
```
## Tech Stack

**Client:** ASP.NET Core MVC

**Database:** EntityFramework

**Libraries:** D3.js, Pandas, NumPy, Matplotlib

**Prediction Algorithm:** K-Means from Scikit-Learn

**Programming languages:** C#, Python, Javascript

