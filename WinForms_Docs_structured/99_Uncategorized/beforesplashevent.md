---
title: beforesplashevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\beforesplashevent.md
created_at: 2025-07-03
---






##### BeforeSplash Event {#beforesplash-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

You can handle the BeforeSplash event to process any code just before the splash screen is displayed. For example in the below code, the event logs are recorded and displayed in the textbox.

 

**Event Data**

 

The event handler receives an argument of type **CancelEventArgs** containing data related to this event. The following CancelEventArgs member provides information specific to this event.

[] 


  -------- -------------------------------------------------
  Member   Description
  Cancel   Indicates whether the event should be canceled.
  -------- -------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [// Handle the BeforeSplash event.]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [this][.splashControl1.BeforeSplash += [new] System.ComponentModel.[CancelEventHandler]([this].splashControl1_BeforeSplash);] |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [private][ [void] splashControl1_BeforeSplash([object] sender, System.ComponentModel.[CancelEventArgs] e)]                    |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"BeforeSplash\"], sender.ToString());]  |
|                                                                                                                                                                                                                                                                                   |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [// To cancel this event, give the below code.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                   |
| [e.Cancel = [true];]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Handle the BeforeSplash event.]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [AddHandler][ [Me].splashControl1.BeforeSplash, [AddressOf] [Me].splashControl1_BeforeSplash]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] splashControl1_BeforeSplash([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs) [Handles] splashControl1.BeforeSplash] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"BeforeSplash\", sender.ToString())]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [textBox1.Text = textBox1.Text & eventlogmessage]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' To cancel this event, give the below code.]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

**[]** 

Figure 989: SplashControl Event Logs Recorded

**[]** 

BeforeSplash event is raised when the **BeforeSplashNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm before the splash window is displayed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.splashPanel1.BeforeSplashNotify();] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.splashPanel1.BeforeSplashNotify()] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

