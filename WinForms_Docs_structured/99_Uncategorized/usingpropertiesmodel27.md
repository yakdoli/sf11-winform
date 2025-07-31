---
title: usingpropertiesmodel27.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel27.md
created_at: 2025-07-03
---






##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

To enable symbol palette customization through the properties model:

 

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class. Assign this model class to **view data**. 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]();]                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [        [public] [ActionResult] FlatDiagram()]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
|                 model.SymbolPalette.Background = "white";                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.BorderColor = ][\"black\"][;]                         |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.ItemMouseOverBorderColor = ][\"red\"][;]              |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupBackground = ][\"black\"][;]        |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupBorderColor = ][\"black\"][;]       |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupForeground = ][\"white\"][;]        |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupHoverBackground = ][\"orange\"][;]  |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupHoverBorderColor = ][\"orange\"][;] |
|                                                                                                                                                                                                                                                                                                   |
| [            model.SymbolPalette.SymbolPaletteGroupHoverForeground = ][\"white\"][;]   |
|                                                                                                                                                                                                                                                                                                   |
| [            model.Width = 900;]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| [            model.Height = 500;]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [            model.DiagramMode = DiagramMode.Canvas;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [            ViewData\[[\"FlatDiagram\"]\] = model;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **view**, invoke the **Diagram** helper with the **view data key** as the control ID.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[ ]                             |
|                                                                                                                                                     |
| ```                                                                                                                    |
| <%{                                                                                                                                                 |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| ```                                                                                                                    |
|       Html.Syncfusion().Diagram("FlatDiagram")                                                                                                      |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| [          .Render();]                                                                         |
|                                                                                                                                                     |
| ```                                                                                                                    |
|   }                                                                                                                                                 |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| [%\>][] |
|                                                                                                                                                     |
| []                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application

[]{#related-topics}

