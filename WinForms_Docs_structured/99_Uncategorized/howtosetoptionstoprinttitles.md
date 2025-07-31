---
title: howtosetoptionstoprinttitles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetoptionstoprinttitles.md
created_at: 2025-07-03
---








  









### How to set options to print Titles? {#how-to-set-options-to-print-titles style="tab-stops: 0pt"}

 

Printing Title Rows

 

The following code illustrates printing Title Rows.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| []                                                                              |
|                                                                                                                     |
| [// Print Rows 1 to 3.]                                           |
|                                                                                                                     |
| [sheet.PageSetup.PrintTitleRows = [\"\$A\$1:\$IV\$3\"];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                    |
| []                                                                             |
|                                                                                                                    |
| [\' Print Rows 1 to 3.]                                          |
|                                                                                                                    |
| [sheet.PageSetup.PrintTitleRows = [\"\$A\$1:\$IV\$3\"]] |
+--------------------------------------------------------------------------------------------------------------------+

[] 

Printing Title Columns

 

The following code illustrates printing Title Columns.

 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [// Print Columns 1 to 3.]                                              |
|                                                                                                                           |
| [sheet.PageSetup.PrintTitleColumns = [\"\$A\$1:\$C\$65536\"];] |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                     |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [\' Print Columns 1 to 3.]                                             |
|                                                                                                                          |
| [sheet.PageSetup.PrintTitleColumns = [\"\$A\$1:\$C\$65536\"]] |
+--------------------------------------------------------------------------------------------------------------------------+

 

For information on Print settings, refer to section .

 

[]{#related-topics}

