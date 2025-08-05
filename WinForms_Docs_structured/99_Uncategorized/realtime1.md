---
title: realtime1.md
original_path: WinForms_Docs/99_Uncategorized/realtime1.md
created_at: 2025-08-05
---








  









## Realtime {#realtime style="tab-stops: 0pt"}

 

Essential Chart is optimized to deal with real time data. It can work with both huge and real time data and render a smooth and dynamic chart using any of the several available chart types.

 

Essentially, this involves updating the chart\'s data points list and optionally updating the chart axis ranges if the default ranges are not user-friendly.

 

While you can use the **ChartSeries.Points** to add new data points to the existing list, for best performance it\'s recommended to implement your own \"model\" to store the data points in real-time scenarios.

 

A sample application that illustrates this, is distributed along with the Essential Chart installation and can be found at:

 

[Sample Location: \"\<sample installation location\>\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\Real Time\\Chart Recorder\"]{.UGHyperlink}

 

[]{#p215} 

[]{#related-topics}

