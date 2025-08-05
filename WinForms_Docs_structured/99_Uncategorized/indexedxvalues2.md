---
title: indexedxvalues2.md
original_path: WinForms_Docs/99_Uncategorized/indexedxvalues2.md
created_at: 2025-08-05
---








  









### Indexed X Values {#indexed-x-values style="tab-stops: 0pt"}

[]{#p81}[] 

By default, points in a series are plotted against their X and Y values. However in some cases the X values are meaningless, they simply represent categories, and you do not want to plot the points against such X values. Such an X axis that ignores the X-values and simply uses the positional value of a point in a series is said to be Indexed.

 

The below given code snippet could be used to make a series as Indexed.

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

Figure 76: Series.Indexed = \"False\"

**[]** 

{border="0"}

Figure 77: Series.Indexed = \"True\"

[]{#related-topics}

