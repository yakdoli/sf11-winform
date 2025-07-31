---
title: addingsymbolitemtosymbolpalette.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingsymbolitemtosymbolpalette.md
created_at: 2025-07-03
---






#### Adding symbol item to Symbol Palette {#adding-symbol-item-to-symbol-palette style="tab-stops: 0pt"}

 

To add a symbol item create an object for SymbolPaletteItem and set the *PaletteItem* property to SymbolPaletteItem.  Then add the created object to the SymbolPaletteItems Collections of the Symbol Palette.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [//  Symbol Palette item has been add in SymbolPaletteItems Collection. Here rectangle added as Symbol Palette Item. ]   |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [SymbolPaletteItem] symbolItem;]                                                                  |
|                                                                                                                                                                            |
| [            symbolItem = [new] [SymbolPaletteItem]();]                                   |
|                                                                                                                                                                            |
| [            [Rectangle] rect = [new] [Rectangle]();]             |
|                                                                                                                                                                            |
| [            rect.Fill = [new] [SolidColorBrush]([Colors].Blue);] |
|                                                                                                                                                                            |
| [            symbolItem.PaletteItem = rect;]                                                                                           |
|                                                                                                                                                                            |
| [            [this].Map.SymbolPalette.SymbolPaletteItems.Add(symbolItem);]                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

 

 

 

 

**[]** 

{border="0"}

Figure 25: Adding Custom Symbol to Symbol Palette**[]**

 

 

[]{#related-topics}

