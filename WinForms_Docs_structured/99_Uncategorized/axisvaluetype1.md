---
title: axisvaluetype1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\axisvaluetype1.md
created_at: 2025-07-03
---








  









### Axis Value Type {#axis-value-type style="tab-stops: 0pt"}

 

You can set the value type for an axis using **Axes.ValueType** property. You can set any of the following value types of which the default is **double**.

 

[·      ]double

[·      ]datetime

[·      ]logarithmic

 

If you set the ValueType to \'Logarithmic\', then you need to specify the log base for the axis using **Axes.LogBase** property. The default value of LogBase is 10.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                |
|                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.ValueType = [ChartValueType].Logarithmic;] |
|                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.LogBase = 3;]                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[Axis Range and Intervals]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p178} 

[]{#related-topics}

