---
title: howtoserializeordeserializethedockingstateforadockedcontrolonloadingtheapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoserializeordeserializethedockingstateforadockedcontrolonloadingtheapplication.md
created_at: 2025-07-03
---






##### How to serialize or deserialize the docking state for a docked control on loading the application? {#how-to-serialize-or-deserialize-the-docking-state-for-a-docked-control-on-loading-the-application style="tab-stops: 0pt"}

[] 

To serialize or deserialize the docking state, follow the below steps.

[] 

Before closing the docked / floating control, access the control\'s parent and cast this to type Syncfusion.Windows.Forms.Tools.DockHost.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [Syncfusion.Windows.Forms.Tools.[DockHost] dhost = ctrl.Parent [as] Syncfusion.Windows.Forms.Tools.[DockHost]; ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [Dim][ dhost [As] Syncfusion.Windows.Forms.Tools.DockHost = [Me].listView1.Parent [as] Syncfusion.Windows.Forms.Tools.DockHost  ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Access the DockHost\'s InternalController and get its current serialization information through the GetSerCurrIndo() method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [Syncfusion.Windows.Forms.Tools.[DockHostController] dhc = dhost.InternalController [as] Syncfusion.Windows.Forms.Tools.[DockHostController]; ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [Dim][ dhc [As] Syncfusion.Windows.Forms.Tools.DockHostController = dhost.InternalController [as]  Syncfusion.Windows.Forms.Tools.DockHostController] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]This returns an object of type Syncfusion.Windows.Forms.Tools.DockInfo. The DockInfo.DockingStyle member gives the dock position of the control with respect to the host form and the DockInfo.rcDockArea

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [Syncfusion.Windows.Forms.Tools.[DockInfo] di = dhc.GetSerCurrentDI(); ] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [Dim][ di [As] Syncfusion.Windows.Forms.Tools.DockInfo = dhc.GetSerCurrentDI()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]You can serialize this information against the control's name, and later upon loading, appropriately use either the DockingManager.DockControl() /  FloatControl() method based on the serialized DockingStyle/rcbounds values to set the control's dock state.

[]{#related-topics}

