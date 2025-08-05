---
title: events96.md
original_path: WinForms_Docs/99_Uncategorized/events96.md
created_at: 2025-08-05
---








  









### Events {#events style="tab-stops: 0pt"}

Table 7: ShapeFileLayer Events


  ------------------ --------------------------------------------- --------------------------------------------------------- -------------- -----------------------------------------------------------------------------------------
  Event              Description                                   Arguments                                                 Type           Reference links
  PreviewZoomIn      Triggered before Zooming the Map              Double Latitude,Double Longitude,and  Double ZoomFactor   Routed Event   
  PreviewZoomOut     Triggered before Zooming out the Map          Double Latitude,Double Longitude, and Double ZoomFactor   Routed Event   
  ZoomedIn           Triggered after Map ZoomedIn                  Double Latitude,Double Longitude, Double ZoomFactor       Routed Event   
  ZoomedOut          Triggered after Map ZoomedOut                 Double Latitude,Double Longitude, Double ZoomFactor       Routed Event   
  Panning            Triggered while Panning the Map               Double Latitude,Double Longitude,and  PanMode panMode     Routed Event   
  Panned             Triggered after Panned the Map                Double Latitude,Double Longitude,and  PanMode panMode     Routed Event   
  SelectionChanged   Triggered when Selection changed in the Map   List RemovedItems, List AddedItems                        Routed Event   
  ------------------ --------------------------------------------- --------------------------------------------------------- -------------- -----------------------------------------------------------------------------------------


 

[]{#related-topics}

