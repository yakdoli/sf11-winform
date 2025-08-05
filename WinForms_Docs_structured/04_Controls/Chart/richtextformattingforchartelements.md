---
title: richtextformattingforchartelements.md
original_path: WinForms_Docs/04_Controls/Chart/richtextformattingforchartelements.md
created_at: 2025-08-05
---






##### Rich-Text Formatting for Chart Elements {#rich-text-formatting-for-chart-elements style="tab-stops: 0pt"}

Chart titles and data labels that are not linked to the worksheet data can be edited directly on the chart. You can also use rich-text formatting for the chart elements to enhance their appearance.

 

The following code examples explain how to apply rich-text formatting to the chart elements.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [\'Step 1: Instantiate the spreadsheet creation engine][]                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]                                                              |
|                                                                                                                                                                                                                                                        |
| [\'Step 2: Instantiate the excel application object]                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [IApplication][ application = excelEngine.Excel;]                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [IWorkbook][ workbook = application.Workbooks.Open([@\"../../Data/Sample.xlsx\"], [ExcelOpenType].Automatic);] |
|                                                                                                                                                                                                                                                        |
| [IWorksheet][ sheet = workbook.Worksheets\[0\];]                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [IChart][ chart = sheet.Charts\[0\];]                                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [chart.ChartTitle = [\"Title with a variable font style\"];]                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [//Rich-text in chart title]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| [//Create a new font with the following properties][]                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [IFont][ redFont = workbook.CreateFont();]                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [redFont.Bold = [true];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [redFont.Italic = [false];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [redFont.Size = 18;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [redFont.FontName = [\"Georgia\"];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [redFont.Color = [ExcelKnownColors].Red;         []]                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [//SetFont(int startIndex, int endIndex, IFont font)][]                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [IChartRichTextString][ chartRTS = chart.ChartTitleArea.RichText;]                                                                                             |
|                                                                                                                                                                                                                                                        |
| [chartRTS.SetFont(0, 12, redFont); ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [//Rich-Text in data label]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [//Create another font with the following properties][]                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [IFont][ greenFont = workbook.CreateFont();          ]                                                                                                         |
|                                                                                                                                                                                                                                                        |
| [greenFont.Bold = [true];]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [greenFont.Italic = [false];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [greenFont.Size = 17;]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [greenFont.FontName = [\"Times New Roman\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [greenFont.Color = [ExcelKnownColors].Green;     []]                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [//SetFont(int startIndex, int endIndex, IFont font)][]                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [chart.Series\[0\].DataPoints\[0\].DataLabels.RichText.SetFont(0, 0, greenFont);\                                                                                                                                                                      |
| \                                                                                                                                                                                                                                                      |
| [//Create a third font with the following properties]]                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [IFont][ blueFont = workbook.CreateFont();]                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [blueFont.Bold = [true];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [blueFont.Italic = [true];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [blueFont.Size = 10;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [blueFont.FontName = [\"Calibri\"];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [blueFont.Color = [ExcelKnownColors].Blue;  []]                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [//SetFont(int startIndex, int endIndex, IFont font)]                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [chart.Series\[0\].DataPoints\[0\].DataLabels.RichText.SetFont(1, 2, blueFont);]                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [//Save workbook][]                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [workbook.Version = [ExcelVersion].Excel2007;]                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [string][ fileName = [@\"../../Output/SampleOutput.xlsx\"];]                                                                              |
|                                                                                                                                                                                                                                                        |
| [workbook.SaveAs(fileName);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [workbook.Close();     ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [excelEngine.Dispose();]                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [\'Step 1: Instantiate the spreadsheet creation engine.][            ]                                                                                          |
|                                                                                                                                                                                                                                                       |
| [Dim][ excelEngine [As] ExcelEngine = [New] ExcelEngine()]                                                             |
|                                                                                                                                                                                                                                                       |
| [\'Step 2 : Instantiate the excel application object.][         ]                                                                                               |
|                                                                                                                                                                                                                                                       |
| [Dim][ application [As] IApplication = excelEngine.Excel]                                                                                   |
|                                                                                                                                                                                                                                                       |
| [Dim][ workbook [As] IWorkbook = application.Workbooks.Open([\"../../Data/Sample.xlsx\"], ExcelOpenType.Automatic)] |
|                                                                                                                                                                                                                                                       |
| [Dim][ worksheet [As] IWorksheet = workbook.Worksheets(0) ]                                                                                 |
|                                                                                                                                                                                                                                                       |
| [Dim][ chart [As] IChart = worksheet.Charts(0)]                                                                                             |
|                                                                                                                                                                                                                                                       |
| [chart.ChartTitle = [\"Title with a variable font style\"]]                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\'Rich-text in chart title]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [\'Create a new font with the following properties][]                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [Dim][ redFont [As] IFont = workbook.CreateFont()                ]                                                                          |
|                                                                                                                                                                                                                                                       |
| [redFont.Bold = [True]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [redFont.Italic = [False]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [redFont.Size = 18]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [redFont.FontName = [\"Georgia\"]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [redFont.Color = ExcelKnownColors.Red]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [Dim][ chartRTS [As] IChartRichTextString = chart.ChartTitleArea.RichText[]]                                          |
|                                                                                                                                                                                                                                                       |
| [\'SetFont(int startIndex, int endIndex, IFont font)][]                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [chartRTS.SetFont(0, 12, redFont)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\'Rich-text in data label]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [\'Create a second font with the following properties][]                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [Dim][ greenFont [As] IFont = workbook.CreateFont()              ]                                                                          |
|                                                                                                                                                                                                                                                       |
| [greenFont.Bold = [True]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [greenFont.Italic = [False]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [greenFont.Size = 18]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [greenFont.FontName = [\"Georgia\"]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [greenFont.Color = ExcelKnownColors.Red]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [\'SetFont(int startIndex, int endIndex, IFont font)]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [chart.Series(0).DataPoints(0).DataLabels.RichText.SetFont(0, 0, greenFont) ]                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [\'Rich-text in data label]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [\'Create a third font with the following properties][]                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [Dim][ blueFont [As] IFont = workbook.CreateFont()               ]                                                                          |
|                                                                                                                                                                                                                                                       |
| [blueFont.Bold = [True]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [blueFont.Italic = [False]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [blueFont.Size = 18]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [blueFont.FontName = [\"Georgia\"]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [blueFont.Color = ExcelKnownColors.Red[]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [\'SetFont(int startIndex, int endIndex, IFont font)][]                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [chart.Series(0).DataPoints(0).DataLabels.RichText.SetFont(0, 0, blueFont) ]                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [\'Save the workbook to disk][                      ]                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [workbook.SaveAs(fileName) ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [\'Close the workbook][]                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [workbook.Close()]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\'No exception will be thrown if there are un-saved workbooks][]                                                                                               |
|                                                                                                                                                                                                                                                       |
| [excelEngine.ThrowNotSavedOnDestroy = [False]            ]                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [excelEngine.Dispose()]**[]**                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

