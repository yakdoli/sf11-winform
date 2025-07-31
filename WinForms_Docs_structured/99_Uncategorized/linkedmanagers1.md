---
title: linkedmanagers1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\linkedmanagers1.md
created_at: 2025-07-03
---






##### Linked Managers {#linked-managers style="tab-stops: 0pt"}

This section covers the following events:

[] 

###### []{#_TransferredToManager_Event}3.2.3.8.8.1 TransferredToManager Event {#transferredtomanager-event style="tab-stops: 0pt"}

[] 

The TransferredToManager event occurs after a dockable control that previously belonged to some other DockingManager has been transferred to the docking layout hosted by the current DockingManager.

[] 

Event Data

**[]** 

The event handler receives an argument of type TransferManagerEventArgs containing data related to this event. The following TransferManagerEventArgs properties provide information specific to this event.

[] 


  --------- ----------------------------------------------------
  Member    Description
  Control   Gets the control which is undergoing the transfer.
  --------- ----------------------------------------------------


**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [// A docking window is being transferred from one docking layout to another.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [// Update the control\'s DockingManager reference.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [protected void ][DockingManager_TransferredToManager(][object ][sender, TransferManagerEventArgs args)] |
|                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine(\"Transferred to Manager Event has been Raised\");]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [DockableControlBase dockablecontrol = args.Control ][as ][DockableControlBase;]                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [dockablecontrol.CurrentDockingManager = sender ][as ][DockingManager;]                                                                                   |
|                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine(\"HostControl Name (Target Page Name) : \"+dockablecontrol.CurrentDockingManager.HostControl.Name);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Protected][ [Sub] DockingManager_TransferredToManager([ByVal] sender [As] [Object], [ByVal] args [As] TransferManagerEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine([\"Transferred to Manager Event has been Raised\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ dockablecontrol [As] DockableControlBase = [CType](ConversionHelpers.AsWorkaround(args.Control, [GetType](DockableControlBase)), DockableControlBase)]                                    |
|                                                                                                                                                                                                                                                                                                                                                      |
| [dockablecontrol.CurrentDockingManager = [CType](ConversionHelpers.AsWorkaround(sender, [GetType](DockingManager)), DockingManager)]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine([\"HostControl Name (Target Page Name) : \"] + dockablecontrol.CurrentDockingManager.HostControl.Name)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample

[] 

A sample which demonstrates the Linked Managers concept is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Docking Package\\LinkedManagers

###### []{#p115}[]{#_TransferringFromManager_Event}3.2.3.8.8.2 TransferringFromManager Event {#transferringfrommanager-event style="tab-stops: 0pt"}

[] 

The TransferringFromManager event occurs when a dockable control hosted by a DockingManager is about to be transferred to the docking layout hosted by some other DockingManager.

[] 

Event Data

**[]** 

The event handler receives an argument of type TransferManagerEventArgs containing data related to this event. The following TransferManagerEventArgs property provide information specific to this event.

[] 


  --------- ----------------------------------------------------
  Member    Description
  Control   Gets the control which is undergoing the transfer.
  --------- ----------------------------------------------------


**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| [//The TransferringFromManager event occurs when a dockable control hosted by this DockingManager is]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [//about to be transferred to the docking layout hosted by some other DockingManager.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [protected void ][DockingManager_TransferringFromManager(][object ][sender, TransferManagerEventArgs args)] |
|                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Transferring From Manager Event has been raised\");]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| [DockableControlBase dockablecontrol = args.Control ][as ][DockableControlBase;]                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| [dockablecontrol.CurrentDockingManager = sender ][as ][DockingManager; ]                                                                                     |
|                                                                                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"HostControl name : \"+dockablecontrol.CurrentDockingManager.HostControl.Name);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\'The TransferringFromManager event occurs when a dockable control hosted by this DockingManager is]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\'about to be transferred to the docking layout hosted by some other DockingManager.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Protected][ [Sub] DockingManager_TransferringFromManager([ByVal] sender [As] [Object], [ByVal] args [As] TransferManagerEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Transferring From Manager Event has been raised\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ dockablecontrol [As] DockableControlBase = [CType](ConversionHelpers.AsWorkaround(args.Control, [GetType](DockableControlBase)), DockableControlBase)]                                       |
|                                                                                                                                                                                                                                                                                                                                                         |
| [dockablecontrol.CurrentDockingManager = [CType](ConversionHelpers.AsWorkaround(sender, [GetType](DockingManager)), DockingManager)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"HostControl name : \"] + dockablecontrol.CurrentDockingManager.HostControl.Name)]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample

[] 

A sample which demonstrates the Linked Managers concept is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Docking Package\\LinkedManagers

 

[]{#related-topics}

