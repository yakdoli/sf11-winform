---
title: animationspeedchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\animationspeedchangedevent.md
created_at: 2025-07-03
---






##### AnimationSpeedChanged Event {#animationspeedchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **AnimationSpeed** property is changed. The AnimationSpeed property indicates the animation speed of the marquee style.

 

The event handler receives an argument of type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Specify the speed of animation for the marquee style.]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.AnimationSpeed = 7;]                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Set the IsMarquee property to \'True\' to activate the animation.]                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.IsMarquee = [true];]                                                                                         |
|                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [// Handle the AnimationSpeedChanged event.]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [this][.statusBarAdvPanel1.AnimationSpeedChanged+=[new] [EventHandler](statusBarAdvPanel1_AnimationSpeedChanged);] |
|                                                                                                                                                                                                                                                   |
| [      ]                                                                                                                                                                                                      |
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
| [private][ [void] statusBarAdvPanel1_AnimationSpeedChanged([object] sender, [EventArgs] e)]   |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Console][.WriteLine([\" AnimationSpeedChanged event is raised \"]);]                                                                 |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Specify the speed of animation for the marquee style. ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel1.AnimationSpeed = 7 ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Set the IsMarquee property to \'True\' to activate the animation. ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel1.IsMarquee = [True] ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Handle the AnimationSpeedChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ [Me].statusBarAdvPanel1.AnimationSpeedChanged, [AddressOf] statusBarAdvPanel1_AnimationSpeedChanged ]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Start the animation. ]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] Form1_Load_1([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                             |
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
| [End][ [Sub ]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] statusBarAdvPanel1_AnimationSpeedChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [    Console.WriteLine([\" AnimationSpeedChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

