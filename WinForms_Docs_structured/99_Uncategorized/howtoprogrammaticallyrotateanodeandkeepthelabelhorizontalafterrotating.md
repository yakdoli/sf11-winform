---
title: howtoprogrammaticallyrotateanodeandkeepthelabelhorizontalafterrotating.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoprogrammaticallyrotateanodeandkeepthelabelhorizontalafterrotating.md
created_at: 2025-07-03
---








  









### How to programmatically rotate a Node and keep the Label horizontal after rotating? {#how-to-programmatically-rotate-a-node-and-keep-the-label-horizontal-after-rotating style="tab-stops: 0pt"}

\
The Node can be programmatically rotated and the Label can be kept horizontal after rotation using the following code snippet.\
\

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [double][ angle = 90;]                                                  |
|                                                                                                                                                              |
| [NewClient.RenderTransform = [new] [RotateTransform](){Angle = angle};]     |
|                                                                                                                                                              |
| [NewClient.Label = [\"90 deg rotation\"];]                                                       |
|                                                                                                                                                              |
| [NewClient.RenderTransformOrigin = [new] System.Windows.[Point](0.5, 0.5);] |
|                                                                                                                                                              |
| [NewClient.LabelAngle = 360 - angle;]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [Dim][ angle [As] [Double] = 90] |
|                                                                                                                                                                 |
| [NewClient.RenderTransform = [New] RotateTransform() [With] {.Angle = angle}]     |
|                                                                                                                                                                 |
| [NewClient.Label = \"90 deg rotation\"]                                                                                     |
|                                                                                                                                                                 |
| [NewClient.RenderTransformOrigin = [New] System.Windows.Point(0.5, 0.5)]                               |
|                                                                                                                                                                 |
| [NewClient.LabelAngle = 360 - angle][]                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
Here NewClient is an instance of Node.

 

[]{#related-topics}

