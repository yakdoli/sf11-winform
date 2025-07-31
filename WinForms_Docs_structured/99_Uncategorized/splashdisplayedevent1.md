---
title: splashdisplayedevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splashdisplayedevent1.md
created_at: 2025-07-03
---






##### SplashDisplayed Event {#splashdisplayed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

When the application is loaded and when the SplashPanel is displayed, the **SplashDisplayed** event will be raised. The event handler receives an argument of type **EventArgs** containing data related to this event.

 

You can handle this event by including the below code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [// Handle the SplashDisplayed event.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [this][.splashPanel1.SplashDisplayed +=[new] EventHandler(splashPanel1_SplashDisplayed);]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [private][ [void] splashPanel1_SplashDisplayed([object] sender, System.[EventArgs] e)]                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashDisplayed\"], (([Control])sender).Name);] |
|                                                                                                                                                                                                                                                                                                                 |
| [if][ ([this].InvokeRequired)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [this][.Invoke([new] SetStringDelegate(OutputText), [new] [object]\[\] { eventlogmessage });]                                                               |
|                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [else]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the SplashDisplayed event.]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ [Me].splashPanel1.SplashDisplayed, [AddressOf] splashPanel1_SplashDisplayed]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] splashPanel1_SplashDisplayed([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] splashPanel1.SplashDisplayed] |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashDisplayed\", ([CType](sender, Control)).Name)]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ [Me].InvokeRequired [Then]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.Invoke([New] SetStringDelegate([AddressOf] OutputText), [New] [Object]() { eventlogmessage })]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Else]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [OutputText(eventlogmessage)]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

SplashClosed**[ ]**event is raised when the **SplashFormDisplayedNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm when the splash window is displayed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                                         |
| []                                                                                    |
|                                                                                                                                         |
| [this][.splashPanel1.SplashFormDisplayedNotify();] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                   |
|                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                      |
| [Me][.splashPanel1.SplashFormDisplayedNotify()] |
+--------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

