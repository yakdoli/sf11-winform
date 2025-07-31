---
title: splashclosingevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splashclosingevent1.md
created_at: 2025-07-03
---






##### SplashClosing Event {#splashclosing-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

At run time, after the splash screen is displayed for a specified time and when it is closing, the **SplashClosing** event will be triggered.

 

**Event Data**

 

The event handler receives an argument of type **CancelEventArgs** containing data related to this event. The following CancelEventArgs member provides information specific to this event.

[] 


  -------- -------------------------------------------------
  Member   Description
  Cancel   Indicates whether the event should be canceled.
  -------- -------------------------------------------------


[] 

You can handle this event by including the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                               |
| [// Handle the SplashClosing event.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [this][.splashPanel1.SplashClosing +=[new] CancelEventHandler(splashPanel1_SplashClosing);]                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [private][ [void] splashPanel1_SplashClosing([object] sender, Syncfusion.Windows.Forms.Tools.[SplashClosedEventArgs] args)]                               |
|                                                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashClosing\"], (([Control])sender).Name);] |
|                                                                                                                                                                                                                                                                                                               |
| [if][ ([this].InvokeRequired)]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [this][.Invoke([new] SetStringDelegate(OutputText), [new] [object]\[\] { eventlogmessage });]                                                             |
|                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [else]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [OutputText(eventlogmessage);]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [if][([this].Controls.Contains([this].splashPanel1) == [false])]                                                                                          |
|                                                                                                                                                                                                                                                                                                               |
| [this][.Controls.Add([this].splashPanel1);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [this][.splashPanel1.Location = [this].currentPt1;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                               |
| [this][.splashPanel1.Visible = [true];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' Handle the SplashClosing event.]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ [Me].splashPanel1.SplashClosing, [AddressOf] splashPanel1_SplashClosing]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] splashPanel1_SplashClosing([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.SplashClosedEventArgs)]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ eventlogmessage [As] [String] = \[String\].Format([\"Event: {0} Object: {1}\"] & Chr(13) & [\"\"] & Chr(10) & [\"\"], [\"SplashClosing\"], [DirectCast](sender, Control).Name)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [If][ [Me].InvokeRequired [Then]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.Invoke([New] SetStringDelegate(OutputText), [New] [Object]() {eventlogmessage})]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Else]                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [OutputText(eventlogmessage)]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [If][ [Me].Controls.Contains([Me].splashPanel1) = [False] [Then]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.Controls.Add([Me].splashPanel1)]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.splashPanel1.Location = [Me].currentPt1]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.splashPanel1.Visible = [True]]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

