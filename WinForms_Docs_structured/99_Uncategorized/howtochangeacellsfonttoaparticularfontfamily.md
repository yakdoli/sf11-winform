---
title: howtochangeacellsfonttoaparticularfontfamily.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangeacellsfonttoaparticularfontfamily.md
created_at: 2025-07-03
---








  









### How to Change a Cell\'s Font to a Particular Font Family {#how-to-change-a-cells-font-to-a-particular-font-family style="tab-stops: 0pt"}

[] 

Introduction

[] 

Use the **FaceName** property of the **font** property on the style object for the cell.

[      ]

  -------------------------------------------------------------------------------------------------------------------
  [gridControl1\[rowIndex, colIndex\].Font.Facename = \"Arial\";]
  -------------------------------------------------------------------------------------------------------------------

[] 

You can also change several font properties in one statement by using the font class's SetXXX method which, will return a reference to the font object.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [// Snippet 1   ][     ]                                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex\].Font.Facename = \"Arial\";]                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex\].Font.Bold = ][true][;]                                      |
|                                                                                                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex\].Font.Size = 10;]                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [// Snippet 2]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex\].Font.SetFacename(\"Arial\").SetBold(][true][).SetSize(10);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' Snippet 1     ][   ]                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [gridControl1(rowIndex, colIndex).Font.Facename = \"Arial\"]                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [gridControl1(rowIndex, colIndex).Font.Bold = ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [gridControl1(rowIndex, colIndex).Font.Size = 10]                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' Snippet 2       ][ ]                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [gridControl1(rowIndex, colIndex).Font.SetFacename(\"Arial\").SetBold(][True][).SetSize(10)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p552} 

 

[]{#related-topics}

