---
title: windows3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\windows3.md
created_at: 2025-07-03
---








  









### Windows {#windows style="tab-stops: 0pt"}

 

Now, you have created a Windows application (refer). This section covers the following:

 

[·      ]Deploying Essential XlsIO in a Windows Application

[·      ]Creating and adding an Excel document (with worksheets) to the Application

 

Deploying Essential XlsIO in a Windows Application

 

The following steps will guide you to deploy Essential XlsIO:

1.   Go to **Solution Explorer** of the application you have created. Right-click the **Reference** folder and then click **Add References**.

2.   Add the following assemblies as references in the application.

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.dll

[·      ]Syncfusion.XlsIO.base.dll

[] 


[{border="0"}][Note:][ For detailed documentation on Windows Application deployment, see: ][[http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf]{.UGHyperlink}](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf)[.]


 

Essential XlsIO is deployed in the Windows application.

 

Creating and Adding an Excel Document (With Worksheets) to the Application

 

The following steps will guide you to create and add XlsIO document to this application:

 

1.   Add the following C# code to import the Syncfusion.XlsIO namespace.

[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                  |
| **[]**                                                           |
|                                                                                                                  |
| [using][ Syncfusion.XlsIO;] |
+------------------------------------------------------------------------------------------------------------------+

[] 

The Syncfusion.XlsIO namespace is imported.

[] 

2.   Create an instance of XlsIO by using the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [// New instance of XlsIO is created.\[Equivalent to launching MS Excel with no workbooks open\].]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [// Instantiate the spreadsheet creation engine.]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [ExcelEngine][ excelEngine = ][new][ ][ExcelEngine][();] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\' New instance of XlsIO is created.\[Equivalent to launching MS Excel with no workbooks open\].]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Instantiate the spreadsheet creation engine.]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ excelEngine ][As][ ExcelEngine = ][New][ ExcelEngine()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

An instance of XlsIO is created.

 

!, for more details.

[] 

3.   Create an instance of the Excel application through the **IApplication** interface.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [// Instantiate the Excel application object.]                                                        |
|                                                                                                                                                         |
| [IApplication][ application = excelEngine.Excel;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [\' Instantiate the Excel application object.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [Dim][ application ][As][ IApplication = excelEngine.Excel] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

An Excel document is created.

 

4.   Create a workbook. A newly created workbook has three worksheets by default. You can change the number of worksheets, using the **Create** method of **IWorkBook** as shown in the following code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| **[]**                                                                                                                      |
|                                                                                                                                                                 |
| [// A new workbook is created.\[Equivalent to creating a new workbook in MS Excel).]                          |
|                                                                                                                                                                 |
| [// The new workbook will have 5 worksheets.]                                                                 |
|                                                                                                                                                                 |
| [IWorkbook][ workbook = application.Workbooks.Create(5);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [\' A new workbook is created.\[Equivalent to creating a new workbook in MS Excel\].]                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [\' The new workbook will have 5 worksheets.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [Dim][ workbook ][As][ IWorkbook = application.Workbooks.Create(5)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A workbook with the mentioned number of worksheets is created in the Excel document.

 

 and , for more details.

 

5.   Access the worksheet in the workbook and set the data for the given range, say \"A1\".

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [// The first worksheet object in the worksheets collection is accessed.]                                                                                          |
|                                                                                                                                                                                                                      |
| [IWorksheet][ sheet = workbook.Worksheets\[0\];      ][                  ] |
|                                                                                                                                                                                                                      |
| [                        ]                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| [// Inserting sample text into the first cell of the first worksheet.]                                                                                             |
|                                                                                                                                                                                                                      |
| [sheet.Range\[\"A1\"\].Text = \"Hello World\";]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [\' The first worksheet object in the worksheets collection is accessed.]                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [Dim][ sheet ][As][ IWorksheet = workbook.Worksheets(0)] |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [\' Inserting sample text into the first cell of the first worksheet.]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [sheet.Range(\"A1\").Text = \"Hello World\"]                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The string \"Hello World\" is written to the cell **A1** of the document.

 

6.   Save and close the workbook.

[] 

+--------------------------------------------------------------------------------------+
| **[\[C#\]]**                                     |
|                                                                                      |
| **[]**                                           |
|                                                                                      |
| [// Saving the workbook to disk.]  |
|                                                                                      |
| [workbook.SaveAs(\"Sample.xls\");] |
|                                                                                      |
| []                                               |
|                                                                                      |
| [// Closing the workbook.]         |
|                                                                                      |
| [workbook.Close();]                |
+--------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                |
|                                                                                     |
| **[]**                                          |
|                                                                                     |
| [\' Saving the workbook to disk.] |
|                                                                                     |
| [workbook.SaveAs(\"Sample.xls\")] |
|                                                                                     |
| []                                |
|                                                                                     |
| [\' Closing the workbook.]        |
|                                                                                     |
| [workbook.Close()]                |
+-------------------------------------------------------------------------------------+

 

The Workbook is saved and closed.

 

!.

[] 

7.   Dispose the Excel engine. Note that the engine should be disposed after completing workbook operations.

[] 

+----------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                  |
| **[]**                                       |
|                                                                                  |
| [// Dispose the Excel engine.] |
|                                                                                  |
| [excelEngine.Dispose();]       |
+----------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                             |
|                                                                                  |
| **[]**                                       |
|                                                                                  |
| [\' Dispose the Excel engine.] |
|                                                                                  |
| [excelEngine.Dispose()]        |
+----------------------------------------------------------------------------------+

 

The Excel engine is disposed.

 

This completes the creation of an Excel document in the Windows Application, using Essential XlsIO.

 

The following screen shot shows the Excel document generated by the above given procedure.

 

{border="0"}

Figure 19: Spreadsheet created in the Windows Application[]

[] 

{border="0"} It is possible to serialize the XlsIO object model to any of the following file formats:

[] 

[·      ]BIFF8

[·      ]BIFF12

[·      ]SpreadsheetML

[·      ]CSV

[]{#p15}**[]** 

[]{#related-topics}

