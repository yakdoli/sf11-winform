---
title: addinghandlersthroughgridbuilder.md
original_path: WinForms_Docs/04_Controls/Grid/addinghandlersthroughgridbuilder.md
created_at: 2025-08-05
---








  









### Adding Handlers through GridBuilder {#adding-handlers-through-gridbuilder style="tab-stops: 0pt"}

 

The following code snippet illustrates adding handlers through **GridBuilder**.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [        **.ClientSideEvents( events =\> {**]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordHoverEvent([\"OnRecordHover\"]);]**                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordSelectionEvent([\"OnRecordSelect\"]);]**                                                                                                            |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordsUnselectionEvent([\"OnRecordUnSelect\"]);]**                                                                                                       |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideDoubleClickEvent([\"OnRecordDoubleClick\"]);]**                                                                                                           |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionBegin([\"OnBegin\"]);]**                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionFailure([\"OnFailure\"]);]**                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionSuccess([\"OnSuccess\"]);]**                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| **[            events.OnLoad([\"OnLoad\"]);]**                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDragStarted([\"OnRowsSelected\"]);]**                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDropped([\"OnDropped\"]);]**                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDropping([\"OnDropping\"]);]**                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| **[            events.OnGridRowDragEvent([\"OnGridRowDrag\"]);]**                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| **[            events.OnGridRowsDropEvent([\"OnGridrowsDrop\"]);]**                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| **[        })   ]**[ ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [        **.ClientSideEvents( events =\> {**]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordHoverEvent([\"OnRecordHover\"]);]**                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordSelectionEvent([\"OnRecordSelect\"]);]**                                                                                                            |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideRecordsUnselectionEvent([\"OnRecordUnSelect\"]);]**                                                                                                       |
|                                                                                                                                                                                                                                                       |
| **[            events.ClientSideDoubleClickEvent([\"OnRecordDoubleClick\"]);]**                                                                                                           |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionBegin([\"OnBegin\"]);]**                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionFailure([\"OnFailure\"]);]**                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| **[            events.OnActionSuccess([\"OnSuccess\"]);]**                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| **[            events.OnLoad([\"OnLoad\"]);]**                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDragStarted([\"OnRowsSelected\"]);]**                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDropped([\"OnDropped\"]);]**                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| **[            events.OnRowDropping([\"OnDropping\"]);]**                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| **[            events.OnGridRowDragEvent([\"OnGridRowDrag\"]);]**                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| **[            events.OnGridRowsDropEvent([\"OnGridrowsDrop\"]);]**                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| **[        })]**[.Render();**  **  ]                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [       [}]]                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

