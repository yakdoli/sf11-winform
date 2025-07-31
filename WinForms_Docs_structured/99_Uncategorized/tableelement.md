---
title: tableelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tableelement.md
created_at: 2025-07-03
---








  









### TABLE Element {#table-element style="tab-stops: 0pt"}

[] 

The **TABLE** element is used to create tables in a document. The table element contains the **TR**, **TD** elements within it. The **TABLEElementImpl** class is used to determine the properties and methods for the table element.

**[]** 

Properties

[] 

[·      ]**ColsCount**: Gets / sets the number of columns present in the table

[·      ]**RowsCount**: Gets / sets the number of rows present in the table

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [// Gets the number of columns and rows present in the table.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [TABLEElementImpl][ table = htmlelements\[[\"table\"]\] [as] [TABLEElementImpl];]                            |
|                                                                                                                                                                                                                                                                                                           |
| [this][.label1.Text = [\"\\nTable(ColsCount and RowsCount):\"] + table.ColsCount.ToString() + [\",\"] + table.RowsCount.ToString();] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' Gets the number of columns and rows present in the table.]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ table [As] TABLEElementImpl = [CType](IIf([TypeOf] htmlelements([\"table\"]) [Is] TABLEElementImpl, htmlelements([\"table\"]), [Nothing]), TABLEElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Me].label1.Text = Constants.vbLf & [\"Table(ColsCount and RowsCount):\"] & table.ColsCount.ToString()+[\",\"]+table.RowsCount.ToString()]                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p65} 

[]{#related-topics}

