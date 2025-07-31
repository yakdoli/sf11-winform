---
title: symbolpaletteitem1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbolpaletteitem1.md
created_at: 2025-07-03
---








  









### SymbolPalette Item {#symbolpalette-item style="tab-stops: 0pt"}

SymbolPalette items are contained in the SymbolPalette group. A SymbolPalette item does not restrict users to the type of content that can be added to it. A SymbolPalette item can be a text box, combo box, image, button, and so on.

 

The **Name** property of the SymbolPaletteItem can be used to refer to the custom item being added in the NodeDrop event. The name of the SymbolPaletteItem becomes the name of the node.

 

The following code snippet can be used to add a SymbolPalette item that has an image as its content.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [SymbolPaletteGroup][ group = [new] [SymbolPaletteGroup]();]                                                                            |
|                                                                                                                                                                                                                                                                              |
| [group.Label = [\"Custom\"];]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [SymbolPalette][.SetFilterIndexes(group, [new] [Int32Collection]([new] [int]\[\] { 0, 6 }));] |
|                                                                                                                                                                                                                                                                              |
| [dc.SymbolPalette.SymbolGroups.Add(group);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [SymbolPaletteItem][ item = [new] [SymbolPaletteItem]();]                                                                               |
|                                                                                                                                                                                                                                                                              |
| [Image][ i = [new] [Image]();]                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [BitmapImage][ bi3 = [new] [BitmapImage]();]                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [bi3.BeginInit();]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [bi3.UriSource = [new] [Uri]([\"Custom.png\"], [UriKind].RelativeOrAbsolute);]                                                              |
|                                                                                                                                                                                                                                                                              |
| [bi3.EndInit();]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [i.Stretch = [Stretch].Fill;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [i.Source = bi3;]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [item.Content = i;]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [group.Items.Add(item);]                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [Dim][ group [As] [New] [SymbolPaletteGroup]()] |
|                                                                                                                                                                                                        |
| [group][.Label = \"Custom\"]                                                                                      |
|                                                                                                                                                                                                        |
| [SymbolPalette.SetFilterIndexes(group, [New] Int32Collection(New [Integer]() { 0, 6 }))]                                 |
|                                                                                                                                                                                                        |
| [dc.SymbolPalette.SymbolGroups.Add(group)]                                                                                                                         |
|                                                                                                                                                                                                        |
| [Dim][ item [As] [New] [SymbolPaletteItem]()]   |
|                                                                                                                                                                                                        |
| [Dim][ i [As] [New] [Image]()]                  |
|                                                                                                                                                                                                        |
| [Dim][ bi3 [As] [New] [BitmapImage]()]          |
|                                                                                                                                                                                                        |
| [bi3.BeginInit()]                                                                                                                                                  |
|                                                                                                                                                                                                        |
| [bi3.UriSource = [New] Uri(\"Custom.png\", UriKind.RelativeOrAbsolute)]                                                                       |
|                                                                                                                                                                                                        |
| [bi3.EndInit()]                                                                                                                                                    |
|                                                                                                                                                                                                        |
| [i.Stretch = Stretch.Fill]                                                                                                                                         |
|                                                                                                                                                                                                        |
| [i.Source = bi3]                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [item.Content = i]                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [group][.Items.Add(item)][]                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds the image content to the newly created SymbolPalette item that belongs to the SymbolPalette group named \"Custom\".

[] 

{border="0"}

Figure 191: Custom Group and Item

More:







