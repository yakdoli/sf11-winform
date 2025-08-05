---
title: throughgridbuilder52.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder52.md
created_at: 2025-08-05
---






##### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

To enable the keyboard interface using **GridBuilder**:

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view, you can use its **Model** property in **Datasource()** to bind the data source.

4.   Set **AllowKeyboardNavigation** to **True** to allow the grid to support keyboard interface functionality.

[] 

[                                                     ]


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().][Syncfusion().][Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"])] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[        .Datasource(Model)        ]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [             ]**[.AllowKeyboardNavigation([true])]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [ .EnablePaging()]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [        .EnableSorting()]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [ [%\>]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

 

[                                                     ]


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().][Syncfusion().][Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"])] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[        .Datasource(Model)        ]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [             ]**[.AllowKeyboardNavigation([true])]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [ .EnablePaging()]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [       .EnableSorting()]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [       .Render();]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [ [}]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

5.   Set its data source and render the view.

[                                                     ]


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[        ]                                                                                                                            |
|                                                                                                                                                                                                                               |
| [ [///][ ][\<summary\>]]                                                                                                  |
|                                                                                                                                                                                                                               |
| [       [///][ Used for rendering the Grid initially.]]                                                                                        |
|                                                                                                                                                                                                                               |
| [       [///][ ][\</summary\>]]                                                                                           |
|                                                                                                                                                                                                                               |
| [       [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                               |
| [       [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                               |
| [       {]                                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [            [var] Data = [new] [StudentDataContext]().AutoFormatStudent.Take(200);]                                    |
|                                                                                                                                                                                                                               |
| [            [return] View(Data);                                      ]                                                                                             |
|                                                                                                                                                                                                                               |
| [       }]                                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

6.   In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the code given below.

 

[                                                     ]


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                    |
|                                                                                                                                                                                               |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                             |
|                                                                                                                                                                                               |
| [        [public] [ActionResult] Index([PagingParams] args)]                         |
|                                                                                                                                                                                               |
| [        {]                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [                [var] Data = [new] [StudentDataContext]().AutoFormatStudent.Take(20);] |
|                                                                                                                                                                                               |
| [                [return] Data.GridActions\<[Student]\>();          ]                                        |
|                                                                                                                                                                                               |
| [        }]***[]***                                                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


***[]*** 

7.   [Run the application. Keyboard shortcuts will be activated in the grid]{.NumberedListChar}[.]

[]{#related-topics}

