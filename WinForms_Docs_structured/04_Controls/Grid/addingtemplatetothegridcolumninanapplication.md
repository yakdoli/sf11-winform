---
title: addingtemplatetothegridcolumninanapplication.md
original_path: WinForms_Docs/04_Controls/Grid/addingtemplatetothegridcolumninanapplication.md
created_at: 2025-08-05
---








  









### Adding Template to the Grid Column in an Application {#adding-template-to-the-grid-column-in-an-application style="tab-stops: 0pt"}

 

Column templates can be rendered in  two ways:

 

1.   By specifying the name of the template in the property **TemplateName** of the particular column.

2.   Rendering the template through the **[UIHint]** annotation attribute of the particular column. In this case, set the **TemplateColumn** property to **True**. There is no need to set the **TemplateName** property as the name of the template is specified through **[UIHint]**[ ]annotation attribute of the particular column.

[] 

For example, refer to the following  code snippets.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Product.Cs \[DTO class\]]**                                                                                            |
|                                                                                                                                                               |
| [\[[UIHint]([\"ProductTemplate\"]), [Required]\]] |
|                                                                                                                                                               |
| [        [public] [string] Product]                                             |
|                                                                                                                                                               |
| [        {]                                                                                                               |
|                                                                                                                                                               |
| [            [get];]                                                                                 |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [            [set];]                                                                                 |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [        }]                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [\<%][=][ Html.Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                           |
| [    .Datasource(Model)]                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [    .Caption([\"Orders\"])]                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [    .Column(column =\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [       {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| [          column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                           |
|                                                                                                                                                                                                                                           |
| [          **column.Add(p =\> p.Product).HeaderText([\"Product\"]).TemplateColumn([true]);[]**]                                     |
|                                                                                                                                                                                                                                           |
| [          column.Add(p =\> p.CustomerID).HeaderText([\"CustomerId\"]);]                                                                                                      |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [                           ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                           |
| [       })]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                           |
| [%\>]                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml\]]**                                                                                                       |
|                                                                                                                                                                                                       |
| [\@{][ Html.Grid\<[Order]\>([\"Grid1\"])]                 |
|                                                                                                                                                                                                       |
| [    .Datasource(Model)]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [    .Caption([\"Orders\"])]                                                                                                              |
|                                                                                                                                                                                                       |
| [    .Column(column =\>]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [       {]                                                                                                                                                        |
|                                                                                                                                                                                                       |
| [          column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                       |
|                                                                                                                                                                                                       |
| [          **column.Add(p =\> p.Product).HeaderText([\"Product\"]).TemplateColumn([true]);[]**] |
|                                                                                                                                                                                                       |
| [          column.Add(p =\> p.CustomerID).HeaderText([\"CustomerId\"]);]                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [                           ]                                                                                                                                     |
|                                                                                                                                                                                                       |
| [       }).Render();]                                                                                                                                             |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

In the code above, the "Product" column will render the template "ProductTemplate".

 

More:







