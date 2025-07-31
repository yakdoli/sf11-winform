---
title: drawingtable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drawingtable.md
created_at: 2025-07-03
---






#### Drawing Table {#drawing-table style="tab-stops: 0pt"}

 

Essential PDF provides support for inserting tables into the PDF page. This feature enables the following:

 

[·      ]Drawing tabular data into the PDF page

[·      ]Built-in support for importing an ADO.NET DataTable into a table in the PDF page

[] 

**PdfLightTable** class represents simple tables that are used for publishing structured data from arrays, data tables or data columns. There are no real cells or rows in these tables, and all the data is taken from the data source by using the **DataSource** property.

[] 


{border="0"}Note: You must add the Syncfusion.Pdf.Tables namespace to work with Tables.


 

The following code example illustrates how to create and format tables.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [//Create Pdf table.]                                                                                                                |
|                                                                                                                                                                                        |
| [PdfLightTable][ table = [new] [PdfLightTable]();]      |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Set Data source.]                                                                                                                 |
|                                                                                                                                                                                        |
| [table.DataSource = dataTable;]                                                                                                                    |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Set table alternate row style.]                                                                                                   |
|                                                                                                                                                                                        |
| [table.Style.AlternateStyle = altStyle;]                                                                                                           |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Set header row style.      ]                                                                                                      |
|                                                                                                                                                                                        |
| [table.Style.HeaderStyle = headerStyle;]                                                                                                           |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Show the header row.]                                                                                                             |
|                                                                                                                                                                                        |
| [table.Style.ShowHeader = [true];]                                                                                            |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Repeat header in all the pages.]                                                                                                  |
|                                                                                                                                                                                        |
| [table.Style.RepeatHeader = [true];]                                                                                          |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Set header data from column caption.]                                                                                             |
|                                                                                                                                                                                        |
| [table.Style.HeaderSource = [PdfHeaderSource].ColumnCaptions;]                                                                |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Set layout properties.]                                                                                                           |
|                                                                                                                                                                                        |
| [PdfLayoutFormat][ format = [new] [PdfLayoutFormat]();] |
|                                                                                                                                                                                        |
| [format.Break = [PdfLayoutBreakType].FitElement;]                                                                             |
|                                                                                                                                                                                        |
| [format.Layout = [PdfLayoutType].Paginate;]                                                                                   |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Draw table.]                                                                                                                      |
|                                                                                                                                                                                        |
| [table.Draw(page, [PointF].Empty, format);]                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [\'Create Pdf table.]                                                                                                                      |
|                                                                                                                                                                                              |
| [Dim][ table [As] PdfLightTable = [New] PdfLightTable()]      |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Set Data source.]                                                                                                                       |
|                                                                                                                                                                                              |
| [ table.DataSource = dataTable]                                                                                                                          |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Set table alternate row style.]                                                                                                         |
|                                                                                                                                                                                              |
| [table.Style.AlternateStyle = altStyle]                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Set header row style.        ]                                                                                                          |
|                                                                                                                                                                                              |
| [table.Style.HeaderStyle = headerStyle]                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Show the header row.]                                                                                                                   |
|                                                                                                                                                                                              |
| [table.Style.ShowHeader = [True]]                                                                                                   |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [\'Repeat header in all the pages.]                                                                                                        |
|                                                                                                                                                                                              |
| [table.Style.RepeatHeader = [True]]                                                                                                 |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [\'Set header data from column caption.]                                                                                                   |
|                                                                                                                                                                                              |
| [table.Style.HeaderSource = PdfHeaderSource.ColumnCaptions]                                                                                              |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Set layout properties.]                                                                                                                 |
|                                                                                                                                                                                              |
| [Dim][ format [As] PdfLayoutFormat = [New] PdfLayoutFormat()] |
|                                                                                                                                                                                              |
| [format.Break = PdfLayoutBreakType.FitElement]                                                                                                           |
|                                                                                                                                                                                              |
| [format.Layout = PdfLayoutType.Paginate]                                                                                                                 |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\'Draw table.]                                                                                                                            |
|                                                                                                                                                                                              |
| [table.Draw(page, PointF.Empty,format)]                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 44: Drawing Table in the PDF page

 

 

[]{#related-topics}

