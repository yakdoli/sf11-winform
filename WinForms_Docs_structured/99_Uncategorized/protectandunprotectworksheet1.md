---
title: protectandunprotectworksheet1.md
original_path: WinForms_Docs/99_Uncategorized/protectandunprotectworksheet1.md
created_at: 2025-08-05
---








  









### Protect and unprotect worksheet {#protect-and-unprotect-worksheet style="tab-stops: 0pt"}

Spreadsheet control supports to protect and unprotect a worksheet. You can set the worksheet as read only. There are two methods to protect and unprotect the worksheet. They are:

[·      ]Using method

[·      ]Using command

 

Protect/Unprotect worksheet using method

Protect

To set a worksheet as password protected, pass the sheet name and the password as String to *ProtectSheet* method. This prevents unwanted changes to the worksheet.

Following code illustrates this:

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                            |
| [spreadControl.ProtectSheet([\"Sheet1\"], [\"asd123\"]);] |
|                                                                                                                                                            |
| []                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[VB\]]**                                                                                                         |
|                                                                                                                                                           |
| [spreadControl.ProtectSheet([\"Sheet1\"], [\"asd123\"])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

UnProtect

To unprotect a worksheet, pass the sheet name and the password as String to the *UnProtectSheet* method.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                              |
| [spreadControl.UnProtectSheet([\"Sheet1\"], [\"asd123\"]);] |
|                                                                                                                                                              |
| []                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                            |
|                                                                                                                                                             |
| [spreadControl.UnProtectSheet([\"Sheet1\"], [\"asd123\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Protect/Unprotect worksheet using Command

You can protect/unprotect the current worksheet using the Protect Sheet dialog box. You can open the Protect Sheet dialog using the *ProtectCurrentSheetCommand. If the current worksheet is already protected* Protect Sheet dialog box will unprotect the worksheet after confirming the password.

 

{border="0"}

Figure 33: Protect Sheet Dialog Box

 

The following code illustrates how to bind the *ProtectCurrentSheetCommand* to a button:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][Button][ Command][=\"{][Binding][ Path][=] [ProtectCurrentSheetCommand}\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][Button][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

