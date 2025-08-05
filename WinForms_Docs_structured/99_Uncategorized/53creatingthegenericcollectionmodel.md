---
title: 53creatingthegenericcollectionmodel.md
original_path: WinForms_Docs/99_Uncategorized/53creatingthegenericcollectionmodel.md
created_at: 2025-08-05
---








  









## 5.3 Creating the Generic Collection Model {#creating-the-generic-collection-model style="MARGIN-LEFT: 28.8pt"}

1.  [Right-click the **Models** folder in the **Solution Explorer** window and select the menu option **Add New Item**.]

2.  [In the **Add New Item** window, select the **Web** category.]

{border="0"}

Figure 157: Add New Item

3.  [Select the **Class** file and give the class file name **Company.cs.** Click the **Add** button.]

4.  [Create a company class containing **Dept Id**, **Dept Name**, **Head Dept**, and **Shape** as properties.]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    [public] [class] [Company]]                                                                          |
|                                                                                                                                                                                                                                  |
| [    {]                                                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the dept id.]]                                                                                      |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The dept id.][\</value\>]]          |
|                                                                                                                                                                                                                                  |
| [        [public] [string] DeptId { [get]; [set]; }]                                    |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the name of the dept.]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The name of the dept.][\</value\>]] |
|                                                                                                                                                                                                                                  |
| [        [public] [string] DeptName { [get]; [set]; }]                                  |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the head dept.]]                                                                                    |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The head dept.][\</value\>]]        |
|                                                                                                                                                                                                                                  |
| [        [public] [string] HeadDept { [get]; [set]; }]                                  |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the shape.]]                                                                                        |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The shape.][\</value\>]]            |
|                                                                                                                                                                                                                                  |
| [        [public] [Shapes] Shape { [get]; [set]; }]                                  |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the width.]]                                                                                        |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The width.][\</value\>]]            |
|                                                                                                                                                                                                                                  |
| [        [public] [int] Width { [get]; [set]; }]                                        |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                                  |
| [        [///][ Gets or sets the height.]]                                                                                       |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                                  |
| [        [///][ ][\<value\>][The height.][\</value\>]]           |
|                                                                                                                                                                                                                                  |
| [        [public] [int] Height { [get]; [set]; }]                                       |
|                                                                                                                                                                                                                                  |
| [    }]                                                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  [Create another **DataContext** class to generate the company list as shown below.]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    [public] [class] [CompanyDataContext]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [///][ ][\<summary\>]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [///][ Gets the company.]]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [///][ ][\<value\>][The company.][\</value\>]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [public] [List]\<[Company]\> Company]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [            [get]]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [            {]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                [List]\<[Company]\> company = [new] [List]\<[Company]\>();]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Client\"], DeptName = [\"Client\"], HeadDept = [\"0\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Company\"], DeptName = [\"Company\"], HeadDept = [\"Client\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]                 |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Plant\"], DeptName = [\"Plant\"], HeadDept = [\"Company\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]                    |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Sales\"], DeptName = [\"Sales Organisation\"], HeadDept = [\"Company\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]       |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Purchase\"], DeptName = [\"Purchase Organisation\"], HeadDept = [\"Company\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Shipping\"], DeptName = [\"Shipping Point\"], HeadDept = [\"Plant\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]          |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"WholeSale\"], DeptName = [\"WholeSale Distribution\"], HeadDept = [\"Sales\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Internet\"], DeptName = [\"Internet Distribution\"], HeadDept = [\"Sales\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]   |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Division1\"], DeptName = [\"Division\"], HeadDept = [\"WholeSale\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Division2\"], DeptName = [\"Division\"], HeadDept = [\"WholeSale\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Division3\"], DeptName = [\"Division\"], HeadDept = [\"Internet\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                company.Add([new] [Company]() { DeptId = [\"Division4\"], DeptName = [\"Division\"], HeadDept = [\"Internet\"], Height = 50, Width = 150, Shape = [Shapes].RoundedRectangle });]            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                [return] company;]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [            }]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

