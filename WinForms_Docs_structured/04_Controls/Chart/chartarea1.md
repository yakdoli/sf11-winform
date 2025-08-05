---
title: chartarea1.md
original_path: WinForms_Docs/04_Controls/Chart/chartarea1.md
created_at: 2025-08-05
---








  









## ChartArea {#chartarea style="tab-stops: 0pt"}

Essential Chart comes with chart divide area support, wherein a single ChartArea can be divided into equal squares to display more than one chart (pie, funnel, or pyramid). To enable this, the ChartArea.DivideArea property should be set to true.

By enabling this property, the following are possible:

[·      ]Retrieve the bounds of each section of the Pie, Funnel, or Pyramid charts.

[·      ]Show the series name as a title for individual sections of a Pie, Funnel, and Pyramid chart types.

[·      ]Draw the Pie series with the same radius.[]

**GetSeriesBounds**() method can be used to get the bounds of the DividedArea when ChartArea.DivideArea is set to true.

[]{#related-topics}

