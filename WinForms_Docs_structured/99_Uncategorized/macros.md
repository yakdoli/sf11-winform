---
title: macros.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\macros.md
created_at: 2025-07-03
---








  









### Macros {#macros style="tab-stops: 0pt"}

**[]** 

XlsIO supports the usage of Macros in the Template file. A macro is created by using the MS Excel GUI, and then saved. The spreadsheet is then opened by using XlsIO, and saved to retain the macro.

[] 

1.   Create a macro by using MS Excel and save the file.

2.   Open the saved file with XlsIO.

3.   XlsIO preserves the macro during the Save process.

[] 

{border="0"}

Figure 152: XlsIO with VBA in Template[]

[] 

XlsIO also provides support for disabling macros in the template workbook as follows. This will just ignore the macros in the template, and work normally as if there were no macros in the template.

[] 

+--------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                 |
|                                                                                                  |
| []                                                           |
|                                                                                                  |
| [workbook.DisableMacrosStart = [true];] |
+--------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                            |
|                                                                                                 |
| []                                                          |
|                                                                                                 |
| [workbook.DisableMacrosStart = [True]] |
+-------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

