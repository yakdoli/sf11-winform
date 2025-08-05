---
title: splashclosingevent.md
original_path: WinForms_Docs/99_Uncategorized/splashclosingevent.md
created_at: 2025-08-05
---






##### SplashClosing Event {#splashclosing-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The **SplashClosing** event is raised when the splash screen is closing. For example in the below code, the event logs are recorded and displayed in a textbox.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [// Handle the SplashClosing event.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [this][.splashControl1.SplashClosing +=[new] [CancelEventHandler](splashControl1_SplashClosing);]                                                  |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [private][ [void] splashControl1_SplashClosing([object] sender, System.ComponentModel.[CancelEventArgs] e)]                   |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"SplashClosing\"], sender.ToString());] |
|                                                                                                                                                                                                                                                                                   |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Handle the SplashClosing event.]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [AddHandler][ [Me].splashControl1.SplashClosing, [AddressOf] splashControl1_SplashClosing]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] splashControl1_SplashClosing([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs) [Handles] splashControl1.SplashClosing] |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashClosing\", sender.ToString())]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [textBox1.Text = textBox1.Text & eventlogmessage]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 991: SplashControl Event Logs Recorded

[] 

SplashClosing event is raised when the **SplashClosingNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm when the splash window is closing.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                |
|                                                                                                                                     |
| [this][.splashControl1.SplashClosingNotify();] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [Me][.splashControl1.SplashClosingNotify()] |
+----------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

