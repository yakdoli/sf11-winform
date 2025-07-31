---
title: symbolpaletteitem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbolpaletteitem.md
created_at: 2025-07-03
---








  









### Symbol Palette Item {#symbol-palette-item style="tab-stops: 0pt"}

[] 

Symbol Palette items are contained in the Symbol Palette group. A Symbol Palette item does not restrict users to the type of content that can be added to it. A Symbol Palette item can be a text box, combo box, image, button, and so on.

 

The **Name** property of the SymbolPaletteItem can be used to refer to the custom item being added in the NodeDrop event. The name of the SymbolPaletteItem becomes the name of the node.

 

The following code snippet can be used to add a Symbol Palette item that has an image as its content.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [ ][ SymbolPaletteGroup][ group = [new] [SymbolPaletteGroup]();]                                                    |
|                                                                                                                                                                                                                                                                                              |
| [  group.HeaderName = [\"Custom\"];    ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [  SymbolPalette][.SetFilterIndexes(group, [new] [List]\<[int]\>() { 0, 6 });]                                                     |
|                                                                                                                                                                                                                                                                                              |
| [  dc.SymbolPalette.SymbolGroups.Add(group);]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [  [SymbolPaletteItem] item = [new] [SymbolPaletteItem]();]                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [  [Image] i = [new] [Image]();]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| [  ][BitmapImage ][bi3 = [new] ][BitmapImage][ ();] |
|                                                                                                                                                                                                                                                                                              |
| [  bi3.BeginInit();]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [  bi3.UriSource = [new] [Uri]([\"Custom.png\"],        [UriKind].RelativeOrAbsolute);]                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [  bi3.EndInit();]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [  i.Stretch = [Stretch].Fill;]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [  i.Source = bi3;]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [  item.Content = i;]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| [  group.Items.Add(item);]                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [Dim][ group [As] [New] [SymbolPaletteGroup]()]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [group.HeaderName = [\"Custom\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                             |
| [SymbolPalette][.SetFilterIndexes(group, [New] [List]([Of] [Integer]) ([New] [Integer]() {0, 6}))] |
|                                                                                                                                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolGroups.Add(group)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [Dim][ item [As] [New] [SymbolPaletteItem]()]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Dim][ i [As] [New] [Image]()]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                             |
| [Dim][ bi3 [As] [New] [BitmapImage]()]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                             |
| [bi3.UriSource = [New] [Uri]([\"Custom.png\"], [UriKind].RelativeOrAbsolute)]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| [i.Stretch = [Stretch].Fill]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [i.Source = bi3]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [item.Content = i]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [group.Items.Add(item)]                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds the image content to the newly created Symbol Palette item that belongs to the Symbol Palette group named \"Custom\".

[] 

{border="0"}

Figure 153: Custom Group and Item**[]**

More:







