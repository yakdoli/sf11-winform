---
title: textsettings2.md
original_path: WinForms_Docs/99_Uncategorized/textsettings2.md
created_at: 2025-08-05
---






##### Text Settings {#text-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

StatusBarAdvPanel has several text settings which will be discussed in this section.

 

The text for the StatusBarAdvPanel can be set through the following property.

[] 


  ---------------------------- ------------------------------------
  StatusBarAdvPanel Property   Description
  Text                         Gets / sets the text of the panel.
  ---------------------------- ------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [this][.statusBarAdvPanel1.Text = [\"StatusBarAdvPanel\"];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [Me][.statusBarAdvPanel1.Text = [\"StatusBarAdvPanel\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The method associated with the above property is given below.

[] 


{border="0"} Note: The GetText() method returns text according to the key state.


[] 

Marquee Settings

[] 

The text inside the control can be made to float in the marquee style by enabling the property given below.

[] 


  ---------------------------- ------------------------------------------------------------------------------
  StatusBarAdvPanel Property   Description
  IsMarquee                    Indicates whether the control uses the marquee style for the displayed text.
  ---------------------------- ------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [this][.statusBarAdvPanel1.IsMarquee = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [Me][.statusBarAdvPanel1.IsMarquee = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Animation Settings

[] 

The animation that has been applied to the text of the StatusBarAdvPanel control can be customized using the properties given below.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------+
| StatusBarAdvPanel Property        | Description                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------+
| AnimationDelay                    | Indicates the delay for the animation of marquee style.                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------+
| AnimationDirection                | Specifies the direction of animation for the marquee style. The options included are as follows. |
|                                   |                                                                                                  |
|                                   |                                                                                                  |
|                                   |                                                                                                  |
|                                   | [·      ]Left and                                                   |
|                                   |                                                                                                  |
|                                   | [·      ]Right.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------+
| AnimationSpeed                    | Indicates the animation speed of the marquee style.                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------+
| AnimationStyle                    | Specifies the style of animation for the marquee style. The options included are as follows.     |
|                                   |                                                                                                  |
|                                   |                                                                                                  |
|                                   |                                                                                                  |
|                                   | [·      ]Scroll,                                                    |
|                                   |                                                                                                  |
|                                   | [·      ]Slide and                                                  |
|                                   |                                                                                                  |
|                                   | [·      ]Alternate.                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------+


[] 


{border="0"} Note:[ ]The IsMarquee property must be set to \'True\' for the animation settings to be visible.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [this][.statusBarAdvPanel1.AnimationDelay = 2;]                                                                                |
|                                                                                                                                                                                                                     |
| [this][.statusBarAdvPanel1.AnimationDirection = Syncfusion.Windows.Forms.Tools.[MarqueeDirection].Right;] |
|                                                                                                                                                                                                                     |
| [this][.statusBarAdvPanel1.AnimationSpeed = 6;]                                                                                |
|                                                                                                                                                                                                                     |
| [this][.statusBarAdvPanel1.AnimationStyle = Syncfusion.Windows.Forms.Tools.[MarqueeStyle].Alternate;]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [Me][.statusBarAdvPanel1.AnimationDelay = 2]                                                                                |
|                                                                                                                                                                                                                  |
| [Me][.statusBarAdvPanel1.AnimationDirection = Syncfusion.Windows.Forms.Tools.[MarqueeDirection].Right] |
|                                                                                                                                                                                                                  |
| [Me][.statusBarAdvPanel1.AnimationSpeed = 6]                                                                                |
|                                                                                                                                                                                                                  |
| [Me][.statusBarAdvPanel1.AnimationStyle = Syncfusion.Windows.Forms.Tools.[MarqueeStyle].Alternate]     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The animation for the text can be enabled and disabled using the methods associated with the above properties. These methods are given below.

[] 


  ---------------- ---------------------------------------------------------------------------------------------------
  Methods          Description
  StartAnimation   Starts the animation for the marquee style.
  StopAnimation    Stops the animation for the marquee style. This will restore the text to it\'s original position.
  ---------------- ---------------------------------------------------------------------------------------------------


[] 

These methods can be called within the below events as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Starts the animation.]                                                                                                                                         |
|                                                                                                                                                                                                                      |
| [private][ [void] Form1_Load([object] sender, [EventArgs] e)]    |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [this][.statusBarAdvPanel1.StartAnimation();]                                                                                   |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Stops the animation.]                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [this][.statusBarAdvPanel1.StopAnimation();]                                                                                    |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [\' Starts the animation.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]    |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.statusBarAdvPanel1.StartAnimation()]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                            |
| [\' Stops the animation.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.statusBarAdvPanel1.StopAnimation()]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

