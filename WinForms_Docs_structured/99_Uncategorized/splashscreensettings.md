---
title: splashscreensettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splashscreensettings.md
created_at: 2025-07-03
---






##### SplashScreen Settings {#splashscreen-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The following are the splash settings available for the SplashControl.

 

**Automatic Launching**

[] 

The properties given below describe the AutoMode features of the SplashControl.

[] 


  ------------------------ -------------------------------------------------------------------------------
  SplashControl Property   Description
  AutoMode                 Specifies if the SplashControl should automatically launch the splash screen.
  AutoModeDisableOwner     Specifies if the SplashControl displays modally when in AutoMode.
  IsShowing                Indicates if the splash screen is currently being displayed.
  ------------------------ -------------------------------------------------------------------------------


[] 

A splash image is displayed when an application is run, and only when **AutoMode** property is set to \'True\'. By default this value will be set to \'True\'. When the AutoMode is set to \'False\', the splash image will not be displayed when the application starts.

 

If the **AutoModeDisableOwner** property is set to \'True\', the splash screen displays modally. The splash screen stops the user from interacting with the rest of the application until it gets hidden. Once the splash screen disappears, the user will be able to interact with the form.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [this][.SplashControl1.AutoMode =[ true;]]             |
|                                                                                                                                                                  |
| [this][.splashControl1.AutoModeDisableOwner = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [Me][.SplashControl1.AutoMode = [True]]             |
|                                                                                                                                                               |
| [Me][.splashControl1.AutoModeDisableOwner = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The methods given below can also be used to show / hide the splash screen at run time.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ShowSplash                        | The splash screen can also be displayed, at run time, when this method is called. It includes the following parameter.               |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   | DisableOwner - Indicates whether the owner form, i.e., the Windows form is enabled or disabled when the splash screen is displaying. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| HideSplash                        | This method will decide whether to show or hide the splash screen that has been displayed using the above method.                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ShowDialogSplash                  | This method will display the splash screen as a modal dialog.                                                                        |
|                                   |                                                                                                                                      |
|                                   | It includes the following parameters.                                                                                                |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   | OwnerForm - Represents the owner form.                                                                                               |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
|                                   | Location - Specifies the location at which the splash screen will be displayed.                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [// Displays the splash screen.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [this][.splashControl1.ShowSplash([true]);]                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [// Hides the splash screen.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [this][.splashControl1.HideSplash();]                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [// Displays the splash screen as a modal dialog.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)]                                       |
|                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [this][.splashControl1.ShowDialogSplash([new] [Point](700,700),[new] [Form1]());] |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [\' Displays the splash screen.]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashControl1.ShowSplash([True]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [\' Hides the splash screen.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashControl1.HideSplash();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [\' Displays the splash screen as a modal dialog.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.splashControl1.ShowDialogSplash([New] Point(700, 700), [New] Form1())]                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below example uses a **button click** event to call this method. This method is overloaded. The overloaded method passes the owner form as a parameter to this method.

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
| [this][.splashControl1.ShowDialogSplash([new] [Form1]());]                            |
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
| [Me][.splashControl1.ShowDialogSplash([New] Form1())]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Time Interval Settings

 

The SplashControl is, by default, a timed display splash screen. The splash screen will be displayed for a specific time period and will then be closed. By default, the value will be set as 5000. User can change this value, run the application and see the difference.

[] 


  ------------------------ -------------------------------------------------------------------------------------
  SplashControl Property   Description
  TimerInterval            The time interval for which the splash screen is to be displayed (in milliseconds).
  ------------------------ -------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                    |
| []                                                                                |
|                                                                                                                                    |
| [this][.splashControl1.TimerInterval = 3000;] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [Me][.splashControl1.TimerInterval = 3000] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[SplashControl Events]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SplashControl_Events)[]{.UGHyperlink}

 

 

 

 

[]{#related-topics}

