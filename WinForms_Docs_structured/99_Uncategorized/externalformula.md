---
title: externalformula.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\externalformula.md
created_at: 2025-07-03
---






#### External Formula {#external-formula style="tab-stops: 0pt"}

**[]** 

Essential XlsIO allows you to insert/preserve formulas that refer values in other worksheets/workbooks. Note that XlsIO can only write/preserve formulas. You cannot update/refresh the calculated values in Excel, which should be refreshed by MS Excel.

[] 

Following code illustrates the insertion of a formula that refers to a value in another workbook.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                          |
| []                                                                                                                   |
|                                                                                                                                                          |
| [// Write external Formula Value. ]                                                                    |
|                                                                                                                                                          |
| [sheet.Range\[[\"C1\"]\].Formula = [\"\[One.xls\]Sheet1!\$A\$1\*5\"];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [\' Write external Formula Value. ]                                                                                             |
|                                                                                                                                                                                   |
| [sheet.Range\[[\"C1\"]\].Formula = [\"\[One.xls\]Sheet1!\$A\$1\*5\"];[ ]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Enable automatic updation of links in Excel, to view the result for the preceding code.


[] 

See Also

[[]]{.UGHyperlink} 

[]{.UGHyperlink}

 

 

[]{#related-topics}

