---
title: howtoarrangethetabgroupsequallyusingtabbedmdimanager.md
original_path: WinForms_Docs/99_Uncategorized/howtoarrangethetabgroupsequallyusingtabbedmdimanager.md
created_at: 2025-08-05
---






#### How to arrange the Tab groups equally using TabbedMDIManager {#how-to-arrange-the-tab-groups-equally-using-tabbedmdimanager style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

TabbedMDIManager has AdjustTabGroupWeightsEqually() method to arrange the Tabgroups equally.

[] 


  Method                         Description
  ------------------------------ ---------------------------------------
  AdjustTabGroupWeightsEqually   Adjusts the TabGroups weights equally


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [private void][ AddGroupButton_click([object] sender, [EventArgs] e)]                        |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [    ][this][.tabbedMDIManager.TabbedGroups.Add(new TabbedGroup(\"TabGroup2\"));]            |
|                                                                                                                                                                                                                                      |
| [    ][ChildForm][ f = [new] [ChildForm]();] |
|                                                                                                                                                                                                                                      |
| [    ][this][.tabbedMDIManager.TabbedGroups\[\"TabGroup2\"\].AddForm(f);]                    |
|                                                                                                                                                                                                                                      |
| [    ][this][.tabbedMDIManager.AdjustTabGroupWeightsEqually();  ]                            |
|                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] AddGroupButton_click([ByVal] sender [As] [Object], [ByVal] e [As] [EventArgs])] |
|                                                                                                                                                                                                                                                                                                                                             |
| [     ][[Me].tabbedMDIManager.TabbedGroups.Add([New] TabbedGroup(\"TabGroup2\"))]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                             |
| [   [Dim] f [As] [ChildForm] = [New] [ChildForm]()]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [   [Me].tabbedMDIManager.TabbedGroups(\"TabGroup2\").AddForm(f)]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [   [Me].tabbedMDIManager.AdjustTabGroupWeightsEqually()]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p943} 

[]{#related-topics}

