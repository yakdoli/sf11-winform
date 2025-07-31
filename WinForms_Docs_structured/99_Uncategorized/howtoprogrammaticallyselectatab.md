---
title: howtoprogrammaticallyselectatab.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoprogrammaticallyselectatab.md
created_at: 2025-07-03
---






#### How to programmatically select a Tab {#how-to-programmatically-select-a-tab style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

\
The following code snippet illustrates the ways to select a Tab programmatically.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                    |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [//Select Second Tab.]                                                                                            |
|                                                                                                                                                                     |
| [this][.tabControlAdv1.SelectedTab = [this].tabPageAdv2;] |
|                                                                                                                                                                     |
| [or]                                                                                                                            |
|                                                                                                                                                                     |
| [//Select Second Tab.]                                                                                            |
|                                                                                                                                                                     |
| [this][.tabControlAdv1.SelectedIndex= 1;]                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] TabControlAdv1_SelectedIndexChanged([ByVal] sender [As] System.Object, [ByVal] e [As] System.EventArgs) [Handles] TabControlAdv1.SelectedIndexChanged] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\'Select Second Tab.]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.tabControlAdv1.SelectedTab = [Me].tabPageAdv2]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [or]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\'Select Second Tab.]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.tabControlAdv1.SelectedIndex = 1]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p898} 

[]{#related-topics}

