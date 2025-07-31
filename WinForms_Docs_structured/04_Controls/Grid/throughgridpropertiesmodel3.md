---
title: throughgridpropertiesmodel3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel3.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"], [\"GridModel\"],] |
|                                                                                                                                                                                                                                                                                                        |
| [          column =\>]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [          {]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                        |
| [              column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                        |
| [              column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [              column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [              column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [              column.Add(p =\> p.CGPA);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                        |
| [          }) [%\>]]                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"], [\"GridModel\"],] |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [          column =\>]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [          {]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [              column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [              column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [              column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [              column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [              column.Add(p =\> p.CGPA);]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [          })][.ToString())[)]    ][]                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Bind the data source using the **Datasource** property and pass the model from controller to view using the **ViewData** class as given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [public][ [ActionResult] Index()]                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Student]\> model = [new] [GridPropertiesModel]\<[Student]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [  **DataSource = [new] [StudentDataContext]().Student.Take(200),**]                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Student List\"],]                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                AllowPaging = [true],                ]                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                AllowSorting = [true] ]                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = model;[ // Pass the model from controller to view using ViewData.]]                                                             |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

[  ][]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][]                     |
|                                                                                                                                                                                                                                     |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                        |
|                                                                                                                                                                                                                                     |
| [        [///][ from the grid. Required response is generated.]]                                                                                     |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties.][\</param\>]] |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                           |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                   |
|                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                               |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [     IEnumerable][ data = [new] [StudentDataContext]().Student.Take(200);]                    |
|                                                                                                                                                                                                                                     |
| [            [return] data.GridActions\<[Student]\>();]                                                                                            |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 92: Generic Collection Grid

**[]** 

[]{#related-topics}

