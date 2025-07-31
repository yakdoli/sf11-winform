---
title: realtime.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\realtime.md
created_at: 2025-07-03
---








  









## Realtime {#realtime style="tab-stops: 0pt"}

[] 

Essential Chart is optimized to deal with real time data. It can work with both huge and real time data and render a smooth and dynamic chart using any of the several available chart types.

Essentially, this involves updating the chart\'s data points list and optionally updating the chart axis ranges if the default ranges are not user-friendly.

While you can use the **ChartSeries.Points** to add new data points to the existing list, for best performance it\'s recommended to implement your own \"model\" to store the data points in real-time scenarios.

 

A sample application that illustrates a real world scenario, is distributed along with the Essential Chart installation and can be found at:

**Sample Location:** \"\<sample installation location\>\\Syncfusion\\EssentialStudio***\\Version Number***\\Web\\chart.web\\Samples\\3.5\\Real-time\\LiveChart\"

[]{#p215} 

[]{#related-topics}

