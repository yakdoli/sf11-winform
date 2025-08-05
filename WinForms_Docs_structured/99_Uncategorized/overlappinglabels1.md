---
title: overlappinglabels1.md
original_path: WinForms_Docs/99_Uncategorized/overlappinglabels1.md
created_at: 2025-08-05
---






#### []{#p92}Overlapping Labels {#overlapping-labels style="tab-stops: 0pt"}

 

This section elaborates on the various features available in Chart, which can avoid overlapping of axis labels. It has the following sections:

**[]** 

[[·      ][Intersecting Labels]]{.UGHyperlink}

[[[·      ][Edge Labels Drawing Modes]]]{.UGHyperlink}

[[[·      ][Hide Partial Labels]]]{.UGHyperlink}

[[[·      ][Label Rotate Angle]]]{.UGHyperlink}

[]{#_Intersecting_Labels}[[[·      ]]Intersecting Labels]{.UGHyperlink}

[]{#p93}[] 

Chart Axis labels may intersect with one another due to chart dimensions. The chart will, by default, render those texts one over the other. The IntersectAction property has some set of actions in order to avoid this overlapping between axis labels. This also helps to improve the readability. 

The ChartLabelIntersectAction type has the five intersect actions such as MultipleRows, Rotate, Hide, Wrap and None. The following table describes the usage of those actions to avoid the overlapping between labels.

[] 


  ----------------- ---------------------------------------------------------------------
  IntersectAction   Usage
  MultipleRows      Wrap the chart label content to multiple rows to avoid the overlap.
  Rotate            Rotate the axis label on the specific angle to avoid intersection.
  Hide              Hide the axis label to avoid intersection.
  Wrap              Wrap the contents into small portions to avoid intersection.
  None              No action. Axis labels will intersect if this option is set.
  ----------------- ---------------------------------------------------------------------


[] 

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

The following images are the result of various options in IntersectAction property.

[] 

{border="0"}

 

Figure 87 : IntersectAction = \"MultipleRows\"[]

[] 

**[]** 

{border="0"}

 

Figure 88 : IntersectAction = \"Rotate\"**[]**

**[]** 

**[]** 

{border="0"}

 

Figure 89 : IntersectAction = \"Hide\"**[]**

**[]** 

**[]** 

{border="0"}

 

Figure 90 : IntersectAction = \"Wrap\"**[]**

[]{#p94} 

More:









