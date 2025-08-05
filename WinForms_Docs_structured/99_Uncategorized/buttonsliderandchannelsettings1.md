---
title: buttonsliderandchannelsettings1.md
original_path: WinForms_Docs/99_Uncategorized/buttonsliderandchannelsettings1.md
created_at: 2025-08-05
---






##### Button, Slider and Channel Settings {#button-slider-and-channel-settings style="tab-stops: 0pt"}

[] 

The properties which controls the size of various components of the TrackBarEx are as follows.

[] 


  -------------------- ------------------------------------------------------------------
  Property             Description
  IncreaseButtonSize   Specifies the size of Increase button. Default value is (18, 18)
  DecreaseButtonSize   Specifies the size of Decrease button. Default value is (18, 18)
  SliderSize           Specifies the size of the slider. Default value is (11, 14).
  ChannelHeight        Specifies the height of the channel. Default value is 4.
  -------------------- ------------------------------------------------------------------


[] 

Button Appearance

[] 

The below properties will let you control the appearance of the Increase, Decrease and slider buttons.

[] 


  ------------------------ ---------------------------------------------------------------------------
  []{#p1192}Property       Description
  ShowButton               Specifies whether to show the Increase and Decrease buttons.
  ButtonColor              Sets the color for the buttons and the slider.
  HighlightedButtonColor   Sets the color for the buttons and the slider, when they are highlighted.
  PushedButtonEndColor     Sets the color of the buttons and the slider, when they are pushed.
  ------------------------ ---------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [this][.trackBarEx1.ShowButtons = [true];]                                      |
|                                                                                                                                                                                           |
| [this][.trackBarEx1.ButtonColor = System.Drawing.[Color].DodgerBlue;]           |
|                                                                                                                                                                                           |
| [this][.trackBarEx1.HighlightedButtonColor = System.Drawing.[Color].AliceBlue;] |
|                                                                                                                                                                                           |
| [this][.trackBarEx1.PushedButtonEndColor = System.Drawing.[Color].OrangeRed;]   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                             |
|                                                                                                                                                                 |
| [Me][.trackBarEx1.ShowButtons = [True] ]              |
|                                                                                                                                                                 |
| [Me][.trackBarEx1.ButtonColor = System.Drawing.Color.DodgerBlue ]          |
|                                                                                                                                                                 |
| [Me][.trackBarEx1.HighlightedButtonColor = System.Drawing.Color.AliceBlue] |
|                                                                                                                                                                 |
| [Me][.trackBarEx1.PushedButtonEndColor = System.Drawing.Color.OrangeRed]   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

              Figure 1437: ButtonColor = \"DodgerBlue\"; HighlightedButtonColor = \"AliceBlue\"

[] 

{border="0"}

[] 

Figure 1438: PushedButtonEndColor = \"OrangeRed\"

 

 

 

 

[]{#related-topics}

