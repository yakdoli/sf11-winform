---
title: kagichart1.md
original_path: WinForms_Docs/04_Controls/Chart/kagichart1.md
created_at: 2025-08-05
---






#### Kagi Chart {#kagi-chart style="tab-stops: 0pt"}

 

Kagi charts are a Japanese invention and date since the late 1870\'s but were popularized in the western world by Steven Nison. They contain a series of connecting vertical lines where the thickness and direction of the lines depend on the price. If the closing prices continue to move in the direction of the prior vertical Kagi line, then that line is extended. However, if the closing price reverses by a pre-determined \"reversal\" amount, a new Kagi line is drawn in the next column in the opposite direction.

The penetration of a prior column\'s high or low, by the latest closing price, alters the colors of the lines. These colors depict either a bullish or bearish pattern. Use the PriceUpColor and PriceDownColor properties to specify the colors for these two patterns. The wider the columns, the stronger the pattern.

Kagi chart can be created through two ways:

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


More:







