---
title: groupinglabels.md
original_path: WinForms_Docs/99_Uncategorized/groupinglabels.md
created_at: 2025-08-05
---






#### Grouping Labels {#grouping-labels style="tab-stops: 0pt"}

**[]** 

Another interesting feature that is available is to be able to group a set of adjoining labels and mark them with a new label. For example, grouping the first three months of the year and marking them as Q1 and so on. The following properties will let you do that.

[] 


  ---------------------- ---------------------------------------------------------------------------------------------------------------------
  ChartAxis Properties   Description
  GroupingLabels         Lets you group a range of default labels and provide them a custom name/label.
  DrawTickLabelGrid      Puts the labels within a grid. Though commonly used when in grouping mode, this feature can be used even otherwise.
  ---------------------- ---------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [ChartAxisGroupingLabel][ Q1 = [new] [ChartAxisGroupingLabel]([new] [DoubleRange](1, 3), [\"Q1\"]);] |
|                                                                                                                                                                                                                                                                                                      |
| [Q1.BorderStyle = [ChartAxisGroupingLabelBorderStyle].Rectangle;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                      |
| [Q1.Font = [new] [Font]([\"Arial\"], 10F, [FontStyle].Bold);]                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.PrimaryXAxis.GroupingLabels.Add(Q1);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [ChartAxisGroupingLabel][ Q2 = [new] [ChartAxisGroupingLabel]([new] [DoubleRange](4, 6), [\"Q2\"]);] |
|                                                                                                                                                                                                                                                                                                      |
| [Q2.BorderStyle = [ChartAxisGroupingLabelBorderStyle].Rectangle;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                      |
| [Q2.Font = [new] [Font]([\"Arial\"], 10F, [FontStyle].Bold);]                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.PrimaryXAxis.GroupingLabels.Add(Q2);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.PrimaryXAxis.DrawTickLabelGrid = [true];]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [Dim][ Q1 [As] [New] ChartAxisGroupingLabel([New] DoubleRange(1, 3), [\"Q1\"])] |
|                                                                                                                                                                                                                                                            |
| [Q1.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [Q1.Font = [New] Font([\"Arial\"], 10.0F, FontStyle.Bold)]                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [Me][.ChartWebControl1.PrimaryXAxis.GroupingLabels.Add(Q1)]                                                                                                           |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Dim][ Q2 [As] [New] ChartAxisGroupingLabel([New] DoubleRange(4, 6), [\"Q2\"])] |
|                                                                                                                                                                                                                                                            |
| [Q2.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [Q2.Font = [New] Font([\"Arial\"], 10.0F, FontStyle.Bold)]                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [Me][.ChartWebControl1.PrimaryXAxis.GroupingLabels.Add(Q2)]                                                                                                           |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [Me][.ChartWebControl1.PrimaryXAxis.DrawTickLabelGrid = [True]]                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 256: Q1 and Q2 Grouping Labels with Grids

[]{#p187} 

[]{#related-topics}

