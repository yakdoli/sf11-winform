---
title: beforesplashevent1.md
original_path: WinForms_Docs/99_Uncategorized/beforesplashevent1.md
created_at: 2025-08-05
---






##### BeforeSplash Event {#beforesplash-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

When the application is loaded and before the splash screen is displayed, the **BeforeSplash** event will be triggered.

 

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

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                              |
| [// Handle the BeforeSplash event.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                              |
| [this][.splashPanel1.BeforeSplash +=[new] CancelEventHandler(splashPanel1_BeforeSplash);]                                                                                                          |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| [private][ [void] splashPanel1_BeforeSplash([object] sender, System.ComponentModel.[CancelEventArgs] e)]                                                 |
|                                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                              |
| [string][ eventlogmessage = [String].Format([\"Event: {0} Object: {1}\\r\\n\"], [\"BeforeSplash\"], (([Control])sender).Name);] |
|                                                                                                                                                                                                                                                                                                              |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| [// To cancel this event, give the below code.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                              |
| [args.Cancel = [true];]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Handle the BeforeSplash event.]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [AddHandler][ [Me].splashPanel1.BeforeSplash, [AddressOf] splashPanel1_BeforeSplash]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] splashPanel1_BeforeSplash([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs) [Handles] splashPanel1.BeforeSplash] |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"BeforeSplash\", ([CType](sender, Control)).Name)]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [If][ [Me].InvokeRequired [Then]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.Invoke([New] SetStringDelegate([AddressOf] OutputText), [New] [Object]() { eventlogmessage })]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Else]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [OutputText(eventlogmessage)]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [If]]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' To cancel this event, give the below code.]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [args.Cancel = [True]]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

