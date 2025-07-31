---
title: howtoaddacomponentinthequickaccessmenuprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddacomponentinthequickaccessmenuprogrammatically.md
created_at: 2025-07-03
---






##### How to add a component in the QuickAccessMenu programmatically? {#how-to-add-a-component-in-the-quickaccessmenu-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

By calling the **SetUseInQuickAccessMenu** method, with the component passed as a parameter, we can include a component in the QuickAccessToolbar.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [this][.ribbonControlAdv1.SetUseInQuickAccessMenu([this].toolStripDropDownButton1, [true]);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.][ribbonControlAdv1.SetUseInQuickAccessMenu([Me].toolStripDropDownButton1, [True])][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: You can also identify whether a particular item is added to the Quick Access Toolbar or not, using the GetUseInQuickAccessMenu method, by passing the item as the parameter.


 

[]{#related-topics}

