---
title: zordercommands1.md
original_path: WinForms_Docs/99_Uncategorized/zordercommands1.md
created_at: 2025-08-05
---








  









### Z-order Commands {#z-order-commands style="tab-stops: 0pt"}

The ordering commands allows you to change the z-index value of the selected objects (nodes and connectors) on the page. The objects can be made to go back or front so that they get displayed over other objects in case two or more objects overlap.

[] 

The commands are listed below.

[] 

BringToFront

Moves the selected object over other objects by increasing the z-index to maximum value.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [DiagramCommandManager][.BringToFront.Execute(diagramView.Page, diagramView);]                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [DiagramCommandManager][.BringToFront.Execute(diagramView.Page, diagramView)**[]**] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 150: Bring To Front[]

[] 

SendToBack

Moves the selected object behind all other objects by setting the z-index to 0.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [DiagramCommandManager][.SendToBack.Execute(diagramView.Page, diagramView);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [DiagramCommandManager][.SendToBack.Execute(diagramView.Page, diagramView)**[]**] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 151: Send To Back[]

[] 

MoveForward

Increases the z-index value of the selected object by 1.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [DiagramCommandManager][.MoveForward.Execute(diagramView.Page, diagramView);]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [DiagramCommandManager][.MoveForward.Execute(diagramView.Page, diagramView)**[]**] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 152: Move Forward[]

[] 

SendBackward

Decreases the z-index value of the selected object by 1.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [DiagramCommandManager][.SendBackward.Execute(diagramView.Page, diagramView);]                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [DiagramCommandManager][.SendBackward.Execute(diagramView.Page, diagramView)**[]**] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 153: Send Backward

[]{#related-topics}

