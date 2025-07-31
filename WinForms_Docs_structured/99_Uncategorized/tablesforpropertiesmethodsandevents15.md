---
title: tablesforpropertiesmethodsandevents15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tablesforpropertiesmethodsandevents15.md
created_at: 2025-07-03
---








  









### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="tab-stops: 0pt"}

Properties

  ------------------------------------ ---------------------------------------------------------------------- --------------------------------------------- ----------------------------------
  **Property**                         **Description**                                                        **Type**                                      **Data Type**
  [BingMapKey]   [Gets or sets the key for enabling Bing Maps.]   [Dependency Property]   [string]
  [ZoomLevel]    [Gets or sets the zoom level.]                   [Dependency property]   [int]
  [MapStyle]     [Gets or sets the style of the Bing Maps.]       [Dependency property]   [MapStyle]
  ------------------------------------ ---------------------------------------------------------------------- --------------------------------------------- ----------------------------------

[] 

Methods

[·    ][]

[\
]

  **[Method ]**[]   **[Description ]**[]       **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]
  ------------------------------------------------------------- ---------------------------------------------------------------------- ----------------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------------------------------
  Zoom[]                                This method can be called to zoom the map.[]   Double ZoomLevel[]                        None[]                              None[]
  Pan                                                           This method can be called to pan the map.                              Double XCoordinate, Double YCoordinate                            None                                                        None

[] 

Events

  **[Event ]**[]   **[Description ]**[]   **[Arguments ]**[]                   **[Type ]**[]
  ------------------------------------------------------------ ------------------------------------------------------------------ -------------------------------------------------------------------------------- -----------------------------------------------------------
  PreviewZoomIn[]                      Triggered before zooming in the map.[]     Double Latitude, Double Longitude, Double ZoomFactor[]   Routed Event[]
  PreviewZoomOut                                               Triggered before zooming out the map.                              Double Latitude, Double Longitude, Double ZoomFactor                             Routed Event
  ZoomedIn                                                     Triggered after the map is zoomed in.                              Double Latitude, Double Longitude, Double ZoomFactor                             Routed Event
  ZoomedOut                                                    Triggered after the map is zoomed out.                             Double Latitude, Double Longitude, Double ZoomFactor                             Routed Event
  Panning                                                      Triggered while panning the map.                                   Double Latitude, Double Longitude, PanMode panMode                               Routed Event
  Panned                                                       Triggered after panning the map.                                   Double Latitude, Double Longitude, PanMode panMode                               Routed Event

[][] 

[]{#related-topics}

