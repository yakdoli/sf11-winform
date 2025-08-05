---
title: pointandfigurechart1.md
original_path: WinForms_Docs/04_Controls/Chart/pointandfigurechart1.md
created_at: 2025-08-05
---






#### Point and Figure Chart {#point-and-figure-chart style="tab-stops: 0pt"}

 

Point and Figure chart is used to identify support levels, resistance levels, and chart patterns. The chart ignores the time factor and concentrates solely on movements in price - a column of Xs or Os may take one day or several weeks to complete. By convention, the first X in a column is plotted one box above the last O in the previous column and the first O in a column is plotted one box below the highest X. 

This is a chart that plots the day-to-day increment and decrement in price. It uses a series of Xs and Os to determine price trends where the Xs represent an upward trend and the Os represent a downward trend. The default value of the ReversalAmount is 1. Use the PriceUpColor to specify the color for the Xs and PriceDownColor to specify the color for the Os.

This chart requires two y values, the high value and the low value for the specified period.                      

Point and Figure chart can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

Chart Details

 


+------------------------------+--------------------------+
| Details                                                 |
+------------------------------+--------------------------+
| Number of Y values per point | 2                        |
+------------------------------+--------------------------+
| Number of Series             | One                      |
+------------------------------+--------------------------+
| Cannot be Combined with      | Pie chart and Bar chart. |
+------------------------------+--------------------------+


[] 

More:







