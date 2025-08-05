---
title: identifytheshapesdroppedonthepagefromthepalette.md
original_path: WinForms_Docs/99_Uncategorized/identifytheshapesdroppedonthepagefromthepalette.md
created_at: 2025-08-05
---








  









### Identify the Shapes Dropped on the Page from the Palette {#identify-the-shapes-dropped-on-the-page-from-the-palette style="tab-stops: 0pt"}

The **SymbolPaletteItemName** property can be used to identify the item dropped on the page in the NodeDrop event. This is particularly useful when you have to identify the item which is dropped and performs an operation on the node before it is added to the View. The **Name** property of the SymbolPaletteItem can be set while adding the item to the palette and thenby using **SymbolPaletteItemName** property in the eventargs of NodeDrop.A reference to the corresponding SymbolPaletteItem can be obtained.\
\

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [SymbolPaletteItem][ ss = [new] [SymbolPaletteItem]();] |
|                                                                                                                                                                                              |
| [Label][ l = [new] [Label]();]                          |
|                                                                                                                                                                                              |
| [l.Content = [\"Label\"];]                                                                                                       |
|                                                                                                                                                                                              |
| [ss.Content = l;]                                                                                                                                        |
|                                                                                                                                                                                              |
| [ss.Name = [\"MyItem\"];]                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [Dim][ ss [As] [New] [SymbolPaletteItem]()] |
|                                                                                                                                                                                                    |
| [Dim][ l [As] [New] [Label]()]              |
|                                                                                                                                                                                                    |
| [l.Content = \"Label\"]                                                                                                                                        |
|                                                                                                                                                                                                    |
| [ss.Content = l]                                                                                                                                               |
|                                                                                                                                                                                                    |
| [ss.Name = \"MyItem\"][]                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
The NodeDrop event can be declared:\
\

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [// Declare the event.]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [diagramView.NodeDrop += ][new][ ][NodeDroppedEventHandler][(diagramView_NodeDrop);]                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [// Handle the event.]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [void][ diagramView_NodeDrop(][object][ sender, ][NodeDroppedRoutedEventArgs][ evtArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [if][(evtArgs.][SymbolPaletteItemName[==][\"MyItem\"][)]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [// User-specified code.]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [\'Declare the event.][]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                |
| [Private][ diagramView.NodeDrop += New NodeDroppedEventHandler(AddressOf diagramView_NodeDrop)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [        [\'Handle the event.]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                |
| [        [Private] [Sub] diagramView_NodeDrop([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeDroppedRoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                |
| [            [If] evtArgs.SymbolPaletteItemName = [\"MyItem\"] [Then]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [                [\'User-specified code.]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [            [End] [If]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [        [End] [Sub]][]                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

