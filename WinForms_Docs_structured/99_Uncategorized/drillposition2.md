---
title: drillposition2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drillposition2.md
created_at: 2025-07-03
---








  









### Drill Position {#drill-position style="tab-stops: 0pt"}

Drill position enables the user to drill the current position of a selected member in the OlapReport. This will exclude the drilled data of the selected member in other positions by using MDX query.

The following code illustrates how to achieve drill position support in current report:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [olapDataManager.CurrentReport.DrillType = ][DrillType][.DrillPosition;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [olapDataManager.CurrentReport.DrillType = ][DrillType][.DrillPosition][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

