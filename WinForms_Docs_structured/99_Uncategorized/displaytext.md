---
title: displaytext.md
original_path: WinForms_Docs/99_Uncategorized/displaytext.md
created_at: 2025-08-05
---






#### DisplayText {#displaytext style="tab-stops: 0pt"}

[] 

Indicates whether a label indicating the data point value should be displayed at the data points.

[] 


+--------------------------+-----------------------+
| Details                                          |
+--------------------------+-----------------------+
| Possible Values          | True, False           |
+--------------------------+-----------------------+
| Default Value            | False                 |
+--------------------------+-----------------------+
| 2D / 3D Limitations      | No                    |
+--------------------------+-----------------------+
| Applies to Chart Element | All series and points |
+--------------------------+-----------------------+
| Applies to Chart Types   | All Chart types       |
+--------------------------+-----------------------+


 

Here is some sample code.

[] 

Series wide setting

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [// Enabling DisplayText]                                                                                                               |
|                                                                                                                                                                                           |
| [this][.ChartWebControl1.Series\[0\].Style.DisplayText = [true];]               |
|                                                                                                                                                                                           |
| [this][.ChartWebControl1.Series\[0\].Style.TextColor = [Color].LightSlateGray;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| **[ \'][ ]**[Enabling DisplayText] |
|                                                                                                                                                                                         |
| [Me][.ChartWebControl1.Series(0).Style.DisplayText = [True]]                  |
|                                                                                                                                                                                         |
| [Me][.ChartWebControl1.Series(0).Style.TextColor = [Color].LightSlateGray]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 109: DisplayText in Pie Chart

**[]** 

{border="0"}

**[]** 

Figure 110: DisplayText in Column Chart

**[]** 

Specific Data Point Setting

**[]** 

To specify text for specific points, use the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [// Enabling DisplayText for the first data point]                                                                                            |
|                                                                                                                                                                                                 |
| [this][.ChartWebControl1.Series\[0\].Styles\[0\].DisplayText = [true];]               |
|                                                                                                                                                                                                 |
| [this][.ChartWebControl1.Series\[0\].Styles\[0\].TextColor = [Color].LightSlateGray;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| **[\']**[Enabling DisplayText for the first data point]                               |
|                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).Styles(0).DisplayText = [True]]               |
|                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series(0).Styles(0).TextColor = [Color].LightSlateGray] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p90} 

[]{#related-topics}

