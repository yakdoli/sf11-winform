---
title: darklightpower.md
original_path: WinForms_Docs/99_Uncategorized/darklightpower.md
created_at: 2025-08-05
---






#### DarkLightPower {#darklightpower style="tab-stops: 0pt"}

[] 

Gets or sets the intensity of the dark and light colors used in DarkLight color mode.

[] 


+--------------------------+--------------------------------+
| Details                                                   |
+--------------------------+--------------------------------+
| Possible Values          | Ranges from 0 to 255 bytes     |
+--------------------------+--------------------------------+
| Default Value            | 100                            |
+--------------------------+--------------------------------+
| 2D / 3D Limitations      | No                             |
+--------------------------+--------------------------------+
| Applies to Chart Element | All series                     |
+--------------------------+--------------------------------+
| Applies to Chart Types   | Renko Chart (Financial Charts) |
+--------------------------+--------------------------------+


**[]** 

Here is some sample code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [// Setting ColorsMode as DarkLight]                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FinancialItem.ColorsMode = [ChartFinancialColorMode].DarkLight;] |
|                                                                                                                                                                                                                             |
| [// Setting the power value of the darklight]                                                                                                                             |
|                                                                                                                                                                                                                             |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FinancialItem.DarkLightPower = 200;]                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [\' Setting ColorsMode as DarkLight]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FinancialItem.ColorsMode =[ ][ChartFinancialColorMode][.]DarkLight] |
|                                                                                                                                                                                                                                                                      |
| [\' Setting the power value of the darklight]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FinancialItem.DarkLightPower = 200]                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Renko Chart with \"DarkLightPower as 200\"

**[]** 

**[See Also]**

[] 

[]{.UGHyperlink}

[]{#p88} 

[]{#related-topics}

