---
title: indexedxvalues4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\indexedxvalues4.md
created_at: 2025-07-03
---








  









### Indexed X Values {#indexed-x-values style="tab-stops: 0pt"}

[]{#p81}[] 

By default, points in a series are plotted against their X and Y values. However, in some cases the X values are meaningless, they simply represent categories, and you do not want to plot the points against such X values. Such an X axis that ignores the X-values and simply uses the positional value of a point in a series, is said to be Indexed.

The following code snippets could be used to make a series as Indexed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion:ChartSeries][ ][IsIndexed][=][\"[True]\"[/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                         |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [ChartSeries][ series = [new] [ChartSeries]();] |
|                                                                                                                                                                                      |
| [series.IsIndexed = [true];]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 73 : Series.Indexed = \"False\"[]

[] 

**[]** 

{border="0"}

 

Figure 74 : Series.Indexed = \"True\"**[]**

**[]** 

[]{#related-topics}

