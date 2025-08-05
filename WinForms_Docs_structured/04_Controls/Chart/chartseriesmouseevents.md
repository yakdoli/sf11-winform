---
title: chartseriesmouseevents.md
original_path: WinForms_Docs/04_Controls/Chart/chartseriesmouseevents.md
created_at: 2025-08-05
---






##### Chart Series Mouse Events {#chart-series-mouse-events style="tab-stops: 0pt"}

The following are the mouse events and their corresponding descriptions:

[] 

Table 170: Event


  ---------------------- -------------------------------------------------------------------------------------------------
  Event                  Description
  MouseClick             This event is handled when any mouse button is clicked, while mouse pointer is over the series.
  MouseDown              This event is handled when any mouse button is pressed, while mouse pointer is over the series.
  MouseEnter             This event is handled when mouse pointer enters the bounds of the series.
  MouseLeave             This event is handled when mouse pointer leaves the bounds of the series.
  MouseUp                This event is handled when any mouse button is released over the series.
  MouseLeftButtonUp      This event is handled when left mouse button is released over the series.
  MouseLeftButtonDown    This event is handled when left mouse button is pressed over the series.
  MouseRightButtonUp     This event is handled when right mouse button is released over the series.
  MouseRightButtonDown   This event is handled when right mouse button is pressed over the series.
  ---------------------- -------------------------------------------------------------------------------------------------


[] 

These events can be initialized using the following lines of code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][sfchart][:][ChartSeries][ Data][=\"0 3 1 4 2 5 3 9 6 4 7 3 8 5 9 11\"][ Type][=\"Pie\"][ MouseClick][=\"ChartSeries_MouseClick\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [MouseHover][=\"ChartSeries_MouseHover\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [ChartSeries][ chartSeries = [new] [ChartSeries]();]                                        |
|                                                                                                                                                                                                                                  |
| [this][.MouseClick += [new] EventHandler(ChartSeries_MouseClick);]                                                     |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [private][ [void] ChartSeries_MouseClick([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [// Your code here]                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also



 

[]{#related-topics}

