---
title: usingbuilder17.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder17.md
created_at: 2025-08-05
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps guide in handling z-order commands through Builder.

1.   In the **view**, [invoke the **Diagram** helper with the control ID as the first argument.][ ]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[ ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [\<%][{]                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| [      Html.Syncfusion().Diagram(][\"FlatDiagram\"][)          ] |
|                                                                                                                                                                                                                                                                             |
| [          .Width(900)              ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [          .Height(500)]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [          .EnableZOrder(][true][)]                                 |
|                                                                                                                                                                                                                                                                             |
| [          .ConnectorZOrderMode(][ZOrderMode][.Default)\                                                                            |
|           .DiagramMode(DiagramMode.Canvas)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [          .Render();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [  }]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [%\>][]                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

[]{#related-topics}

