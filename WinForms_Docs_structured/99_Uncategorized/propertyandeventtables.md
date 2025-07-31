---
title: propertyandeventtables.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\propertyandeventtables.md
created_at: 2025-07-03
---






#### Property and Event Tables {#property-and-event-tables style="tab-stops: 0pt"}

 

Properties

+-------------+-----------------------------------------------------------------------------------+---------------------+------------------------------------------------------------+----------------------------------------+
| Property    | Description                                                                       | Type of Property    | Value it Accepts                                           | Dependencies                           |
+-------------+-----------------------------------------------------------------------------------+---------------------+------------------------------------------------------------+----------------------------------------+
| ItemType    | Gets or sets the type of content to be added as a symbol into the symbol palette. | Dependency property | Enum:                                                      | No (This is not supported in SVG Mode) |
|             |                                                                                   |                     |                                                            |                                        |
|             |                                                                                   |                     | [·      ]ItemType.Content     |                                        |
|             |                                                                                   |                     |                                                            |                                        |
|             |                                                                                   |                     | [·      ]ItemType.CustomShape |                                        |
|             |                                                                                   |                     |                                                            |                                        |
|             |                                                                                   |                     |                                                            |                                        |
+-------------+-----------------------------------------------------------------------------------+---------------------+------------------------------------------------------------+----------------------------------------+

 

 

Events

  Event                            Description                                                              Arguments                                       Type
  -------------------------------- ------------------------------------------------------------------------ ----------------------------------------------- -------------------
  ClientSideOnCustomShapeDrawing   Raised when the custom shape is added. This event cannot be cancelled.   Node---The node on which the event is raised.   Client-side event

 

 

[]{#related-topics}

