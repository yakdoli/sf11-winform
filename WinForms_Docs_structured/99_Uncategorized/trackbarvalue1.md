---
title: trackbarvalue1.md
original_path: WinForms_Docs/99_Uncategorized/trackbarvalue1.md
created_at: 2025-08-05
---






##### TrackBar Value {#trackbar-value style="tab-stops: 0pt"}

[] 

The TrackBarEx control slides between the minimum and maximum values, which are specified in **Minimum** and **Maximum** properties. The properties with description are listed in the below table.

[] 


  -------------- -----------------------------------------------------------------------------------
  Property       Description
  Minimum        Specifies the minimum value of the trackbar. Default is 10.
  Maximum        Specifies the maximum value of the trackbar. Default is 20.
  Value          Specifies the value of the trackbar position. i.e, slider position. Default is 5.
  SmallChange    Specifies the small change of Trackbar value. Default is 1.
  LargeChange    Specifies the large change of Trackbar value. Default is 5.
  TimeInterval   Specifies the interval for the timer. Default is 100.
  -------------- -----------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [this][.trackBarEx1.Minimum = 10;]                                             |
|                                                                                                                                                                     |
| [this][.trackBarEx1.Maximum = 25;]                                             |
|                                                                                                                                                                     |
| [this][.trackBarEx1.Value = 5;]                                                |
|                                                                                                                                                                     |
| [this][.trackBarEx1.SmallChange = 5;]                                          |
|                                                                                                                                                                     |
| [this][.trackBarEx1.LargeChange = 15;]                                         |
|                                                                                                                                                                     |
| [this][.trackBarEx1.TimerInterval = 50;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                              |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.Minimum = 10]                                             |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.Maximum = 30]                                             |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.Value = 5]                                                |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.SmallChange = 5]                                          |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.LargeChange = 15]                                         |
|                                                                                                                                                                  |
| [Me][.trackBarEx1.TimerInterval = 50][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following are the methods for the TrackBarEx control which gives the respective results based on SmallChange and LargeChange properties.[]{#p1194}

[] 


  --------------- ----------------------------------------------------------------------------
  Methods         Description
  LargeIncrease   Increases the value by large change specified in **LargeChange** property.
  LargeDecrease   Decreases the value by large change specified in **LargeChange** property.
  SmallDecrease   Decreases the value by small change specified in **SmallChange** property.
  SmallIncrease   Increases the value by small change specified in **SmallChange** property.
  --------------- ----------------------------------------------------------------------------


 

[]{#related-topics}

