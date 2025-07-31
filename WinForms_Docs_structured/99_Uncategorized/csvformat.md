---
title: csvformat.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\csvformat.md
created_at: 2025-07-03
---








  









### CSV Format {#csv-format style="tab-stops: 0pt"}

 

The Comma Separated Value (CSV) file format is a file type that stores tabular data. The CSV file format is often used to exchange data between disparate applications. The file format, as it is used in Microsoft Excel, has become a pseudo standard throughout the industry, even among non-Microsoft platforms.

 

XlsIO provides support for reading and writing CSV files. The following code example illustrates how to open a **.csv** file.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [// Opening a File.]                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [IWorkbook][ workbook = application.Workbooks.Open([\"CSVfile.csv\"], [\",\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [\' Opening a File.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [Dim][ workbook [As] IWorkbook = application.Workbooks.Open([\"CSVfile.csv\"], [\",\"])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

While saving files, you have options to save as Unicode, ASCII, and other Non-Unicode encoding. The following code example illustrates how to save a file to the CSV format.

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| **[]**                                                                                    |
|                                                                                                                                             |
| [// Saving the workbook to disk. ]                                                        |
|                                                                                                                                             |
| [sheet.SaveAs([\"Sample.csv\"],[\",\"],Encoding.ASCII); ] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                       |
|                                                                                                                                            |
| **[]**                                                                                                 |
|                                                                                                                                            |
| [\' Saving the workbook to disk.]                                                        |
|                                                                                                                                            |
| [sheet.SaveAs([\"Sample.csv\"],[\",\"],Encoding.ASCII) ] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

For More Information Refer:

 

[]

 

**[]** 

**[]** 

[]{#related-topics}

