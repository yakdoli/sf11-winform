---
title: howtoaddachartheadertoanolaparea.md
original_path: WinForms_Docs/04_Controls/Chart/howtoaddachartheadertoanolaparea.md
created_at: 2025-08-05
---






##### How to add a Chart header to an OlapArea? {#how-to-add-a-chart-header-to-an-olaparea style="tab-stops: 0pt"}

[] 

Chart header is the title of the chart, which is usually displayed at the top center of the ChartArea.  The following illustration displays the Chart header displayed in the chart area:

 

{border="0"}

Figure 27:  An OlapChart with Chart header

[] 

Steps to Add a Chart Header[]

***[]*** 

The steps to add a chart header are as follows:

 

1.   In general, ChartSeries contains the ChartArea instance, which can be used to customize the OlapArea. The following code snippet describes how to add a chart header to an OlapChart:

 

+----------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                           |
|                                                                                                                      |
|                                                                                                                      |
|                                                                                                                      |
| [       this].olapchart1.Series\[0\].Area.Header = [\"Simple report\"]; |
|                                                                                                                      |
|                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                     |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| [      Me].olapchart1.Series(0).Area.Header = [\"Simple report\"] |
|                                                                                                                |
|                                                                                                                |
+----------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The series will be available only after the data is bound to the control. In other words, you can access the series property of the OlapChart only after the call to DataBind() is made.


[] 

See also:

Chart Area Header

[] 

[]{#related-topics}

