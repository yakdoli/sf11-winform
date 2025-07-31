---
title: indexedxvalues.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\indexedxvalues.md
created_at: 2025-07-03
---








  









### Indexed X Values {#indexed-x-values style="tab-stops: 0pt"}

**[]** 

By default points in a series are plotted against their x and y values. However in some cases the x values are meaningless, they simply represent categories, and you do not want to plot the points against such x values. Such an x-axis that ignores the x-values and simply uses the positional value of a point in a series is said to be Indexed.

 

In the figure below, the first chart shows a line chart that is not-indexed while the second chart shows a line chart whose x-axis is indexed.

[] 

{border="0"}

**[]** 

Figure 240: Non-Indexed X Values

**[]** 

{border="0"}

**[]** 

Figure 241: Indexed X Values

**[]** 


{border="0"}Note: Indexing is supported only on the x-axis in Essential Chart.


[] 

You can enable x-axis indexing or categorizing through the **Indexed** property of the Chart as shown below:

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| **[]**                                                                       |
|                                                                                                                                |
| [this][.ChartWebControl1.Indexed = true;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                          |
|                                                                                                                             |
| **[]**                                                                    |
|                                                                                                                             |
| [Me][.ChartWebControl1.Indexed = True] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

The above property automatically affects all the x-axes in the chart.

[] 

You can also optionally customize the labels of the points in such an indexed series as explained in[ ][Chart Labels Customization]{.UGHyperlink}.

[]{#p176} 

 

[]{#related-topics}

