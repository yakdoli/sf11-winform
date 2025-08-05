---
title: errorbarssymbolshape.md
original_path: WinForms_Docs/99_Uncategorized/errorbarssymbolshape.md
created_at: 2025-08-05
---






#### ErrorBarsSymbolShape {#errorbarssymbolshape style="tab-stops: 0pt"}

[] 

This property determines the shape of the error bar symbol when [DrawErrorBars]{.UGHyperlink} is **true**.

[] 

[] 


+-------------------------------------+--------------------------------------------------------------------+
|                                                                                                          |
|                                                                                                          |
| Details                                                                                                  |
+-------------------------------------+--------------------------------------------------------------------+
| Possible Values                     | None - No marker will be shown.\                                   |
|                                     | Line - A Line will be drawn as the marker.\                        |
|                                     | Square - A Square will be drawn as the marker.\                    |
|                                     | Circle - A Circle will be drawn as the marker.\                    |
|                                     | Diamond - A Diamond will be drawn as the marker.\                  |
|                                     | Triangle - A Triangle will be drawn as the marker.                 |
|                                     |                                                                    |
|                                     | VertLine - A VerticalLine will be drawn as the marker.             |
|                                     |                                                                    |
|                                     | Cross - A Cross will be drawn as the marker.                       |
|                                     |                                                                    |
|                                     | Hexagon - An Hexagon will be drawn as the marker.                  |
|                                     |                                                                    |
|                                     | Horizline - An Horizontal Line will be drawn as the marker.        |
|                                     |                                                                    |
|                                     | Image - An Image will be drawn as the marker.                      |
|                                     |                                                                    |
|                                     | InvertedTriangle - A InvertedTriangle will be drawn as the marker. |
|                                     |                                                                    |
|                                     | Pentagon - A Pentagon will be drawn as the marker.                 |
|                                     |                                                                    |
|                                     | Star - A Star will be drawn as the marker.                         |
+-------------------------------------+--------------------------------------------------------------------+
| Default Value                       | Diamond                                                            |
+-------------------------------------+--------------------------------------------------------------------+
| 2D / 3D Limitations                 | No                                                                 |
+-------------------------------------+--------------------------------------------------------------------+
| Applies to Chart Element            | All Series                                                         |
+-------------------------------------+--------------------------------------------------------------------+
| Applies to Chart Types              | Line Chart                                                         |
+-------------------------------------+--------------------------------------------------------------------+


**[]** 

Here is some sample code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [this.][ChartWebControl1.Series\[0\].DrawErrorBars =[ true];]                           |
|                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series\[0\].ErrorBarsSymbolShape = [ChartSymbolShape].Circle;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.ChartWebControl1.Series(0).DrawErrorBars = [true]]                           |
|                                                                                                                                                                                              |
| [Me][.ChartWebControl1.Series(0).ErrorBarsSymbolShape = [ChartSymbolShape].Circle] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 119: Line Chart with ErrorBarSymbol set to \"Circle\"

**[]** 

See Also

[] 

[Line Chart]{.UGHyperlink}[, ]{.UGHyperlink}[DrawErrorBars]{.UGHyperlink}[]{.UGHyperlink}

[]{#p99} 

[]{#related-topics}

