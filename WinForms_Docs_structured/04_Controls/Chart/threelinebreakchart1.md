---
title: threelinebreakchart1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\threelinebreakchart1.md
created_at: 2025-07-03
---






#### Three Line Break Chart {#three-line-break-chart style="tab-stops: 0pt"}

 

Three Line Break chart is similar in concept to the Point and Figure charts. The Three Line Break charting method is so-named because of the number of lines typically used. It displays a series of vertical boxes (\"lines\") that are based on changes in the prices. It ignores the passage of time.

The Three Line Break chart looks like a series of rising and falling lines of varying heights. Each new line, like the Xs and Os of a Point and Figure chart, occupies a new column. Based on the closing prices or highs and lows, a new rising line is drawn if the previous high is exceeded and a new falling line is drawn if the price hits a new low. Change in the price trends are highlighted by changing the colors. Use the PriceUpColor to indicate the bullish trend and PriceDownColor to indicate the bearish trend.

The ReversalAmount specifies the threshold amount by which the price should change to begin rendering a new vertical box in the appropriate direction.                      

Three Line Break chart can be created in two ways:

[·      ]Builder

[·      ]ChartModel

[] 

 

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







