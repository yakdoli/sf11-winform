---
title: docking1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\docking1.md
created_at: 2025-07-03
---






##### Docking {#docking style="tab-stops: 0pt"}

[] 

This section covers the following events:

[] 

###### []{#_DockAllow_Event}3.2.3.8.1.1 DockAllow Event {#dockallow-event style="tab-stops: 0pt"}

[]{#p85}[] 

[This event is illustrated in ]How to Prevent tabbed docking.[]

###### []{#p86}[]{#_DockControlActivated_Event}3.2.3.8.1.2 DockControlActivated Event {#dockcontrolactivated-event style="tab-stops: 0pt"}

[] 

The DockControlActivated event occurs when a dockable control gets activated. When the user clicks on the dockable control or the docked control, this event will be triggered. It can display the control name which has been activated currently.

**[]** 

Event Data

[] 

The event handler receives an argument of type DockActivationChangedEventArgs containing data related to this event. The following DockActivationChangedEventArgs properties provide information specific to this event.

[] 


  --------- -------------------------------------------
  Member    Description
  Control   The control which has been activated now.
  --------- -------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                   |
| [//The DockControlActivated event occurs when a dockable control gets activated.]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                   |
| [private void ][dockingManager1_DockControlActivated(][object ][sender, Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                   |
| [//If we click on the Docked control or click on the Docked control title bar,]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [// DockControlActivated event will be triggered]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                   |
| [//DockActivationChangedEventArgs has the property called Control which has the details of the]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [// Activated control.]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Dock Control Activated Event is Fired\");]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                   |
| [//Here Display the name of the control that is being active currently.]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Activated Control Name : \"+arg.Control.Name);]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[VB.NET\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'The DockControlActivated event occurs when a dockable control gets activated.]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] dockingManager1_DockControlActivated([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'If we click on the Docked control or click on the Docked control title bar,]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'DockControlActivated event will be triggered]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'DockActivationChangedEventArgs has the property called Control which has the details of the]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'Activated control]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Dock Control Activated Event is Fired\"])]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\'Here Display the name of the control that is being active currently.]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Activated Control Name : \"] + arg.Control.Name)]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#_DockControlDeactivated_Event}3.2.3.8.1.3 DockControlDeactivated Event[]{#p87} {#dockcontroldeactivated-event style="tab-stops: 0pt"}

[] 

Whenever a dockable control or the docked control loses focus, DockControlDeactivated event will be raised. In other words, when a dockable control gets deactivated, this event will be fired. This event can display the control name that is deactivated.

[] 

Event Data

**[]** 

The event handler receives an argument of type DockedActivationChangedEventArgs containing data related to this event. The following DockActivationChangedEventArgs property provide information specific to this event.

[] 


  --------- -------------------------------------------
  Member    Description
  Control   The control which has been activated now.
  --------- -------------------------------------------


**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [//The DockControlDeactivated event occurs when a dockable control gets deactivated.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [private void ][dockingManager1_DockControlDeactivated(][object ][sender, Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                     |
| [//Deactivation Event will be triggered when the control has lost the focus.]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Console.WriteLine(\"Dock Control Deactivated Event is Fired\");]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                     |
| [//Here Display the name of the control that is being active currently.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Console.WriteLine(\"Deactivated Control Name : \"+arg.Control.Name);]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\'The DockControlDeactivated event occurs when a dockable control gets deactivated.]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] dockingManager1_DockControlDeactivated([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\'Deactivation Event will be triggered when the control has lost the focus.]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\"Dock Control Deactivated Event is Fired\"])]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\'Here Display the name of the control that is being active currently.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\"Deactivated Control Name : \"] + arg.Control.Name)]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

