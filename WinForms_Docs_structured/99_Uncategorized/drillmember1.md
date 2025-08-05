---
title: drillmember1.md
original_path: WinForms_Docs/99_Uncategorized/drillmember1.md
created_at: 2025-08-05
---








  





### Drill Member {#drill-member style="tab-stops: 0pt"}

Drill member is the default drilling type in an OLAP grid. When multiple dimensions are added in an axis, expanding a single cell will expand the corresponding member element across all of its positions.

[] 

Adding Drill Member to an Application

Adding the drill member feature to an application is described in the following code snippet:

 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                              |
| [dataManager.CurrentReport.DrillType = [DrillType].DrillMember;] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                            |
|                                                                                                                             |
| [dataManager.CurrentReport.DrillType = [DrillType].DrillMember] |
+-----------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

