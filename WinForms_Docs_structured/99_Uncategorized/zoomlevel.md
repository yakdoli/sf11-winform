---
title: zoomlevel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\zoomlevel.md
created_at: 2025-07-03
---






#### ZoomLevel {#zoomlevel style="tab-stops: 0pt"}

 

When changing the ZoomLevel, it automatically changes the ZoomFactor value, so Map will be get zoomed based on the ZoomFactor value. ZoomFactor value is determined when the ZoomLevel is changed.  When the initial ZoomFactor value is multiplied by the ZoomLevel value, a new value is set as ZoomFactor.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [      ][      [MapControl] map = [new] [MapControl]();] |
|                                                                                                                                                                                                                                                 |
| [            map.ZoomLevel += 1;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            [ShapeFileLayer] shapeLayer = [new] [ShapeFileLayer]();]                                                     |
|                                                                                                                                                                                                                                                 |
| [            shapeLayer.Uri = [\"WindowsPhoneApplication1.ShapeFiles.wv.shp\"];]                                                                                       |
|                                                                                                                                                                                                                                                 |
| [            map.LayeredContent = shapeLayer;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            LayoutRoot.Children.Add(map);]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

