---
title: howtousenamedrangeswithxlsio.md
original_path: WinForms_Docs/99_Uncategorized/howtousenamedrangeswithxlsio.md
created_at: 2025-08-05
---








  









### How to use Named Ranges with XlsIO? {#how-to-use-named-ranges-with-xlsio style="tab-stops: 0pt"}

**[]** 

The **NamedRanges** collection belongs to the workbook, and not to the worksheet. If you define two named ranges with the same name, then the named range that is defined last will replace the previous named range.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Looping through the Named Ranges in a spreadsheet.  ]                                                                  |
|                                                                                                                                                                              |
| [foreach][ ([IName] name [in] mySheet.Names)] |
|                                                                                                                                                                              |
| [{]                                                                                                                                      |
|                                                                                                                                                                              |
| [MessageBox][.Show(name.Name.ToString());]                                              |
|                                                                                                                                                                              |
| [}]                                                                                                                                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// There is already a named range called \"One\", I am changing the address that it points to. ]                          |
|                                                                                                                                                                              |
| [mySheet.Names\[[\"One\"]\].RefersToRange = mySheet.Range\[[\"B6\"]\];]                    |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Named ranges are added to the workbook collection in both the methods mentioned below. ]                               |
|                                                                                                                                                                              |
| [// Adding the named Range to the workbook.  ]                                                                             |
|                                                                                                                                                                              |
| [myWorkbook.Names.Add([\"TestRangeBook\"], mySheet.Range\[[\"A5\"]\]);]                    |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Adding the named Range to the workbook. Internally named range is added to the workbook names coll.  ]                 |
|                                                                                                                                                                              |
| [mySheet.Names.Add([\"TestRangeSheet\"], mySheet.Range\[[\"A5\"]\]);]                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Referencing from the sheet. ]                                                                                          |
|                                                                                                                                                                              |
| [mySheet.Range\[[\"TestRangeSheet\"]\].Number = 100;]                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' Looping through the Named Ranges in a spreadsheet. ]                                                            |
|                                                                                                                                                                       |
| [Dim][ name [As] Syncfusion.XlsIO.IName]                    |
|                                                                                                                                                                       |
| [For][ [Each] name [In] mySheet.Names] |
|                                                                                                                                                                       |
| [MessageBox.Show(name.Name.ToString()) ]                                                                                          |
|                                                                                                                                                                       |
| [Next][ name]                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' There is already a named range called \"One\", I am changing the address that it points to.]                    |
|                                                                                                                                                                       |
| [mySheet.Names([\"One\"]).RefersToRange = mySheet.Range([\"B6\"])]                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' Named ranges are added to the workbook collection in both the methods mentioned below.]                         |
|                                                                                                                                                                       |
| [\' Adding the named Range to the workbook.  ]                                                                      |
|                                                                                                                                                                       |
| [myWorkbook.Names.Add([\"TestRangeBook\"], mySheet.Range([\"A5\"]))]                |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' Adding the named Range to the workbook. Internally named range is added to the workbook names coll. ]           |
|                                                                                                                                                                       |
| [mySheet.Names.Add([\"TestRangeSheet\"], mySheet.Range([\"A5\"]))]                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' Referencing from the sheet.]                                                                                    |
|                                                                                                                                                                       |
| [mySheet.Range([\"TestRangeSheet\"]).Number = 100]                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

