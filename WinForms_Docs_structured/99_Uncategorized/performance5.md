---
title: performance5.md
original_path: WinForms_Docs/99_Uncategorized/performance5.md
created_at: 2025-08-05
---






#### Performance {#performance style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

[]{#p988}The TreeViewAdv performance can be improved by the following properties and methods.

[] 


  ------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Foreground SettingsTreeViewAdv Properties   Description
  SuspendExpandRecalculate                    Improves performance of the TreeViewAdv with large number of nodes. Generally the time taken to populate 5000 child nodes to a root node takes 10 ms. But after setting the SuspendExpandRecalculate property to true, the time taken for populating is decreased to half of its original time i.e, 5 ms. The unnecessary calling of Recalculate dimensions for the child nodes when the Root nodes are collapsed is also reduced.
  RecalculateExpansion                        Indicates if node dimension calculation should be done on load. By default it is true. This property when set to false, greatly improves the performance of the tree nodes on load.
  ------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 


  --------------------- ---------------------------------------------------------------------------------------------------------------
  TreeViewAdv Methods   Description
  BeginUpdate           Calling this method will stop the redraws of the control and makes the node addition more faster than normal.
  EndUpdate             Resumes the painting of the control suspended by BeginUpdate method.
  --------------------- ---------------------------------------------------------------------------------------------------------------


[] 


{border="0"} Note: While adding more than one node to the treeViewAdv control, calling the BeginUpdate and EndUpdate method will improve performance of the control.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                     |
| [this][.][treeViewAdv1.SuspendExpandRecalculate=[true]; ] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [this][.][treeViewAdv1.BeginUpdate();]                                         |
|                                                                                                                                                                                                                     |
| [//add more number of nodes]                                                                                                                                      |
|                                                                                                                                                                                                                     |
| [\'\...]                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [this][.][treeViewAdv1.EndUpdate();][]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p989}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [Me][.treeViewAdv1.SuspendExpandRecalculate=[True]]                                                |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [Me][.][treeViewAdv1.BeginUpdate()]                                     |
|                                                                                                                                                                                                              |
| [\'add more number of nodes]                                                                                                                               |
|                                                                                                                                                                                                              |
| [\'\...]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [Me][.][treeViewAdv1.EndUpdate()][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

