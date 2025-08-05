---
title: throughgridpropertiesmodel38.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel38.md
created_at: 2025-08-05
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

To customize the grid toolbar using **GridPropertiesModel**:

 

1.   Create a model in the application (Refer to [[[Getting Started\>Adding a Model to the Application]]{.underline}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[ ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], column=\>] |
|                                                                                                                                                                                                                                                                 |
| [                         {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"OrderID\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"CustomerID\"]);]                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p. EmployeeID).HeaderText([\"EmployeeID\"]);]                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.ShipAddress).HeaderText([\"ShipAddress\"]);]                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.ShipCountry).HeaderText([\"ShipCountry\"]);]                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [                         }));]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [%\>]                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[ ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                        |
| [@(][new][ [HtmlString](Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], column=\>] |
|                                                                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [         column.Add(p =\> p.OrderID).HeaderText([\"OrderID\"]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                        |
| [         column.Add(p =\> p.CustomerID).HeaderText([\"CustomerID\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [         column.Add(p =\> p.EmployeeID).HeaderText([\"EmployeeID\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [         column.Add(p =\> p.ShipAddress).HeaderText([\"ShipAddress\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [         column.Add(p =\> p.ShipCountry).HeaderText([\"ShipCountry\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [    }).ToString()]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [    )[)]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| **[]**[]                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Create a **GridPropertiesModel** in the **Index** method and assign the grid properties in the model. Set the **OnToolbarClickEvent** to handle the toolbar click event.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [            [GridPropertiesModel]\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                Caption = [\"Orders\"],]                                                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| [                AllowPaging=[true],]                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [                AllowSorting=[true],]                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [                AllowGrouping=[true],]                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                AutoFormat = [Skins].Sandune]                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [            };]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [            **model.ClientSideEvents.OnToolbarClickEvent = [\"OnToolbarClickEvent\"];**]                                                                                                    |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"Grid1\"]\] = model;]                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [            ]                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   To add custom toolbar items, configure the toolbar as given in the following code snippet. 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [               ][// Configure the toolbar][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [           [ToolbarSettings] toolbar = [new] [ToolbarSettings]();]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [           toolbar.Enable = [true];]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [            [// Add the add new, edit, delete, save, cancel button in toolbar.]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [          toolbar.Items.Add([new] [ToolbarOptions]() { ItemType = [GridToolBarItems].Custom, Title = [\"ExpandAll\"], Caption = [\"Expand\"], CssClass = [\"ExpandItem\"] });]        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [           toolbar.Items.Add([new] [ToolbarOptions]() { ItemType = [GridToolBarItems].Custom, Title = [\"CollapseAll\"], Caption = [\"Collapse\"], CssClass = [\"CollapseItem\"] });] |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [           toolbar.Items.Add([new] [ToolbarOptions]() { ItemType = [GridToolBarItems].Custom, Title = [\"Refresh\"], Caption = [\"Refresh\"], CssClass = [\"Refresh\"] });]           |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [           model.ToolBar = toolbar;]                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Handle the **OnToolbarClickEvent** as shown below.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [    [\<][script] [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                            |
| [      ]                                                                                                                               |
|                                                                                                                                                                            |
| [        [function] OnToolbarClickEvent(sender, args) {]                                                          |
|                                                                                                                                                                            |
| [          [// Handling the toolbar click event.]]                                                           |
|                                                                                                                                                                            |
| [    }]                                                                                                                                |
|                                                                                                                                                                            |
| [     [\</][script][\>]]                                              |
|                                                                                                                                                                            |
| []                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 299: Grid with Custom Toolbar

 

[]{#related-topics}

