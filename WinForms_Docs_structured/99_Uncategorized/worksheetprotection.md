---
title: worksheetprotection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\worksheetprotection.md
created_at: 2025-07-03
---






#### Worksheet Protection {#worksheet-protection style="tab-stops: 0pt"}

**[]** 

When you share an Excel file, so that others can collaborate on the data, you can prevent any user from making changes to specific worksheet or workbook elements, by protecting certain parts of the file.

[] 

Excel allows to protect a worksheet, and provides an option to specify the elements, users will be allowed to change, when you protect a worksheet. You can do this, by opening the **Tools** menu, and then clicking **Protection** option.

[] 

WorkSheet Protection XlsIO

[] 

XlsIO provides support for protecting and unprotecting elements in worksheets by using the **Protect** method of **IWorksheet**. By**[ ]**[u]sing the **ExcelSheetProtection** enumerator, you can set the elements that need protection.

[] 

Following code example illustrates how to protect a worksheet with a password. It also restricts formatting columns in the worksheet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                  |
| **[]**                                                                                                                       |
|                                                                                                                                                                  |
| [// Protecting the Worksheet by using a Password.]                                                             |
|                                                                                                                                                                  |
| [sheet.Protect([\"syncfusion\"], [ExcelSheetProtection].FormattingColumns);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                     |
| **[]**                                                                                          |
|                                                                                                                                     |
| [\' Protecting the Worksheet by using a Password.]                                |
|                                                                                                                                     |
| [sheet.Protect([\"syncfusion\"],ExcelSheetProtection.FormattingColumns)] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can also unprotect the worksheet by using the **Unprotect** method of XlsIO. It allows the user to remove the restriction added to worksheet elements.

 

Following code example illustrates how to remove worksheet protection.

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [// Unprotecting (unlocking) the Worksheet using the Password.] |
|                                                                                                                   |
| [sheet.Unprotect([\"syncfusion\"]);]                  |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [\' Unprotecting (unlocking) the Worksheet using the Password.] |
|                                                                                                                   |
| [sheet.Unprotect([\"syncfusion\"])]                    |
+-------------------------------------------------------------------------------------------------------------------+

[] 

Chart Sheet Protection

[] 

Essential XlsIO now provides support to protect or unprotect a chart sheet.

 

a\) Protecting a Chart Sheet

[] 

XlsIO provides options to protect chart sheets by using the **Protect** method. This method allows you to protect selected elements in a worksheet, so that they cannot be modified.

 

By using the **ExcelSheetProtection** enumeration, you can set the elements that need protection.

 

Following sample code illustrates protection of chart sheet (with password).

 

[·      ]This default call will protect the chart for Contents and Objects.

[·      ]You can also choose protection by using the overload.

 

The code mentioned below will choose default enumerations \"Contents\" and \"Objects\". The password chosen in the code snippet below is \"syncfusion\".

 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                |
| []                                                         |
|                                                                                                |
| [// Protect chart sheet.]                    |
|                                                                                                |
| [chart.Protect([\"syncfusion\"]);] |
+------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                          |
|                                                                                               |
| []                                                        |
|                                                                                               |
| [\' Protect chart sheet.]                   |
|                                                                                               |
| [chart.Protect([\"syncfusion\"])] |
+-----------------------------------------------------------------------------------------------+

 

The protection can also be performed by using the enumerations in the code as shown below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Protect chart sheet.]                                                                            |
|                                                                                                                                                        |
| [chart.Protect([\"syncfusion\"], [ExcelSheetProtection].Content);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                             |
| []                                                                                      |
|                                                                                                                             |
| [\' Protect chart sheet.]                                                 |
|                                                                                                                             |
| [chart.Protect([\"syncfusion\"], ExcelSheetProtection.Content)] |
+-----------------------------------------------------------------------------------------------------------------------------+

 

The chart sheet is protected. The content in the sheet cannot be edited.

 

b\) Removing protection of a Chart Sheet

 

You can remove the protection of a protected chart sheet by using the **Unprotect** method. Following code sample illustrates this.

 

+--------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                 |
|                                                                                                  |
| []                                                           |
|                                                                                                  |
| [// Unprotect chart sheet]                     |
|                                                                                                  |
| [chart.Unprotect([\"syncfusion\"]);] |
+--------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                            |
|                                                                                                 |
| []                                                          |
|                                                                                                 |
| [\' Unprotect chart sheet.]                   |
|                                                                                                 |
| [chart.Unprotect([\"syncfusion\"])] |
+-------------------------------------------------------------------------------------------------+

 

The protection of the chart sheet is removed.

 

[]{#related-topics}

