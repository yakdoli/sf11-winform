---
title: howtoturnoffdefaultpaginginthegridgroupingcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoturnoffdefaultpaginginthegridgroupingcontrol.md
created_at: 2025-07-03
---








  









## How to turn off default paging in the GridGroupingControl {#how-to-turn-off-default-paging-in-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

You can turn off default paging in the GridGroupingControl by either setting the **CurrentPage** property to **0** or by setting the **PageSize** property to **-1**. The following code example illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                 |
|                                                                                                                                     |
| [this][.GridGroupingControl1.PageSize = -1;]   |
|                                                                                                                                     |
| [this][.GridGroupingControl1.CurrentPage = 0;] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [Me][.GridGroupingControl1.PageSize = -1]   |
|                                                                                                                                  |
| [Me][.GridGroupingControl1.CurrentPage = 0] |
+----------------------------------------------------------------------------------------------------------------------------------+

[]{#p128} 

[]{#related-topics}

