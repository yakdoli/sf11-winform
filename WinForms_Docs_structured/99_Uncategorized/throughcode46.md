---
title: throughcode46.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode46.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

A SplashControl can be created through code by following the below steps.

[] 

1.               Create a C# or VB.NET application though Visual Studio.

[] 

2.   Add the required assembly references.

[] 

3.   Declare and initialize a SplashControl using the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [private][ Syncfusion.Windows.Forms.Tools.[SplashControl] splashControl1;]                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [this][.splashControl1 = [new] Syncfusion.Windows.Forms.Tools.[SplashControl]();] |
|                                                                                                                                                                                                                  |
| [this][.SuspendLayout();]                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [Friend][ [WithEvents] SplashControl1 [As] Syncfusion.Windows.Forms.Tools.SplashControl] |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [Me][.splashControl1 = [New] Syncfusion.Windows.Forms.Tools.SplashControl() ]                                 |
|                                                                                                                                                                                                                         |
| [Me][.SuspendLayout()]                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set the following properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [this][.splashControl1.CustomSplashPanel = [null];]                                          |
|                                                                                                                                                                                                        |
| [this][.splashControl1.HostForm = [this];]                                                   |
|                                                                                                                                                                                                        |
| [this][.splashControl1.HostFormWindowState = System.Windows.Forms.[FormWindowState].Normal;] |
|                                                                                                                                                                                                        |
| [this][.splashControl1.TimerInterval = 3000;]                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Me][.SplashControl1.CustomSplashPanel = [Nothing]]                |
|                                                                                                                                                                              |
| [Me][.SplashControl1.HostForm = [Me]]                              |
|                                                                                                                                                                              |
| [Me][.SplashControl1.HostFormWindowState = System.Windows.Forms.FormWindowState.Normal] |
|                                                                                                                                                                              |
| [Me][.SplashControl1.TimerInterval = 3000]                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Run the application.

[] 

{border="0"}

[] 

Figure 983: SplashControl created Through Code

[] 

See Also

[] 

[[Through Designer]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Through_Designer_1)[, ][[SplashScreen Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SplashScreen_Settings)[]

 

 

 

 

[]{#related-topics}

