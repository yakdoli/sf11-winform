---
title: drillmember.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drillmember.md
created_at: 2025-07-03
---








  





### Drill Member {#drill-member style="tab-stops: 0pt"}

The Drill Member is the default drilling type in an OlapChart. When multiple dimensions are added in an axis, expanding a single cell will expand the corresponding member element across all of its positions.

[] 

Adding Drill Member to an Application

 

Adding Drill Member feature to an application is described in the following code snippet:

 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[CS\]]**                                                                             |
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

