---
title: interactivezoomingandscrolling.md
original_path: WinForms_Docs/99_Uncategorized/interactivezoomingandscrolling.md
created_at: 2025-08-05
---








  









## Interactive Zooming and Scrolling {#interactive-zooming-and-scrolling style="tab-stops: 0pt"}

**[]** 

**Essential BI Olap Chart** for Web, supports interactive zooming features along the x and y axis. During runtime, the user can simply select the range they want to zoom with the mouse, and the chart would accordingly zoom-in. Scrollbars are activated to browse the areas that become hidden on zooming-in.

 

Enable zooming via the **EnableXZooming** and **EnableYZooming** properties.

[] 

[] 

{border="0"}

 

Figure 50: Chart to be Zoomed

{border="0"}

 

Figure 51: Zooming and Scrolling

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                        |
|                                                                                                                                                                                                            |
| [this][. olapChart1.EnableXZooming = [true];]                                                    |
|                                                                                                                                                                                                            |
| [this][. olapChart1.EnableXZooming = [true];]                                                    |
|                                                                                                                                                                                                            |
| [this][. olapChart1.PrimaryXAxis.ZoomFactor = 1.0;]                                                                   |
|                                                                                                                                                                                                            |
| [this][. olapChart1.PrimaryYAxis.ZoomFactor = 1.0;]                                                                   |
|                                                                                                                                                                                                            |
| [this][.olapChart1.ShowScrollBars = [true];][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                     |
|                                                                                                                                                                                                         |
| [Me][.olapChart1.EnableXZooming = [True]]                                                     |
|                                                                                                                                                                                                         |
| [Me][.olapChart1.EnableXZooming = [True]]                                                     |
|                                                                                                                                                                                                         |
| [Me][.olapChart1.PrimaryXAxis.ZoomFactor = 1.0]                                                                    |
|                                                                                                                                                                                                         |
| [Me.][olapChart1.PrimaryYAxis.ZoomFactor = 1.0]                                                                    |
|                                                                                                                                                                                                         |
| [Me][.olapChart1.ShowScrollBars = [True]][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

Table 28: Zooming and Scrolling

 


  ---------------- ----------------------------------------------------------------------- ------------------------------------ ------------------------------ -------------------------------------
  Methods          [Description]                                     [Parameters]   [Type]   [Return Type]
  EnableXZooming   Enables zooming on x-axis.                                              Server side                          boolean                        \-
  EnableXZooming   Enables zooming on y-axis.                                              Server side                          boolean                        \-
  ZoomingFactor    Sets a value to present a zooming effect accordingly on x and y axis.   Server side                          double                         \-
  ShowScrollBars   Enables\\disables the appearance of the scroll bar.                     Server side                          boolean                        \-
  ---------------- ----------------------------------------------------------------------- ------------------------------------ ------------------------------ -------------------------------------


 

Sample Link

A sample demo is available at the following location:

 

..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\ Zooming and Scrolling\\Zooming and Scrolling Demo\\[]

[]{#related-topics}

