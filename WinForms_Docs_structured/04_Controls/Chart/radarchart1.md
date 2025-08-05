---
title: radarchart1.md
original_path: WinForms_Docs/04_Controls/Chart/radarchart1.md
created_at: 2025-08-05
---








  









### Radar Chart {#radar-chart style="tab-stops: 0pt"}

A Radar chart is the clock face form of a Line chart. It represents each data series as a line around a central point. The X-axis values are plotted at equidistant points around the perimeter of the chart. The Y-axis values are plotted as a radius starting from the center of the graph. Each category has individual Y-axis radiating from the center.

The uses of Radar charts are as follows:

[·      ]Helps compare the aggregate values of a number of data series.

[·      ]Helps display performance data for the actual and ideal performance graphically. Users can distinctively categorize performance as strengths and weaknesses based on Radar charts.

[·      ]Helps display categories that have a natural cyclic order. For example, seasons in a year.

 

Example

 

The following example shows how a Radar chart can be used. The following table provides the data set for the chart:

 


  ------------------------ ----------------------------- ----------------------------
  Organization Budget      Allocated Budget in Dollars   Actual Spending in Dollars
  Sales                    40                            50
  Administration           20                            22
  Information Technology   33                            25
  Customer Support         25                            20
  Development              60                            20
  Marketing                20                            45
  ------------------------ ----------------------------- ----------------------------


 

This example represents two data sets namely the Allocated Budget in Dollars and Actual Spending in Dollars for a category named Organization Budget. You can create two different Chart series on a Radar chart for the data sets. The organization budget values are marked on the X-axis at equidistant points and Y values are marked in a way that it starts from and exceeds the upper limit of both the data sets.

 

{border="0"}

Figure 145: Radar chart

Chart Details

The following table provides details pertaining to the Radar chart:

 


+----------------------------------------+-----------------+
| Details                                                  |
+----------------------------------------+-----------------+
| Number of series of Y values per point | One             |
+----------------------------------------+-----------------+
| Number of Series                       | Two             |
+----------------------------------------+-----------------+
| Cannot be Combined with                | Any other type. |
+----------------------------------------+-----------------+


[] 

More:









