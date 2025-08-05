---
title: drillposition7.md
original_path: WinForms_Docs/99_Uncategorized/drillposition7.md
created_at: 2025-08-05
---








  





### Drill Position {#drill-position style="tab-stops: 0pt"}

Drill position feature enables the user to drill only the current position of a selected member in the OlapReport. This excludes the drilled data of the selected member in other positions by using MDX query.

 

Use Case Scenarios

This feature is useful when the objective of analysis is to view the drilled data only in current position of selected member.[]

[] 

Adding Drill Position to an Application

 

Adding Drill Position feature to an application is described in the following code snippet:

 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[CS\]]**                                                                               |
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

