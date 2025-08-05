---
title: howtoprotectlinksfromuserselectionmanipulation1.md
original_path: WinForms_Docs/99_Uncategorized/howtoprotectlinksfromuserselectionmanipulation1.md
created_at: 2025-08-05
---








  









## How To Protect Links From User Selection / Manipulation {#how-to-protect-links-from-user-selection-manipulation style="tab-stops: 0pt"}

[] 

You can protect links from user selection / manipulation by making use of the **EditStyle** class. By setting the **Enabled** property of the EditStyle class to *False*, you can disable the selection of a node link.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [//Creating Line connector.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [LineConnector][ conn = [new] [LineConnector]([new] [PointF](1, 1), [new] [PointF](2, 2));] |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [//Disabling selection of the line connector.]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| [conn.EditStyle.Enabled = [false];]                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [\'Creating Line connector.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| [Dim][ conn [As] LineConnector = [New] LineConnector([New] PointF(1, 1), [New] PointF(2, 2))] |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [\'Disabling selection of the line connector.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [conn.EditStyle.Enabled = [False]]                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p97} 

 

[]{#related-topics}

