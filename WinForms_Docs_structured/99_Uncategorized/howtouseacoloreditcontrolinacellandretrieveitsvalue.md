---
title: howtouseacoloreditcontrolinacellandretrieveitsvalue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtouseacoloreditcontrolinacellandretrieveitsvalue.md
created_at: 2025-07-03
---








  









### How to Use a ColorEdit Control in a Cell and Retrieve its Value {#how-to-use-a-coloredit-control-in-a-cell-and-retrieve-its-value style="tab-stops: 0pt"}

[] 

Introduction

[] 

It is simple to use the ColorEdit control to specify a cell\'s value. Just set the [CellType]{.UGHyperlink} property in the cell style to \"ColorEdit\" and set the text property to an appropriate value.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set the controltype.]                                                                                                                        |
|                                                                                                                                                                                                    |
| [gridControl1\[4, 4\].CellType = \"ColorEdit\"; ]                                                                                                |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set initial value to Color.Aqua or to set a RGB color, use something like ]                                                                  |
|                                                                                                                                                                                                    |
| [gridControl1\[4, 4\].Text = \"2, 12, 255\"; ]                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set initial value][ ][to RGB(2,12,255).] |
|                                                                                                                                                                                                    |
| [gridControl1\[4, 4\].Text = \"Aqua\";        ]                                                                                                  |
|                                                                                                                                                                                                    |
| [                ]                                                                                                                               |
|                                                                                                                                                                                                    |
| [//\....        ]                                                                                                                                |
|                                                                                                                                                                                                    |
| [// To retrieve a color object from this cell, use code such as]                                                                                 |
|                                                                                                                                                                                                    |
| [Color c = (Color)System.ComponentModel.TypeDescriptor.GetConverter(typeof(Color)).ConvertFromString(gridControl1\[4, 4\].Text);]                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Set controltype    .]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [GridControl1(4, 4).CellType = \"ColorEdit\" ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Set initial value to Color.Aqua or to set a RGB color, use something like  ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [gridControl1\[4, 4\].Text = \"2, 12, 255\";][ ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// Set initial value][ ][to RGB(2,12,255) ]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [GridControl1(4, 4).Text = \"Aqua\" ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'\....        ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' To retrieve a color object from this cell, use code such as]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ c ][As][ Color = ][CType][(System.ComponentModel.TypeDescriptor.GetConverter(][GetType][(Color)).ConvertFromString(GridControl1(4, 4).Text), Color)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p577} 

 

[]{#related-topics}

