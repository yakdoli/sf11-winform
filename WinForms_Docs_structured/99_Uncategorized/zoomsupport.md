---
title: zoomsupport.md
original_path: WinForms_Docs/99_Uncategorized/zoomsupport.md
created_at: 2025-08-05
---






#### Zoom Support {#zoom-support style="tab-stops: 0pt"}

[] 

One of the interactive feature in Essential Diagram control is the zooming feature. You can zoom the nodes in / out by using the following client methods.

[] 

[·      ]ZoomIn()

[·      ]ZoomOut()

[·      ]ZoomToSelection()

[·      ]ZoomToActual()

[] 

The zooming is performed using the ZoomTool. This tool allows the user to zoom the diagram with minimum and maximum magnification.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [this][.diagram1.Controller.ActivateTool([\"ZoomTool\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [Me][.diagram1.Controller.ActivateTool([\"ZoomTool\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Properties of the Zoom Tool 

**[]** 


  ---------------------- -------------------------------------------------------------------------------------
  Properties             Description
  MaximumMagnification   Specifies the maximum magnification value for zooming. Default value is ***1000***.
  MinimumMagnification   Specifies the minimum magnification value for zooming. Default value is ***10***.
  ZoomIncrement          Specifies the amount to zoom each time the mouse is clicked.
  ---------------------- -------------------------------------------------------------------------------------


**[]** 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                                 |
| []                                                                          |
|                                                                                                                 |
| [diagram1.Controller.ActivateTool([\"ZoomTool\"]);] |
|                                                                                                                 |
| [ZoomTool z = (ZoomTool)diagram1.Controller.ActiveTool;]                    |
|                                                                                                                 |
| [z.MaximumMagnification = 100;]                                             |
|                                                                                                                 |
| [z.MinimumMagnification = 50;]                                              |
|                                                                                                                 |
| [z.ZoomIncrement = 10;]                                                     |
+-----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 92: Zoom In

**[]** 

{border="0"}

**[]** 

Figure 93: Zoom Out

 

[]{#p53} 

 

[]{#related-topics}

