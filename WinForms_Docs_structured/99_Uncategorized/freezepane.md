---
title: freezepane.md
original_path: WinForms_Docs/99_Uncategorized/freezepane.md
created_at: 2025-08-05
---






##### Freeze Pane {#freeze-pane style="tab-stops: 0pt"}

[] 

Essential Grid supports MS Excel-like **Freeze Pane** feature. In a large worksheet, it is often required that column or row labels remain in view. This feature enables you to freeze either columns or rows in the Grid, so that they remain visible while you scroll. The number of  rows to be frozen can be specified by using **Model.Rows.FrozenCount** property and the number of columns to be frozen can be specified by using **Model.Cols.FrozenCount** property.

 

The Freeze Pane feature can be enabled for Essential Grid by using the following code:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                                        |
| []                                                                                 |
|                                                                                                                                        |
| [this][.gridControl1.Model.Rows.FrozenCount = 4;] |
|                                                                                                                                        |
| [this][.gridControl1.Model.Cols.FrozenCount = 3;] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                  |
|                                                                                                                                     |
| []                                                                              |
|                                                                                                                                     |
| [Me][.gridControl1.Model.Rows.FrozenCount = 4] |
|                                                                                                                                     |
| [Me][.gridControl1.Model.Cols.FrozenCount = 3] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 


 {border="0"}Note: You can unfreeze the frozen rows/columns by clicking Unfreeze Current Row/Col button on the UI.


[] 

{border="0"}

[] 

*[Figure ][122][: Freeze Pane feature Illustrated]*

 

[]{#p112} 

 

[]{#related-topics}

