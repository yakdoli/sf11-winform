---
title: showaswellashidetheedgelabelsinolapchartaxes.md
original_path: WinForms_Docs/04_Controls/Chart/showaswellashidetheedgelabelsinolapchartaxes.md
created_at: 2025-08-05
---








  









## Show as well as Hide the Edge Labels in OLAP Chart Axes? {#show-as-well-as-hide-the-edge-labels-in-olap-chart-axes style="tab-stops: 0pt"}

In order to show the edge labels clearly, set the EdgeLabelsDrawingMode property to Shift as shown in the following code snippets:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [this][.olapChart1.PrimaryXAxis.EdgeLabelsDrawingMode = [ChartAxisEdgeLabelsDrawingMode].Shift;]                                       |
|                                                                                                                                                                                                                                                     |
| [this][.olapChart1.PrimaryYAxis.EdgeLabelsDrawingMode = [ChartAxisEdgeLabelsDrawingMode].Shift;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                                     |
|                                                                                                                                                                                                            |
| [Me][.olapChart1.PrimaryXAxis.EdgeLabelsDrawingMode = [ChartAxisEdgeLabelsDrawingMode].Shift] |
|                                                                                                                                                                                                            |
| [Me][.olapChart1.PrimaryYAxis.EdgeLabelsDrawingMode = [ChartAxisEdgeLabelsDrawingMode].Shift] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

 

Figure 68: Showing Edge Labels

In order to show the edge labels clearly, set the HidePartialLabels property to true as shown in the following code snippets:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                              |
|                                                                                                                                                                     |
| [this][.olapChart1.ChartArea.HidePartialLabels = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                           |
|                                                                                                                                                                  |
| [Me][.olapChart1.ChartArea.HidePartialLabels = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

 

Figure 69: Hiding Edge Labels

[]{#related-topics}

