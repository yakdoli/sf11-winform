---
title: drillposition8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drillposition8.md
created_at: 2025-07-03
---








  





### Drill Position {#drill-position style="tab-stops: 0pt"}

The drill position feature enables the user to drill only the current position of a selected member in the OlapReport. This will exclude the drilled data of the selected member in other positions by using an MDX query.

 

Use Case Scenarios

This feature is useful when the objective of analysis is to view the drilled data only in the current position of the selected member.[]

[] 

Adding Drill Position to an Application

Adding the drill position feature to an application is described in the following code snippet:

 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                |
| [dataManager.CurrentReport.DrillType = [DrillType].DrillPosition;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                              |
|                                                                                                                               |
| [dataManager.CurrentReport.DrillType = [DrillType].DrillPosition] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

