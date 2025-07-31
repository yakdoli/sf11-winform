---
title: howtoavoidtheabcandor123intheheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoavoidtheabcandor123intheheaders.md
created_at: 2025-07-03
---








  









### How to Avoid the A, B, C and / or 1, 2, 3 in the Headers {#how-to-avoid-the-a-b-c-and-or-1-2-3-in-the-headers style="tab-stops: 0pt"}

[] 

Introduction

[] 

In a GridControl, whether the headers contain the default A, B, C, \... or 1, 2, 3, \... values is controlled by the properties in the Model.Options property.

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [// Hiding the A, B, C in the column headers.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [this][.gridControl1.Model.Options.NumberedColHeaders = ][false][;] |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [// Hiding the 1, 2, 3 in the row headers.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| [this][.gridControl1.Model.Options.NumberedRowHeaders = ][false][;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [\' Hiding the A, B, C in the column headers.]                                                                                                                   |
|                                                                                                                                                                                                                    |
| [Me][.GridControl1.Model.Options.NumberedColHeaders = ][False] |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [\' Hiding the 1, 2, 3 in the row headers.]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [Me][.gridControl1.Model.Options.NumberedRowHeaders = ][False] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p546} 

 

[]{#related-topics}

