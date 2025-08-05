---
title: howtocustomizetheseriesborderproperties.md
original_path: WinForms_Docs/99_Uncategorized/howtocustomizetheseriesborderproperties.md
created_at: 2025-08-05
---






##### How to customize the series border properties? {#how-to-customize-the-series-border-properties style="tab-stops: 0pt"}

[] 

You can customize the thickness of the series border of an OlapChart by using the following code snippet:

 

[] 

+--------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                   |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|        [this].olapchart1.Series\[0\].Stroke = [Brushes].Black;\ |
|        [this].olapchart1.Series\[0\].StrokeThickness = 4;                               |
|                                                                                                              |
|                                                                                                              |
+--------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                |
|                                                                                                           |
|                                                                                                           |
|                                                                                                           |
|           [Me].olapchart1.Series(0).Stroke = [Brushes].Black |
|                                                                                                           |
|           [Me].olapchart1.Series(0).StrokeThickness = 4                              |
|                                                                                                           |
|                                                                                                           |
+-----------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: The behaviour of the series border will vary for different chart types. The following illustration describes them in detail.


**** 

The series border is applied for the first series of a Column chart by using the StrokeThickness property. Notice that the first series element is surrounded with the applied border.

{border="0"}

 

Figure 31: Stroke applied for a single series in a column type chart[]

***[]*** 

Notice the variation. The same series border property is applied for a series in the line chart. Instead of creating a 4 pixel width border it increases the thickness of the particular series line.

[] 

{border="0"}

Figure 32: Stroke property applied for a series in a line chart[]

[] 

Since, you know that the pie chart renders everything in a single series each block in the pie chart known as segments will have the border applied on them. This is described in the following illustration:

{border="0"}

Figure 33: Stroke property applied for a Pie chart[]

[] 

[]{#related-topics}

