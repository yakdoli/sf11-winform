---
title: xlsx.md
original_path: WinForms_Docs/99_Uncategorized/xlsx.md
created_at: 2025-08-05
---








  









### XLSX {#xlsx style="tab-stops: 0pt"}

 

Excel 2007 version of MS Excel has various advanced features, and overcomes the drawbacks of previous versions. Essential XlsIO introduces basic support for Excel 2007 and Excel 2010 **xlsx** format that includes support to read and write basic elements (listed below) into the document.

 

Here is a sample code snippet that opens an **xlsx** file, makes some changes, and saves it as an xlsx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening ]                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [//.xlsx files]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [IWorkbook][ workbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"], [ExcelOpenType].Automatic);]               |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//The first worksheet object in the worksheets collection is accessed.]                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [IWorksheet][ sheet = workbook.Worksheets\[0\];]                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//Write data]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [sheet.Range\[[\"C3:O28\"]\].Text = [\"Hello world\"];]                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//Select the version to be saved]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [workbook.Version = ][ExcelVersion][.Excel2007; ][//or] |
|                                                                                                                                                                                                                                                                   |
| [//workbook.Version = ExcelVersion.Excel2010;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//Save it as \"Excel2007\" format.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [workbook.SaveAs([\"Sample.xlsx\"]);]                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [\'Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening ]                                                                                                |
|                                                                                                                                                                                                                                                    |
| [\'.xlsx files]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [Dim][ workbook [As] IWorkbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"], ExcelOpenType.Automatic)] |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Select the version to be saved.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [workbook.Version = ExcelVersion.Excel2007][ \'or]                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'workbook.Version = ExcelVersion.Excel2010]                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [\'The first worksheet object in the worksheets collection is accessed.]                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [Dim][ sheet [As] IWorksheet = workbook.Worksheets(0)]                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Write data]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [sheet.Range([\"C3:O28\"]).Text = [\"Hello world\"]]                                                                                                             |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Save it as \"Excel 2007\" format.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [workbook.SaveAs([\"Sample.xlsx\"])]                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You can use the very same API to work with the xlsx file or any other older format.


 

You can also set the **default version** of the workbook when you want to work with the same format.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [ExcelEngine ][excelEngine = new ExcelEngine();]                                                            |
|                                                                                                                                                                                                  |
| [IApplication][ application = excelEngine.Excel;]                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [//Select the default version as Excel 2007 or Excel 2010;]                                                                                    |
|                                                                                                                                                                                                  |
| [application.DefaultVersion = ExcelVersion.Excel2007;][ //or]                                |
|                                                                                                                                                                                                  |
| [//application.DefaultVersion = ExcelVersion.Excel2010;]                                                                                       |
|                                                                                                                                                                                                  |
| [//Open an existing Excel 2007 file. ]                                                                                                         |
|                                                                                                                                                                                                  |
| [IWorkbook][ workbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"]);] |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [//Save it as \"Excel2007\" format.]                                                                                                           |
|                                                                                                                                                                                                  |
| [workbook.SaveAs([\"Sample.xlsx\"]);]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [Dim][ excelEngine [As] ExcelEngine = [New] ExcelEngine()]                                 |
|                                                                                                                                                                                                                           |
| [Dim][ application [As] IApplication = excelEngine.Excel]                                                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Set the default version as Excel 2007;]                                                                                                                              |
|                                                                                                                                                                                                                           |
| [application.DefaultVersion = ExcelVersion.Excel2007 ][\'Or]                                                          |
|                                                                                                                                                                                                                           |
| [\'application.DefaultVersion = ExcelVersion.Excel2010]                                                                                                                 |
|                                                                                                                                                                                                                           |
| [\'Open an existing Excel 2007 file. ]                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [Dim][ workbook [As] IWorkbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"])] |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Save it as \"Excel 2007\" format.]                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [workbook.SaveAs([\"Sample.xlsx\"])]                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Essential XlsIO also allows to open an existing .xls file and save it to the .xlsx format \[with supported elements\], or open an .xlsx file and save it to the .xls format.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening ]                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [//.xlsx files]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                     |
| [IWorkbook][ workbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"], [ExcelOpenType].Automatic);] |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//Select the version to be saved.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                     |
| [workbook.Version = [ExcelVersion].Excel97to2003;]                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//The first worksheet object in the worksheets collection is accessed.]                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [IWorksheet][ sheet = workbook.Worksheets\[0\];]                                                                                                            |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//Write data]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [sheet.Range\[[\"C3:O28\"]\].Text = [\"Hello world\"];]                                                                                                         |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//Save it as \"Excel 97 t0 2003\" format.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [workbook.SaveAs([\"Sample.xls\"]);]                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening ]                                                                                                |
|                                                                                                                                                                                                                                                    |
| [\'.xlsx files]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [Dim][ workbook [As] IWorkbook = excelEngine.Excel.Workbooks.Open([\"Excel2007.xlsx\"], ExcelOpenType.Automatic)] |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Select the version to be saved.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [workbook.Version = ExcelVersion.Excel97to2003]                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'The first worksheet object in the worksheets collection is accessed.]                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [Dim][ sheet [As] IWorksheet = workbook.Worksheets(0)]                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [\'Write data]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [sheet.Range([\"C3:O28\"]).Text = [\"Hello world\"]]                                                                                                             |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [\'Save it as \"Excel 97 to 2003\" format.]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [workbook.SaveAs([\"Sample.xls\"])]                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Xlsx File Format Support List

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Support for Excel 2007 file formats in XlsIO                                                                                                                                                                                  |
+===========================================================+===================================================================================================================================================================+
|  XML-based File Format Support                            | []                                                                                                |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Gets/sets cells (text, date time, time span, error, number, Boolean, formula).                                                                                    |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | New dimensions: 2\^20 x 2\^14.                                                                                                                                    |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Range operations such as copy/move range, insert/remove row/column, formula updates after these operations.                                                       |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Merged cells support.                                                                                                                                             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Row and column settings (default style, height/width, visibility).                                                                                                |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Named ranges support.                                                                                                                                             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Ability to open 2007 files and save into 2003 format (without unsupported items).                                                                                 |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | AutoFilters (existing functionality).                                                                                                                             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Read/write data validation (existing functionality).                                                                                                              |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | \- Read/Write conditional formatting (existing functionality).                                                                                                    |
|                                                           |                                                                                                                                                                   |
|                                                           | \- Increase possible rules number (in Excel 97-2003 there can be only three rules).                                                                               |
|                                                           |                                                                                                                                                                   |
|                                                           | \- New visualizations \[Data bar, Icon sets and Color scales\].                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Adjust row/column height & width, insert rows/cols, group/ungroup \[with summary settings\], freeze pane and split pane.                                          |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Images operations (insert/remove/move/resize/open/save, without fill).                                                                                            |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Read/Write hyperlinks (existing functionality).                                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Comments (open/save/move/resize/add/remove/get and set rtf text, author, without fill).                                                                           |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Document properties (built-in and custom) and sheet level properties.                                                                                             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Page Setup (all existing properties including header/footer images and page breaks), page layout, zoom, sheet alignment \[right to left\] and page break preview. |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Worksheet properties (tab color, background image, hide and rename).                                                                                              |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Ignore error indicator, show/hide gridlines and gridline color.                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Gets/sets RTF string.                                                                                                                                             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Worksheet protection with or without password, workbook window or structure protection without password.                                                          |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Encryption and Decryption.                                                                                                                                        |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | TextBox, CheckBox and Combo Box -- Read/Write support.                                                                                                            |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Pivot Table creation and formatting.                                                                                                                              |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Tables -- Read/Write and Styles support (Table Formulas are not supported).                                                                                       |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Read/Write Excel 2007 Formulas.                                                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Chart - existing functionality except the options given below which are not supported.                                                                            |
|                                                           |                                                                                                                                                                   |
|                                                           |                                                                                                                                                                   |
|                                                           |                                                                                                                                                                   |
|                                                           | 1\. Secondary axes \[partial\].                                                                                                                                   |
|                                                           |                                                                                                                                                                   |
|                                                           | 2\. Marker filling options.                                                                                                                                       |
|                                                           |                                                                                                                                                                   |
|                                                           | 3\. Drop lines.                                                                                                                                                   |
|                                                           |                                                                                                                                                                   |
|                                                           | 4\. Chart referring to values in other worksheet/workbook.                                                                                                        |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Objects Preservation while Opening and Saving XLSX Format |                                                                                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Pivot Tables                                                                                                                                                      |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Shapes (auto shapes, Image styles).                                                                                                                               |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cell Styles Support                                       |                                                                                                                                                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Read/Write/Set Cell styles (All styles in Biff8 format).                                                                                                          |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Themes                                                                                                                                                            |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | 32-bit colors                                                                                                                                                     |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Excel 2007 Built-In Styles.                                                                                                                                       |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | Gradient Fill                                                                                                                                                     |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                           | New count restriction - \~65000.                                                                                                                                  |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

The following screen shot shows the output file generated by Essential XlsIO, with all the basic features supported \[Multiple conditional formatting\].

 

{border="0"}

Figure 30: Sample .xlsx file created with XlsIO[]

[] 

For More Information Refer:

**[]** 

[[]]{.MsoHyperlink}

[[]]{.MsoHyperlink} 

More:





