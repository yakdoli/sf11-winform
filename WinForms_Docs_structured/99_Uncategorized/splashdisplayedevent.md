---
title: splashdisplayedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splashdisplayedevent.md
created_at: 2025-07-03
---






##### SplashDisplayed Event {#splashdisplayed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The **SplashDisplayed** event is raised after the splash screen is displayed on the screen. For example in the below code, the event logs are recorded and displayed in a textbox.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [// Handle the SplashDisplayed event.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [this][.splashControl1.SplashDisplayed += [new] System.[EventHandler]([this].splashControl1_SplashDisplayed);]                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [private][ [void] splashControl1_SplashDisplayed([object] sender, System.[EventArgs] e)]                                        |
|                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashDisplayed\"], sender.ToString());] |
|                                                                                                                                                                                                                                                                                     |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Handle the SplashDisplayed event.]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [AddHandler][ [Me].splashControl1.SplashDisplayed, [AddressOf] [Me].splashControl1_SplashDisplayed]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] splashControl1_SplashDisplayed([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] splashControl1.SplashDisplayed] |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashDisplayed\", sender.ToString())]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [textBox1.Text = textBox1.Text & eventlogmessage]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 990: SplashControl Event Logs Recorded

[] 

SplashDisplayed**[ ]**event will be triggered when the **SplashDisplayedNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm when the splash window is displayed.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                |
|                                                                                                                                     |
| [this][.splashPanel1.SplashDisplayedNotify();] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [Me][.splashPanel1.SplashDisplayedNotify()] |
+----------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

