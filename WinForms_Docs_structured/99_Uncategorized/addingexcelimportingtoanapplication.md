---
title: addingexcelimportingtoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingexcelimportingtoanapplication.md
created_at: 2025-08-05
---






#### Adding Excel Importing to an Application {#adding-excel-importing-to-an-application style="tab-stops: 0pt"}

You can Import the entire Excel Spreadsheet to a GridControl. You can also import the Excel97to2003 and Excel2007to2010 formats

 

Importing the single sheet to a GridControl

 

In order to import the single sheet to grid control, open the file and pass this file as stream to the ImportFromExcel method as illustrated in the following code snippet:

**** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [FileStream][ fileStream = [new] [FileStream]([@\"..\\..\\Data\\Sample.xlsx\"], [FileMode].Open);] |
|                                                                                                                                                                                                                                                                                         |
| [byte][\[\] file = [new] [byte]\[fileStream.Length\];]                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Read(file, 0, ([int])fileStream.Length);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Close();]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [this][.gridControl.Model.ImportFromExcel([new] [MemoryStream](file));]                                                                               |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Importing the entire workbook to a GridControl

 

Open the workbook

 

To import the entire workbook to a GridControl, initially you have to open the workbook by using the XLSIO library as shown in the following code snippet:

**** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [FileStream][ fileStream = [new] [FileStream]([@\"..\\..\\Data\\Sample.xlsx\"], [FileMode].Open);] |
|                                                                                                                                                                                                                                                                                         |
| [byte][\[\] file = [new] [byte]\[fileStream.Length\];]                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Read(file, 0, ([int])fileStream.Length);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Close();]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [IApplication][ application = excelEngine.Excel;]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [IWorkbook][ workbook = application.Workbooks.Open([new] [MemoryStream](file), [ExcelOpenType].Automatic);]                |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Import the workbook into GridModel

 

After opening the workbook, you can import the workbook to GridModel by using the ImportFromExcel method. It will return the model collection; you can use it in your application. It will import all the styles, Conditional Formatting, Data Validation and book marks to model. While using this method it will take some time to import all the styles into models.

For importing the workbook you can use the following code snippet.

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                            |
| [GridModel][\[\] modelCollection = [GridModelImportExtensions].ImportFromExcel(workBook);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Importing the entire workbook to a virtual GridControl

Open the workbook

 

To import the entire workbook to a virtual GridControl, initially you have to open the workbook by using the XLSIO library as shown in the following code snippet.

**** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [FileStream][ fileStream = [new] [FileStream]([@\"..\\..\\Data\\Sample.xlsx\"], [FileMode].Open);] |
|                                                                                                                                                                                                                                                                                         |
| [byte][\[\] file = [new] [byte]\[fileStream.Length\];]                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Read(file, 0, ([int])fileStream.Length);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [fileStream.Close();]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [IApplication][ application = excelEngine.Excel;]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [IWorkbook][ workbook = application.Workbooks.Open([new] [MemoryStream](file), [ExcelOpenType].Automatic);]                |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Import the layout into GridModel

 

After that you can import the workbook by using the ImportFromExcelToVirtualGrid method it will return the model collection. GridModel have only the  layout styles, to import the other styles and data for cells you have to use the ConvertExcelRangeToVirtualGrid method.

**** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [GridModel][\[\] modelCollection = [GridModelImportExtensions].ImportFromExcelToVirtualGrid(workBook);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Import data into GridModel

 

To load the data in grid cells, you have to use the ConvertExcelRangeToVirtualGrid method, this will import the formulas, cellvalue, conditional formats, data validation and the styles from the excel range to grid cells. To import the data into cells you can call the ConvertExcelRangeToVirtualGrid method in Querycellinfo Event as shown in the following code snippet:

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [void][ Model_QueryCellInfo([object] sender, [GridQueryCellInfoEventArgs] e)]    |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [GridModel][ gridModel = sender [as] [GridModel];]                            |
|                                                                                                                                                                                                                    |
| [if][ (!e.Style.IsChanged)]                                                                                                   |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [int][ index = modelCollection.ToList().IndexOf(gridModel);]                                                                  |
|                                                                                                                                                                                                                    |
| [IWorksheet][ sheet = workBook.Worksheets\[index\];]                                                                       |
|                                                                                                                                                                                                                    |
| [if][ (sheet != [null])]                                                                                 |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [IRange][ range = sheet.Range;]                                                                                            |
|                                                                                                                                                                                                                    |
| [if][ (e.Cell.RowIndex \>= range.Row && e.Cell.ColumnIndex \>= range.Column)]                                                 |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [IRange][ rangeToConvert = sheet.Range\[e.Cell.RowIndex, e.Cell.ColumnIndex\];]                                            |
|                                                                                                                                                                                                                    |
| [GridModelImportExtensions][.ConvertExcelRangeToVirtualGrid(e.Style, sheet, rangeToConvert, [null]);] |
|                                                                                                                                                                                                                    |
| [gridModel.Data\[e.Cell.RowIndex, e.Cell.ColumnIndex\] = e.Style.Store;]                                                                                                       |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

