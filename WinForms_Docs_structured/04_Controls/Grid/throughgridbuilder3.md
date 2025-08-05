---
title: throughgridbuilder3.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder3.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [How to\>Creating the Generic Collection Model]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}).

3.   In the view you can use its **Model** property in **Datasource** in order to bind the data source.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"])] |
|                                                                                                                                                                                                                                                               |
| [    **.Datasource(Model)**]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [    .Caption([\"Student List\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [    .EnablePaging()]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [    .EnableSorting()]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [    .Column( column =\> {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [        column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [        column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [        column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [        column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                      |
|                                                                                                                                                                                                                                                               |
| [        column.Add(p =\> p.CGPA);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [        })]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [    [%\>]]                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"])] |
|                                                                                                                                                                                                            |
| [    **.Datasource(Model)**]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [    .Caption([\"Student List\"])]                                                                                                             |
|                                                                                                                                                                                                            |
| [    .EnablePaging()]                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [    .EnableSorting()]                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [    .Column( column =\> {]                                                                                                                                            |
|                                                                                                                                                                                                            |
| [        column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                |
|                                                                                                                                                                                                            |
| [        column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                            |
|                                                                                                                                                                                                            |
| [        column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                           |
|                                                                                                                                                                                                            |
| [        column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                   |
|                                                                                                                                                                                                            |
| [        column.Add(p =\> p.CGPA);]                                                                                                                                    |
|                                                                                                                                                                                                            |
| [        }).Render();]                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [    [}]]                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Set its data source and render the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [///][ ][\<summary\>][]               |
|                                                                                                                                                                                                                               |
| [        [///][ Used to bind the Grid. ]]                                                                                                      |
|                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                          |
|                                                                                                                                                                                                                               |
| [        [///][ ][\<returns\>][View page, it displays the Grid][\</returns\>]] |
|                                                                                                                                                                                                                               |
| [        [public] [ActionResult] Index()]                                                                                                    |
|                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [     var][ data = [new] [StudentDataContext]().Student.Take(200);]                         |
|                                                                                                                                                                                                                               |
| [            [return] View(data);]                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the code below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [///][ ][\<summary\>][]                      |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                         |
|                                                                                                                                                                                                                                      |
| [        [/// ][from the grid. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                            |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [StudentDataContext]().Student.Take(200);]                                          |
|                                                                                                                                                                                                                                      |
| [            [return] data.GridActions\<[Student]\>();]                                                                                             |
|                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 91: Generic Collection Grid

[]{#related-topics}

