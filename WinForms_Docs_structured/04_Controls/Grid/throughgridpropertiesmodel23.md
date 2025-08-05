---
title: throughgridpropertiesmodel23.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel23.md
created_at: 2025-08-05
---






##### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [        ][ ][   [\<%][=]Html.Grid\<[Order]\>([\"Grid1\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID)\                                                                                                                                                                                                                                                     |
|             columns.Add(p =\> p.CustomerID)\                                                                                                                                                                                                                                                  |
|             columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                                                               |
|             columns.Add(P =\> P.ShipCountry);]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                               |
| [            columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [           })[%\>]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [   ]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ ][@(][new][ [HtmlString](][Html.Grid\<[Order]\>([\"Grid1\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID)\                                                                                                                                                                                                                                                                                                                                                                             |
|             columns.Add(p =\> p.CustomerID)\                                                                                                                                                                                                                                                                                                                                                                          |
|             columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                                                                                                                                                                                       |
|             columns.Add(P =\> P.ShipCountry);]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [           }).][ToString())[)] ][]                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

3.   Create a **GridPropertiesModel** in the **Index** method. Use the **ActionMode** property to set the JSON mode.

4.   Use the **AllowSummaries** property to enable the summaries.

[] 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [   [public] [ActionResult] Index()\                                                                                                                                                                                                              |
|    {\                                                                                                                                                                                                                                                                                          |
|       ][   [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                                                |
| [      {]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [               Caption = [\"Orders\"],]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [               AutoFormat = Syncfusion.Mvc.Shared.[Skins].Sandune,]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [               **AllowSummaries = true,**]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                |
| **[               ActionMode = ActionMode.JSON]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| **[                ]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [      };]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                                                             |
|         ViewData\[[\"GridModel\"]\] = gridModel;\                                                                                                                                                                                                                      |
|         [return] View();\                                                                                                                                                                                                                                                 |
|    }][]                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

5.   Set up a summary column by instantiating the **GridSummaryColumnDescriptor** specifying the **SummaryType** and format.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [// Create instance to GridSummaryColumnDescriptor.][]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [                [GridSummaryColumnDescriptor] maxCGPA = [new] [GridSummaryColumnDescriptor]();][]                   |
|                                                                                                                                                                                                                                                                                                             |
| [                maxCGPA.Name = [\"Maximum CGPA\"]; [// Specify the name of the summary column.]][]                                         |
|                                                                                                                                                                                                                                                                                                             |
| [                maxCGPA.SummaryType = [SummaryType].DoubleAggregate;[// Specify the summary type.]][]                                      |
|                                                                                                                                                                                                                                                                                                             |
| [                maxCGPA.DataMember = [\"CGPA\"];[// Gets or sets the mapping for this column.]][]                                          |
|                                                                                                                                                                                                                                                                                                             |
| [                maxCGPA.DisplayColumn= [\"CGPA\"];[// The target column in which to display the summary.]][]                               |
|                                                                                                                                                                                                                                                                                                             |
| [                maxCGPA.Format = [\"{Maximum:##.##}\"];[// The format string used to format the text to display in the summary column.]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Define a **SummaryRow** and add the **SummaryColumn** to it.[ ]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                      |
| [///][ A GridSummaryRowDescriptor declares a summary row with one or multiple GridSummaryColumnDescriptor elements.][] |
|                                                                                                                                                                                                                                                                                                      |
| [                [///][ ][\<param name=\"name\"\>][The descriptor name.][\</param\>]]                                                    |
|                                                                                                                                                                                                                                                                                                      |
| [                [GridSummaryRowDescriptor] maxRow = [new] [GridSummaryRowDescriptor]([\"Largest\"]);]                                                 |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [                [///][ Title displayed in the summary row.]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [                maxRow.Title = [\"Largest\"];]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [                [///][ Custom text which can be prefixed with the maxCGPA summary.]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                      |
| [                maxCGPA.Prefix = [\"Max:\"];             ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [                [///][ Summary columns are added to the summary row.                ]]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [                maxRow.SummaryColumns.Add(maxCGPA);]                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Finally, add the summary row to the grid using **SummaryRows**.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Add summary rows to the grid.][]                                                                                  |
|                                                                                                                                                                                                                                       |
| [            [foreach] ([GridSummaryRowDescriptor] summaryRow [in] [this].SummaryCollection)] |
|                                                                                                                                                                                                                                       |
| [                gridModel.SummaryRows.Add(summaryRow);]                                                                                                                             |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   If you enable the paging and sorting features, rebind the **SummaryRow** property again in **Post** actions as given below.[ ]

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                              |
|                                                                                                                                                                                                                          |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                        |
|                                                                                                                                                                                                                          |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                    |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [IEnumerable] data = [new] [StudentDataContext]().AutoFormatStudent.Skip(0).Take(20).ToList();]    |
|                                                                                                                                                                                                                          |
| [            [ActionResult] result = data.GridActions\<[Student]\>();]                                                               |
|                                                                                                                                                                                                                          |
| [            [var] engineSource = result [as] [GridHtmlActionResult]\<[Student]\>;]        |
|                                                                                                                                                                                                                          |
| [            [// Rebinding the SummaryRows.]]                                                                                                                  |
|                                                                                                                                                                                                                          |
| [            [foreach] ([GridSummaryRowDescriptor] summaryRow [in] [this].SummaryCollection)] |
|                                                                                                                                                                                                                          |
| [                engineSource.GridModel.SummaryRows.Add(summaryRow);]                                                                                                                |
|                                                                                                                                                                                                                          |
| [            [return] result;]                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [        }][]                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.   Run the application. The grid will appear as shown below:

[] 

{border="0"}

Figure 218: Summary-Enabled Grid

 

[]{#related-topics}

