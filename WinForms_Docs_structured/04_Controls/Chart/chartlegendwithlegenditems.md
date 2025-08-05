---
title: chartlegendwithlegenditems.md
original_path: WinForms_Docs/04_Controls/Chart/chartlegendwithlegenditems.md
created_at: 2025-08-05
---








  









## Chart Legend with Legend Items {#chart-legend-with-legend-items style="tab-stops: 0pt"}

Essential Chart by default displays a legend with information on each series that has been plotted on the chart.

[] 

{border="0"}

Figure 285: Chart with legend and legend items

[] 

**Legend** - The rectangular region that lists one or more legend items.

**Legend Item** - Represented by an icon or image and a text. This usually gets rendered automatically corresponding to each ChartSeries in the chart. You can also add custom legend items to a legend.

**Symbols** - These refer to the symbols drawn at the data points in a plot. The legend items corresponding to the series can also be rendered with this symbol instead of an icon.

You can turn off the legend by setting the ShowLegend property in the chart to false. The legend instances in the chart are exposed by using the Legends collection. The first entry in this list is considered the \"default legend\" and is exposed by using the Legend property.

More:









