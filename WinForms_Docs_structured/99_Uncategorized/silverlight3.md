---
title: silverlight3.md
original_path: WinForms_Docs/99_Uncategorized/silverlight3.md
created_at: 2025-08-05
---








  









### Silverlight {#silverlight style="tab-stops: 0pt"}

 

Now, you have created a Silverlight application (refer ). This section covers the following:

 

[·      ]Deploying Essential XlsIO in a Silverlight Application

[·      ]Creating and adding an Excel document (with worksheets) to the application

 

Deploying Essential XlsIO in a Silverlight Application

 

The following steps will guide you to deploy Essential XlsIO:

 

1.   Open the **MainPage.xaml** of the application in the designer.

2.   Add the **Syncfusion.Compression.Silverlight.dll** and **Syncfusion.XlsIO.Silverlight.dll** assemblies as references to the application.

 

Essential XlsIO is now deployed in your Silverlight application.

 

Creating and Adding an Excel Document (With Worksheets) to the Application

 

Essential XlsIO for Silverlight has support for creation and manipulation of richly formatted Excel \[97-2003\] format spreadsheets from scratch on the client side. Advanced features like Data Validation, Conditional Formatting and Charts can also be used in this approach.

 

Following steps will guide you to create a simple spreadsheet:

[] 

1.   Add references to the following assemblies.

[] 

[·      ]Syncfusion.Compression.Silverlight.dll

[·      ]Syncfusion.XlsIO.Silverlight.dll

[] 

2.   The next step is to add reference to the following namespace.

[] 

[·      ]**Syncfusion.XlsIO** (using Syncfusion.XlsIO)

**[]** 

+------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                  |
| **[]**                                                           |
|                                                                                                                  |
| [using][ Syncfusion.XlsIO;] |
+------------------------------------------------------------------------------------------------------------------+

[] 

3.   Instantiate the [Excel Engine].

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [// New instance of XlsIO is created.\[Equivalent to launching MS Excel with no workbooks open\].]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [// The instantiation process consists of two steps.]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [// Step 1: Instantiate the spreadsheet creation engine.]                                                                                                                                                                                                                                                             |
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
| [\' The instantiation process consists of two steps.]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Step 1: Instantiate the spreadsheet creation engine.]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ excelEngine ][As][ ExcelEngine = ][New][ ExcelEngine()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Instantiate the Excel application through the **IApplication** interface which represents an Excel application.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [// Step 2: Instantiate the excel application object.]                                                |
|                                                                                                                                                         |
| [IApplication][ application = excelEngine.Excel;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [\' Step 2: Instantiate the excel application object.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [Dim][ application ][As][ IApplication = excelEngine.Excel] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

An Excel document is created.

[] 

5.   Create a workbook. A newly created workbook has three worksheets by default. You can change the count of the worksheets by using the **Create** method of .

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

[] 

A workbook with the mentioned number of worksheets is created in the Excel document.

[] 

6.   Access the  in the workbook and set the data for the given Range, say \"A1\".

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

[] 

The string \"Hello World\" is written to the cell A1 of the document.

[] 

7.   Save to stream and close the workbook. Also, dispose the Excel engine.

[] 


{border="0"}Note: The engine should be disposed after completing workbook operations.


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [// Save the file on to disk.]                                                                                                        |
|                                                                                                                                                                                         |
| [SaveFileDialog][ sfd = [new] [SaveFileDialog]();] |
|                                                                                                                                                                                         |
| [sfd.DefaultExt = [\".xls\"];]                                                                                              |
|                                                                                                                                                                                         |
| [sfd.Filter = [\"Files(\*.xls)\|\*.xls\"];]                                                                                 |
|                                                                                                                                                                                         |
| [if][ (sfd.ShowDialog() == [true])]                                           |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    using][ ([Stream] stream = sfd.OpenFile())]                           |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        workbook.SaveAs(stream);]                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [      [// Closing the workbook.]]                                                                                            |
|                                                                                                                                                                                         |
| [      workbook.Close();]                                                                                                                           |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [      [// Dispose the Excel Engine.]]                                                                                        |
|                                                                                                                                                                                         |
| [      excelEngine.Dispose();]                                                                                                                      |
|                                                                                                                                                                                         |
| [   }]                                                                                                                                              |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                         |
| [\' Save the file on to disk.]                                                                                                        |
|                                                                                                                                                                                         |
| [Dim][ sfd [As] SaveFileDialog = [New] SaveFileDialog()] |
|                                                                                                                                                                                         |
| [sfd.DefaultExt = \".xls\"]                                                                                                                         |
|                                                                                                                                                                                         |
| [sfd.Filter = \"Files(\*.xls)\|\*.xls\"]                                                                                                            |
|                                                                                                                                                                                         |
| [If][ sfd.ShowDialog() = [True] [Then]]                  |
|                                                                                                                                                                                         |
| [      [Using] stream [As] Stream = sfd.OpenFile()]                                                       |
|                                                                                                                                                                                         |
| [            workbook.SaveAs(stream)]                                                                                                               |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [\' Closing the workbook.]]                                                                                      |
|                                                                                                                                                                                         |
| [            workbook.Close()]                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [\' Dispose the Excel Engine.]]                                                                                  |
|                                                                                                                                                                                         |
| [            excelEngine.Dispose()]                                                                                                                 |
|                                                                                                                                                                                         |
| [      [End] [Using]]                                                                                     |
|                                                                                                                                                                                         |
| [End][ [If]]                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

The Workbook is saved and closed and the Excel engine is disposed.

[] 


{border="0"}Note:       This is a very basic usage scenario where \"Hello World\" is inserted into the cell \"A1\" of the spreadsheet. The more advanced usage scenarios of creating complex spreadsheets from scratch are explained in detail in this user guide.


[] 

{border="0"}

Figure 23: Spreadsheet created in the Silverlight Application[]

[] 

 

A spreadsheet has been created in the Silverlight application.

 

Following are the list of supported elements in XlsIO for Silverlight.

 


+-------------------------------------------------------------------------------------+-------------------+-------------------+-----------------+
| Element                                                                             | xls                                   | xlsx            |
|                                                                                     +-------------------+-------------------+-----------------+
|                                                                                     | Read              | Write             | Not Supported   |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Font settings                                                                       | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Alignments                                                                          | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Number formatting                                                                   | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Border settings                                                                     | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Fill settings                                                                       | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Autofit                                                                             | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Cell styles                                                                         | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| RGB Colors                                                                          | Yes (Indexed)     | Yes (Indexed)     |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Conditional formatting                                                              | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Hide/unhide rows/cols                                                               | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Hide/Unhide worksheet                                                               | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Copy/Move worksheet                                                                 | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Sheet protection                                                                    | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Workbook protection                                                                 | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Sheet format\[sheet name, tab color\]                                               | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Bitmap Images                                                                       | Yes               | Yes               |                 |
|                                                                                     |                   |                   |                 |
|                                                                                     |                   |                   |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Vector Images                                                                       | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Charts                                                                              | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Hyperlinks                                                                          | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Header/Footer                                                                       | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Pivot tables                                                                        | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Auto Shapes                                                                         | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Text Box                                                                            | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Check Box                                                                           | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Combo Box                                                                           | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Page setup                                                                          | Yes               | Yes               |                 |
|                                                                                     |                   |                   |                 |
| \[Margin,origin,page size\]                                                         |                   |                   |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Page breaks                                                                         | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Background image                                                                    | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Print settings\[Print area,Print titles,page order\]                                | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Formulas                                                                            | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Calculation options                                                                 | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Names                                                                               | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Formula auditing \[ Ignore error \]                                                 | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Autofilter                                                                          | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Data validation                                                                     | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Template marker                                                                     | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Outlines\[group/ungroup, summary settings\]                                         | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Comments                                                                            | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Freeze pane, split pane                                                             | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| View\[Zoom,show/hide gridline,show/hide headings\], horizontal/vertical scroll bars | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Macros                                                                              | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Encryption                                                                          | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Decryption                                                                          | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Ole Objects                                                                         | No                | No                |                 |
|                                                                                     |                   |                   |                 |
|                                                                                     |                   |                   |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Track changes                                                                       | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Streams                                                                             | Yes               | Yes               |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+                 |
| Tables                                                                              | No                | No                |                 |
+-------------------------------------------------------------------------------------+-------------------+-------------------+-----------------+


 

[]{#p18}**[]** 

[]{#related-topics}

