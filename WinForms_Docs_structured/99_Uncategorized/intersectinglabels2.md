---
title: intersectinglabels2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\intersectinglabels2.md
created_at: 2025-07-03
---






##### Intersecting Labels {#intersecting-labels style="tab-stops: 0pt"}

[]{#p93}[] 

Chart Axis labels may intersect with one another due to the chart dimensions. The charts will, by default render those texts one over the other. The IntersectAction property has some set of actions to avoid this overlapping between axis labels. This also helps to improve the readability. 

 

The ChartLabelIntersectAction type has the five intersect actions such as MultipleRows, Rotate, Hide, Wrap and None. The below table describes the usage of those actions to avoid the overlapping between labels.

 


  ----------------- ---------------------------------------------------------------------
  IntersectAction   Usage
  MultipleRows      Wrap the chart label content to multiple rows to avoid the overlap.
  Rotate            Rotate the axis label on the specific angle to avoid intersection.
  Hide              Hide the axis label to avoid intersection.
  Wrap              Wrap the contents into small portions to avoid intersection.
  None              No action. Axis labels will intersect if this option is set.
  ----------------- ---------------------------------------------------------------------


 

The following are the part of XAML and CS code to set the IntersectAction property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [     \<][syncfusion:ChartAxis][ ][IntersectAction][=][\"[MultipleRows]\"[ ][Header][=]\"[Country Name]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ \</][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                             |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [ChartArea][ area = [new] [ChartArea]();] |
|                                                                                                                                                                          |
| [ChartAxis][ axis = [new] [ChartAxis]();] |
|                                                                                                                                                                          |
| [axis.Header = [\"Country Name\"];]                                                                          |
|                                                                                                                                                                          |
| [axis.IntersectAction = ChartLabelIntersectAction.MultipleRows;]                                                                     |
|                                                                                                                                                                          |
| [area.PrimaryAxis = axis][;]                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following images as the result of various options in IntersectAction property

[] 

{border="0"}

Figure 91: IntersectAction = \"MultipleRows\"

**[]** 

{border="0"}

Figure 92: IntersectAction = \"Rotate\"

**[]** 

{border="0"}

Figure 93: IntersectAction = \"Hide\"

**[]** 

{border="0"}

Figure 94: IntersectAction = \"Wrap\"

 

[]{#p94} 

[]{#related-topics}

