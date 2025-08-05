---
title: customcolorpalette4.md
original_path: WinForms_Docs/99_Uncategorized/customcolorpalette4.md
created_at: 2025-08-05
---








  









### CustomColorPalette {#customcolorpalette style="tab-stops: 0pt"}

With CustomColorPalette, the color palette for the Map can be customized. CurrentMapColorPalette is used to set custom color palette. CurrentMapColorPalette is the Collection of MapColorPalette.

{border="0"}

Figure 25: CustomColorPalette

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [      ][        [MapControl] map = [new] [MapControl]();]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.EnableColorPalette = [true];]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              [ShapeFileLayer] shapeLayer = [new] [ShapeFileLayer]();]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              shapeLayer.Uri = [\"WpfApplication1.ShapeFiles.wv.shp\"];]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.ColorPalette = [ColorPalettes].CustomColorPalette;]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.Layers.Items.Add(shapeLayer);]                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.LayeredContent = shapeLayer;]                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              LayoutRoot.Children.Add(map);]                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Cyan) });]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Blue) });]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Orange) });]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Purple) });]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Red) });]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [              map.CurrentMapColorPalette.Add([new] [MapColorPallette] { PathStroke = [new] [SolidColorBrush]([Colors].Black), PathStrokeThickness = 1d, ShapeFill = [new] [SolidColorBrush]([Colors].Magenta) });] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [       ]                                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

