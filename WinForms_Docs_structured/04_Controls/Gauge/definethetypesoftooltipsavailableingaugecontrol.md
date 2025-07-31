---
title: definethetypesoftooltipsavailableingaugecontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\definethetypesoftooltipsavailableingaugecontrol.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Define the types of tooltips available in Gauge control. {#define-the-types-of-tooltips-available-in-gauge-control. style="tab-stops: 0pt"}

The *OLAP Gauge* control can display the tooltip information when the mouse pointer is moved over the gauge pointer or marker.

[] 

Pointer ToolTip

[] 

The *OLAP Gauge* control for WPF provides value information when the mouse pointer is moved over the pointer. This is achieved by enabling the *ShowPointersTooltip* property of the gauge control. The following code example illustrates the setting of this property.

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                          |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [this] [.olapGauge1.ShowPointersTooltip = true;] |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                       |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [Me] [.olapGauge1.ShowPointersTooltip = True] |
+------------------------------------------------------------------------------------------------------------------------------------+

 

The following screen shot illustrates a pointer tooltip displayed for the OLAP Gauge.

[] 

{border="0"}

Figure 30: Pointer Tooltip

 

Marker ToolTip

[] 

The *OLAP Gauge* control for WPF provides goal information when the mouse pointer is moved over the marker. This is achieved by enabling the *ShowMarkersTooltip* property of the *Gauge* control. The following code example illustrates the setting of this property.

 

+-----------------------------------------------------------------------+
| \[C#\]                                                                |
|                                                                       |
|                                                                       |
|                                                                       |
| [this].olapGauge1.ShowMarkersTooltip = true;     |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| \[VB\]                                                                |
|                                                                       |
|                                                                       |
|                                                                       |
| [Me].olapGauge1.ShowMarkersTooltip = True        |
+-----------------------------------------------------------------------+

 

The following screen shot illustrates a marker tooltip displayed for the OLAP Gauge.

 

{border="0"}

Figure 31: Marker Tooltip

Sample Location

**[]**  

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\WPF\\OLAPGauge.WPF\\Samples\\Product ShowCase\\Product Showcase Demo\\**

 

 

 

[]{#related-topics}

