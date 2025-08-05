---
title: customizingappearancethroughcss.md
original_path: WinForms_Docs/02_Concepts/customizingappearancethroughcss.md
created_at: 2025-08-05
---






##### Customizing appearance through CSS {#customizing-appearance-through-css style="tab-stops: 0pt"}

[] 

The look-and-feel of the Splitter can be customized using the css properties to enrich the appearance settings which has been discussed below.

You need to create new css file and set **CustomCSS** property of Splitter to the path of this css file. After this setting, the default css setting will no more be applied to the Splitter control.

Splitter, SplitterBar, SlitPane, SlidingZone, SlidingPane are inherited from WebControl, so, you can use WebControl style properties for customization Splitter appearance (CssClass, BackColor, ForeColor, BorderColor, BorderStyle, BorderWidth, etc).

Also you can use SplitterBarSize property of Splitter to set the size in pixels of the split bar.

Moreover, the SplitterBar can be customized and the styles can be set using the following properties.

[] 


  ---------------------------- -------------------------------------------------------------------------------
           Property            Description
  HoverCssClass                CSS Class name applied to the SplitterBar on mouse over.
  ExpandCollapseAreaCssClass   CSS Class name applied to the expand/collapse image container of SplitterBar.
  ExpandCollapseImageWidth     The width of the expand/collapse images.
  ExpandCollapseImageHeight    The height of the expand/collapse images.
  ExpandImageUrl               Specifies the image for expand button in SplitterBar.
  CollapseImageUrl             Specifies the image for collapse button in SplitterBar.
  ExpandImageHoverUrl          Specifies the image for expand button in SplitterBar on mouse over.
  CollapseImageHoverUrl        Specifies the image for collapse button in SplitterBar on mouse over.
  ---------------------------- -------------------------------------------------------------------------------


[] 

[·      ]**DragSplitterBar_Default**: css classname that is applied to the SplitterBar\'s drag effect html element

[·      ]**ErrorDragSplitterBar_Default**: css classname that is applied to the SplitterBar\'s drag effect html element, when the user moves the SplitterBar outside the allowed dragging area

[] 

The following code example demonstrates how to use these properties for customizing Splitter appearance.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][cc1][:][Splitter][ [runat][=\"server\"] [ID][=\"Splitter1\"] **[Width][=\"300px\"] [Height][=\"150px\"]** **[CustomCSS][=\"../CSS/Splitter_style.css\"]**] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    **[SplitterBarSize][=\"10\"] [BorderColor][=\"#8FB7D1\"] [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"]**[\>]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][SplitPane] [runat][=\"server\"] [ID][=\"BottomPane\"] **[BackColor][=\"#E7F3FC\"]**[\>]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        Left pane]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\</][cc1][:][SplitPane][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][SplitterBar] [runat][=\"server\"] [ID][=\"SplitterBar1\"] [CollapseMode][=\"Both\"] **[CssClass][=\"SplitterBar_Default\"]**]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[HoverCssClass][=\"SplitterBar_Hover\"] [ExpandCollapseImageWidth][=\"10\"] [ExpandCollapseImageHeight][=\"34\"]**]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[ExpandImageUrl][=\"../images/expandimage_default.gif\"] [ExpandHoverImageUrl][=\"../images/expandimage_hover.gif\"]**]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[CollapseImageUrl][=\"../images/collapseimage_default.gif\"] [CollapseHoverImageUrl][=\"../images/collapseimage_hover.gif\"]** [/\>]]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][SplitPane] [runat][=\"server\"] [ID][=\"MiddlePane\"] **[BackColor][=\"#E7F3FC\"]**[\>]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        Middle pane[\</][cc1][:][SplitPane][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][SplitterBar] [runat][=\"server\"] [ID][=\"SplitterBar2\"] [CollapseMode][=\"Both\"]**[CssClass][=\"SplitterBar_Default\"]**]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[HoverCssClass][=\"SplitterBar_Hover\"] [ExpandCollapseImageWidth][=\"10\"] [ExpandCollapseImageHeight][=\"34\"]**]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[ExpandImageUrl][=\"../images/expandimage_default.gif\"] [ExpandHoverImageUrl][=\"../images/expandimage_hover.gif\"]**]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        **[CollapseImageUrl][=\"../images/collapseimage_default.gif\"] [CollapseHoverImageUrl][=\"../images/collapseimage_hover.gif\"]** [/\>]]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][SplitPane] [runat][=\"server\"] [ID][=\"LeftPane\"] **[BackColor][=\"#E7F3FC\"]**[\>]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        Right pane]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\</][cc1][:][SplitPane][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][cc1][:][Splitter][\>]                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Images

[] 

Expand image Default

[] 

{border="0"}

[] 

Collapse Image

[] 

{border="0"}

[] 

Expand Image Hover

[] 

{border="0"}

[] 

Collapse Image Hover

[] 

{border="0"}

[] 

Splitter_style.css file

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                                                                    |
|                                                                                                                                                                      |
| **[]**                                                                                                        |
|                                                                                                                                                                      |
| [SplitterBar_Default]                                                                                             |
|                                                                                                                                                                      |
| [{]                                                                                                                              |
|                                                                                                                                                                      |
| [    [background-image]:[url(../images/splitterbar_bg_default.gif)];]                   |
|                                                                                                                                                                      |
| [    [border-left]:[1px] [solid] [#8FB7D1];]  |
|                                                                                                                                                                      |
| [    [border-right]:[1px] [solid] [#8FB7D1];] |
|                                                                                                                                                                      |
| [}]                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 397: Default Splitter Bar

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                                                                    |
|                                                                                                                                                                      |
| **[]**                                                                                                        |
|                                                                                                                                                                      |
| [SplitterBar_Hover]                                                                                               |
|                                                                                                                                                                      |
| [{]                                                                                                                              |
|                                                                                                                                                                      |
| [    [background-color]:[#FEEECD];            ]                                         |
|                                                                                                                                                                      |
| [    [border-left]:[1px] [solid] [#8FB7D1];]  |
|                                                                                                                                                                      |
| [    [border-right]:[1px] [solid] [#8FB7D1];] |
|                                                                                                                                                                      |
| [}]                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 398: Hover Splitter Bar

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                                                               |
|                                                                                                                                                                 |
| **[]**                                                                                                   |
|                                                                                                                                                                 |
| [DragSplitterBar_Default]                                                                                    |
|                                                                                                                                                                 |
| [{]                                                                                                                         |
|                                                                                                                                                                 |
| [    [z-index] : [500];]                                                           |
|                                                                                                                                                                 |
| [    [background-color]: [#D2E3F0];]                                               |
|                                                                                                                                                                 |
| [    [filter]:[progid:DXImageTransform.Microsoft.Alpha(opacity=60)]; ]             |
|                                                                                                                                                                 |
| [    [opacity]: [0.6];]                                                            |
|                                                                                                                                                                 |
| [    [border]: [1px] [solid] [#8FB7D1];] |
|                                                                                                                                                                 |
| [}]                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 399: Default DragSplitterBar

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                                                           |
|                                                                                                                                                             |
| **[]**                                                                                               |
|                                                                                                                                                             |
| [ErrorDragSplitterBar_Default]                                                                           |
|                                                                                                                                                             |
| [{]                                                                                                                     |
|                                                                                                                                                             |
| [    [z-index] : [500];]                                                       |
|                                                                                                                                                             |
| [    [border]: [1px] [solid] [red];] |
|                                                                                                                                                             |
| [    [background-color]: [#f60];]                                              |
|                                                                                                                                                             |
| [    [filter]:[progid:DXImageTransform.Microsoft.Alpha(opacity=60)]; ]         |
|                                                                                                                                                             |
| [    [opacity]: [0.6];]                                                        |
|                                                                                                                                                             |
| [}]                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 400: Default DragSplitterBar for errors

[] 

Images

[] 

The result will be like this.

[] 

{border="0"}

Figure 401

[] 

SlidingPane\'s additional css properties to enrich the appearance settings.

[] 


  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
  Property            Description
  TabAppearanceMode   Specifies enum values: TextOnly, ImageOnly, TextAndImage.
  ImageUrl            Specifies the image to be displayed on slide. This image will be displayed only if we set **TabAppearanceMode** property to TextandImage/ImageOnly.
  DockImageUrl        Specifies the url for the dock image for the pane.
  UnDockImageUrl      Specifies the url for the undock image for the pane.
  CollapseImageUrl    Specifies the url for the collapse image for the pane.
  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------


[] 


  ---------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------
  Class                                    Description
  SlidingPaneCollapseHeaderCssClass        This collapse header part will get affected by setting these properties - SlidingPaneCollapseHeaderCssClass and SlidingPaneCollapseHeaderHoverCssClass.
  SlidingPaneCollapseHeaderHoverCssClass   Specifies the css class for a collapsed sliding pane when hovered.
  SlidingPaneExpandHeaderCssClass          This expand header part will get affected by setting these properties - SlidingPaneCollapseHeaderCssClass and SlidingPaneCollapseHeaderHoverCssClass.
  SlidingPaneExpandHeaderHoverCssClass     Specifies the css class for an expanded sliding pane when hovered.
  SlidingPaneResizeBarCssClass             Specifies the resize bar css class of the sliding pane.
  SlidingPaneResizeBarHoverCssClass        Specifies the resize bar hover css class of the sliding pane.
  ---------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

TabAppearanceMode

[] 

{border="0"}

[] 

ImageURL

[] 

{border="0"}

**[]** 

SlidingPaneCollapseHeaderCssClass

**[]** 

{border="0"}

**[]** 

SlidingPaneExpandHeaderCssClass

**[]** 

{border="0"}

[] 

SlidingPaneResizeBarCssClass

[] 

{border="0"}

 

 

 

[]{#related-topics}

