---
title: splashmouseleaveevent.md
original_path: WinForms_Docs/99_Uncategorized/splashmouseleaveevent.md
created_at: 2025-08-05
---






##### SplashMouseLeave Event {#splashmouseleave-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

When an application with SplashPanel is loaded, the splash screen will be displayed based on the alignment that is set. At this time, when the mouse moves over the SplashPanel and then leaves the SplashPanel, the **SplashMouseLeave** event will be raised. This event will not be triggered after the splash screen is closed.

 

The event handler receives an argument of type **EventArgs** containing data related to this event.

 

You can handle this event by including the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                  |
| [// Handle the SplashMouseLeave event.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                  |
| [this][.splashPanel1.SplashMouseLeave +=[new] EventHandler(splashPanel1_SplashMouseLeave);]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                  |
| [private][ [void] splashPanel1_SplashMouseLeave([object] sender, System.[EventArgs] e)]                                                                      |
|                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashMouseLeave\"], (([Control])sender).Name);] |
|                                                                                                                                                                                                                                                                                                                  |
| [if][ ([this].InvokeRequired)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [this][.Invoke([new] SetStringDelegate(OutputText), [new] [object]\[\] { eventlogmessage });]                                                                |
|                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [else]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [string][ text = eventlogmessage;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [textBox1.Text = textBox1.Text + text;]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Handle the SplashMouseLeave event.]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [AddHandler][ [Me].splashPanel1.SplashMouseLeave, [AddressOf] splashPanel1_SplashMouseLeave]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] splashPanel1_SplashMouseLeave([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] splashPanel1.SplashMouseLeave] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashMouseLeave\", ([CType](sender, Control)).Name)]                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [If][ [Me].InvokeRequired [Then]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.Invoke([New] SetStringDelegate([AddressOf] OutputText), [New] [Object]() { eventlogmessage })]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Else]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [OutputText(eventlogmessage)]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

