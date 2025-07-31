---
title: builtinframes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builtinframes.md
created_at: 2025-07-03
---






##### Built-in Frames {#built-in-frames style="tab-stops: 0pt"}

Circular gauge contains variety of built-in frame types to provide effective rim styles. And also you can customize the built-in frame types through circular gauge properties such as FirstFrameThickness, SecondFrameThickness, FirstFrameFillColor, SecondFrameFillcolor and InnerFrameFillcolor.

 

Following built-in frame types are available in circular gauge.

[] 

[·      ]**FullCircle**---circular gauge with default template will be displayed as full circle.

[·      ]**HalfCircle**---circular gauge with default template will be displayed as half circle.

[·      ]**CircularWithDarkOuterFrames**---circular gauge frame with dark first and second frame.

[·      ]**CircularWithInnerTopGradient**---circular gauge frame with inner top gradient.

[·      ]**CircularWithInnerLeftGradient**---circular gauge frame with inner left gradient.

[·      ]**CircularCenterGradient**---circular gauge with center gradient.

[·      ]**CounterclockwiseHalfCircle---**counter clockwise half circular gauge.

[] 

The following code example illustrates how to set the frame type for the Circular Gauge to *CircularWithDarkOuterFrames*.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<!\--Circular gauge with frame type as CircularWithDarkOuterFrames.\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][CircularGauge][ Margin][=\"5\"][ Name][=\"circularGauge1\"][ FrameType][=\"CircularWithDarkOuterFrames\"/\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [\<!\--Circular gauge with frame type as CircularWithDarkOuterFrames.\--\>]                                                                                    |
|                                                                                                                                                                                                                                  |
| [CircularGauge][ circularGauge1 = [new] [CircularGauge]();] |
|                                                                                                                                                                                                                                  |
| [circularGauge1.FrameType = [GaugeFrameType].CircularWithDarkOuterFrames;]                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shots illustrate the different types of circular frame types that are available in the gauge library.

[] 

{border="0"}

Figure 20: Circular Gauge with \"FullCircle\" Frame

***[]*** 

{border="0"}

Figure 21: Circular Gauge with \"CircularWithInnerTopGradient\" Frame

***[]*** 

***[{border="0"}]**[]***

Figure 22:  Circular Gauge with \"CircularCenterGradient\" Frame

***[]*** 

{border="0"}

Figure 23: Circular Gauge with \"CircularWithDarkOuterFrames\" Frame

***[]*** 

{border="0"}

Figure 24: Circular Gauge with \"CircularWithInnerLeftGradient\" Frame

***[]*** 

{border="0"}

Figure 25: Circular Gauge with \"HalfCircle\" Frame

 

[]{#related-topics}

