---
title: creatingacirculargauge.md
original_path: WinForms_Docs/04_Controls/Gauge/creatingacirculargauge.md
created_at: 2025-08-05
---








  









### Creating a Circular Gauge {#creating-a-circular-gauge style="tab-stops: 0pt"}

 

Circular Gauge can be created in two ways:

[·      ]Through View Customization

[·      ]Through CircularGaugeModel Properties

 

 


+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Property             | Description                                | Type of Property                                       | Value It Accepts                                                                                                                                               | Any other dependencies/Sub properties associated                                                                 |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| FirstFrameFillColor  | Sets the first frame background.           | System.Windows.Media.[Brushes] | Refer to the below Link for  Value for the Brushes class.                                                                                                      | [NA][] |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx) |                                                                                                                  |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| SecondFrameFillColor | Sets the second frame background.          | System.Windows.Media.[Brushes] | Refer to the below Link for  Value for the Brushes class.                                                                                                      | [NA][] |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx) |                                                                                                                  |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| CenterFrameFillColor | Sets the center frame background.          | System.Windows.Media.[Brushes] | Refer to the below Link for  Value for the Brushes class.                                                                                                      | [NA][] |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx) |                                                                                                                  |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Radius               | Set the radius of the circle.              | [double]                          | [double]                                                                                                                                  | [NA][] |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| FrameType            | Sets the frame type of the Circular Gauge. | [enum]                            |  [GaugeFrameType].CircularOuterFrames                                                                                                  | [NA][] |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [GaugeFrameType].CircularWithInnerTopGradient                                                                                          |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [GaugeFrameType].CircularWithInnerLeftGradient                                                                                         |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [GaugeFrameType].CircularCenterGradient                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [GaugeFrameType].FullCircle                                                                                                            |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        |                                                                                                                                                                |                                                                                                                  |
|                      |                                            |                                                        | [GaugeFrameType].HalfCircle                                                                                                            |                                                                                                                  |
+----------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+


 

Circular Gauge contains variety of built-in frame types to provide effective rim styles. And also you can customize the built-in frame types through circular Gauge properties such as  FirstFrameFillColor, SecondFrameFillcolor and InnerFrameFillcolor.                                                                       

More:







