---
title: tickplacement.md
original_path: WinForms_Docs/99_Uncategorized/tickplacement.md
created_at: 2025-08-05
---






#### Tick Placement {#tick-placement style="tab-stops: 0pt"}

[] 

The **TickPlacement** property specifies the placement of Ticks and Labels around the control. The position can be specified:

[] 

[·      ]Top or Down for Horizontal orientation

[·      ]Left or Right for vertical orientation

[·      ]Both or None for both the orientations

[] 

The following code snippets illustrate this:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"Both\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"None\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"Top\"]                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Orientation][=\"Horizontal\"][ [ TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"Down\"]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Orientation][=\"Horizontal\"][ [ TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"Left\"]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Orientation][=\"Vertical\"][ [ TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][RangeSliderControl][ x][:][Name][=\"rangeSlider\"][ Range][=\"20,60\"][ TickPlacement][=\"Right\"]                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Orientation][=\"Vertical\"][ [ TickFrequency][=\"20\"\>\</][Syncfusion][:][RangeSliderControl][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [RangeSliderControl][ RangeSlider = [new] [RangeSliderControl]();] |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].Both;]                                                                                                         |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].None;]                                                                                                         |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].Left;]                                                                                                         |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].Right;]                                                                                                        |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].Top;]                                                                                                          |
|                                                                                                                                                                                                                                         |
| [RangeSlider.TickPlacement = [Tickplacement].Down;]                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

[] 

Figure 925: Range Slider with TickPlacement set to None

***[]*** 

***[]*** 

{border="0"}

***[]*** 

Figure 926: Range Slider with TickPlacement set to Top

***[]*** 

***[]*** 

{border="0"}

***[]*** 

Figure 927: Range Slider with TickPlacement set to Left

***[]*** 

***[]*** 

{border="0"}

***[]*** 

Figure 928: Range Slider with TickPlacement set to Down

***[]*** 

{border="0"}

***[]*** 

Figure 929: Range Slider with TickPlacement set to Right

 

[]{#p488} 

[]{#related-topics}

