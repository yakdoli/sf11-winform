---
title: displaysettings.md
original_path: WinForms_Docs/99_Uncategorized/displaysettings.md
created_at: 2025-08-05
---






##### Display Settings {#display-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The section illustrates the display settings available for the SplashPanel control.

[] 

The SplashPanel can be displayed or hidden according to the needs of the user. It can be displayed at any specified location. The display settings of the SplashPanel control are illustrated through the following methods.

[] 


  ------------------ ------------------------------------------------------
  Methods            Description
  ShowSplash         Displays the SplashPanel.
  HideSplash         Hides the SplashPanel.
  ShowDialogSplash   Displays the SplashPanel as a modal dialog.
  IsShowing          Indicates whether the splash is currently displayed.
  ------------------ ------------------------------------------------------


[] 


[{border="0"}] Note:[ ]The time interval for which the SplashPanel is displayed can be customized using the [Time Interval]{.UGHyperlink} settings provided in the SplashPanel control.


[] 

The above methods are explained below in detail.

 

**ShowSplash()** - This method is used to display the SplashPanel at run time.

 

The parameters discussed for the ShowSplash() method are as follows.

[] 


  -------------- ------------------------------------------------------------------------------
  Parameters     Description
  Location       Indicates the point in screen coordinates. The value can be \'Point.Empty\'.
  OwnerForm      Indicates the form that will embed the splash form.
  DisableOwner   Indicates whether the owner form is to be disabled.
  -------------- ------------------------------------------------------------------------------


 

When the SplashPanel is getting displayed, the owner form will be disabled when the DisableOwner parameter is passed as \'True\'. You can assign any form as the owner form.

 

The below code snippet will display the SplashPanel at the specified location with the owner form being disabled. The location will be effective only when the **DesktopAlignment** property is set as \'Custom\'.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [Form2][ f2 = [new] [Form2]();]                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [// To display the SplashPanel call the ShowSplash() method.]                                                                                                            |
|                                                                                                                                                                                                                            |
| [this][.splashPanel1.ShowSplash([new] [Point](100, 100), f2, [true]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [Private][ f2 [As] Form2 = [New] Form2]                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\' To display the SplashPanel call the ShowSplash() method.]                                                                                 |
|                                                                                                                                                                                                 |
| [Me][.splashPanel1.ShowSplash([New] Point(100,100), f2, [True])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**HideSplash()** - The SplashPanel can be hidden by calling this method at run time.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
| **[]**                                                               |
|                                                                                                                          |
| [// To hide the SplashPanel call the HideSplash() method.]             |
|                                                                                                                          |
| [this][.splashPanel1.HideSplash();] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                    |
|                                                                                                                       |
| **[]**                                                            |
|                                                                                                                       |
| [\' To hide the SplashPanel call the HideSplash() method.]          |
|                                                                                                                       |
| [Me][.splashPanel1.HideSplash()] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ShowSplashDialog()** - The method is used to display the SplashPanel as a modal dialog during run time.

 

When this method is called, the user will not be able to interact with the application until the SplashPanel is closed. This is the only difference between the ShowSplash() method and this method.

[] 

The parameters discussed for the method are as follows.

[] 


  ------------ --------------------------------------------------------------------
  Parameters   Description
  OwnerForm    Represents the owner form.
  Location     Specifies the location at which the SplashPanel will be displayed.
  ------------ --------------------------------------------------------------------


 

The SplashPanel will be displayed at the position / location specified in this method. By passing a new instance of the owner form to this method, we can display the SplashPanel as a modal dialog.

 

The below example uses a button click event to call this method. This method is overloaded.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)]                                       |
|                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [this][.splashPanel1.ShowDialogSplash([new] [Point](700, 700), [new] [Form1]());] |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashPanel1.ShowDialogSplash([New] Point(700, 700), [New] Form1())]                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

This overloaded method passes the owner form as a parameter to this method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [this][.splashPanel1.ShowDialogSplash([new] [Form1]());]                              |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashPanel1.ShowDialogSplash([New] Form1())]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[·      ]**IsShowing()** - This method will tell you whether the SplashPanel is currently displayed or not. This method returns \'True\' if the SplashPanel is displayed and \'False\' if it is not displayed.

 

You can call this method in a button click event and view the result in the output window as given below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [// To know whether splash screen is showing]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [private][ [void] button1_Click_1([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [this][.splashPanel1.IsShowing();]                                                                                                |
|                                                                                                                                                                                                                        |
| [Console][.Write([this].splashPanel1.IsShowing());]                                                          |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [\' To know whether splash screen is showing]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashPanel1.IsShowing()]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [Console.Write([Me].splashPanel1.IsShowing())]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Location

[] 

The location for displaying the splash window is specified using the property given below.

[] 


  ---------------------- --------------------------------------------------------
  SplashPanel Property   Description
  DiscreetLocation       Gets / sets the location to display the splash window.
  ---------------------- --------------------------------------------------------


 

A Sample which demonstrates the ShowSplash() and ShowSplashDialog() methods is available in the below sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Tools.Windows\\Samples\\2.0\\Notification Package\\SplashPanel***

[] 

 

 

 

 

###### []{#_SplashPanel_in_TaskBar}3.7.3.3.1.1      SplashPanel in TaskBar {#splashpanel-in-taskbar style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

The SplashPanel can be displayed in the taskbar and it\'s appearance can be customized using the properties given below.

 


  ---------------------- -------------------------------------------------------------
  SplashPanel Property   Description
  ShowInTaskBar          Specifies if the SplashPanel is to be shown in the taskbar.
  FormIcon               Gets / sets the icon for the SplashPanel.
  Text                   Specifies the text when displayed in the taskbar.
  ---------------------- -------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [this][.splashPanel1.ShowInTaskbar = [true];]                                                                                            |
|                                                                                                                                                                                                                                                    |
| [this][.splashControl1.FormIcon = ((System.Drawing.[Icon])(resources.GetObject([\"splashControl1.FormIcon\"])));] |
|                                                                                                                                                                                                                                                    |
| [this][.splashPanel1.Text = [\"Splash Panel\"];]                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [Me][.splashPanel1.ShowInTaskbar = [true]]                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [Me][.splashControl1.FormIcon = [DirectCast]((resources.GetObject([\"splashControl1.FormIcon\"])), System.Drawing.Icon)] |
|                                                                                                                                                                                                                                                           |
| [Me][.splashPanel1.Text = [\"Splash Panel\"]]                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 998: SplashPanel displayed in the TaskBar

 

 

 

 

###### 3.7.3.3.1.2      Time Interval {#time-interval style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The SplashPanel is, by default, a timed display splash screen. The SplashPanel uses internally, a System.Windows.Forms.Timer, to automatically close the splash screen after the set interval is elapsed. This behavior can be changed by setting the TimerInterval property to -1.

[] 


  ---------------------- --------------------------------------------------------------------------------------
  SplashPanel Property   Description
  TimerInterval          The time interval for which the splash screen should be displayed (in milliseconds).
  ---------------------- --------------------------------------------------------------------------------------


[] 

The splash screen will be displayed for a specific time period and will then be closed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.splashPanel1.TimerInterval = 7000;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.splashPanel1.TimerInterval = 7000] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

