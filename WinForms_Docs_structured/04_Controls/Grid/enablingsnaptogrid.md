---
title: enablingsnaptogrid.md
original_path: WinForms_Docs/04_Controls/Grid/enablingsnaptogrid.md
created_at: 2025-08-05
---






#### Enabling Snap to Grid {#enabling-snap-to-grid style="tab-stops: 0pt"}

The Snap to Grid feature for nodes and connectors can be enabled by setting DiagramView's SnapToHorizontalGrid and SnapToVerticalGrid properties to "True", as shown in the following code snippets.

In the following code snippets, diagramView is an instance of DiagramView.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][DiagramView][ [ x][:][Name][=\"diagramView\"][ SnapToHorizontalGrid][=\"True\"][ SnapToVerticalGrid][=\"True\" \>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][DiagramView][\>][]                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| [// Enable snap to vertical grid.][]                  |
|                                                                                                                                             |
| [diagramView.SnapToVerticalGrid = [true];]                                         |
|                                                                                                                                             |
| [// Enable snap to horizontal grid.][]                |
|                                                                                                                                             |
| [diagramView.SnapToHorizontalGrid = [true];][] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                             |
|                                                                                                                                            |
| [\'Enable snap to vertical grid.][]                  |
|                                                                                                                                            |
| [diagramView.SnapToVerticalGrid = [True]]                                         |
|                                                                                                                                            |
| [\'Enable snap to horizontal grid.][]                |
|                                                                                                                                            |
| [diagramView.SnapToHorizontalGrid = [True]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 116: Snap to Grid Enabled

 

**[]** 

**[Customizing Snap to Grid Offset Values]**

By default, the SnapOffsetX and SnapOffsetY values are set to 25 pixels. However, these values can be changed so that objects will snap to the horizontal grid by using SnapOffsetX and snap to the vertical grid by using SnapOffsetY, as shown in the following code snippets.

In the following code snippets, diagramView is an instance of DiagramView.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][DiagramView][ [ x][:][Name][=\"diagramView\"][ SnapOffsetX ][=\"50\"][ SnapOffsetY ][=\"50\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][DiagramView][\>][]                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                            |
|                                                                                                           |
| [diagramView.SnapOffsetX = 50;]                                       |
|                                                                                                           |
| [diagramView.SnapOffsetY = 50;][] |
+-----------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                           |
|                                                                                                          |
| [diagramView.SnapOffsetX = 50]                                       |
|                                                                                                          |
| [diagramView.SnapOffsetY = 50][] |
+----------------------------------------------------------------------------------------------------------+

 

Note:

SnapToGrid will snap objects based on the offset values specified in DiagramView's SnapOffsetX and SnapOffsetY values and it works independently from grid lines. However, to snap objects along with the grid lines, specify the same offset values for grid lines and snap offset.

 

Also, snapping of objects will occur only when the objects are dragged during runtime. Even after snapping is enabled, users can specify their own offset values in code behind.

Properties

The properties of the Snap to Grid feature are described in the following tabulation:

Table 6: Properties Table

+----------------------+----------------------------------------------+---------------------+------------------+-----------------+
| Property             | Description                                  | Type                | Data Type        | Reference links |
+----------------------+----------------------------------------------+---------------------+------------------+-----------------+
| SnapOffsetX          | Snaps to the horizontal offset value.        | Dependency property | double           | Not applicable  |
+----------------------+----------------------------------------------+---------------------+------------------+-----------------+
| SnapOffsetY          | Snaps to the vertical offset value.          | Dependency property | double           | Not applicable  |
+----------------------+----------------------------------------------+---------------------+------------------+-----------------+
| SnapToHorizontalGrid | Enables or disables snap to horizontal grid. | Dependency property | bool, true/false |  Not applicable |
|                      |                                              |                     |                  |                 |
|                      |                                              |                     |                  |                 |
+----------------------+----------------------------------------------+---------------------+------------------+-----------------+
| SnapToVerticalGrid   | Enables or disables snap to vertical grid.   | Dependency property | bool, true/false |  Not applicable |
|                      |                                              |                     |                  |                 |
|                      |                                              |                     |                  |                 |
+======================+==============================================+=====================+==================+=================+

[] 

Sample Link

To view a sample:

1.   Open the Diagram Sample Browser from the dashboard. (Refer to the [Samples and Location] chapter.)

2.   Navigate to Editable Diagram -\> SnapToGrid Demo.

[] 

[]{#related-topics}

