---
title: throughgridbuilder56.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder56.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

To customize the grid toolbar using **GridBuilder**:

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   Create the Grid control in the view and configure its properties.

4.   Set the **OnToolbarClickEvent** handler for handling the toolbar click events.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[ ]                                                                                                             |
|                                                                                                                                                                                                            |
| [\<%][=Html.Syncfusion().Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                                            |
| [                         .Datasource(Model)]                                                                                                                          |
|                                                                                                                                                                                                            |
| [                         .Caption([\"Orders\"])]                                                                                              |
|                                                                                                                                                                                                            |
| [                         .Column(column =\>]                                                                                                                          |
|                                                                                                                                                                                                            |
| [                         {]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                         |
|                                                                                                                                                                                                            |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                   |
|                                                                                                                                                                                                            |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"EmployeeID\"]);]                                                    |
|                                                                                                                                                                                                            |
| [                             column.Add(p =\> p.ShipCountry).HeaderText([\"ShipCountry\"]);]                                                  |
|                                                                                                                                                                                                            |
| [                             column.Add(p =\> p.ShipAddress).HeaderText([\"ShipAddress\"]);]                                                  |
|                                                                                                                                                                                                            |
| [                         })]                                                                                                                                          |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [             **.ClientSideEvents(e =\> e.OnToolbarClickEvent([\"OnToolbarClickEvent\"]))**]                                                   |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [             **.ToolBar(tools =\>**]                                                                                                                                  |
|                                                                                                                                                                                                            |
| **[               {       ]**                                                                                                                                          |
|                                                                                                                                                                                                            |
| **[               [// Adding the custom toolbar items.] ]**                                                                                      |
|                                                                                                                                                                                                            |
| **[               [// Add(customItemtitle, customItemcaption, customItemCssClass)]                   ]**                                         |
|                                                                                                                                                                                                            |
| **[                tools.Add([\"ExpandAll\"], [\"Expand\"], [\"ExpandItem\"])]**               |
|                                                                                                                                                                                                            |
| **[                .Add([\"CollapseAll\"], [\"Collapse\"], [\"CollapseItem\"])]**              |
|                                                                                                                                                                                                            |
| **[                 .Add([\"Refresh\"], [\"Refresh\"], [\"Refresh\"]);]**                      |
|                                                                                                                                                                                                            |
| **[                })]**                                                                                                                                               |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [%\>]                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[ ]                                                                                                             |
|                                                                                                                                                                                                              |
| [\@{][ Html.Syncfusion().Grid\<[EditableOrder]\>([\"Grid1\"])]   |
|                                                                                                                                                                                                              |
| [                         .Datasource(Model)]                                                                                                                            |
|                                                                                                                                                                                                              |
| [                         .Caption([\"Orders\"])]                                                                                                |
|                                                                                                                                                                                                              |
| [                         .Column(column =\>]                                                                                                                            |
|                                                                                                                                                                                                              |
| [                         {]                                                                                                                                             |
|                                                                                                                                                                                                              |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                           |
|                                                                                                                                                                                                              |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                     |
|                                                                                                                                                                                                              |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"EmployeeID\"]);]                                                      |
|                                                                                                                                                                                                              |
| [                             column.Add(p =\> p.ShipCountry).HeaderText([\"ShipCountry\"]);]                                                    |
|                                                                                                                                                                                                              |
| [                             column.Add(p =\> p.ShipAddress).HeaderText([\"ShipAddress\"]);]                                                    |
|                                                                                                                                                                                                              |
| [                         })]                                                                                                                                            |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [             **.ClientSideEvents(e =\> e.OnToolbarClickEvent([\"OnToolbarClickEvent\"]))**]                                                     |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| **[       .ToolBar(tools =\>]**                                                                                                                                          |
|                                                                                                                                                                                                              |
| **[       {   ]**                                                                                                                                                        |
|                                                                                                                                                                                                              |
| **[        [// Adding the custom toolbar items.] ]**                                                                                               |
|                                                                                                                                                                                                              |
| **[        [// Add(customItemtitle, customItemcaption, customItemCssClass)]]**                                                                     |
|                                                                                                                                                                                                              |
| **[        tools.Add([\"ExpandAll\"], [\"Expand\"], [\"ExpandItem\"])[]]** |
|                                                                                                                                                                                                              |
| **[              .Add([\"CollapseAll\"], [\"Collapse\"], [\"CollapseItem\"])]**                  |
|                                                                                                                                                                                                              |
| **[              .Add([\"Refresh\"], [\"Refresh\"], [\"Refresh\"]);]**                           |
|                                                                                                                                                                                                              |
| **[                })]**                                                                                                                                                 |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                        .Render();]                                                                                                                                     |
|                                                                                                                                                                                                              |
| [}][]                                                                                                            |
|                                                                                                                                                                                                              |
| **[]**[]                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Handle the **OnToolbarClickEvent** as shown in the code block.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [    [\<][script] [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                            |
| [      ]                                                                                                                               |
|                                                                                                                                                                            |
| [        [function] OnToolbarClickEvent(sender, args) {]                                                          |
|                                                                                                                                                                            |
| [          [//Handling the toolbar click event]]                                                             |
|                                                                                                                                                                            |
| [    }]                                                                                                                                |
|                                                                                                                                                                            |
| [     [\</][script][\>]]                                              |
|                                                                                                                                                                            |
| []                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Render the view.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                             |
|                                                                                                                                                                        |
| [        [public] [ActionResult] Index()]                                             |
|                                                                                                                                                                        |
| [        {]                                                                                                                        |
|                                                                                                                                                                        |
| [           [var] data = [new] [NorthwindDataContext]().Orders;] |
|                                                                                                                                                                        |
| [            [return] View(data);]                                                                            |
|                                                                                                                                                                        |
| [        }]                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 298: Grid with Custom Toolbar

[] 

[]{#related-topics}

