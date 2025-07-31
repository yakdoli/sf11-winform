---
title: revamping3dchartsinchartwpffeature.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\revamping3dchartsinchartwpffeature.md
created_at: 2025-07-03
---






##### Revamping 3D charts in Chart WPF Feature {#revamping-3d-charts-in-chart-wpf-feature style="tab-stops: 0pt"}

Charts are implemented in 3D with customization to improve the look and feel of the chart.

Display 3D Chart, by using the following code:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [//To display the chart type in 3d mode]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][ChartArea.Chart3DSettings][\>]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                        ][\<][syncfusion][:][Chart3D][ BackWallThickness][=\"0\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [ShowBackWall][=\"False\"][ LeftWallBackground][=\"Transparent\"][ LeftWallThickness][=\"0\"][ ]                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [BottomWallBackground][=\"Transparent\"][ BottomWallThickness][=\"0\"/\>]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    ][\</][syncfusion][:][ChartArea.Chart3DSettings][\>]                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                            |
|                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                              |
| [//To set the background]                                                                                                                                                                |
|                                                                                                                                                                                                                              |
| [Chart1.Areas\[0\].Chart3DSettings.BackWallBackground = [Brushes].AliceBlue;]                                                                                    |
|                                                                                                                                                                                                                              |
| [// To set the back wall thickness]                                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.BackWallThickness = 0.5;]                                                                                                             |
|                                                                                                                                                                                                                              |
| [//To set the back ground for the Bottom wall]                                                                                                                                           |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.BottomWallBackground = [Brushes].Black;]                                                                      |
|                                                                                                                                                                                                                              |
| [// To set the thickness for bottom wall]                                                                                                                                                |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.BottomWallThickness = 0.5;]                                                                                                           |
|                                                                                                                                                                                                                              |
| [// To set the Camera projection]                                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.CameraProjection = ]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [CameraProjection][.Orthographic;]                                                                                                   |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [               ]                                                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [                [Light] light=[new] [AmbientLight]([Color].FromArgb(200, 200, 200, 200));] |
|                                                                                                                                                                                                                              |
| [//To set the chart light]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ChartLight = light;]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [// To set the back ground for left wall]                                                                                                                                                |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.LeftWallBackground = [Brushes].Yellow;]                                                                       |
|                                                                                                                                                                                                                              |
| [// To set the Thickness for Left wall]                                                                                                                                                  |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.LeftWallThickness = 0.5;]                                                                                                             |
|                                                                                                                                                                                                                              |
| [// TO set the background for right wall]                                                                                                                                                |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.RightWallBackground = [Brushes].Green;]                                                                       |
|                                                                                                                                                                                                                              |
| [// To set the thickness for Rightwall]                                                                                                                                                  |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.RightWallThickness = 0.5;]                                                                                                            |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.RotateOnMouseDown = [true];]                                                                                     |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowBackWall = [true];]                                                                                          |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowBottomWall = [true];]                                                                                        |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowPrimaryAxis = [true];]                                                                                       |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowRightWall = [true];]                                                                                         |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowSecondaryAxis = [true];]                                                                                     |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ShowTopWall = [true];]                                                                                           |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.TopWallBackground = [Brushes].IndianRed;]                                                                     |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.TopWallThickness = 0.5;]                                                                                                              |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ViewDefaultRotate = 1.5;]                                                                                                             |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ViewDefaultTilt = 2.5;]                                                                                                               |
|                                                                                                                                                                                                                              |
| [                Chart1.Areas\[0\].Chart3DSettings.ViewDefaultTurn = 10; Screen ]                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

when the coed runs, the following output displays.

[] 

{border="0"}

Figure 77: 3D Settings for Pyramid Chart

**[]** 

 

[]{#p42} 

 

[]{#related-topics}

