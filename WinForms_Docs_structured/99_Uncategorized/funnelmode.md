---
title: funnelmode.md
original_path: WinForms_Docs/99_Uncategorized/funnelmode.md
created_at: 2025-08-05
---






#### FunnelMode {#funnelmode style="tab-stops: 0pt"}

[] 

Gets or sets the chart funnel mode.

[] 

[] 


+---------------------------------------+--------------------------------------------------------------------------+
| **[]**                                         |
|                                                                                                                  |
| Details                                                                                                          |
+---------------------------------------+--------------------------------------------------------------------------+
| Possible Values                       | YIsWidth - DataPoint y-value controls the radius of the funnel segment.\ |
|                                       | YIsHeight - DataPoint y-value controls the height of the funnel segment. |
+---------------------------------------+--------------------------------------------------------------------------+
| Default Value                         | YIsHeight                                                                |
+---------------------------------------+--------------------------------------------------------------------------+
| 2D / 3D Limitations                   | No                                                                       |
+---------------------------------------+--------------------------------------------------------------------------+
| Applies to Chart Element              | All series                                                               |
+---------------------------------------+--------------------------------------------------------------------------+
| Applies to Chart Types                | Funnel Chart                                                             |
+---------------------------------------+--------------------------------------------------------------------------+


**[]** 

Here is some sample code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.FunnelMode = ChartFunnelMode.YIsHeight;] |
|                                                                                                                                                                                           |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.FunnelMode = ChartFunnelMode.YIsWidth;]  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| **[]**                                                                                                                             |
|                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.FunnelMode = ChartFunnelMode.YIsHeight] |
|                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.FunnelMode = ChartFunnelMode.YIsWidth]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 130: Funnel Chart with FunnelMode as \"Height\"

**[]** 

{border="0"}

**[]** 

Figure 131: Funnel Chart with FunnelMode as \"Width\"

**[]** 

See Also

**[]** 

[Funnel Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p106} 

[]{#related-topics}

