---
title: howtochangethecolorofallheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethecolorofallheaders.md
created_at: 2025-07-03
---








  









### How to Change the Color of All Headers {#how-to-change-the-color-of-all-headers style="tab-stops: 0pt"}

[] 

Introduction

[] 

The styles of the Header cells are controlled by base styles. The \"Header\" base style will affect all column headers including cell 0,0. The \"Column Header\" **base style** will affect the column headers excluding cell 0,0. The \"RowHeader\" base style will affect all row headers excluding cell 0,0.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [// Column headers including cell 0,0.\                                                                                                                                                                                                 |
| ][this][.grid.BaseStylesMap\[\"Header\"\].StyleInfo.BackColor = Color.Blue;]       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Column headers excluding cell 0,0.\                                                                                                                                                                                                 |
| ][this][.grid.BaseStylesMap\[\"Column Header\"\].StyleInfo.BackColor = Color.Red;] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Row headers excluding cell 0,0.\                                                                                                                                                                                                    |
| ][this][.grid.BaseStylesMap\[\"Row Header\"\].StyleInfo.BackColor = Color.Green;]  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                                                        |
|                                                                                                                                                                                 |
| [\' Column headers including cell 0,0.]                                                                                       |
|                                                                                                                                                                                 |
| [Me][.grid.BaseStylesMap(\"Header\").StyleInfo.BackColor = Color.Blue]       |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [\' Column headers excluding cell 0,0.]                                                                                       |
|                                                                                                                                                                                 |
| [Me][.grid.BaseStylesMap(\"Column Header\").StyleInfo.BackColor = Color.Red] |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [\' Row headers excluding cell 0,0.]                                                                                          |
|                                                                                                                                                                                 |
| [Me][.grid.BaseStylesMap(\"Row Header\").StyleInfo.BackColor = Color.Green]  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p610} 

 

[]{#related-topics}

