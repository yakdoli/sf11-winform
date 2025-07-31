---
title: drillreplace1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drillreplace1.md
created_at: 2025-07-03
---








  









### Drill Replace {#drill-replace style="tab-stops: 0pt"}

Drill Replace displays only the immediate child members and ancestors on drill-down and drill-up respectively.

The following code illustrates how to achieve drill replace support in a current report:

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
|     olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace; |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
| **[\[VB\]]**                      |
|                                                                       |
|     olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace  |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

 

[]{#related-topics}

