---
title: howtopreventreorderingoftabpagesintabbedmdimanagercontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtopreventreorderingoftabpagesintabbedmdimanagercontrol.md
created_at: 2025-07-03
---






#### How to prevent reordering of Tab Pages in TabbedMDIManager Control {#how-to-prevent-reordering-of-tab-pages-in-tabbedmdimanager-control style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The reordering of tab pages can be prevented by implementing the below code snippet. For this derive a class from TabbedMDIManager and override the **MDITabPanel** property and set the **UserMoveTabs** property of MDITabPanel to True.

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                            |
|                                                                                                           |
| []                                                      |
|                                                                                                           |
| [// Derive a class from TabbedMDIManager. ]             |
|                                                                                                           |
| [// Override MDITabPanel property. ]                    |
|                                                                                                           |
| [// Set MDITabPanel\'s UserMoveTabs property to False.] |
|                                                                                                           |
| [tabPanel.UserMoveTabs = [false];]               |
+-----------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                        |
|                                                                                                           |
| []                                                       |
|                                                                                                           |
| [\' Derive a class from TabbedMDIManager. ]             |
|                                                                                                           |
| [\' Override MDITabPanel property. ]                    |
|                                                                                                           |
| [\' Set MDITabPanel\'s UserMoveTabs property to False.] |
|                                                                                                           |
| [tabPanel.UserMoveTabs = [False]]                |
+-----------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p937} 

[]{#related-topics}

