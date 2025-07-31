---
title: howtoaddcustomlegends.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddcustomlegends.md
created_at: 2025-07-03
---








  









## How To Add Custom Legends? {#how-to-add-custom-legends style="tab-stops: 0pt"}

It\'s easy to replace existing, default, legend items with custom items in Chart or Chart Area legends.

[] 

Remember to clear the existing default entries, before adding new custom items. Otherwise, this will result in exceptions. The following lines of code can be used to add items to chart legend.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| []                                                                                                                  |
|                                                                                                                                                         |
| [ChartLegend][ legend = new [ChartLegend]();] |
|                                                                                                                                                         |
| [legend.Items.Clear();]                                                                                             |
|                                                                                                                                                         |
| [legend.Items.Add([\"Legend 1\"]);]                                                         |
|                                                                                                                                                         |
| [legend.Items.Add([\"Legend 2\"]);]                                                         |
|                                                                                                                                                         |
| [legend.Items.Add([\"Legend 3\"]);]                                                         |
|                                                                                                                                                         |
| [Chart1.Legends.Add(legend);]                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 287: Custom Legend Set for the Chart

 

See Also

**[]** 

[]{#p174}[]{.UGHyperlink}

[]{#related-topics}

