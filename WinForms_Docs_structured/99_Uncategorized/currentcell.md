---
title: currentcell.md
original_path: WinForms_Docs/99_Uncategorized/currentcell.md
created_at: 2025-08-05
---






##### Current Cell {#current-cell style="tab-stops: 0pt"}

[] 

Essential Grid supports MS-Excel like **Current Cell** feature. This feature can be enabled by setting **ExcelLikeCurrentCell** property to *true*. When the user moves the current cell out of a selected range, the range will be cleared. If the user moves the current cell inside a selected range, the range will stay.

 

Current Cell feature can be enabled for Essential Grid by using the following code:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [this][.gridControl1.ExcelLikeCurrentCell = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.gridControl1.ExcelLikeCurrentCell = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][119][: Current Cell]*

 

[]{#p109} 

 

[]{#related-topics}

