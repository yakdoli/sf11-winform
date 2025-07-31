---
title: howtoremoveitemsfromthequickaccesstoolbarprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoremoveitemsfromthequickaccesstoolbarprogrammatically.md
created_at: 2025-07-03
---






##### How to remove items from the Quick Access Toolbar programmatically? {#how-to-remove-items-from-the-quick-access-toolbar-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Call RibbonControlAdv.Header.QuickItem.RemoveAt method for this purpose. The parameter idx is a zero based index of the item, to remove.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                                             |
|                                                                                                                                                                                      |
| [this][.ribbonControlAdv1.Header.QuickItems.RemoveAt(1);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1202}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                                                          |
|                                                                                                                                                                                   |
| [Me][.ribbonControlAdv1.Header.QuickItems.RemoveAt(1)][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

