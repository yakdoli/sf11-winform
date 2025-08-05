---
title: howtopreventwrappingoftextingridcells.md
original_path: WinForms_Docs/04_Controls/Grid/howtopreventwrappingoftextingridcells.md
created_at: 2025-08-05
---








  









## How to prevent wrapping of text in Grid cells {#how-to-prevent-wrapping-of-text-in-grid-cells style="tab-stops: 0pt"}

[] 

By default, the text in the Grid cells get wrapped when there is a lack of space in the browser or when the control width is too small. To prevent this, you have to set the **WrapText** property to **False**. The following code example illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                            |
|                                                                                                                                                                                |
| [// To avoid text wrapping]                                                                                                  |
|                                                                                                                                                                                |
| [this][.GridGroupingControl1.Appearance.AnyCell.WrapText = [false];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [\' To avoid text wrapping]                                                                                               |
|                                                                                                                                                                             |
| [Me][.GridGroupingControl1.Appearance.AnyCell.WrapText = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p123} 

[]{#related-topics}

