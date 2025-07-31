---
title: throughgridbuilder31.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder31.md
created_at: 2025-07-03
---






##### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

To configure the keyboard interface using **GridBuilder**:

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

In the view, you can use its **Model** property in **Datasource()** to bind the data source.

3.   Set **AllowKeyboardNavigation** to **True** in order to allow the grid to support keyboard interface.

4.   Configure the keys for all the actions using the **KeyConfigurator** method. For example, **ExportToExcel** and **FocusKey** actions are configured in the following code snippet.

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.][Syncfusion().][Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"])] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[       .Datasource(Model)        ]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [             ]**[.AllowKeyboardNavigation([true])]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[ .KeyConfigurator(key =\> {]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[                        key.ExportToExcel([Keys].AltPlusA);]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[                        key.FocusKey([Keys].CtrlPlusAltPlusA);]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[             })]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [ .EnablePaging()]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [       .EnableSorting()]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [    [%\>]]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| ***[]***                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| ***[]***                                                                                                                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\@{][ ][Html.][Syncfusion().][Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"])] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[       .Datasource(Model)        ]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [             ]**[.AllowKeyboardNavigation([true])]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[ .KeyConfigurator(key =\> {]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[                        key.ExportToExcel([Keys].AltPlusA);]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[                        key.FocusKey([Keys].CtrlPlusAltPlusA);]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[             })]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [ .EnablePaging()]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [       .EnableSorting()]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [       .Render();]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [    [}]]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| ***[]***                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| ***[]***                                                                                                                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

5.   Set the data source and render the view.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                    |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [ [///][ ][\<summary\>]]                                                                                                  |
|                                                                                                                                                                                                                               |
| [       [///][ Used for rendering the grid initially.]]                                                                                        |
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
| [           [return] View(Data);   ]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [       }]***[]***                                                                                                                                                |
|                                                                                                                                                                                                                               |
| ***[]***                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

6.   In order to work with paging and sorting actions, create a **Post** method for **Index** actions and  bind the data source to the grid as shown in the following code.

***[]*** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                        |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [  ///][ ][\<summary\>][] |
|                                                                                                                                                                                                                   |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the ]]                                      |
|                                                                                                                                                                                                                   |
| [        [///][ HtmlActionResult from the grid. The required response is generated.]]                                              |
|                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                              |
|                                                                                                                                                                                                                   |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                 |
|                                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index([PagingParams] args)]                                             |
|                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [                [var] Data = [new] [StudentDataContext]().AutoFormatStudent.Take(20);]                     |
|                                                                                                                                                                                                                   |
| [                [return] Data.GridActions\<[Student]\>();          ]                                                            |
|                                                                                                                                                                                                                   |
| [        }]***[]***                                                                                                       |
|                                                                                                                                                                                                                   |
| ***[]***                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

***[]*** 

[7.   ]Run the application. Now **FocusKey** and **ExportToExcel** actions keyboard shortcuts are configured.[]

 

[]{#related-topics}

