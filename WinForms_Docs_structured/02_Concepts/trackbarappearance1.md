---
title: trackbarappearance1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\trackbarappearance1.md
created_at: 2025-07-03
---






##### TrackBar Appearance {#trackbar-appearance style="tab-stops: 0pt"}

[]{#p1193}[] 

FocusRectangle

**[]** 

A focus rectangle for the TrackBarEx control can be shown or hidden using **ShowFocusRect** property.

[] 

{border="0"}

[] 

Figure 1439: TrackBarEx with FocusRectangle

[] 

Gradient Start and End Color

**[]** 

By default, the TrackBarEx control has a gradient appearance. The start color and end color for this gradient appearance can be specified using **TrackBarGradientStart** and **TrackBarGradientEnd** properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [this][.trackBarEx1.TrackBarGradientEnd = System.Drawing.[Color].CadetBlue;]                                         |
|                                                                                                                                                                                                                                |
| [this][.trackBarEx1.TrackBarGradientStart = System.Drawing.[Color].MintCream;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [Me][.trackBarEx1.TrackBarGradientEnd = System.Drawing.Color.CadetBlue]   |
|                                                                                                                                                                |
| [Me][.trackBarEx1.TrackBarGradientStart = System.Drawing.Color.MintCream] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 1440: GradientStartColor = \"MintCream\"; GradientEndColor = \"CadetBlue\"

**[]** 

The control can be given a transparent background by enabling the **Transparent** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                      |
| [this][.trackBarEx1.Transparent = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                  |
|                                                                                                                                                                                                      |
| [Me][.trackBarEx1.Transparent = [True]][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[{border="0"}][]**

**[]** 

Figure 1441: TrackBarEx with Transparent Background

**[]** 

TrackBarEx Orientation

**[]** 

This control has options for vertical and horizontal orientation.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                      |
|                                                                                                                                                                          |
| [//To set the control to be vertically oriented]                                                                       |
|                                                                                                                                                                          |
| [this][.trackBarEx1.Orientation = [Orientation].Vertical;]     |
|                                                                                                                                                                          |
| [//To set the control to be horizontally oriented]                                                                     |
|                                                                                                                                                                          |
| [this][.trackBarEx1.Orientation = [Orientation].Horizontal;  ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                           |
|                                                                                                                                              |
| []                                                                                          |
|                                                                                                                                              |
| [\'To set the control to be vertically oriented]                                           |
|                                                                                                                                              |
| [Me][.trackBarEx1.Orientation = Orientation.Vertical]   |
|                                                                                                                                              |
| [\'To set the control to be horizontally oriented]                                         |
|                                                                                                                                              |
| [Me][.trackBarEx1.Orientation = Orientation.Horizontal] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 1442: Vertical and Horizontal Orientation for TrackBarEx

 

[]{#related-topics}

