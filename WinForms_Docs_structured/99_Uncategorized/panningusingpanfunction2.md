---
title: panningusingpanfunction2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\panningusingpanfunction2.md
created_at: 2025-07-03
---






#### Panning using Pan Function {#panning-using-pan-function style="tab-stops: 0pt"}

 

Pan method of ShapeFileLayer can also be used to pan the Map. The parameters for Pan() method are the X coordinate and Y coordinate.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| [            MapControl][ map = [new] [MapControl]();]                                                                      |
|                                                                                                                                                                                                                                                                  |
| [ ][           ShapeFileLayer][ shapeLayer = [new] [ShapeFileLayer]();] |
|                                                                                                                                                                                                                                                                  |
| [            shapeLayer.Uri = [\"SilverlightApplication1.ShapeFiles.wv.shp\"];]                                                                                                                      |
|                                                                                                                                                                                                                                                                  |
| [            map.Layers.Items.Add(shapeLayer);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| [            map.LayeredContent = shapeLayer;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| [            shapeLayer.Pan(10, 10);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                  |
| [            map.EnablePan=[ false;]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| [            LayoutRoot.Children.Add(map);][]                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

