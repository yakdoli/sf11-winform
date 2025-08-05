---
title: creatingahalfcirculargauge.md
original_path: WinForms_Docs/04_Controls/Gauge/creatingahalfcirculargauge.md
created_at: 2025-08-05
---






#### Creating a Half Circular Gauge {#creating-a-half-circular-gauge style="tab-stops: 0pt"}

[] 

Half Circular Gauge can be created by setting the CircularGaugeModel class's Frame**Type** property to HalfCircle.

**[]** 


+-------------------------------+----------------------------------------------------+-------------------------------+----------------------------------------------------------------------------------+--------------------------------------------------+
| Property                      | Description                                        | Type of Property              | Value It Accepts                                                                 | Any other dependencies/Sub properties associated |
+-------------------------------+----------------------------------------------------+-------------------------------+----------------------------------------------------------------------------------+--------------------------------------------------+
| HalfCircleInnerRadius         | Sets the Radius of the inner half circle.          | [double] | [double]                                                    | Dependency(when FrameType is set to HalfCircle)  |
+-------------------------------+----------------------------------------------------+-------------------------------+----------------------------------------------------------------------------------+--------------------------------------------------+
| HalfCircleInnerSweepDirection | Sets the sweep direction of the inner half circle. | [enum]   | [SweepDirection].Clockwise                               | Dependency(when FrameType is set to HalfCircle)  |
|                               |                                                    |                               |                                                                                  |                                                  |
|                               |                                                    |                               |                                                                                  |                                                  |
|                               |                                                    |                               |                                                                                  |                                                  |
|                               |                                                    |                               | [SweepDirection].Counterclockwise                        |                                                  |
+-------------------------------+----------------------------------------------------+-------------------------------+----------------------------------------------------------------------------------+--------------------------------------------------+
| HalfCircleSweepDirection      | Sets the sweep direction of the half circle.       | [enum]   | [SweepDirection].Clockwise                               | Dependency(when FrameType is set to HalfCircle)  |
|                               |                                                    |                               |                                                                                  |                                                  |
|                               |                                                    |                               | [SweepDirection].Counterclockwise[] |                                                  |
+-------------------------------+----------------------------------------------------+-------------------------------+----------------------------------------------------------------------------------+--------------------------------------------------+


**[]** 

More:







