---
title: arrayformula.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\arrayformula.md
created_at: 2025-07-03
---






#### Array Formula {#array-formula style="tab-stops: 0pt"}

 

Array Formula is a special type of formula in Excel. It works with an array or series of data values, rather than a single data value. XlsIO supports the usage of Array formula through the FormulaArray property.

 

Following code example explains how an array of values, from Named Range, is used for computation. For more details on Named Ranges, please refer .

  

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Insert Array Formula.]                                                                           |
|                                                                                                                                                        |
| [sheet.Range\[[\"A1:D1\"]\].FormulaArray = [\"{1,2,3,4}\"];]       |
|                                                                                                                                                        |
| [sheet.Names.Add([\"ArrayRange\"], sheet.Range\[[\"A1:D1\"]\]);]   |
|                                                                                                                                                        |
| [sheet.Range\[[\"A2:D2\"]\].FormulaArray = [\"ArrayRange+100\"]; ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [\' Insert Array Formula.]                                                                     |
|                                                                                                                                                  |
| [sheet.Range([\"A1:D1\"]).FormulaArray = [\"{1,2,3,4}\"]]      |
|                                                                                                                                                  |
| [sheet.Names.Add([\"ArrayRange\"],sheet.Range([\"A1:D1\"]))]   |
|                                                                                                                                                  |
| [sheet.Range([\"A2:D2\"]).FormulaArray = [\"ArrayRange+100\"]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 119: XlsIO with Array Formula[]

 

See Also

 

[]{.UGHyperlink}

 

[]{#related-topics}

