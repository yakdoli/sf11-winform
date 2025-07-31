---
title: throughgridpropertiesmodel22.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel22.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [  [\<%][=]Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                             |
| [             {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [                 column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [                 column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [                 column.Add(P =\> P.Duration);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [                 column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                           |
|                                                                                                                                                                                                                                                             |
| [                 column.Add(p =\> p.CGPA);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [             }) [%\>]]                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Student]\>([\"StudentGrid\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [             {]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                 column.Add(p =\> p.UniversityCode).HeaderText([\"University Code\"]);]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                 column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                 column.Add(P =\> P.Duration);]                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                 column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                 column.Add(p =\> p.CGPA);]                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [             })]                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [.][ToString())[)] ][]                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[] 

3.   Create a **GridPropertiesModel** in the **Index** action method. Use the **AllowSummaries** property to enable the summaries feature.

[        ][]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [GridPropertiesModel][\<[Student]\> gridModel = [new] [GridPropertiesModel]\<[Student]\>()] |
|                                                                                                                                                                                                                                                                                  |
| [            {]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                  |
| [                DataSource = [new] [StudentDataContext]().AutoFormatStudent.Skip(0).Take(20).ToList(),]                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| [                Caption=[\"Student Details\"],]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [                AllowPaging=[true],]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| [                AllowSorting=[true],]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| [                **AllowSummaries=[true],**]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [                AutoFormat=[Skins].Sandune]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [            };]                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

4.   Set up a summary column by instantiating **GridSummaryColumnDescriptor** specifying the **SummaryType** and format.[]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Create instance to GridSummaryColumnDescriptor.][]                                                                                |
|                                                                                                                                                                                                                             |
| [                [GridSummaryColumnDescriptor] maxCGPA = [new] [GridSummaryColumnDescriptor]();]                   |
|                                                                                                                                                                                                                             |
| [                maxCGPA.Name = [\"Maximum CGPA\"];[// Specify the name to summary column.]]                                              |
|                                                                                                                                                                                                                             |
| [                maxCGPA.SummaryType = [SummaryType].DoubleAggregate;[// Specify the SummaryType.]]                                       |
|                                                                                                                                                                                                                             |
| [                maxCGPA.DataMember = [\"CGPA\"];[// Gets or sets the mapping for this column.]]                                          |
|                                                                                                                                                                                                                             |
| [                maxCGPA.DisplayColumn= [\"CGPA\"];[// The target column to which the summary is displayed.]]                             |
|                                                                                                                                                                                                                             |
| [                maxCGPA.Format = [\"{Maximum:##.##}\"];[// The format string used to format the text to display in the summary column.]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Define a SummaryRow and add the SummaryColumn into it.

 

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
| [                [///][ Title displayed in the summary row. ]]                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [                maxRow.Title = [\"Largest\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                [///][ Custom text which can be prefixed with the maxCGPA summary.]]                                                                                          |
|                                                                                                                                                                                                                                                               |
| [                maxCGPA.Prefix = [\"Max:\"];             ]                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                [///][ Summary columns are added into the summary row.                ]]                                                                                      |
|                                                                                                                                                                                                                                                               |
| [                maxRow.SummaryColumns.Add(maxCGPA);]                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Finally add the summary row to the grid using **SummaryRows**. [      ]

[         ][[ ]]{.Heading1Char}

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| [             ]                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [   [// Add summary rows to the grid.]]                                                                                                                        |
|                                                                                                                                                                                                                          |
| [            [foreach] ([GridSummaryRowDescriptor] summaryRow [in] [this].SummaryCollection)] |
|                                                                                                                                                                                                                          |
| [                gridModel.SummaryRows.Add(summaryRow);]                                                                                                                             |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: In this sample, summary rows are defined inside the private property "SummaryRows".


[] 

7.   If you enable the paging and sorting features, rebind the **SummaryRow** property again in **Post** actions as given below.

 

[  ]

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
| [            [// Rebinding the SummaryRows.]]                                                                                                                              |
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

 

8.   Run the sample. The grid will look like this:

[] 

{border="0"}

Figure 216: Grid with Summary Rows

 

[]{#related-topics}

