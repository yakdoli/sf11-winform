---
title: zoomwithzoommethod2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\zoomwithzoommethod2.md
created_at: 2025-07-03
---






#### Zoom With Zoom() Method {#zoom-with-zoom-method style="tab-stops: 0pt"}

 

With the Zoom method, the Map can be zoomed. The parameter for this method is the ZoomFactor value.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [      ][      [MapControl] map = [new] [MapControl]();] |
|                                                                                                                                                                                                                                                 |
| [            [ShapeFileLayer] shapeLayer = [new] [ShapeFileLayer]();]                                                     |
|                                                                                                                                                                                                                                                 |
| [            shapeLayer.Uri = [\"SilverlightApplication1.ShapeFiles.wv.shp\"];]                                                                                        |
|                                                                                                                                                                                                                                                 |
| [            map.LayeredContent = shapeLayer;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            shapeLayer.Zoom(5);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            LayoutRoot.Children.Add(map);]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

