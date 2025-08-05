---
title: animationstylechangedevent.md
original_path: WinForms_Docs/02_Concepts/animationstylechangedevent.md
created_at: 2025-08-05
---






##### AnimationStyleChanged Event {#animationstylechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **AnimationStyle** property is changed. The AnimationStyle property specifies the style of animation for the marquee style.

 

The event handler receives an argument of type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [// Specify the style of animation for the marquee style.]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.AnimationStyle = Syncfusion.Windows.Forms.Tools.[MarqueeStyle].Slide;]                                       |
|                                                                                                                                                                                                                                                   |
| [// Set the IsMarquee property to \'True\' to activate the animation.]                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.IsMarquee = [true];]                                                                                         |
|                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [// Handle the AnimationSpeedChanged event.]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.AnimationStyleChanged+=[new] [EventHandler](statusBarAdvPanel1_AnimationStyleChanged);] |
|                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [// Start the animation.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [private][ [void] Form1_Load_1([object] sender, [EventArgs] e)]                               |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.StartAnimation();]                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [// Stop the animation.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [private][ [void] button1_Click_1([object] sender, [EventArgs] e)]                            |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.StopAnimation();]                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [private][ [void] statusBarAdvPanel1_AnimationStyleChanged([object] sender, [EventArgs] e)]   |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Console][.WriteLine([\" AnimationStyleChanged event is raised \"]);]                                                                 |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Specify the style of animation for the marquee style. ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel1.AnimationStyle = Syncfusion.Windows.Forms.Tools.MarqueeStyle.Slide ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Set the IsMarquee property to \'True\' to activate the animation. ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel1.IsMarquee = [True] ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Handle the AnimationSpeedChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ [Me].statusBarAdvPanel1.AnimationStyleChanged, [AddressOf] statusBarAdvPanel1_AnimationStyleChanged ]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Start the animation. ]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                               |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [Me].statusBarAdvPanel1.StartAnimation()]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Stop the animation. ]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] button1_Click_1([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                          |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [Me].statusBarAdvPanel1.StopAnimation()]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] statusBarAdvPanel1_AnimationStyleChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [    Console.WriteLine([\" AnimationStyleChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

