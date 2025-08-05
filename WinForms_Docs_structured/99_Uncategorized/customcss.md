---
title: customcss.md
original_path: WinForms_Docs/99_Uncategorized/customcss.md
created_at: 2025-08-05
---






##### Custom CSS {#custom-css style="tab-stops: 0pt"}

[] 

The appearance of the Slider can be customized using the **CustomCss** Property.

[] 

1.   Set the Path of the CSS file to the CustomCss property.

37.  Set the Root Name of the CSS file to the **ControlRootCSSClass** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][ssw][:][Slider][  [id][=\"Slider1\"] [CustomCSS][=\"css/SliderDefault.css\"] [ControlRootCSSClass][=\"SliderRoot_Default\"] [runat][=\"server\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][ssw][:][Slider][\>]                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                      |
| []                                                                               |
|                                                                                                                                      |
| [// Path of css file]                                              |
|                                                                                                                                      |
| [Slider1.CustomCSS = [\"css/SliderDefault.css\"];]        |
|                                                                                                                                      |
| []                                                                               |
|                                                                                                                                      |
| [// Root css name]                                                 |
|                                                                                                                                      |
| [Slider1.ControlRootCSSClass = [\"SliderRoot_Default\"];] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                     |
| []                                                                              |
|                                                                                                                                     |
| [// Path of css file]                                             |
|                                                                                                                                     |
| [Slider1.CustomCSS = [\"css/SliderDefault.css\"]]        |
|                                                                                                                                     |
| []                                                                              |
|                                                                                                                                     |
| [// Root css name]                                                |
|                                                                                                                                     |
| [Slider1.ControlRootCSSClass = [\"SliderRoot_Default\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 366: CSS Style applicable Segments

[] 

CSS File

[] 

+----------------------------------------------------------------------------------------------------------------------+
| [.SliderRoot_Default]                                            |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-color:Transparent;]                                  |
|                                                                                                                      |
| [background-repeat:repeat-x;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [position:relative;]                                             |
|                                                                                                                      |
| [padding:20px;]                                                  |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .SliderRoot_Table]                          |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [cursor: default;]                                               |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .horizontalTrack]                           |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-image:url(\'../Images/HorizontalBg.png\');]          |
|                                                                                                                      |
| [height:11px;]                                                   |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [left:0px;]                                                      |
|                                                                                                                      |
| [top:-3px;]                                                      |
|                                                                                                                      |
| [background-repeat:repeat-x;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .horizontalRightImage]                      |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-image:url(\'../Images/HorizontalCornerRight.png\');] |
|                                                                                                                      |
| [width:3px;]                                                     |
|                                                                                                                      |
| [height:11px;]                                                   |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [left:0px;]                                                      |
|                                                                                                                      |
| [top:-3px;]                                                      |
|                                                                                                                      |
| [background-repeat:repeat-x;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .horizontalLeftImage]                       |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-image:url(\'../Images/HorizontalCornerLeft.png\');]  |
|                                                                                                                      |
| [width:3px;]                                                     |
|                                                                                                                      |
| [height:11px;]                                                   |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [left:0px;]                                                      |
|                                                                                                                      |
| [top:-3px;]                                                      |
|                                                                                                                      |
| [background-repeat:repeat-x;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .horizontalHandle]                          |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [position:relative;]                                             |
|                                                                                                                      |
| [background-image:url(\'../Images/HorizontalHandle.png\');]      |
|                                                                                                                      |
| [width:13px;]                                                    |
|                                                                                                                      |
| [height:13px;]                                                   |
|                                                                                                                      |
| [cursor:pointer;]                                                |
|                                                                                                                      |
| [background-repeat:no-repeat;]                                   |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [top:0px;]                                                       |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .horizontalHandleHover]                     |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [position:relative;]                                             |
|                                                                                                                      |
| [background-image:url(\'../Images/HorizontalHandle.png\');]      |
|                                                                                                                      |
| [width:13px;]                                                    |
|                                                                                                                      |
| [height:13px;]                                                   |
|                                                                                                                      |
| [cursor:pointer;]                                                |
|                                                                                                                      |
| [background-repeat:no-repeat;]                                   |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [top:0px;]                                                       |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .verticalTrack]                             |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-image:url(\'../Images/VerticalBg.png\');]            |
|                                                                                                                      |
| [width:6px;]                                                     |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [left:-4px;]                                                     |
|                                                                                                                      |
| [top:0px;]                                                       |
|                                                                                                                      |
| [background-repeat:repeat-y;]                                    |
|                                                                                                                      |
| [background-position: center]                                    |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .verticalTopImage]                          |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [background-image:url(\'../Images/VerticalCornersTop.png\');]    |
|                                                                                                                      |
| [width:11px;]                                                    |
|                                                                                                                      |
| [height:3px;]                                                    |
|                                                                                                                      |
| [left:-4px;]                                                     |
|                                                                                                                      |
| [top:0px;]                                                       |
|                                                                                                                      |
| [background-repeat:repeat-y;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .verticalBottomImage]                       |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [left:-4px;]                                                     |
|                                                                                                                      |
| [top:0px;]                                                       |
|                                                                                                                      |
| [background-image:url(\'../Images/VerticalCornersBottom.png\');] |
|                                                                                                                      |
| [width:11px;]                                                    |
|                                                                                                                      |
| [height:3px;]                                                    |
|                                                                                                                      |
| [background-repeat:repeat-y;]                                    |
|                                                                                                                      |
| [background-position: center;]                                   |
|                                                                                                                      |
| [z-index:-1;]                                                    |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .verticalHandleHover]                       |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [position:relative;]                                             |
|                                                                                                                      |
| [background-image:url(\'../Images/VerticalHandle.png\');]        |
|                                                                                                                      |
| [width:13px;]                                                    |
|                                                                                                                      |
| [height:13px;]                                                   |
|                                                                                                                      |
| [cursor:pointer;]                                                |
|                                                                                                                      |
| [background-repeat:no-repeat;]                                   |
|                                                                                                                      |
| [}]                                                              |
|                                                                                                                      |
| []                                                               |
|                                                                                                                      |
| [.SliderRoot_Default .verticalHandle]                            |
|                                                                                                                      |
| [{]                                                              |
|                                                                                                                      |
| [position:relative;]                                             |
|                                                                                                                      |
| [background-image:url(\'../Images/VerticalHandle.png\');]        |
|                                                                                                                      |
| [width:13px;]                                                    |
|                                                                                                                      |
| [height:13px;]                                                   |
|                                                                                                                      |
| [cursor:pointer;]                                                |
|                                                                                                                      |
| [left]                                                           |
|                                                                                                                      |
| [background-repeat:no-repeat;]                                   |
|                                                                                                                      |
| [}]                                                              |
+----------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

