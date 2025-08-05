---
title: cameraprojectionviews.md
original_path: WinForms_Docs/99_Uncategorized/cameraprojectionviews.md
created_at: 2025-08-05
---






##### Camera Projection Views {#camera-projection-views style="tab-stops: 0pt"}

Chart 3D supports two types of camera projection views namely perspective and orthographic. Camera projection for the chart can be changed using the **CameraProjection** property of the Chart3D type, as follows.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][sfchart][:][ChartArea][ View3DMode][=\"True\"\>]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<][sfchart][:][ChartArea.Chart3DSettings][\>]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [        ][\<][sfchart][:][Chart3D][ CameraProjection][=\"Orthographic\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\</][sfchart][:][ChartArea.Chart3DSettings][\>]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][sfchart][:][ChartArea][\>]                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [chart1.Areas\[0\].Chart3DSettings.CameraProjection = [CameraProjection].Perspective;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 259: Perspective Projection

[] 

{border="0"}

Figure 260: Orthographic Projection

**[]** 

See Also



 

[]{#related-topics}

