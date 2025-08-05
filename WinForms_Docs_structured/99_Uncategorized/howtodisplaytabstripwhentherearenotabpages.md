---
title: howtodisplaytabstripwhentherearenotabpages.md
original_path: WinForms_Docs/99_Uncategorized/howtodisplaytabstripwhentherearenotabpages.md
created_at: 2025-08-05
---






#### How to Display TabStrip when there are no TabPages {#how-to-display-tabstrip-when-there-are-no-tabpages style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The TabStrip can be made visible even if there are no TabPages added. The TabControlAdv has a **ReserveTabSpace** property which makes the tabstrip visible when set to True and **ReservedSpace** property that is used to specify the height of the tabstrip when the above bool property is enabled.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [//Setting the visibility of tabstrip.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [this][.tabControlAdv1.ReserveTabSpace = ][true][;] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [//Specifying the height of the tabstrip.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [this][.tabControlAdv1.ReservedSpace = 25;]                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| [\'Setting the visibility of tabstrip.]                                                                                                           |
|                                                                                                                                                                                                     |
| [Me][.tabControlAdv1.ReserveTabSpace =  ][True] |
|                                                                                                                                                                                                     |
| []                                                                                                                                                 |
|                                                                                                                                                                                                     |
| [\'Specifying the height of the tabstrip.]                                                                                                        |
|                                                                                                                                                                                                     |
| [Me][.tabControlAdv1.ReservedSpace = 25]                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1081: ReserveTabSpace property enabled for the TabControlAdv

 

 

 

[]{#p891} 

[]{#related-topics}

