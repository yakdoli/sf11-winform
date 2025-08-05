---
title: 3drelated.md
original_path: WinForms_Docs/99_Uncategorized/3drelated.md
created_at: 2025-08-05
---








  









### 3D Related {#d-related style="tab-stops: 0pt"}

[] 

Here are some properties that affect the rendering of an axis when in **3D** mode, which is set using the **Series3D** property.

[] 


+-----------------------------------+---------------------------------------------------------------------------------+
|                                   |                                                                                 |
|                                   |                                                                                 |
| Chart Web Control Properties      | Description                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------+
| Series3D                          | Specifies if the chart should be rendered in 3D mode.                           |
+-----------------------------------+---------------------------------------------------------------------------------+
| RealMode3D                        | Specifies if the chart should be rendered in a 3D plane.                        |
+-----------------------------------+---------------------------------------------------------------------------------+
| Depth                             | Specifies the depth of the axes in the z co-ordinate. Default value is **50f**. |
+-----------------------------------+---------------------------------------------------------------------------------+
| Tilt                              | Specifies the tilt angle relative to Y axis. Default value is **30f**.          |
+-----------------------------------+---------------------------------------------------------------------------------+
| Rotation                          | Specifies the angle of rotation relative to X-axis. Default value is **30f**.   |
+-----------------------------------+---------------------------------------------------------------------------------+
| ColumnDrawMode                    | Specifies the mode of column drawing when in 3D.                                |
|                                   |                                                                                 |
|                                   | **PlaneMode** - Columns from different series are drawn with same depth.        |
|                                   |                                                                                 |
|                                   | **InDepthMode** - Columns from different series are drawn with different depth. |
+-----------------------------------+---------------------------------------------------------------------------------+
| EnableMouseRotation               | Enables rotation of the chart at run-time using Middle / Right mouse button.    |
+-----------------------------------+---------------------------------------------------------------------------------+


**[]** 

**[]** 

3D Mode Sample

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| **[]**                                                                                              |
|                                                                                                                                                       |
| [this][.ChartWebControl1.Series3D = true;]                       |
|                                                                                                                                                       |
| [this][.ChartWebControl1.Depth = 55F;]                           |
|                                                                                                                                                       |
| [this][.ChartWebControl1.Tilt = 55F;]                            |
|                                                                                                                                                       |
| [this][.ChartWebControl1.[Rotation] = 60;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| **[]**                                                                                           |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.Series3D = [True\                                                          |
| Me].ChartWebControl1.Depth = 55F]                                                         |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.Tilt = 55F]                            |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.[Rotation] = 60] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 261: 3D Chart control with Depth=55f, Tilt=55f and Rotation=60

**[]** 

Real 3D Mode sample

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [this][.ChartWebControl1.ChartArea.Series3D = [true];] |
|                                                                                                                                                                  |
| [this][.ChartWebControl1.Tilt = 0;]                                         |
|                                                                                                                                                                  |
| [this][.ChartWebControl1.Depth = 150;]                                      |
|                                                                                                                                                                  |
| [this][.ChartWebControl1.Rotation = 10;]                                    |
|                                                                                                                                                                  |
| [this][.ChartWebControl1.RealMode3D = [true];]         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [Me][.ChartWebControl1.ChartArea.Series3D = [True]] |
|                                                                                                                                                               |
| [Me][.ChartWebControl1.Tilt = 0]                                         |
|                                                                                                                                                               |
| [Me][.ChartWebControl1.Depth = 150]                                      |
|                                                                                                                                                               |
| [Me][.ChartWebControl1.Rotation = 10]                                    |
|                                                                                                                                                               |
| [Me][.ChartWebControl1.RealMode3D = [True]]         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 262: 3D Chart in a 3D plane with Tilt=0, Depth=150, Rotation=10

**[]** 

Rotating Chart

[] 

The end-users can be allowed to rotate the chart at run-time, using the mouse (middle or right mouse button) by setting the **EnableMouseRotation** property to **true**.

**[]** 


{border="0"}Note: Rotation will not be possible with the LEFT-MOUSE button by enabling this property.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [this][.ChartWebControl1.RealMode3D = [true];]          |
|                                                                                                                                                                   |
| [this][.ChartWebControl1.EnableMouseRotation = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [Me][.ChartWebControl1.RealMode3D = [True]]          |
|                                                                                                                                                                |
| [Me][.ChartWebControl1.EnableMouseRotation = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 263: Real3D Mode Chart Being Rotated by using Mouse

[]{#p190} 

[]{#related-topics}

