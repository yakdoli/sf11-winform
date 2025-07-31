---
title: throughcode53.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode53.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The following code illustrates the creation of RangeSlider.[]{#p1084}

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                                |
|                                                                                                                                                                                           |
| [RangeSlider][ rangeSlider = [new] [RangeSlider]();] |
|                                                                                                                                                                                           |
| [rangeSlider.Maximum = 20;]                                                                                                                           |
|                                                                                                                                                                                           |
| [rangeSlider.Minimum = 0;]                                                                                                                            |
|                                                                                                                                                                                           |
| [rangeSlider.SliderMax = 15;]                                                                                                                         |
|                                                                                                                                                                                           |
| [rangeSlider.SliderMin = 5;]                                                                                                                          |
|                                                                                                                                                                                           |
| [rangeSlider.RangeColor = [Color].Brown;]                                                                                     |
|                                                                                                                                                                                           |
| [rangeSlider.ChannelColor = [Color].DarkGray;]                                                                                |
|                                                                                                                                                                                           |
| [rangeSlider.ChannelHeight = 5;]                                                                                                                      |
|                                                                                                                                                                                           |
| [rangeSlider.HighlightedThumbColor = [Color].DarkBlue;]                                                                       |
|                                                                                                                                                                                           |
| [rangeSlider.PushedThumbColor = [Color].Crimson;]                                                                             |
|                                                                                                                                                                                           |
| [rangeSlider.ThumbColor = [Color].Aqua;]                                                                                      |
|                                                                                                                                                                                           |
| [rangeSlider.Location = [new] [Point](80, 30);]                                                          |
|                                                                                                                                                                                           |
| [this][.Controls.Add(rangeSlider);][]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the code.

[] 

Output

**[]** 

{border="0"}

***[]*** 

Figure 1266: Range Slider

 

[]{#related-topics}

