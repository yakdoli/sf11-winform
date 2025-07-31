---
title: zoomwithzoomfactor2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\zoomwithzoomfactor2.md
created_at: 2025-07-03
---






#### Zoom with ZoomFactor {#zoom-with-zoomfactor style="tab-stops: 0pt"}

 

By changing the ZoomFactor value, it is possible to zoom the Map. If ZoomFactor value is increased, then Map will be ZoomedIn. If ZoomFactor value is decreased,  the Map will be Zoomed out.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [      ][      [MapControl] map = [new] [MapControl]();] |
|                                                                                                                                                                                                                                                 |
| [            map.ZoomFactor += 0.3;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [            [ShapeFileLayer] shapeLayer = [new] [ShapeFileLayer]();]                                                     |
|                                                                                                                                                                                                                                                 |
| [            shapeLayer.Uri = [\"SilverlightApplication1.ShapeFiles.wv.shp\"];]                                                                                        |
|                                                                                                                                                                                                                                                 |
| [            map.LayeredContent = shapeLayer;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            LayoutRoot.Children.Add(map);]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

