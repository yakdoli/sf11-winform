---
title: howtodetectwhetheraparticularcontrolisinmdimodeornot.md
original_path: WinForms_Docs/99_Uncategorized/howtodetectwhetheraparticularcontrolisinmdimodeornot.md
created_at: 2025-08-05
---






##### How to detect whether a particular control is in MDI mode or not?[] {#how-to-detect-whether-a-particular-control-is-in-mdi-mode-or-not style="tab-stops: 0pt"}

[] 

To know whether the control is in MDI mode or not, the below method can be called.

[] 

**IsMDIMode** method let you detect whether the specified control is in MDI child mode or not. The return value will be true if the control is in MDI mode, else value will be false.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [this][.dockingManager1.IsMDIMode([this].listBox2);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| **[]**                                                                                                  |
|                                                                                                                                                           |
| [Me][.dockingManager1.IsMDIMode([Me].listBox2)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[MDI Child Transition]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

