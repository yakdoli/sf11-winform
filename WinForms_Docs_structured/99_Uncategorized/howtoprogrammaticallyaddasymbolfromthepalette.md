---
title: howtoprogrammaticallyaddasymbolfromthepalette.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoprogrammaticallyaddasymbolfromthepalette.md
created_at: 2025-07-03
---








  









## How To Programmatically Add a Symbol From the Palette {#how-to-programmatically-add-a-symbol-from-the-palette style="tab-stops: 0pt"}

[] 

The following code sample demonstrates how you can programmatically add a symbol from the symbol palette to a diagram.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                               |
| [if][ (paletteGroupView1.Palette.Nodes.Count \> 0)]                                      |
|                                                                                                                                                                               |
| [{]                                                                                                                                       |
|                                                                                                                                                                               |
| [       [Node] nc =([Node])paletteGroupView1.Palette.Nodes\[0\].Clone();                ] |
|                                                                                                                                                                               |
| [       diagram1.Model.AppendChild(nc);]                                                                                                  |
|                                                                                                                                                                               |
| [}]                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                      |
|                                                                                                                                                                          |
| [If][ paletteGroupView1.Palette.Nodes.Count \> 0 [Then] ]      |
|                                                                                                                                                                          |
| [      [Dim] nc [As] Node = DirectCast(paletteGroupView1.Palette.Nodes(0).Clone(), Node) ] |
|                                                                                                                                                                          |
| [      diagram1.Model.AppendChild(nc) ]                                                                                              |
|                                                                                                                                                                          |
| [End If ]                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p91} 

 

[]{#related-topics}

