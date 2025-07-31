---
title: howtoworkwiththewebpalettegroupbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoworkwiththewebpalettegroupbar.md
created_at: 2025-07-03
---








  









## How to work with the Web PaletteGroupBar?[] {#how-to-work-with-the-web-palettegroupbar style="tab-stops: 0pt"}

[] 

**PaletteGroupBar** control is very much similar to the Tools.Web GroupBar. But, PaletteGroupBar can render the palette\'s items (Syncfusion.Windows.Forms.Diagram.SymbolPalette).

[] 

{border="0"}

Figure 77

[] 

PaletteGroupBar will create a separate tab for each palette. Users can specify the items\' layout using the **NodesLayout** property and **ItemsInRow** property.

Possible Layouts are \'Flow\' and \'Vertical\'.

Control is interactive, user can drag nodes from it to any Diagram.Web control on page (if such exists). **DraggingStyle** property specifies the dragging style (works like in Diagram.Web control).

User can add palettes through the Visual Studio designer.

[] 

{border="0"}

Figure 78

[] 

Also, users can add symbol palettes through code. There is an overload function **AddPalette** which adds a symbol palette to the control.

[] 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                                |
| []                                            |
|                                                                                                |
| [AddPalette([string] sFullPath)]      |
|                                                                                                |
| [AddPalette([SymbolPalette] Palette)] |
|                                                                                                |
| [AddPalette(Stream strmPalette)]                           |
+------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                        |
|                                                                                           |
| []                                       |
|                                                                                           |
| [AddPalette([String] sFullPath)] |
|                                                                                           |
| [AddPalette(SymbolPalette Palette)]                   |
|                                                                                           |
| [AddPalette(Stream strmPalette)]                      |
+-------------------------------------------------------------------------------------------+

[] 

Here is an example to add a symbol palette.

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                    |
| []                                                                |
|                                                                                                                    |
| [PaletteGroupBarCtrl.AddPalette([@\"D:\\Comps.edp\"]);] |
+--------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                               |
|                                                                                                                  |
| []                                                              |
|                                                                                                                  |
| [PaletteGroupBarCtrl.AddPalette([\"D:\\Comps.edp\"])] |
+------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

