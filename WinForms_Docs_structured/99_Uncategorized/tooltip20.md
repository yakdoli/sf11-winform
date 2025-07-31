---
title: tooltip20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tooltip20.md
created_at: 2025-07-03
---








  









### Tooltip {#tooltip style="tab-stops: 0pt"}

The *OLAP Gauge* control can display the tooltip information when the mouse pointer is moved over the Gauge pointer or marker.

[] 

**[Pointer ToolTip]**

[] 

The *OLAP Gauge* control for Silverlight provides value information when the mouse pointer is moved over the pointer. This is achieved by enabling the *ShowPointersTooltip* property of the *Gauge* control. The following code example illustrates the setting of this property.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                          |
| **[]**                                                                                               |
|                                                                                                                                          |
| **[this][.olapGauge1.ShowPointersTooltip = true;]** |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                  |
|                                                                                                                                   |
| []                                                                                            |
|                                                                                                                                   |
| [Me][.olapGauge1.ShowPointersTooltip = True] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates a pointer tooltip displayed for the *OLAP Gauge*.

[] 

{border="0"}

 

Figure 26: Pointer Tooltip[]

[] 

Marker ToolTip

[] 

The *OLAP Gauge* control for Silverlight provides goal information when the mouse pointer is moved over the marker. This is achieved by enabling the *ShowMarkersTooltip* property of the *Gauge* control. The following code example illustrates the setting of this property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                     |
| []                                                                                              |
|                                                                                                                                     |
| [this][.olapGauge1.ShowMarkersTooltip = true;] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                 |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [Me][.olapGauge1.ShowMarkersTooltip = True] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The following screen shot illustrates a marker tooltip displayed for the OLAP Gauge.

[] 

{border="0"}

 

Figure 27: Marker Tooltip[]

[] 

 

[]{#related-topics}

