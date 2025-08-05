---
title: zoomwithzoomlevel3.md
original_path: WinForms_Docs/99_Uncategorized/zoomwithzoomlevel3.md
created_at: 2025-08-05
---






#### Zoom with ZoomLevel {#zoom-with-zoomlevel style="tab-stops: 0pt"}

When changing the ZoomLevel it will automatically change the ZoomFactor value, so Map will be zoomed based on the ZoomFactor value. ZoomFactor value is determined when ZoomLevel is changed.  Initial ZoomFactor value is multiplied by the ZoomLevel value, then new value will be  set as ZoomFactor.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [      ][      [MapControl] map = [new] [MapControl]();] |
|                                                                                                                                                                                                                                                 |
| [            map.ZoomLevel += 1;]                                                                                                                                                              |
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

