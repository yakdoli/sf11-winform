---
title: splashclosedevent1.md
original_path: WinForms_Docs/99_Uncategorized/splashclosedevent1.md
created_at: 2025-08-05
---






##### SplashClosed Event {#splashclosed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

At run time, after the splash screen is displayed for a specified time and when it is closed, the **SplashClosed** event will be triggered.

 

**Event Data**

 

The event handler receives an argument of type **SplashClosedEventArgs** containing data related to this event. The following SplashClosedEventArgs member provides information specific to this event.

[] 


  ----------------- ---------------------------------------------------------------------------
  Member            Description
  SplashCloseType   Returns the value which indicates the way in which the splash was closed.
  ----------------- ---------------------------------------------------------------------------


[] 

You can handle this event by including the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                               |
| [// Handle the SplashClosed event.]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [this][.splashPanel1.SplashClosed +=[new] SplashClosedEventHandler(splashPanel1_SplashClosed);]                                                                                                     |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [private][ [void] splashPanel1_SplashClosed([object] sender, Syncfusion.Windows.Forms.Tools.[SplashClosedEventArgs] args)]                                |
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
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [// Returns the SplashCloseType value indicating the way in which the splash was closed.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                               |
| [args.SplashCloseType.ToString();]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Handle the SplashClosed event.]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [AddHandler][ [Me].splashPanel1.SplashClosed, [AddressOf] splashPanel1_SplashClosed]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] splashPanel1_SplashClosed([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.SplashClosedEventArgs) [Handles] splashPanel1.SplashClosed] |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ eventlogmessage [As] [String] = [String].Format(\"Event: {0} Object: {1}\" & Constants.vbCrLf, \"SplashClosing\", ([CType](sender, Control)).Name)]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [If][ [Me].InvokeRequired [Then]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.Invoke([New] SetStringDelegate([AddressOf] OutputText), [New] [Object]() { eventlogmessage })]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Else]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [OutputText(eventlogmessage)]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [If][ [Me].Controls.Contains([Me].splashPanel1) = [False] [Then]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.Controls.Add([Me].splashPanel1)]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.splashPanel1.Location = [Me].currentPt1]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.splashPanel1.Visible = [True]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Returns the SplashCloseType value indicating the way in which the splash was closed.]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [args.SplashCloseType.ToString()]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

SplashClosed**[ ]**event is raised when the **SplashFormClosedNotify()** method is called. This method is an implementation of the ISplashWrapperFormListener for receiving notification from the SplashWrapperForm when the splash window is closed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                      |
| [this][.splashPanel1.SplashFormClosedNotify();] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [Me][.splashPanel1.SplashFormClosedNotify()] |
+-----------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

