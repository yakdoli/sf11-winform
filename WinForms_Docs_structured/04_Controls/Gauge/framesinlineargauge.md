---
title: framesinlineargauge.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\framesinlineargauge.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Frames in Linear Gauge {#frames-in-linear-gauge style="tab-stops: 0pt"}

[In Linear Gauge, there are three frames: ]

[·      ]Outer Frame

[·      ]Inner Frame

[·      ]Frame Interior

 

 

[You can set the border width, color and gradient colors by using the properties tabulated below.]

[The linear gauge also supports three types of frame styles:]

[1.   Rounded Rectangle]

[2.   Rectangle]

[3.   Cropped Rectangle.]

[The frame style can be set by using the property **FrameType, (**tabulated below, along with the other properties for the three frames):]

  ---------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
  **[Property ]** []   **[Description ]** []     **[Type ]** []     **[Data Type ]** []   **[Reference links ]** []
  [ FrameOuterWidth]                                              [Sets the width for the outer frame of the circular gauge ]          [Server-Side] []   [Double ]                                                        [NA]
  [FrameOuterColor]                                               [Sets the background color for the outer frame]                      [Server-Side]                                                 [Color]                                                          [NA]
  [FrameInnerWidth]                                               [Sets the width for the inner frame]                                 [Server-Side]                                                 [Double]                                                         [NA]
  [FrameInnerColor]                                               [Sets the background color for the inner frame]                      [Server-Side]                                                 [Color]                                                          [NA]
  [FrameInterior]                                                 [Sets the gradient color for the background of the circular gauge]   [Server-Side]                                                 [ColorInfo\[\]]                                                  [NA]
  [FrameType]                                                     [Sets the style of the frame in linear gauge]                        [Server-Side]                                                 [Enum]                                                           [NA]
  [Orientation]                                                   [Sets the orientation for the frame]                                 [Server-Side]                                                 [Enum]                                                           [NA]
  ---------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------

[] 


Note: the properties for Frames in the circular and linear gauges are the same.


 

[To set the gradient color for the interior frame use the following code snippets:]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this] [.LinearGauge1.FrameInterior = [new][Brush]([new][ColorInfo]\[\] { [new][ColorInfo](System.Drawing.[ColorTranslator].FromHtml([this].ColorPallete1.SelectedColor), 0),[ new][ColorInfo](System.Drawing.[ColorTranslator].FromHtml([this].ColorPallete2.SelectedColor), 0.5), [new][ColorInfo](System.Drawing.[ColorTranslator].FromHtml([this].ColorPallete3.SelectedColor), 1) });] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this] [.LinearGauge1.FrameType = [LinearGaugeFrameType].RoundedRectangle;] []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me] [.LinearGauge1.FrameInterior = [New] Brush([New] ColorInfo() {[New] ColorInfo(System.Drawing.ColorTranslator.FromHtml([Me].ColorPallete1.SelectedColor), 0),[ New] ColorInfo(System.Drawing.ColorTranslator.FromHtml([Me].ColorPallete2.SelectedColor), 1), [New] ColorInfo(System.Drawing.ColorTranslator.FromHtml([Me].ColorPallete3.SelectedColor), 1)})] [] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me] [.LinearGauge1.FrameType = [LinearGaugeFrameType].RoundedRectangle] []                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Follow similar procedures to tweak the frames as well as the frame styles.

{border="0"}

Figure 45: Vertical linear gauge with a rounded rectangle frame, and gradient color in the interior frame

 


Note: Properties for the frames of Circular and linear gauges are all the same.


[]{#related-topics}

