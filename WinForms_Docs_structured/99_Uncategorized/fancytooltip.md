---
title: fancytooltip.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\fancytooltip.md
created_at: 2025-07-03
---






#### FancyToolTip {#fancytooltip style="tab-stops: 0pt"}

**[]** 

Defines the styles for a fancy tooltip. These styles include font, marker style, symbol shape, back color and other related styles.

[] 


+-------------------------------------+--------------------------------------------------+
| Details                                                                                |
+-------------------------------------+--------------------------------------------------+
| Possible Values                     | Specifies symbol, symbol styles for the ToolTip. |
+-------------------------------------+--------------------------------------------------+
| Default Value                       | Visible - False                                  |
|                                     |                                                  |
|                                     | Angle  - 15                                      |
|                                     |                                                  |
|                                     | Alignment - Left                                 |
|                                     |                                                  |
|                                     | ForeColor - Color.Black                          |
|                                     |                                                  |
|                                     | BackColor - Color.Info                           |
|                                     |                                                  |
|                                     | SymbolColor - Color.Red                          |
|                                     |                                                  |
|                                     | Font - Arial, 8 pt                               |
|                                     |                                                  |
|                                     | Symbol Size - (10,10)                            |
|                                     |                                                  |
|                                     | Symbol - Circle                                  |
|                                     |                                                  |
|                                     | Style - SmoothRectangle                          |
+-------------------------------------+--------------------------------------------------+
| 2D / 3D Limitations                 | No                                               |
+-------------------------------------+--------------------------------------------------+
| Applies to Chart Element            | All series                                       |
+-------------------------------------+--------------------------------------------------+
| Applies to Chart Types              | All Chart Types                                  |
+-------------------------------------+--------------------------------------------------+


**[]** 

Here is some sample code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].FancyToolTip.Angle = 180;]                                                |
|                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].FancyToolTip.Style = [MarkerStyle].SmoothRectangle;] |
|                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].FancyToolTip.Symbol = [ChartSymbolShape].Hexagon;]   |
|                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].FancyToolTip.Visible = [true];]                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                           |
| [Me][.ChartWebControl1.Series(0).FancyToolTip.Angle = 180]                           |
|                                                                                                                                                                           |
| [Me][.ChartWebControl1.Series(0).FancyToolTip.Style = MarkerStyle.SmoothRectangle]   |
|                                                                                                                                                                           |
| [Me][.ChartWebControl1.Series(0).FancyToolTip.Symbol = ChartSymbolShape.Hexagon]     |
|                                                                                                                                                                           |
| [Me.][ChartWebControl1.Series(0).FancyToolTip.Visible =[ True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 123: Stacking Bar Chart with FancyToolTip

**[]** 

See Also

[] 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p103} 

[]{#related-topics}

