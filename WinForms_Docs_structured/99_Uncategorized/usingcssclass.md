---
title: usingcssclass.md
original_path: WinForms_Docs/99_Uncategorized/usingcssclass.md
created_at: 2025-08-05
---






#### Using CssClass() {#using-cssclass style="tab-stops: 0pt"}

Essential Grid uses **CssClass()** method for formatting the column with CSS styles.

1.   Create a model in to application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource()** to bind the data source.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .**Datasource(Model)**]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [            .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [            .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);                ]                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [            }) ]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[]                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .**Datasource(Model)**]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [            .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [            .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);                ]                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [            }).Render();     [}]]                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create **CssClass** in the view.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [\<][style][ [type][=\"text/css\"\>]] |
|                                                                                                                                                                                                                        |
| [    [.CustomCss]]                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [        [text-align]:[right];]                                                                                                           |
|                                                                                                                                                                                                                        |
| [        [background-color]:[Aqua];]                                                                                                      |
|                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [\</][style][\>][]            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

5.   Specify the CSS styles to columns using the **CssClass()** method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [            .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [            .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"])**.CssClass([\"CustomCss\"])**;]                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);                ]                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [            }) ]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [            .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [            .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"])**.CssClass([\"CustomCss\"])**;]                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);                ]                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [            }).Render(); ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [    [}]]                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

6.   Run the sample. The grid will look like this:

[] 

{border="0"}

Figure 206: Grid Formatting using CssClass()

 

[]{#related-topics}

