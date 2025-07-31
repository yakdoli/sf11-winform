---
title: table.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\table.md
created_at: 2025-07-03
---








  









### Table {#table style="tab-stops: 0pt"}

 

**WTable** class represents a table in a Word document. Every table in the Word document consists of table rows (one or more). Every table row consists of table cells (one or more).

 

WTable class has similar architecture. It contains a collection of table rows. This collection is accessible through the **Rows** property, which returns the object of the WRowCollection type. Collection of rows consists of **WTableRow** objects. For more details about WTableRow, refer the WTableRow documentation. This class also contains the **TableFormat** property which defines formatting for the whole table. This property returns the object of the RowFormat type. For more details about RowFormat, see 

 

[·      ]**ResetCells**: enables you to create tables with the specified number of rows and specified number of cells in each row.

[·      ]**WTableRow AddRow(bool isCopyFormat)**: enables you to add a new row to the existing table. The **isCopyFormat** parameter defines whether to copy the row format from the previous row.

[·      ]**WTableRow AddRow(bool isCopyFormat, bool autoPopulateCells)**: enables the user to add a new row to the existing table, but the second parameter,  autoPopulateCells, defines whether to create the same number of cells as in the previous row of the table and copy its formatting.

 

**Class Hierarchy**

 

TextBodyItem

                 \|   

            WTable

 

Public Constructors

 


  ------------------------------------- ---------------------------------------------------
  Name                                  Description
  WTable.WTable (IWordDocument)         Initializes a new instance of the WTable class.  
  WTable.WTable (IWordDocument, bool)   Initializes a new instance of the WTable class.  
  ------------------------------------- ---------------------------------------------------


 

Public Properties

 


  --------------- ----------------------------------------------------------------------------
  Name            Description
  ChildEntities   Gets the child entities.  
  EntityType      Gets the type of the entity.
  FirstRow        Get first row of the table.
  LastCell        Get last cell of the table.
  LastRow         Get last row of the table.
  Rows            Get the table rows.
  TableFormat     Sets table formatting after ResetCells call.
  Width           Gets the width of the table (in points).
  StyleName       Gets the table style name.
  Title           Gets or sets the table title (Microsoft Word 2010 specific property)
  Description     Gets or sets the table description (Microsoft Word 2010 specific property)
  --------------- ----------------------------------------------------------------------------


 

Public Methods

 


  ------------ --------------------------------------------
  Name         Description
  AddRow       Adds new row to the table.
  Clone        Clones this instance.  
  Find         Finds text by specified pattern.  
  Replace      Replaces the text by specified pattern.
  ResetCells   Resets rows / columns number.
  ApplyStyle   Applies built-in table style to the table.
  ------------ --------------------------------------------


 

The following example illustrates how to create an empty table with two rows. Each row has two cells (two columns).

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                                       |
|                                                                                                                                                                                |
| [IWordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                                |
| [IWSection][ section = doc.AddSection();]                                                 |
|                                                                                                                                                                                |
| [IWParagraph][ paragraph = section.AddParagraph();]                                       |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [paragraph.AppendText([\"Tiny table\"]);]                                                                           |
|                                                                                                                                                                                |
| [paragraph = section.AddParagraph();]                                                                                                      |
|                                                                                                                                                                                |
| [IWTable][ table = section.AddTable();]                                                   |
|                                                                                                                                                                                |
| [table.ResetCells(2, 2);]                                                                                                                  |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [doc.Save([\"Table.doc\"]);]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ doc As ][IWordDocument][ = ][New][ WordDocument()] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ section As ][IWSection][ = doc.AddSection()]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ paragraph As ][IWParagraph][ = section.AddParagraph()]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [paragraph.AppendText(\"Tiny table\")]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [paragraph = section.AddParagraph()]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ table As ][IWTable][ = section.AddTable()]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [table.ResetCells(2, 2)]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [doc.Save(\"Table.doc\")]                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 37: Table with Two Rows and two Columns

 

Nested Table

 

You can create nested tables by creating a table in the cell of the parent table by using DocIO. The following code illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                    |
| **[]**                                                                         |
|                                                                                                                    |
| [// Adding a nested Table to the cell (2,2)of the parent table.] |
|                                                                                                                    |
| [IWTable nestTable = table\[2, 2\].AddTable();]                                |
|                                                                                                                    |
| [nestTable.ResetCells(3, 3);]                                                  |
+--------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                             |
|                                                                                                                  |
| **[]**                                                                       |
|                                                                                                                  |
| [\' Adding a new Table to the cell (2,2) of the parent table.] |
|                                                                                                                  |
| [Dim nestTable as IWTable = table\[2, 2\].AddTable()]                        |
|                                                                                                                  |
| [nestTable.ResetCells(3, 3)]                                                 |
+------------------------------------------------------------------------------------------------------------------+

 

Cell Image

 

You can also insert images in the table cells by appending a picture to the cell paragraph. The following code illustrates how to insert a picture in the first cell.

 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                  |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [IWTable][ table = section.Body.AddTable();] |
|                                                                                                                                   |
| [table.ResetCells(1, 1);          ]                                                           |
|                                                                                                                                   |
| []                                                                                            |
|                                                                                                                                   |
| [WTableRow][ row = table.Rows\[0\];]         |
|                                                                                                                                   |
| [paragraph = (IWParagraph)row.Cells\[0\].AddParagraph();]                                     |
|                                                                                                                                   |
| [paragraph.AppendPicture(new Bitmap([\"image.png\"]));]                |
+-----------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                |
| **[]**                                                                                                                     |
|                                                                                                                                                                |
| [Dim][ table [As] IWTable = section.Body.AddTable()] |
|                                                                                                                                                                |
| [table.ResetCells(1, 1)]                                                                                                   |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [Dim][ row [As] WTableRow = table.Rows(0)]           |
|                                                                                                                                                                |
| [paragraph = DirectCast(row.Cells(0).AddParagraph(), IWParagraph)]                                                         |
|                                                                                                                                                                |
| [paragraph.AppendPicture(New Bitmap([\"image.png\"]))]                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

More:











