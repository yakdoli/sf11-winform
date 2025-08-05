---
title: renkochart1.md
original_path: WinForms_Docs/04_Controls/Chart/renkochart1.md
created_at: 2025-08-05
---






#### Renko Chart {#renko-chart style="tab-stops: 0pt"}

Renko charting method is thought to have acquired its name from \"renga\", which is the Japanese word for bricks. Renko charts were introduced by Steve Nison. Renko (bricks) are drawn equal in size for a determined amount. A brick is drawn in the direction of the prior move only if the prices move by a minimum amount. If the prices change by the determined amount or more, a new brick is drawn. If the prices change by less than the determined amount (specified by ReversalAmount), the new price is ignored. The default value of the ReversalAmount is 1.

If the new closing price penetrates the previous bricks closing price in the opposite direction a trend reversal highlighted by the change in color of the bricks happens. Use the PriceUpColor to indicate the bullish trend and PriceDownColor to indicate the bearish trend.

Since a Renko chart isolates the underlying trends by filtering out the minor ups and downs, Renko charts are excellent in determining support and resistance levels.                    

Renko charts can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

Chart Details

 


+------------------------------+--------------------------+
| Details                                                 |
+------------------------------+--------------------------+
| Number of Y values per point | 1                        |
+------------------------------+--------------------------+
| Number of Series             | One                      |
+------------------------------+--------------------------+
| Cannot be Combined with      | Pie chart and Bar chart. |
+------------------------------+--------------------------+


[] 

More:







