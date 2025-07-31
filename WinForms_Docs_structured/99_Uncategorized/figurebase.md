---
title: figurebase.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\figurebase.md
created_at: 2025-07-03
---






#### FigureBase {#figurebase style="tab-stops: 0pt"}

**[]** 

Specifies the drawing style for the funnel or pyramid chart base.

[] 


+-------------------------------------+-------------------------------------------------------+
| Details                                                                                     |
+-------------------------------------+-------------------------------------------------------+
| Possible Values                     | Circle - Renders the chart with a circular base.      |
|                                     |                                                       |
|                                     | Square - Renders the chart with a square base.        |
+-------------------------------------+-------------------------------------------------------+
| Default Value                       | Circle for Funnel Chart and Square for Pyramid Chart. |
+-------------------------------------+-------------------------------------------------------+
| 2D / 3D Limitations                 | 3D Only                                               |
+-------------------------------------+-------------------------------------------------------+
| Applies to Chart Element            | All series                                            |
+-------------------------------------+-------------------------------------------------------+
| Applies to Chart Types              | Funnel and Pyramid                                    |
+-------------------------------------+-------------------------------------------------------+


[] 

Here is some sample code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [// Setting FigureBase For Pyramid Chart]                                                                                                                    |
|                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PyramidItem.FigureBase = [ChartFigureBase].Circle;] |
|                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PyramidItem.FigureBase = [ChartFigureBase].Square;] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Setting FigureBase For Funnel Chart]                                                                                                                     |
|                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Circle;]  |
|                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Square;]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [\' Setting FigureBase For Pyramid]                                                                                                                    |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PyramidItem.FigureBase=[ChartFigureBase].Circle]  |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PyramidItem.FigureBase=[ChartFigureBase].Square]  |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                          |
| [\' Setting FigureBase For Funnel Chart]                                                                                                               |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Circle] |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Square] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Pyramid Chart

[] 

{border="0"}

**[]** 

Figure 124: Pyramid Chart with Figure Base set to \"Circle\"

**[]** 

{border="0"}

**[]** 

Figure 125: Pyramid Chart with Figure Base set to \"Square\"

**[]** 

Funnel Chart

[] 

{border="0"}

[] 

Figure 126: Funnel Chart with Figure Base set to \"Circle\"

**[]** 

{border="0"}

**[]** 

Figure 127: Funnel Chart with Figure Base set to \"Square\"

**[]** 

See Also

**[]** 

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p104} 

[]{#related-topics}

