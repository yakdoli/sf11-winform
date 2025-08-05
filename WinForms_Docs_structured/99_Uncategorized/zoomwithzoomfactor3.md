---
title: zoomwithzoomfactor3.md
original_path: WinForms_Docs/99_Uncategorized/zoomwithzoomfactor3.md
created_at: 2025-08-05
---






#### Zoom with ZoomFactor {#zoom-with-zoomfactor style="tab-stops: 0pt"}

By changing the ZoomFactor value it is possible to Zoom the Map. If ZoomFactor value is increased then Map will be ZoomIn. If ZoomFactor value is decreased then Map will be Zoomout.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [      ][      [MapControl] map = [new] [MapControl]();] |
|                                                                                                                                                                                                                                                 |
| [            map.ZoomFactor += 0.3;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [            [ShapeFileLayer] shapeLayer = [new] [ShapeFileLayer]();]                                                     |
|                                                                                                                                                                                                                                                 |
| [            shapeLayer.Uri = [\"WpfApplication1.ShapeFiles.wv.shp\"];]                                                                                                |
|                                                                                                                                                                                                                                                 |
| [            map.LayeredContent = shapeLayer;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            LayoutRoot.Children.Add(map);]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

