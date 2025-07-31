---
title: howtoadddifferenticonstomditabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoadddifferenticonstomditabs.md
created_at: 2025-07-03
---






#### How to add different Icons to MDI Tabs {#how-to-add-different-icons-to-mdi-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This can be done programmatically using the below code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [// Derive CustomTabbedMDIManager class from TabbedMDIManager]                                                                               |
|                                                                                                                                                                                                |
| [// to expose the internal TabControlAdv. ]                                                                                                  |
|                                                                                                                                                                                                |
| [// Override the MDITabPanel code function.]                                                                                                 |
|                                                                                                                                                                                                |
| [this][.MdiTabPanel = tabPanel;]                                                                          |
|                                                                                                                                                                                                |
| [// Add the images to the Image List.]                                                                                                       |
|                                                                                                                                                                                                |
| [TabControlAdv tabcontrol = [this].tabbedMdiManager.GetMdiTabPanel() [as] [TabControlAdv];] |
|                                                                                                                                                                                                |
| [tabcontrol.ImageList = [this].imageList1;]                                                                                           |
|                                                                                                                                                                                                |
| [// Assign the images to the child tabs.]                                                                                                    |
|                                                                                                                                                                                                |
| [foreach][ ([TabPageAdv] page [in] tabcontrol.TabPages)]        |
|                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                |
| [page.ImageIndex = index;]                                                                                                                                 |
|                                                                                                                                                                                                |
| [index++;]                                                                                                                                                 |
|                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Derive CustomTabbedMDIManager class from TabbedMDIManager]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                        |
| [\' to expose the internal TabControlAdv. ]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Override the MDITabPanel code function.]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [Me][.MdiTabPanel = tabPanel]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Add the images to the Image List.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [Dim][ tabcontrol [As] TabControlAdv = [CType](IIf([TypeOf] [Me].tabbedMdiManager.GetMdiTabPanel() [Is] TabControlAdv, ] |
|                                                                                                                                                                                                                                                                                                                        |
| [Me][.tabbedMdiManager.GetMdiTabPanel(), [Nothing]), TabControlAdv)]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [tabcontrol.ImageList = [Me].imageList1]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Assign the images to the child tabs.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [For][ [Each] page [As] TabPageAdv [In] tabcontrol.TabPages]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                        |
| [page.ImageIndex = index]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                        |
| [index += 1]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                        |
| [Next][ page]                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p933} 

[]{#related-topics}

