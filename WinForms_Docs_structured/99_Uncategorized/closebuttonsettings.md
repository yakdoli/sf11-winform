---
title: closebuttonsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\closebuttonsettings.md
created_at: 2025-07-03
---






##### CloseButton Settings {#closebutton-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabControl can have CloseButtons for all the TabPages as in Internet Explorer 7 to close the corresponding TabPages irrespective of the Style set.

[] 

{border="0"}

[] 

Figure 1069: Close buttons displayed for all the Pages in the TabControlAdv

[] 

Close Button on all the TabItems can be made visible by setting the **ShowTabCloseButton** property to True.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [this][.tabControlAdv1.ShowTabCloseButton = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                              |
|                                                                                                                                                             |
| **[]**                                                                                                    |
|                                                                                                                                                             |
| [Me][.tabControlAdv1.ShowTabCloseButton = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Also the Tab Close Button can be restricted to be shown only for Active TabPages. This can be done by setting the **ShowCloseButtonForActiveTabOnly** property to True.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| **[]**                                                                                                                    |
|                                                                                                                                                                             |
| [this][.tabControlAdv1.ShowCloseButtonForActiveTabOnly = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                           |
|                                                                                                                                                                          |
| **[]**                                                                                                                 |
|                                                                                                                                                                          |
| [Me][.tabControlAdv1.ShowCloseButtonForActiveTabOnly = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 1070: Close button displayed only for the Active Page in the TabControlAdv

[] 


{border="0"} Note:[ ]Close Button can be set for the whole TabControlAdv by using [[TabPrimitives]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TabPrimitives).


 

 

 

 

[]{#related-topics}

