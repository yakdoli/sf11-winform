---
title: propertytables2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\propertytables2.md
created_at: 2025-07-03
---






#### Property tables {#property-tables style="tab-stops: 0pt"}

 

Properties of the Symbol Palette Group

+-------------+--------------------------------------------------------------------------------------------+----------------------+-------------------------------------------+--------------------------------------------------+
| Property    | Description                                                                                | Type of the Property | Value it Accepts                          | Any Other Dependencies/Sub-Properties Associated |
+-------------+--------------------------------------------------------------------------------------------+----------------------+-------------------------------------------+--------------------------------------------------+
| HeaderName  | Gets or sets the name of the symbol palette group.                                         | Dependency property  | String                                    | No (This is not supported in SVG Mode)           |
+-------------+--------------------------------------------------------------------------------------------+----------------------+-------------------------------------------+--------------------------------------------------+
| Index       | Gets or sets the position of the symbol palette group to be added into the symbol palette. | Dependency property  | int                                       | No (This is not supported in SVG Mode)           |
|             |                                                                                            |                      |                                           |                                                  |
|             |                                                                                            |                      |                                           |                                                  |
+-------------+--------------------------------------------------------------------------------------------+----------------------+-------------------------------------------+--------------------------------------------------+
| Items       | Sets the item collection of the group.                                                     | Dependency property  | [SymbolPaletteItem] | Yes (This is not supported in SVG Mode)          |
|             |                                                                                            |                      |                                           |                                                  |
|             |                                                                                            |                      |                                           |                                                  |
+-------------+--------------------------------------------------------------------------------------------+----------------------+-------------------------------------------+--------------------------------------------------+

 

Properties of the Symbol Palette Items

+-------------+-------------------------------------------------------------------------------+----------------------+------------------+--------------------------------------------------+
| Property    | Description                                                                   | Type of the Property | Value it Accepts | Any Other Dependencies/Sub-Properties Associated |
+-------------+-------------------------------------------------------------------------------+----------------------+------------------+--------------------------------------------------+
| ContentId   | We can add any type of content inside the symbol palette using this property. | Dependency property  | String           | No (This is not supported in SVG Mode)           |
+-------------+-------------------------------------------------------------------------------+----------------------+------------------+--------------------------------------------------+
| Name        | Gets or sets then name of the symbol palette item.                            | Dependency property  | String           | No (This is not supported in SVG Mode)           |
|             |                                                                               |                      |                  |                                                  |
|             |                                                                               |                      |                  |                                                  |
+-------------+-------------------------------------------------------------------------------+----------------------+------------------+--------------------------------------------------+

 

[]{#related-topics}

