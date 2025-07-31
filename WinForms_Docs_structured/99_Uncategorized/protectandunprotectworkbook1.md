---
title: protectandunprotectworkbook1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\protectandunprotectworkbook1.md
created_at: 2025-07-03
---








  









### Protect and unprotect workbook {#protect-and-unprotect-workbook style="tab-stops: 0pt"}

Spreadsheet control provides support to protect and unprotect the workbook with a password. When you protect the workbook the following option will be disabled:

[·      ]Insert Worksheet

[·      ]Delete Worksheet

[·      ]Hide Worksheet

[·      ]Unhide Worksheet

 

Protect workbook

You can protect the workbook using the Protect Structure and Windows dialog box. You can open the Protect Structure and Windows dialog using the *ProtectWorkbookCommand.*

 

       {border="0"}

Figure 31: Protect Structure and Windows dialog box

 

The following code illustrates how to bind the *ProtectWorkbookCommand* to a button:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][Button][ Command][=\"{][Binding][ Path][=] [ProtectWorkbookCommand}\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][Button][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


Note: The ProtectWorkbookCommand will open the Unprotect Workbook dialog box if the workbook is already protected.


***[]*** 

Unprotect workbook

You can unprotect the workbook using the Unprotect Workbook dialog box. You can open the Unprotect Workbook dialog using the *ProtectWorkbookCommand.*

 

{border="0"}

Figure 32: Unprotect Workbook dialog box

 

[]{#related-topics}

