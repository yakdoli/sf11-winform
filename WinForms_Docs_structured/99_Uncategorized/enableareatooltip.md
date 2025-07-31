---
title: enableareatooltip.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enableareatooltip.md
created_at: 2025-07-03
---






#### EnableAreaToolTip {#enableareatooltip style="tab-stops: 0pt"}

 

To display proper tooltip for the Area charts, use the **Series.EnableAreaToolTip** property. When this property is enabled, the series index and the point index will be returned, which will be suitable for the various [PointsToolTipFormats] also.

 

This splits up the region between two points into two parts while hovering the mouse on the region and displays the tooltip with respect to the nearby chart point.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [this][.chartControl1[.Series\[0\].EnableAreaToolTip = ][true][;]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\`

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [Me][.chartControl1.Series(0).[EnableAreaToolTip] = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 123: EnableAreaToolTip = \"True\"

[]{#p97} 

[]{#related-topics}

