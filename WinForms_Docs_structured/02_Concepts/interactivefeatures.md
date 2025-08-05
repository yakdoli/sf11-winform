---
title: interactivefeatures.md
original_path: WinForms_Docs/02_Concepts/interactivefeatures.md
created_at: 2025-08-05
---








  









### Interactive Features {#interactive-features style="tab-stops: 0pt"}

[] 

Interactive Cursor

[] 

This feature let you position the mouse pointer at a specific data point in a series and hint you on it\'s x and y values via a horizontal and vertical line passing through the data point and intersecting the x and y axis. These lines can be dragged around in order to position them at specific data points.

Interactive Cursor can be implemented by creating an instance of **ChartInteractiveCursor** with the ChartSeries as its input. Then add the instance to the Interactive Cursors collection as shown below.

This cursor can be moved forward in vertical and horizontal positions.

To move vertically or horizontally in a forward direction, set the **VerticalMove**() or **HorizontalMove**() methods to **true**. To move vertically or horizontally in a reverse direction, set the **VerticalMove**() or **HorizontalMove**() methods to **false**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// Create a new instance of the ChartInteractiveCursor class and initialize chartseries into it.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [ChartInteractiveCursor cursor1 = ][new][ ChartInteractiveCursor(][this][.chartControl1.Series\[0\]);] |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// Add the instance to the ChartInteractive Cursor collection.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.][ChartWebControl1[.ChartArea.InteractiveCursors.Add(cursor1));]]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// To specify forward movement of Interactive Cursor]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.ChartArea.InteractiveCursors\[0\].VerticalMove([true]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.ChartArea.InteractiveCursors\[0\].HorizontalMove([true]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// To specify reverse movement of Interactive Cursor]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.ChartArea.InteractiveCursors\[0\].VerticalMove([false]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.ChartArea.InteractiveCursors\[0\].HorizontalMove([false]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [//Color of the pointer]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                |
| [cursor1.Color = Color.Red;]                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                           |
| [\' Create a new instance of the ChartInteractiveCursor class and initialize chartseries into it.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [ChartInteractiveCursor cursor1 = ][New][ ChartInteractiveCursor(][Me][.chartControl1.Series(0))] |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [\' Add the instance to the ChartInteractive Cursor collection.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.][ChartWebControl1[.ChartArea.InteractiveCursors.Add(cursor1))]]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [\' To specify forward movement of Interactive Cursor]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartWebControl1.ChartArea.InteractiveCursors(0).VerticalMove([True])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartWebControl1.ChartArea.InteractiveCursors(0).HorizontalMove([True])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [\' To specify reverse movement of Interactive Cursor]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartWebControl1.ChartArea.InteractiveCursors(0).VerticalMove([True])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartWebControl1.ChartArea.InteractiveCursors(0).HorizontalMove([True])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [\'Color of the pointer]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                           |
| [cursor1.Color = Color.Red]                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 294: Chart Interactive Cursor

[]{#p204} 

[]{#related-topics}

