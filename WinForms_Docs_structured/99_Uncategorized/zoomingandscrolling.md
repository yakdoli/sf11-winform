---
title: zoomingandscrolling.md
original_path: WinForms_Docs/99_Uncategorized/zoomingandscrolling.md
created_at: 2025-08-05
---








  









### Zooming and Scrolling {#zooming-and-scrolling style="tab-stops: 0pt"}

[] 

Interactive Zooming

**[]** 

Zooming via Mouse

**[]** 

Essential Chart supports interactive zooming features along the x and y axis. During runtime, the user can simply select the range he wants to zoom with the mouse and the chart will accordingly zoom-in. Scrollbars will be activated to browse the areas that become hidden on zooming in.

 

Enable Zooming via the **EnableXZooming** and **EnableYZooming** properties.

[] 

{border="0"}

[] 

Figure 282: Select a region in the chart to Zoom-In

[] 

{border="0"}

**[]** 

Figure 283: Resultant Zoomed-In Chart

**[]** 

**In the ChartWebControl**, the scrollbars can be displayed or hidden using the**  ChartWebControl.ShowScrollBars** property.

The user can zoom out by clicking the \"Zoom Out\" button in the scrollbar.

[] 

{border="0"}

**[]** 

Figure 284: Zoom Out button beside the Scroll Bar

[] 

**ZoomOutIncrement** property specifies the increment by which to zoom out. The default value is **0.2**.

 

It is also possible to hide this ZoomOut button in ChartWeb control. This is done by setting **ShowScrollbarsResetButton** property to **true**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [this][.ChartWebControl1.ShowScrollBarsResetButton=[true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [Me][.ChartWebControl1.ShowScrollBarsResetButton=[True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Panning Support for Zoomed Chart

[] 

Now, you will be able to pan a chart when it is zoomed. Set the **ChartControl.MouseAction** to \'Panning\' to enable this feature. Set the MouseAction to \'None\' to disable this feature. The panning action can be controlled using the **ZoomActions** property that is available for individual axis.

[] 


+-----------------------------------+-----------------------------------------------------------------------+
| Chart Axes Properties             | Description                                                           |
+-----------------------------------+-----------------------------------------------------------------------+
| ZoomActions                       | Specifies the zoom action on the corresponding axis. The options are, |
|                                   |                                                                       |
|                                   | *Panning* - Enables panning in the zoomed chart.                      |
|                                   |                                                                       |
|                                   | *None* - Disables panning in the zoomed chart.                        |
+-----------------------------------+-----------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [this][.chartControl1.MouseAction = [ChartMouseAction].Panning;]                |
|                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.ZoomActions = [ChartZoomingAction].Panning;] |
|                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryYAxis.ZoomActions = [ChartZoomingAction].Panning;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [Me][.chartControl1.MouseAction = [ChartMouseAction.Panning]]      |
|                                                                                                                                                                               |
| [Me][.chartControl1.PrimaryXAxis.ZoomActions = ChartZoomingAction.Panning] |
|                                                                                                                                                                               |
| [Me][.chartControl1.PrimaryYAxis.ZoomActions = ChartZoomingAction.Panning] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Remember to enable zooming on both the axis using EnableXZooming and EnableYZooming properties, before trying out the above panning feature. You cannot pan a chart without zooming it.


**[]** 

Formatted Axes Lables

[] 

It is possible to show formatted axes labels for a zoomed chart. Essential Chart\'s **SmartDateZoom** property when set to **true** enables this feature. You can set any one of the following custom label formats to the chart axis.

[] 

[·      ]SmartDateZoomDayLevelLabelFormat

[·      ]SmartDateZoomYearLevelLabelFormat

[·      ]SmartDateZoomWeekLevelLabelFormat

[·      ]SmartDateZoomSecondLevelLabelFormat

[·      ]SmartDateZoomMonthLevelLabelFormat

[·      ]SmartDateZoomHourLevelLabelFormat

[·      ]SmartDateZoomMinuteLevelLabelFormat

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [this][.chartControl1.PrimaryXAxis.SmartDateZoom = [true];]                                    |
|                                                                                                                                                                                                          |
| [this][.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = [\"dd MM/yy HH.00\"];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [Me][.chartControl1.PrimaryXAxis.SmartDateZoom = [True]]                                    |
|                                                                                                                                                                                                       |
| [Me][.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = [\"dd MM/yy HH.00\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 285: SmartDateZoomDayLevelLabelFormat = \"dd MM/yy  HH.00\"


{border="0"}Note: The value type of the axis should be \"DateTime\" for setting the above formatted labels.

 


Cancel Zooming via Keyboard

 

Essential Chart enables users to use keyboard shortcuts to cancel Zooming. This feature can be enabled using the **ZoomCancel** property.

 

The following property is used to cancel zooming action that can be mapped to specific keys:

 

 


  ------------------------ --------------------------------------------------------------------------------------
  Chart control Property   Description
  ZoomCancel               Specifies the keyboard shortcut to control Zoom cancel. The default value is ESCAPE.
  ------------------------ --------------------------------------------------------------------------------------


**[]** 

 

The following code snippet illustrates this:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[C#\]]                                                                                                                     |
|                                                                                                                                                                   |
| [//Set the Enter key to cancel zooming of control.][       ]                |
|                                                                                                                                                                   |
| [this][.ChartWebControl1.ZoomCancel = [Keys].Enter;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[VB\]]                                                                                                                  |
|                                                                                                                                                                |
| [//Set the Enter key to cancel zooming of control.][       ]             |
|                                                                                                                                                                |
| [Me][.ChartWebControl1.ZoomCancel = [Keys].Enter] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


 


[]{#p200} 

[]{#related-topics}

