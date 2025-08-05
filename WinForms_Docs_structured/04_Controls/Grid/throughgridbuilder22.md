---
title: throughgridbuilder22.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder22.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource()** to bind the data source.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"])] |
|                                                                                                                                                                                                                                                               |
| [       .Datasource(Model)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [       .Caption([\"Orders\"]) ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [.EnablePaging()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [       .EnableSorting()      ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [       .AutoFormat([Skins].Sandune)            ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [       .Column( column =\> {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [           column.Add(P =\> P.Duration);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                   |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.CGPA);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           })]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [       [%\>]]                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"])] |
|                                                                                                                                                                                                                                                               |
| [       .Datasource(Model)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [       .Caption([\"Orders\"]) ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [.EnablePaging()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [       .EnableSorting()      ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [       .AutoFormat([Skins].Sandune)            ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [       .Column( column =\> {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [           column.Add(P =\> P.Duration);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                   |
|                                                                                                                                                                                                                                                               |
| [           column.Add(p =\> p.CGPA);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           }).Render();]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [       [}]]                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

4.   Create a **GridPropertiesModel** in the **Index** method. Use the **AllowSummaries** property to enable the summary feature.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Index]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [// Create an instance to GridPropertiesModel.][]                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [            [GridPropertiesModel]\<[Student]\> gridModel = [new] [GridPropertiesModel]\<[Student]\>();] |
|                                                                                                                                                                                                                                                                   |
| [            ]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [            [// Enable the summary feature.]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [            gridModel.AllowSummaries = [true];]                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Set up a summary column by instantiating **GridSummaryColumnDescriptor** specifying the **SummaryType** and format.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Create instance to GridSummaryColumnDescriptor.][]                                                                                |
|                                                                                                                                                                                                                             |
| [                [GridSummaryColumnDescriptor] maxCGPA = [new] [GridSummaryColumnDescriptor]();]                   |
|                                                                                                                                                                                                                             |
| [                maxCGPA.Name = [\"Maximum CGPA\"];[// Specify the name of the summary column.]]                                          |
|                                                                                                                                                                                                                             |
| [                maxCGPA.SummaryType = [SummaryType].DoubleAggregate;[// Specify the summary type.]]                                      |
|                                                                                                                                                                                                                             |
| [                maxCGPA.DataMember = [\"CGPA\"];[// Gets or sets the mapping for this column.]]                                          |
|                                                                                                                                                                                                                             |
| [                maxCGPA.DisplayColumn= [\"CGPA\"];[// The target column at which to display the summary.]]                               |
|                                                                                                                                                                                                                             |
| [                maxCGPA.Format = [\"{Maximum:##.##}\"];[// The format string used to format the text to display in the summary column.]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Define a **SummaryRow** and add the **SummaryColumn** to it.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [///][ A GridSummaryRowDescriptor declares a summary row with one or multiple GridSummaryColumnDescriptor elements.][] |
|                                                                                                                                                                                                                                                               |
| [                [///][ ][\<param name=\"name\"\>][The descriptor name.][\</param\>]]                          |
|                                                                                                                                                                                                                                                               |
| [                [GridSummaryRowDescriptor] maxRow = [new] [GridSummaryRowDescriptor]([\"Largest\"]);]                       |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                [///][ Title displayed in the summary row.]]                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [                maxRow.Title = [\"Largest\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                [///][ Custom text which can be prefixed with the maxCGPA summary.]]                                                                                          |
|                                                                                                                                                                                                                                                               |
| [                maxCGPA.Prefix = [\"Max:\"];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [             ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                [///][ Summary columns are added into the summary row.                ]]                                                                                      |
|                                                                                                                                                                                                                                                               |
| [                maxRow.SummaryColumns.Add(maxCGPA);]                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

7.   Finally add the summary row to the grid using **SummaryRows**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| [             ]                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [                [// Add summary rows to the grid.]]                                                                                                           |
|                                                                                                                                                                                                                          |
| [            [foreach] ([GridSummaryRowDescriptor] summaryRow [in] [this].SummaryCollection)] |
|                                                                                                                                                                                                                          |
| [                gridModel.SummaryRows.Add(summaryRow);]                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: In this sample, SummaryRows are defined inside the private property "SummaryRows"


[] 

8.   Pass the **GridPropertiesModel** to the view using the **ViewData()** method. Use the **grid's ID** as the key in **ViewData**.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [// Pass the GridPropertiesModel to the grid using GridID. Here StudentGrid is the grid\'s ID.][] |
|                                                                                                                                                                                         |
| [            ViewData\[[\"StudentGrid\"]\] = gridModel;]                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

9.   If you enable the paging and sorting features, rebind the **SummaryRow** property again in **Post** actions as given below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                      |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                         |
|                                                                                                                                                                                                                                      |
| [        [///][ from the grid. The required response is generated.]]                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult returns the data displayed in the grid.]]                                                                            |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [StudentDataContext]().AutoFormatStudent.Skip(0).Take(20).ToList();]                |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [            [ActionResult] result = data.GridActions\<[Student]\>();]                                                                           |
|                                                                                                                                                                                                                                      |
| [            [var] engineSource = result [as] [GridHtmlActionResult]\<[Student]\>;]                    |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [            [// Rebinding the summary rows.]]                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [            [foreach] ([GridSummaryRowDescriptor] summaryRow [in] [this].SummaryCollection)]             |
|                                                                                                                                                                                                                                      |
| [                engineSource.GridModel.SummaryRows.Add(summaryRow);]                                                                                                                            |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [            [return] result;]                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

10.  Run the sample. The grid will appear as shown below.

[] 

[] 

{border="0"}

Figure 215: Grid with Summary Rows

 

[]{#related-topics}

