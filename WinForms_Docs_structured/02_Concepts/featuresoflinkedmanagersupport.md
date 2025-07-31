---
title: featuresoflinkedmanagersupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresoflinkedmanagersupport.md
created_at: 2025-07-03
---






##### Features of Linked Manager Support {#features-of-linked-manager-support style="tab-stops: 0pt"}

###### 3.14.7.7.3.1        Adding DockingManager to TargetManagers List {#adding-dockingmanager-to-targetmanagers-list style="tab-stops: 0pt"}

To add DockingManager to TargetManagers List

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| [//Control from one docking Manager to be transferred to another docking //manager]                   |
|                                                                                                                                                         |
| [//dockingManager1 and dockingManager2 is the instance of DockingManager]                             |
|                                                                                                                                                         |
| [this][.dockingManager1.AddToTargetManagersList(dockingManager2);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| [\'Control from one docking Manager to be transferred to another docking \'manager]                |
|                                                                                                                                                      |
| [\'dockingManager1 and dockingManager2 is the instance of DockingManager]                          |
|                                                                                                                                                      |
| [Me][.dockingManager1.AddToTargetManagersList(dockingManager2)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.14.7.7.3.2        Removing DockingManager from TargetManagers List {#removing-dockingmanager-from-targetmanagers-list style="tab-stops: 0pt"}

To remove DockingManager from TargetManagers List

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| [//Control from one docking Manager to be transferred to another docking //manager]                        |
|                                                                                                                                                              |
| [//dockingManager1 and dockingManager2 is the instance of DockingManager]                                  |
|                                                                                                                                                              |
| [this][.dockingManager1.RemoveFromTargetManagersList(dockingManager2);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| [\'Control from one docking Manager to be transferred to another docking \'manager]                     |
|                                                                                                                                                           |
| [\'dockingManager1 and dockingManager2 is the instance of DockingManager]                               |
|                                                                                                                                                           |
| [Me][.dockingManager1.RemoveFromTargetManagersList(dockingManager2)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

  

 

[]{#related-topics}

