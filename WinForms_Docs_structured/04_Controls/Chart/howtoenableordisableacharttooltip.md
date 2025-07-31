---
title: howtoenableordisableacharttooltip.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoenableordisableacharttooltip.md
created_at: 2025-07-03
---






##### How to enable or disable a chart tool tip? {#how-to-enable-or-disable-a-chart-tool-tip style="tab-stops: 0pt"}

[] 

The tooltip in an OlapChart can be enabled or disabled by setting the ShowToolTip property.

The following code snippet shows how to disable the series tooltip:

[] 

+------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                     |
|                                                                                                |
|                                                                                                |
|                                                                                                |
| [this].olapchart1.Series\[0\].ShowToolTip = [false]; |
|                                                                                                |
|                                                                                                |
+------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                |
|                                                                                           |
|                                                                                           |
|                                                                                           |
| [Me].olapchart1.Series(0).ShowToolTip = [False] |
|                                                                                           |
|                                                                                           |
+-------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

