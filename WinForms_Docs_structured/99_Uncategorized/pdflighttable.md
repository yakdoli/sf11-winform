---
title: pdflighttable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pdflighttable.md
created_at: 2025-07-03
---






##### PdfLightTable {#pdflighttable style="tab-stops: 0pt"}

 

The PdfLightTable class represents simple tables that are used for publishing structured data from arrays, data tables or data columns. There are no real cells or rows, and all the data is taken from the data source (DataSource property).

Using PdfLightTable, any type of table can be created using its event handlers. PdfLightTable in Silverlight supports IEnumerable and TableDirect data sources and not arrays, data tables or data columns. This section explains how to draw PdfLightTable elements using Essential PDF. It includes the following topics:

 

###### []{#_Properties,_Methods_and_1}4.1.2.3.1.1 Properties, Methods and Events {#properties-methods-and-events style="tab-stops: 0pt"}

 

Properties

 


  -------------------------- ---------------------------------------------------------------------------------------------- -----------------------------
  Name                       Description                                                                                    Data Type
  AllowRowBreakAcrossPages   Gets or sets a value indicating the row break is to be made or not                             Boolean
  Columns                    Gets the columns                                                                               PdfColumnCollection
  DataMember                 Gets or sets the data member                                                                   String
  DataSource                 Gets or sets the data source                                                                   Object
  DataSourceType             Gets or sets the data source type of the PdfLightTable                                         PdfLightTableDataSourceType
  IgnoreSorting              Gets or sets a value indicating whether PdfLightTable should ignore sorting in the DataTable   Boolean
  Rows                       Gets the rows                                                                                  PdfRowCollection
  Style                      Gets or sets the properties                                                                    PdfLightTableStyle
  -------------------------- ---------------------------------------------------------------------------------------------- -----------------------------


 

Methods

 


+-----------------+---------------------+---------------------------------------------------------------------------------+---------------------------+
| Method          | Description         | Parameters                                                                      | Return Type               |
+-----------------+---------------------+---------------------------------------------------------------------------------+---------------------------+
| Draw            | Draws PdfLightTable | Overloads:                                                                      | Void                      |
|                 |                     |                                                                                 |                           |
|                 |                     | (PdfGraphics graphics)                                                          |                           |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, PointF location)                                                 | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, RectangleF bounds)                                               | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfGraphics graphics, PointF location)                                         | Void                      |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfGraphics graphics, RectangleF bounds)                                       | Void                      |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, float x, float y)                                                | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, PointF location, PdfLightTableLayoutFormat format)               | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, PointF location, PdfLayoutFormat format)                         | PdfLayoutResult           |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, RectangleF bounds, PdfLightTableLayoutFormat format)             | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, PointF location, PdfLayoutFormat format)                         | PdfLayoutResult           |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfGraphics graphics, float x, float y)                                        | void                      |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfGraphics graphics, PointF location, float width)                            | void                      |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, float x, float y, float width)                                   | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | PdfPage page, float x, float y, PdfLightTableLayoutFormat format)               | PdfLightTableLayoutResult |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, float x, float y, PdfLayoutFormat format)                        | PdfLayoutResult           |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfGraphics graphics, float x, float y, float width)                           | void                      |
|                 |                     +---------------------------------------------------------------------------------+---------------------------+
|                 |                     | (PdfPage page, float x, float y, float width, PdfLightTableLayoutFormat format) | PdfLightTableLayoutResult |
+=================+=====================+=================================================================================+===========================+


 

Events

 


+-----------------------------------+-----------------------------------------------------------------+
| Name                              | Description                                                     |
+-----------------------------------+-----------------------------------------------------------------+
| BeginCellLayout                   | This event is raised on starting cell layout.                   |
+-----------------------------------+-----------------------------------------------------------------+
| BeginPageLayout                   | This event is raised before the element is printed on the page. |
|                                   |                                                                 |
|                                   | (Inherited from PdfLayoutElement.)                              |
+-----------------------------------+-----------------------------------------------------------------+
| BeginRowLayout                    | This event is raised on starting row layout.                    |
+-----------------------------------+-----------------------------------------------------------------+
| EndCellLayout                     | This event is raised on having finished cell layout.            |
+-----------------------------------+-----------------------------------------------------------------+
| EndPageLayout                     | This event is raised after the element is printed on the page.  |
|                                   |                                                                 |
|                                   | (Inherited from PdfLayoutElement.)                              |
+-----------------------------------+-----------------------------------------------------------------+
| EndRowLayout                      | This event is raised on finishing row layout.                   |
+-----------------------------------+-----------------------------------------------------------------+
| QueryColumnCount                  | This event is raised when the column number is requested.       |
+-----------------------------------+-----------------------------------------------------------------+
| QueryNextRow                      | This event is raised when the next row data is requested.       |
+-----------------------------------+-----------------------------------------------------------------+
| QueryRowCount                     | This event is raised when the row number is requested.          |
+-----------------------------------+-----------------------------------------------------------------+


 

###### []{#_PDFLightTable_Creation}4.1.2.3.1.2 PdfLightTable Creation {#pdflighttable-creation style="tab-stops: 0pt"}


Note: You should add the Syncfusion.Pdf.Tables namespace to work with PdfLightTable.


 

You may create a PdfLightTable simply by specifying a new operator with the proper constructor. After assigning the data source, it can be drawn using one of the overloads of Draw method as follows:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| [// Creating a PdfLightTable.]                                                                                                                |
|                                                                                                                                                                                                 |
| [PdfLightTable][ pdfLightTable = [new] [PdfLightTable]();] |
|                                                                                                                                                                                                 |
| [            ]                                                                                                                                              |
|                                                                                                                                                                                                 |
| [// Assigning data source.]                                                                                                                   |
|                                                                                                                                                                                                 |
| [pdfLightTable.DataSource = dataSource;]                                                                                                                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Drawing PdfLightTable.]                                                                                                                   |
|                                                                                                                                                                                                 |
| [pdfLightTable.Draw(graphics);]                                                                                                                             |
|                                                                                                                                                                                                 |
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| [\' Creating a PdfLightTable.][]                                                                          |
|                                                                                                                                                                                                 |
| [Dim][ pdfLightTable [As] [New] PdfLightTable()]                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\' Assigning data source.][]                                                                             |
|                                                                                                                                                                                                 |
| [pdfLightTable.DataSource = dataSource]                                                                                                                     |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\' Drawing PdfLightTable.][]                                                                             |
|                                                                                                                                                                                                 |
| [pdfLightTable.Draw(graphics)]                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Different types of data can be set to PdfLightTable. Also, the draw method facilitates overloads that would help you to layout the PdfLightTable as required. The topics that discuss them are:

[[·      ]]{.UGHyperlink}[[Data ]]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[[Layout]]{.UGHyperlink}

 

Ignore Sorting

 

If there is a DataTable assigned as a data source, you may specify whether you need sorted or unsorted data. If this property is set to True, the DataTable sorting will be ignored.


Note: Sorting is disabled, by default. This is because sorted data takes more time.


 

AllowRowBreakAcrossPages

 

This property allows changing the row split behavior across pages. By default, this Boolean property is set to True, which allows splitting the row across pages when the row cannot accommodate within the bounds of the page. If set to false, the entire row will be shifted to the next page.


Note: If the row height is greater than the page height, it will be forcibly split across pages ignoring this property.


 

[]{#_Data}4.1.2.3.1.2.1      Data

[] 

You can initialize the data to the PdfLightTable with the help of the DataSource property. This is achieved through:

[·      ]External DataSource: By assigning the External data source

[·      ]Table Direct : By adding columns and rows to the PdfLightTable

[·      ]Event Handlers : By adding columns and rows by using the event handlers

 

4.1.2.3.1.2.1.1    External DataSource

 

Data source is an object that might be an array (two-dimensional, one-dimensional or nested), a DataTable, DataColumn, DataView or DataSet. To draw an external data source, you must set DataSourceType property to PdfLightTableDataSourceType.External.

The following code example illustrates how to assign external data source to PdfLightTable:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
|                                                                                                                                                                         |
|                                                                                                                                                                         |
| [pdfLightTable][.DataSourceType = [PdfLightTableDataSourceType].External;] |
|                                                                                                                                                                         |
| [pdfLightTable][.DataSource = dataTable;]                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
| [pdfLightTable][.DataSourceType = [PdfLightTableDataSourceType].External] |
|                                                                                                                                                                        |
| [pdfLightTable][.DataSource = dataTable]                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Note:  External data source is the default data source.

 


4.1.2.3.1.2.1.2    [Table Direct]

 

You can directly add rows and columns to PdfLightTable. To achieve this, set DataSourceType property to PdfLightTableDataSourceType .TableDirect. The following code example illustrates this:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [PdfLightTable][ pdfLightTable = [new] [PdfLightTable]();  ]                                                                               |
|                                                                                                                                                                                                                                                                           |
| [         ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [// Setting the DataSourceType as Direct]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.DataSourceType = [PdfLightTableDataSourceType].TableDirect;]                                                                                                |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [// Creating Columns]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.Columns.Add([new] [PdfColumn]([\"Roll Number\"]));]                                                             |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.Columns.Add([new] [PdfColumn]([\"Name\"]));]                                                                    |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.Columns.Add([new] [PdfColumn]([\"Class\"]));]                                                                   |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [// Adding Rows]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.Rows.Add([new] [object]\[\] {[\"111\"],[\"Maxim\"],[\"III\"] });] |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [// Drawing the PdfLightTable]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [pdfLightTable][.Draw(page, [PointF].Empty);]                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [Dim][ pdfLightTable[ As] PdfLightTable = [New] PdfLightTable()]                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\' Setting the DataSourceType as Direct]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.DataSourceType = PdfLightTableDataSourceType.TableDirect]                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\' Creating Columns]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.Columns.Add([New] PdfColumn(\"Roll Number\"))]                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.Columns.Add([New] PdfColumn(\"Name\"))]                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.Columns.Add([New] PdfColumn(\"Class\"))]                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\' Adding Rows]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.Rows.Add([New] [Object]() {\"[111]\",\"[Maxim]\",\"[III]\" })] |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\' Drawing the PdfLightTable]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [pdfLightTable][.Draw(page, PointF.Empty)]                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.1.2.3.1.2.1.2.1   [IEnumerable ]{.Heading9Char}[]

[] 

PdfLightTable in Silverlight platform can take input from IEnumerable objects.The following is the code snippet:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                        |
| [//Creating PdfLightTable.]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                        |
| [PdfLightTable][ pdfLightTable = [new] [PdfLightTable]();]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [//Creating IEnumerable source.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| [Dictionary][\<[string], [string]\> dictionary = [new] [Dictionary]\<[string], [string]\>();] |
|                                                                                                                                                                                                                                                                                                                        |
| [dictionary.Add([\"AAA\"], [\"111\"]);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [dictionary.Add([\"BBB\"], [\"112\"]);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [dictionary.Add([\"CCC\"], [\"113\"]);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [pdfLightTable.DataSource = dictionary;]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [//Draw.]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [pdfLightTable.Draw(page, [PointF].Empty);]                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [\'Creating PdfLightTable.][]                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [Dim][ pdfLightTable [As] [New] PdfLightTable()]                                                                                   |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [\'Creating IEnumerable source.][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [Dim][ dictionary [As] [New] Dictionary([Of] [String], [String])()] |
|                                                                                                                                                                                                                                                                   |
| [dictionary][.Add([\"AAA\"], [\"111\"])]                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [dictionary][.Add([\"BBB\"], [\"112\"])]                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [dictionary][.Add([\"CCC\"], [\"113\"])]                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [pdfLightTable.DataSource = dictionary]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [\'Drawing the PdfLightTable][]                                                                                                                                             |
|                                                                                                                                                                                                                                                                   |
| [pdfLightTable.Draw(page, PointF.Empty)]                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.1.2.3.1.2.1.3    Event Handlers

 

Data to PdfLightTable can also be set using the following three events:

[·      ]QueryColumnCount -- Sets the number of columns.

[·      ]QueryRowCount -- Sets the number of rows.

[·      ]QueryNextRow -- Sets data to the PdfLightTable.


Note: These events will act only when the DataSource property is not set.


 

The following code snippet illustrates this:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| [public][ [string]\[\]\[\] datastring = [new] [string]\[2\]\[\];]                         |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Giving it some column arrays]                                                                                                                                                           |
|                                                                                                                                                                                                                                               |
| [datastring\[0\] = [new] [string]\[\] { [\"111\"], [\"Maxim\"], [\"100\"] };]           |
|                                                                                                                                                                                                                                               |
| [datastring\[1\] = [new] [string]\[\] { [\"222\"], [\"Calvin\"], [\"95\"] };]           |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Creating PdfLightTable]                                                                                                                                                                 |
|                                                                                                                                                                                                                                               |
| [PdfLightTable][ pdfLightTable = [new] [PdfLightTable]();]                                               |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [pdfLightTable.QueryColumnCount += [new] [QueryColumnCountEventHandler](pdfLightTable_QueryColumnCount);]                                                    |
|                                                                                                                                                                                                                                               |
| [pdfLightTable.QueryNextRow += [new] [QueryNextRowEventHandler](pdfLightTable_QueryNextRow);]                                                                |
|                                                                                                                                                                                                                                               |
| [pdfLightTable.QueryRowCount += [new] [QueryRowCountEventHandler](pdfLightTable_QueryRowCount);]                                                             |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Drawing the PdfLightTable]                                                                                                                                                              |
|                                                                                                                                                                                                                                               |
| [pdfLightTable.Draw(page, [PointF].Empty);]                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Getting the number of columns]                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [void][ pdfLightTable_QueryColumnCount([object] sender, [QueryColumnCountEventArgs] args)]                  |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [    args.ColumnCount = 3;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Getting the number of rows]                                                                                                                                                             |
|                                                                                                                                                                                                                                               |
| [void][ pdfLightTable_QueryRowCount([object] sender, [QueryRowCountEventArgs] args)]                        |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [    args.RowCount = 2;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Getting the row data]                                                                                                                                                                   |
|                                                                                                                                                                                                                                               |
| [void][ pdfLightTable_QueryNextRow([object] sender, [QueryNextRowEventArgs] args)]                          |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [    [if] (args.RowIndex \< datastring.Length)]                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [        args.RowData = [new] [string]\[\] { datastring\[args.RowIndex\]\[0\],           datastring\[args.RowIndex\]\[1\], datastring\[args.RowIndex\]\[2\] };] |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Public][ datastring(1)() [As] [String]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Giving it some column arrays][]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ datastring(0) = [New] [String]() { [\"111\"], [\"Maxim\"], [\"100\"] }]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ datastring(1) = [New] [String]() { [\"222\"], [\"Calvin\"], [\"95\"] }]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Creating PdfLightTable][]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ pdfLightTable [As] [New] PdfLightTable()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [pdfLightTable.QueryColumnCount += [New] QueryColumnCountEventHandler([AddressOf] pdfLightTable_QueryColumnCount)]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [pdfLightTable.QueryNextRow += [New] QueryNextRowEventHandler([AddressOf] pdfLightTable_QueryNextRow)]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [pdfLightTable.QueryRowCount += [New] QueryRowCountEventHandler([AddressOf] pdfLightTable_QueryRowCount)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Drawing the PdfLightTable][]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [pdfLightTable.Draw(page, PointF.Empty)]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Getting the number of columns][]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][[ ]]{.apple-converted-space}[Sub ][pdfLightTable_QueryColumnCount([Object] sender, QueryColumnCountEventArgs args)] |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      args.ColumnCount = 3]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][[ ]]{.apple-converted-space}[Sub]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Getting the number of rows][]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][[ ]]{.apple-converted-space}[Sub ][pdfLightTable_QueryRowCount([Object] sender, QueryRowCountEventArgs args)]       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      args.RowCount = 2]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][[ ]]{.apple-converted-space}[Sub]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Getting row data][]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][[ ]]{.apple-converted-space}[Sub][ pdfLightTable_QueryNextRow([Object] sender, QueryNextRowEventArgs args)]         |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      [If] args.RowIndex \< datastring.Length [Then]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            args.RowData = [New] [String]() { datastring(args.RowIndex)(0), datastring(args.RowIndex)(1), datastring(args.RowIndex)(2) }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      [End] [If]]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][[ ]]{.apple-converted-space}[Sub]                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_Table_Layout}4.1.2.3.1.2.2      Layout

 

PdfLightTableLayoutFormat

 

Layouting PdfLightTable can be done using the PdfLightTableLayoutFormat class. Overloads accepting pages can accept standard formats as other layouting elements. However, they treat the PdfLayoutBreakType.FitElement value of Format.Break property as one, for a single row and not for the entire PdfLightTable.

 

 Properties

 


  ------------------ -------------------------------------------------------------- --------------------
  Name               Description                                                    Data Type
  Break              Gets or sets the break type                                    PdfLayoutBreakType
  EndColumnIndex     Gets or sets the end column index                              Integer
  Layout             Gets or sets the layout type                                   PdfLayoutType
  PaginateBounds     Gets or sets the PdfLightTable bounds for the following page   RectangleF
  StartColumnIndex   Gets or sets the start column index                            Integer
  ------------------ -------------------------------------------------------------- --------------------


 

Also, you may select a range of column using the PdfLightTableLayoutFormat properties, StartColumnIndex and EndColumnIndex. You should pass an instance of this class to one of the Draw overloads, instead of the PdfLayoutFormat class instance.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [PdfLightTableLayoutFormat][ format = [new] [PdfLightTableLayoutFormat]();] |
|                                                                                                                                                                                                            |
| [format.StartColumnIndex = 0;]                                                                                                                                         |
|                                                                                                                                                                                                            |
| [format.EndColumnIndex = 3;]                                                                                                                                           |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [// Draws the PdfLightTable from the first to the fourth column]                                                                                         |
|                                                                                                                                                                                                            |
| [pdfLightTable.Draw(page, [PointF].Empty, format);]                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [Dim][ format [As] [PdfLightTableLayoutFormat] = [New] [PdfLightTableLayoutFormat]()] |
|                                                                                                                                                                                                                                                                |
| [format.StartColumnIndex = 0]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [format.EndColumnIndex = 3]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\'Drawing the PdfLightTable from the first to the fourth column]                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [pdfLightTable.Draw(page, PointF.Empty, format)]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The PdfLayoutType class is used to specify the type of pagination. The Paginate LayoutType draws the PdfLightTable on the (immediate) following pages, if the element exceeds the page. The OnePage layout draws the element only on one page. The following code example illustrates this:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [PdfLightTableLayoutFormat][ format = [new] [PdfLightTableLayoutFormat]();] |
|                                                                                                                                                                                                            |
| [format.Layout = [PdfLayoutType].Paginate;]                                                                                                       |
|                                                                                                                                                                                                            |
| [format.Break = [PdfLayoutBreakType].FitElement;]                                                                                                 |
|                                                                                                                                                                                                            |
| [format.StartColumnIndex = 1;]                                                                                                                                         |
|                                                                                                                                                                                                            |
| [format.EndColumnIndex = 2;]                                                                                                                                           |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [// Drawing the PdfLightTable with the layout format]                                                                                                    |
|                                                                                                                                                                                                            |
| [pdfLightTable.Draw(page, [PointF].Empty, format);]                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [Dim][ format [As] PdfLightTableLayoutFormat = [New] PdfLightTableLayoutFormat()] |
|                                                                                                                                                                                                                  |
| [format.Layout = PdfLayoutType.Paginate]                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [format.Break = PdfLayoutBreakType.FitElement]                                                                                                                               |
|                                                                                                                                                                                                                  |
| [format.StartColumnIndex = 1]                                                                                                                                                |
|                                                                                                                                                                                                                  |
| [format.EndColumnIndex = 2]                                                                                                                                                  |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [\' Drawing the PdfLightTable with the layout format]                                                                                                          |
|                                                                                                                                                                                                                  |
| [pdfLightTable.Draw(page, PointF.Empty, format)]                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

PdfLightTableLayoutResult

 

You can get the layout settings for the drawn PdfLightTable with the help of PdfLightTableLayoutResult class. Also, you can get the bounds and the last page where the PdfLightTable is drawn using the Bounds and Page properties. This is mainly used to write some text or any other element below the large table that shows the number of pages.

 

Properties

 


  -------------- ----------------------------------------------------- ------------
  Name           Description                                           Data Type
  Bounds         Gets the bounds in the last page where it was drawn   RectangleF
  LastRowIndex   Gets the index of the last row                        Integer
  Page           Gets the last page where PdfLightTable was drawn      PdfPage
  -------------- ----------------------------------------------------- ------------


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [// Drawing the PdfLightTable.]                                                                                                                  |
|                                                                                                                                                                                                    |
| [PdfLightTableLayoutResult][ result = pdfLightTable.Draw(page, [PointF].Empty, format);] |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [// Returning the rectangle value for the last page.]                                                                                            |
|                                                                                                                                                                                                    |
| [Console][.WriteLine(result.Bounds.ToString());]                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
| [\' Drawing the PdfLightTable.]                                                                                                                        |
|                                                                                                                                                                                                          |
| [Dim][ result [As] PdfLightTableLayoutResult = pdfLightTable.Draw(page, PointF.Empty, format)] |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
| [\' Returning the rectangle value for the last page.]                                                                                                  |
|                                                                                                                                                                                                          |
| [Console.WriteLine(result.Bounds.ToString())]                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### []{#_PDFLightTable_Formatting}4.1.2.3.1.3 PdfLightTable Formatting {#pdflighttable-formatting style="tab-stops: 0pt"}

This section talks about the most direct and indirect formatting options (through events) that are possible with PdfLightTable. The PdfLightTableStyle class, accessed through Style property of PdfLightTable instance has a number of properties that allow formatting the entire PdfLightTable or parts of it. Border and few other properties are discussed below. Header, Cell, Row and Column are discussed in the following links:

[·      ]Header

[·      ]Row

[·      ]Column

[·      ]Cell

 

Border

 

Border for the entire PdfLightTable can be set using the BorderPen property. Also, border styles applied to individual cells might override this value. You can specify the  to be used to draw border with any color.

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                                             |
|                                                                                                             |
|                                                                                                             |
| [pdfLightTable.Style.BorderPen = [PdfPens].Khaki;] |
+-------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                  |
|                                                                                     |
|                                                                                     |
|                                                                                     |
| [pdfLightTable.Style.BorderPen = PdfPens.Khaki] |
+-------------------------------------------------------------------------------------+

 

BorderOverlapStyle

 

This property decides whether the cell border overlaps with neighboring cells or if it should be drawn inside cell.


Note: This property applies for all cells in the PdfLightTable. You need to be careful when using overlapping borders, because they may produce bad results if they are not of the same width and color.

 


+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                      |
|                                                                                                                                      |
|                                                                                                                                      |
| [pdfLightTable.Style.BorderOverlapStyle = [PdfBorderOverlapStyle].Overlap;] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                           |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
| [pdfLightTable.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap] |
+--------------------------------------------------------------------------------------------------------------+

 

Padding and Spacing

 

You can also specify the cell spacing (distance between cells) and cell padding (distance between cell text and border) for all cells.

 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                      |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
| [pdfLightTable[.Style.CellPadding = 4;]]  |
|                                                                                                     |
| [pdfLightTable[.Style.CellSpacing = 10;]] |
+-----------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                 |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
| [pdfLightTable[.Style.CellPadding = 4]]  |
|                                                                                                    |
| [pdfLightTable[.Style.CellSpacing = 10]] |
+----------------------------------------------------------------------------------------------------+

 

[]{#_Header_1}4.1.2.3.1.3.1      Header

 

Header is a set of rows that repeat on each page and has its own style. Rows for the header might be taken either from column captions or from ordinary rows. In the latter case, the rows are treated as headers and do not appear in the body of the PdfLightTable.

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
|                                                                                                                                 |
|                                                                                                                                 |
| [// Header from column captions]                                              |
|                                                                                                                                 |
| [pdfLightTable.Style.ShowHeader = [true];]                             |
|                                                                                                                                 |
| [pdfLightTable.Style.HeaderSource = [PdfHeaderSource].ColumnCaptions;] |
|                                                                                                                                 |
| [pdfLightTable.Style.RepeateHeader = [true];]                          |
|                                                                                                                                 |
| [pdfLightTable.Style.HeaderStyle = headerStyle;]                                            |
|                                                                                                                                 |
|                                                                                                                                 |
|                                                                                                                                 |
| [// Header from rows]                                                         |
|                                                                                                                                 |
| [pdfLightTable.Style.ShowHeader = [true];]                             |
|                                                                                                                                 |
| [pdfLightTable.Style.HeaderSource = [PdfHeaderSource].Rows;]           |
|                                                                                                                                 |
| [pdfLightTable.Style.RepeatHeader = [true];]                           |
|                                                                                                                                 |
| [pdfLightTable.Style.HeaderRowCount = 3;]                                                   |
|                                                                                                                                 |
| [pdfLightTable.Style.HeaderStyle = headerStyle;]                                            |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                      |
|                                                                                                         |
|                                                                                                         |
|                                                                                                         |
| [\' Header from column captions]                      |
|                                                                                                         |
| [pdfLightTable.Style.ShowHeader = [True]]      |
|                                                                                                         |
| [pdfLightTable.Style.HeaderSource = PdfHeaderSource.ColumnCaptions] |
|                                                                                                         |
| [pdfLightTable.Style.RepeatHeader = [True]]    |
|                                                                                                         |
| [pdfLightTable.Style.HeaderStyle = headerStyle]                     |
|                                                                                                         |
|                                                                                                         |
|                                                                                                         |
| [\' Header from rows]                                 |
|                                                                                                         |
| [pdfLightTable.Style.ShowHeader = [True]]      |
|                                                                                                         |
| [pdfLightTable.Style.HeaderSource = PdfHeaderSource.Rows]           |
|                                                                                                         |
| [pdfLightTable.Style.RepeatHeader = [True]]    |
|                                                                                                         |
| [pdfLightTable.Style.HeaderRowCount = 3]                            |
|                                                                                                         |
| [pdfLightTable.Style.HeaderStyle = headerStyle]                     |
+---------------------------------------------------------------------------------------------------------+

 

The headerStyle is an instance of [PdfCellStyle]() that can be set to header row.

 

4.1.2.3.1.3.2      Row

 

The values of existing row, entered with DataSourceType as PdfLightTableDataSourceType.TableDirect can be edited using the Values property. The following is the code:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [pdfLightTable.Rows\[1\].Values = [new] [string]\[\] { [\"333\"], [\"John\"], [\"234\"] };] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                              |
| [pdfLightTable.Rows(1).Values = [New] [String]() { [\"333\"], [\"John\"], [\"234\"] }] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The minimum height of a row in PdfLightTable can be set using [BeginRowLayout]() and [EndRowLayout]() events.

 

[]{#_Column_1}4.1.2.3.1.3.3      Column

 


  -------------- ----------------------------------------------- -----------------
  Name           Description                                     Data Type
  ColumnName     Gets or sets the column name                    String
  StringFormat   Gets of sets the string format for the column   PdfStringFormat
  Width          Gets of sets the width of the column            float
  -------------- ----------------------------------------------- -----------------


 

ColumnName

 

By default, PdfLightTable displays the column text as the DataSource column name. You can change the column text with the help of the ColumnName property. The following code snippet illustrates this:

 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [// Specifying Column name]                                            |
|                                                                                                                          |
| [pdfLightTable.Columns\[2\].ColumnName = [\"Student Name\"];] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                           |
|                                                                                              |
|                                                                                              |
|                                                                                              |
| [\' Specifying Column name]                |
|                                                                                              |
| [pdfLightTable.Columns(2).ColumnName = \"Student Name\"] |
+----------------------------------------------------------------------------------------------+

 

StringFormat

 

The format of the data for a single column can be changed using the StringFormat property.Check String Formatting in   for more details.

 

Width

 

By default, all the columns in a PdfLightTable have equal width, and the columns automatically fill the entire width of the PdfLightTable. If the width of any of the column(s) is increased or decreased, the width of other columns changes appropriately.

To customize initial column widths, you can invoke the Width property for each column of the PdfLightTable. The following code snippet illustrates this:

 

+---------------------------------------------------------------------------------------+
| **[\[C#\]]**                        |
|                                                                                       |
|                                                                                       |
|                                                                                       |
| [// Setting width for third column] |
|                                                                                       |
| [pdfLightTable.Columns\[2\].Width = 10;]          |
+---------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                    |
|                                                                                       |
|                                                                                       |
|                                                                                       |
| [\' Setting width for third column] |
|                                                                                       |
| [pdfLightTable.Columns(2).Width = 10]             |
+---------------------------------------------------------------------------------------+

 


Note: The unit of the Width property is always points. You can set the PDF units only as points. Also, you can use the  class to convert the other units to points.


 

Column Span

You can set column span in PdfLightTable using BeginRowLayout event. Check the following link for more details.

 []

[] 

[]{#_Cell_1}[4.1.2.3.1.3.4      Cell]{.Heading7Char}

 

You can specify the default cell style by using the DefaultStyle property. The style for the header cells is set by using the HeaderStyle property.

Also, you can specify an alternate style by using the AlternateStyle property. This property is used to customize the appearance of the odd row cells.

 

Properties

 


  ----------------- ----------------------------------------------------------------- -----------------
  Name              Description                                                       Data Type
  BackgroundBrush   Gets or sets the brush with which, the background will be drawn   PdfBrush
  Border            Gets or sets the pen with which, the border will be drawn         PdfPen
  Font              Gets or sets the font                                             PdfFont
  StringFormat      Gets or sets the string format of the text                        PdfStringFormat
  TextBrush         Gets or sets the brush, which will be used to draw font           PdfBrush
  TextPen           Gets or sets the pen, which will be used to draw text outlines    PdfPen
  ----------------- ----------------------------------------------------------------- -----------------


 

The Style property enables you to specify the font along with its appearance (brush, pen and string format), and border along with the background of cells. Although there are fixed properties for styles, you can specify different styles using [BeginCellLayout]() and [EndCellLayou]()t events.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [PdfCellStyle][ altStyle = [new] [PdfCellStyle](font, [PdfBrushes].White, [PdfPens].Green);]    |
|                                                                                                                                                                                                                                                                          |
| [altStyle.BackgroundBrush = [PdfBrushes].DarkGray;]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [PdfCellStyle][ headerStyle = [new] [PdfCellStyle](font, [PdfBrushes].White, [PdfPens].Brown);] |
|                                                                                                                                                                                                                                                                          |
| [headerStyle.BackgroundBrush = [PdfBrushes].Red;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [pdfLightTable.Style.AlternateStyle = altStyle;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [pdfLightTable.Style.HeaderStyle = headerStyle;]                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [Dim][ altStyle [As] Syncfusion.Pdf.Tables.PdfCellStyle = [New]Syncfusion.Pdf.Tables.PdfCellStyle(Font, PdfBrushes.White, PdfPens.Green)]    |
|                                                                                                                                                                                                                                                                             |
| [altStyle.BackgroundBrush = PdfBrushes.DarkGray]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [Dim][ headerStyle [As] Syncfusion.Pdf.Tables.PdfCellStyle = [New]Syncfusion.Pdf.Tables.PdfCellStyle(Font, PdfBrushes.White, PdfPens.Brown)] |
|                                                                                                                                                                                                                                                                             |
| [headerStyle.BackgroundBrush = PdfBrushes.Red]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [pdfLightTable.Style.AlternateStyle = altStyle]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [pdfLightTable.Style.HeaderStyle = headerStyle]                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### []{#_PDFLightTable_Customization}4.1.2.3.1.4 PdfLightTable Customization {#pdflighttable-customization style="tab-stops: 0pt"}

 

PdfLightTable offers a set of events that help to change the look and feel in the PDF. The following are the list of events and links that discuss them:

 

[]{#_BeginPageLayout}4.1.2.3.1.4.1      BeginPageLayout

 

This event is raised before layout starts on a page. The arguments of this event are as follows.

[·      ]Page (read-only): Page on which layout should be performed

[·      ]Bounds: Size of the PdfLightTable part, which should be laid out on the page

[·      ]Cancel: Enables to cancel layout

 

[]{#_EndPageLayout_(sub_section}[]{#_EndPageLayout}4.1.2.3.1.4.2      EndPageLayout

 

This event is raised when layout on a page finishes. The arguments of this event are as follows:

[·      ]Result (read-only): Layout result for the current page

[·      ]NextPage: Page on which layout should continue

 

[]{#_BeginRowLayout_(sub_section}[]{#_BeginRowLayout}[4.1.2.3.1.4.3      BeginRowLayout ]{.Heading8Char}

 

This event is raised when row layout starts. The arguments of this event are as follows:

[·      ]RowIndex (read-only): Index of the row (zero based)

[·      ][CellStyle]() : Style of the cells within the row

[·      ][ColumnSpanMap]() : Array of integers specifying column span

[·      ]Cancel: Enables to cancel layout

[·      ]IgnoreColumnFormat: Gets or sets a value indicating whether column string format should be ignored.

[·      ]Skip: Enables to skip the entire row

[·      ]MinimalHeight: Enables to specify the minimal row height, which is used to preserve space for images

 

The following code example illustrates how to set the row height.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
| [//Subscribing the event]                                                                                                                                           |
|                                                                                                                                                                                                                       |
| [pdfLightTable.BeginRowLayout += [new] [BeginRowLayoutEventHandler](pdfLightTable_BeginRowLayout);]                                     |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
| [//Setting row height for the second row]                                                                                                                           |
|                                                                                                                                                                                                                       |
| [void][ pdfLightTable_BeginRowLayout([object] sender, [BeginRowLayoutEventArgs] args)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [  [if] (args.RowIndex == 1)]                                                                                                                                |
|                                                                                                                                                                                                                       |
| [  {]                                                                                                                                                                             |
|                                                                                                                                                                                                                       |
| [     args.MinimalHeight = 25;]                                                                                                                                                   |
|                                                                                                                                                                                                                       |
| [  }]                                                                                                                                                                             |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [\'Subscribing the event]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ pdfLightTable.BeginRowLayout += [New]BeginRowLayoutEventHandler(pdfLightTable_BeginRowLayout)]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [\'Setting rowheight for the second row]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] pdfLightTable_BeginRowLayout([ByVal] sender [As] [Object], [ByVal] args [As]BeginRowLayoutEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [  [If] args.RowIndex = 1 [Then]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [       args.MinimalHeight = 25]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                           |
| [  [End] [If]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_EndRowLayout}4.1.2.3.1.4.4      EndRowLayout

 

This event is raised when row layout finishes. The arguments of this event are as follows:

[·      ]RowIndex (read-only): Index of the row (zero based)

[·      ]Cancel: Enables to cancel layout

[·      ]LayoutCompleted (read-only):  Gets a value indicating whether the row was drawn completely.

[·      ]Bounds (read-only): Bounds of the row on the page

 

[]{#_BeginCellLayout}4.1.2.3.1.4.5      BeginCellLayout

 

This event is raised when cell layout starts. The arguments of this event are as follows:

[·      ]RowIndex (read-only): Index of the current row

[·      ]CellIndex (read-only): Index of the current cell within the row

[·      ]Value (read-only): Text value of the cell

[·      ]Bounds (read-only): Bounds of the cell

 : Graphics on which the cell should be drawn

[·      ]Skip: Indicates if the cell should be skipped

 

The following code example illustrates how to draw the graphics elements inside the cell.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [ [//Subscribing the event]]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [pdfLightTable.BeginCellLayout += [new ][BeginCellLayoutEventHandler](pdfLightTable_BeginCellLayout);]                               |
|                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [// Drawing ellipse inside the cell]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [void][ pdfLightTable_BeginCellLayout([object] sender, [BeginCellLayoutEventArgs] ] |
|                                                                                                                                                                                                                    |
| [args)]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [  [if] (args.RowIndex == 0 && args.CellIndex == 2)]                                                                                                      |
|                                                                                                                                                                                                                    |
| [  {]                                                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [      args.Graphics.DrawEllipse([PdfBrushes].Red, args.Bounds);]                                                                                         |
|                                                                                                                                                                                                                    |
| [  }]                                                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [\'Subscribing the event]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [Private][ pdfLightTable.BeginCellLayout += [New ]BeginCellLayoutEventHandler(pdfLightTable_BeginCellLayout)]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [\' Drawing ellipse inside the cell]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] pdfLightTable_BeginCellLayout([ByVal] sender [As] [Object], [ByVal] args [As ]BeginCellLayoutEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                              |
| [  [If] args.RowIndex = 0 [AndAlso] args.CellIndex = 2 [Then]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                              |
| [     args.Graphics.DrawEllipse(PdfBrushes.Red, args.Bounds)]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                              |
| [  [End] [If]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_EndCellLayout}4.1.2.3.1.4.6      EndCellLayout

 

This event is raised when cell layout finishes. The arguments of this event are as follows:

[·      ]RowIndex (read-only): Index of the current row

[·      ]CellIndex (read-only): Index of the current cell within the row

[·      ]Value (read-only): Text value of the cell

[·      ]Bounds (read-only): Bounds of the cell

: Graphics on which the cell should be drawn

 

[]{#related-topics}

