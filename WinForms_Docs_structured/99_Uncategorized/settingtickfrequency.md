---
title: settingtickfrequency.md
original_path: WinForms_Docs/99_Uncategorized/settingtickfrequency.md
created_at: 2025-08-05
---






#### Setting Tick Frequency {#setting-tick-frequency style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[]{#p1091} 

The ticks can be placed at required intervals by setting the **TickFrequency** property to required number. For example, if the range is set from 0-100, where minimum is set to 0 and maximum is set to 100, and the **TickFrequency** is set to 20, then Ticks will be placed at positions 0,20,40,..,100.

 

The following example illustrates the same.

[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                             |
|                                                                                                            |
| []                                                                     |
|                                                                                                            |
| [rangeSlider.TickFrequency = 3;][] |
+------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

{border="0"}

***[]*** 

Figure 1280: Tick Frequency set to 3

 

[]{#related-topics}

