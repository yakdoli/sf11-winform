---
title: splashclosedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splashclosedevent.md
created_at: 2025-07-03
---






##### SplashClosed Event {#splashclosed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The SplashClosed event is raised after the splash screen is closed. For example in the below code, the event logs are recorded and displayed in a textbox.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [// Handle the SplashClosed event.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [this][.splashControl1.SplashClosed += [new] System.[EventHandler]([this].splashControl1_SplashClosed);]                     |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                  |
| [private][ [void] splashControl1_SplashClosed([object] sender, System.[EventArgs] e)]                                        |
|                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashClosed\"], sender.ToString());] |
|                                                                                                                                                                                                                                                                                  |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Handle the SplashClosed event.]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [AddHandler][ [Me].splashControl1.SplashClosed, [AddressOf] [Me].splashControl1_SplashClosed]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] splashControl1_SplashClosed([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] splashControl1.SplashClosed] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashClosed\", sender.ToString())]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [textBox1.Text = textBox1.Text & eventlogmessage]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 992: SplashControl Event Logs Recorded

[] 

SplashClosed**[ ]**event is raised when the **SplashClosedNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm when the splash window is closed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.splashPanel1.SplashClosedNotify();] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.splashPanel1.SplashClosedNotify()] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

