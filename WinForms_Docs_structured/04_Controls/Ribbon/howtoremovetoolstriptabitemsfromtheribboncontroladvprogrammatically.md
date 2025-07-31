---
title: howtoremovetoolstriptabitemsfromtheribboncontroladvprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Ribbon\howtoremovetoolstriptabitemsfromtheribboncontroladvprogrammatically.md
created_at: 2025-07-03
---






##### How to remove ToolStripTabItems from the RibbonControlAdv Programmatically? {#how-to-remove-toolstriptabitems-from-the-ribboncontroladv-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Call RibbonControlAdv.Header.MainItem.RemoveAt method for this purpose. The parameter idx is a zero based index of the item to remove.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                                          |
|                                                                                                                                                                                     |
| [this][.ribbonControlAdv1.Header.MainItems.RemoveAt(1);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                                                         |
|                                                                                                                                                                                  |
| [Me][.ribbonControlAdv1.Header.MainItems.RemoveAt(1)][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

