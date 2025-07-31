---
title: howtocopyandpastethevaluesofthecellsthatcontainonlyformulas.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocopyandpastethevaluesofthecellsthatcontainonlyformulas.md
created_at: 2025-07-03
---








  









### How to copy and paste the values of the cells that contain only formulas? {#how-to-copy-and-paste-the-values-of-the-cells-that-contain-only-formulas style="tab-stops: 0pt"}

 

You can copy and paste the values of the cells that contain only formulas by setting ExcelCopyRangeOptions of the CopyTo method to None. The following code example illustrates this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                          |
| []                                                                                                     |
|                                                                                                                                                          |
| [IRange][ src = sheet1.Range\[[\"A3\"]\]; ]  |
|                                                                                                                                                          |
| [IRange][ dest = sheet1.Range\[[\"B1\"]\]; ] |
|                                                                                                                                                          |
| [src.CopyTo(dest,[ExcelCopyRangeOptions].None);  ]                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [Dim][ src [As] IRange = sheet1.Range([\"A3\"])]  |
|                                                                                                                                                                                    |
| [Dim][ dest [As] IRange = sheet1.Range([\"B1\"])] |
|                                                                                                                                                                                    |
| [src.CopyTo(dest,ExcelCopyRangeOptions.None)]                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

