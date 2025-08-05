---
title: frozencolumnsrows.md
original_path: WinForms_Docs/99_Uncategorized/frozencolumnsrows.md
created_at: 2025-08-05
---








  









### Frozen Columns / Rows {#frozen-columns-rows style="tab-stops: 0pt"}

[] 

GridGroupingControl allows us to lock specific columns / rows so that they will always be visible on the screen, no matter how far you scroll. The columns / rows that are locked are called frozen columns / rows.

[] 

Enable Scrolling

[] 

Essential Grid supports both Horizontal and Vertical scrolling. Specifying the **Width** and **Height** properties for the grid, will display the ScrollBars on the client browser, if necessary.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.GridGroupingControl1.Width = 400;]  |
|                                                                                                                                  |
| [this][.GridGroupingControl1.Height = 500;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                           |
|                                                                                                                               |
| [Me][.GridGroupingControl1.Width = 400]  |
|                                                                                                                               |
| [Me][.GridGroupingControl1.Height = 500] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

Frozen Columns / Rows

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [this][.GridGroupingControl1.FrozenColumns = 5;] |
|                                                                                                                                       |
| [this][.GridGroupingControl1.FrozenRows = 10;]   |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| []                                                                                |
|                                                                                                                                    |
| [Me][.GridGroupingControl1.FrozenColumns = 5] |
|                                                                                                                                    |
| [Me][.GridGroupingControl1.FrozenRows = 10]   |
+------------------------------------------------------------------------------------------------------------------------------------+

[]{#p43} 

[]{#related-topics}

