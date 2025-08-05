---
title: xhtmlcell.md
original_path: WinForms_Docs/99_Uncategorized/xhtmlcell.md
created_at: 2025-08-05
---






##### XHTML Cell {#xhtml-cell style="tab-stops: 0pt"}

[] 

An XHTML page can be displayed in a grid cell by using Xhtml Cell cell type. A custom cell type can be created and registered to provide XHTML functionality. It requires derivation of two classes:

[] 

[·      ]GridCellModelBase

[·      ]GridCellRendererBase

[] 

The **CellModel** (read GridCellModelBase class in this document) handles any serialization that a cell type requires, and also creates the CellRenderer (read GridCellRendererBase class in this document) class that is associated with the cell type. The **CellRenderer** class manages the UI aspects of the cell type.

 

The XHTML page can be displayed by using the following set of codes.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [string][ xhtml1 = [\"\<body style=\\\"font-family:Arial; line-height:1em\\\"\> \"];]                       |
|                                                                                                                                                                                                                          |
| [xhtml1 += [\"\<h1 style=\\\"text-align:center; color:#EE7A03 \\\"\>XhtmlCells\</h1\>\"];]                                                                   |
|                                                                                                                                                                                                                          |
| [xhtml1 += [\"\<p/\>\"];]                                                                                                                                    |
|                                                                                                                                                                                                                          |
| [xhtml1 += [\"\<p\>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.\</p\>\"];] |
|                                                                                                                                                                                                                          |
| [xhtml1 += [\"\</body\>\"];]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [gridControl1\[rowIndex, 1\].CellType = [\"XhtmlCell\"];]                                                                                                    |
|                                                                                                                                                                                                                          |
| [gridControl1\[rowIndex, 1\].Text = xhtml1;]                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Dim][ xhtml1 [As] [String] = [\"\<body style=\"\"font-family:Arial; line-height:1em\"\"\> \"]] |
|                                                                                                                                                                                                                                                        |
| [xhtml1 += [\"\<h1 style=\"\"text-align:center; color:#EE7A03 \"\"\>XhtmlCells\</h1\>\"]]                                                                                                  |
|                                                                                                                                                                                                                                                        |
| [xhtml1 += [\"\<p/\>\"]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [xhtml1 += [\"\<p\>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.\</p\>\"]]                                |
|                                                                                                                                                                                                                                                        |
| [xhtml1 += [\"\</body\>\"]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, 1).CellType = [\"XhtmlCell\"]]                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, 1).Text = xhtml1]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][114][: XHTML Cell]*

 

[]{#p103} 

 

[]{#related-topics}

