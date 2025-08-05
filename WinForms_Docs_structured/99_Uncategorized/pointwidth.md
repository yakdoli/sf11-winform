---
title: pointwidth.md
original_path: WinForms_Docs/99_Uncategorized/pointwidth.md
created_at: 2025-08-05
---






#### PointWidth {#pointwidth style="tab-stops: 0pt"}

**[]** 

Sets the width of this point relative to the total width available. It is very useful to render series that overlap.

[] 


+---------------------------------------+---------------------------------------+
| **[]**      |
|                                                                               |
| Details                                                                       |
+---------------------------------------+---------------------------------------+
| Possible Values                       | 0.0F to 1.0F                          |
+---------------------------------------+---------------------------------------+
| Default Value                         | 1.0F                                  |
+---------------------------------------+---------------------------------------+
| 2D / 3D Limitations                   | No                                    |
+---------------------------------------+---------------------------------------+
| Applies to Chart Element              | Any Series                            |
+---------------------------------------+---------------------------------------+
| Applies to Chart Types                | Gantt Chart                           |
+---------------------------------------+---------------------------------------+


**[]** 

Here is a code snippet using PointWidth in Gantt Chart.

[] 

Series Wide Setting

[] 

+-------------------------------------------------------------------------------------------+
| **[\[C#\]]**                            |
|                                                                                           |
| **[]**                                  |
|                                                                                           |
| [ganttSeries.Style.PointWidth = 0.25f;] |
+-------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| **[]**                                                                                            |
|                                                                                                                                                     |
| [Private][ ganttSeries.Style.PointWidth = 0.25f] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 170: Chart with default PointWidth

**[]** 

{border="0"}

**[]** 

Figure 171: Chart with PointWidth set to \"0.25f\"

**[]** 

Specific Data Point Setting

**[]** 

You can also set the PointWidth for specific points using **Series.Styles\[0\].PointWidth** for the first data point, **Series.Styles\[1\].PointWidth** for the second data point and so on.

[] 

+-------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                  |
|                                                                                                 |
| **[]**                                        |
|                                                                                                 |
| [ganttSeries.Styles\[0\].PointWidth = 0.25f;] |
|                                                                                                 |
| [ganttSeries.Styles\[1\].PointWidth = 0.5f;]  |
+-------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [Private][ ganttSeries.Styles(0).PointWidth = 0.25f] |
|                                                                                                                                                         |
| [Private][ ganttSeries.Styles(1).PointWidth = 0.5f]  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[Gantt Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p133} 

[]{#related-topics}

