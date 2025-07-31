---
title: originaxissupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\originaxissupport.md
created_at: 2025-07-03
---






#### Origin Axis Support {#origin-axis-support style="TEXT-ALIGN: justify; TEXT-INDENT: -54pt; MARGIN-LEFT: 54pt; tab-stops: 54.0pt"}

Essential Chart for Windows Phone ships with support for an origin axis. Users can customize the appearance of the axis which includes the thickness and stroke color. The values in the series are plotted in accordance with the origin line. Thus the negative values for the series will be plotted along the negative axis.

 

Use Case Scenarios

1.  Users can plot negative values by positioning the origin value at zero.

2.  Users can also reposition the origin line dynamically by changing the origin value of the axis.

Properties

+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+
| **Property**                     | **Description**                                | **Type**                                      | **Data Type**                    | **Reference links**                  |
+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+
| Origin[] | To place the origin for the axis               | Dependency Property[] | Double[] | Ref. Link[]  |
+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+
| OriginLineStroke                 | Determines the stroke color of the origin line | Dependency property                           | Brush                            | Ref. Link[ ] |
|                                  |                                                |                                               |                                  |                                      |
|                                  |                                                |                                               |                                  |                                      |
|                                  |                                                |                                               |                                  |                                      |
|                                  |                                                |                                               |                                  |                                      |
+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+
| OriginLineStrokeThickness        | Determines the thickness of the origin line    | Dependency Property                           | Double                           | Ref. Link[]  |
|                                  |                                                |                                               |                                  |                                      |
|                                  |                                                |                                               |                                  |                                      |
+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+
| ShowOriginLine                   | Enables or disables display of the origin line | Dependency Property                           | Boolean                          | Ref. Link[]  |
+----------------------------------+------------------------------------------------+-----------------------------------------------+----------------------------------+--------------------------------------+

[] 

Sample Link

1.  Open the Windows Phone sample browser.

2.  Navigate to **Chart** \> **Negative Axis Support**.

 

{border="0"}

Figure 108: WP7 Sample Browser: Negative Axis Support Sample

{border="0"}

Figure 109: WP7 Sample Browser: Negative Axis Sample Demo

 

[]{#related-topics}

