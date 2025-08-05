---
title: usingbuilder23.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder23.md
created_at: 2025-08-05
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

1.   In the **view**, [invoke the ]**Diagram**[ helper with the control ID as the first argument.][ ]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View ]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [\<%][{]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                             |
| [          **.IsSymbolPaletteEnabled([true])     ** ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                             |
| [          .BoundaryConstraintsEnabled([false])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [          .SymbolPaletteWidth(151)]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [          .DiagramMode(][DiagramMode][.Canvas)][         ] |
|                                                                                                                                                                                                                                                                                                                             |
| [          .Render();]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| [  }]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [%\>][]                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.    Build and run the application.

[]{#related-topics}

