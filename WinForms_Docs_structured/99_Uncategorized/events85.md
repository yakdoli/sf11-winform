---
title: events85.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events85.md
created_at: 2025-07-03
---








  









### Events {#events style="tab-stops: 0pt"}

 

Table 7: ShapeFileLayer Events


  Event              Description                                   Arguments                                                 Type     Reference links
  ------------------ --------------------------------------------- --------------------------------------------------------- -------- -----------------------------------------------------------------------------------------
  PreviewZoomIn      Triggered before zooming-in the Map           Double Latitude,Double Longitude, and Double ZoomFactor   Event    
  PreviewZoomOut     Triggered before zooming-out the Map          Double Latitude,Double Longitude, and Double ZoomFactor   Event    
  ZoomedIn           Triggered after Map is zoomed-in              Double Latitude,Double Longitude, and Double ZoomFactor    Event   
  ZoomedOut          Triggered after Map is zoomed-out             Double Latitude,Double Longitude, and Double ZoomFactor   Event    
  Panning            Triggered while panning the Map               Double Latitude,Double Longitude, and PanMode             Event    
  Panned             Triggered after panning the Map               Double Latitude,Double Longitude, and PanMode             Event    
  SelectionChanged   Triggered when Selection changes in the Map   List RemovedItems, and List AddedItems                    Event    


 

 

 

[]{#related-topics}

