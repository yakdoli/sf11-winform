---
title: dockedcontrol.md
original_path: WinForms_Docs/99_Uncategorized/dockedcontrol.md
created_at: 2025-08-05
---






##### Docked Control {#docked-control style="tab-stops: 0pt"}

[] 

This section covers the following events:

[] 

###### 3.2.3.8.4.1 ControlMaximized Event {#controlmaximized-event style="tab-stops: 0pt"}

***[]*** 

The docked control gets maximized, when the maximized button of the docked control is clicked. ControlMaximized event will be triggered after the control is maximized.

[] 

Event Data

**[]** 

The event handler receives an argument of type ControlMaximizedEventArgs containing data related to this event. The following  ControlMaximizedEventArgs properties provide information specific to this event.

[] 


  --------- --------------------------------------------------------------------------
  Members   Description
  Cancel    Gets / sets value that indicates whether to cancel the operation or not.
  --------- --------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [private void ][dockingManager1_ControlMaximized(][object ][sender, Syncfusion.Windows.Forms.Tools.ControlMaximizedEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [// You can see the below line in output window during runtime.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Control Maximized event is raised\");]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Displays the docked control name]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name);]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [arg.Cancel=][true][;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub ][dockingManager1_ControlMaximized(][ByVal][ sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.[ControlMaximizedEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"Control Maximized event is raised\")]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Displays the docked control name]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name)]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [arg.Cancel=][True]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p97}[]{#_ControlMaximizing_Event}3.2.3.8.4.2 ControlMaximizing Event {#controlmaximizing-event style="tab-stops: 0pt"}

[] 

When the user clicks on the maximize button, and when the control is going to be maximized, the ControlMaximizing event will be raised.

[] 

Event Data

**[]** 

The event handler receives an argument of type ControlMaximizeEventArgs containing data related to this event. The following  ControlMaximizeEventArgs properties provide information specific to this event.

[] 


  --------- --------------------------------------------------------------------------
  Members   Description
  Cancel    Gets / sets value that indicates whether to cancel the operation or not.
  --------- --------------------------------------------------------------------------


**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [private void ][dockingManager1_ControlMaximizing(][object ][sender, Syncfusion.Windows.Forms.Tools.ControlMaximizeEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [// You can see the below line in output window during runtime.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Control Maximizing event is raised\");]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Displays the docked control name]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name);]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [arg.Cancel=][True]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub ][dockingManager1_ControlMaximizing(][ByVal][ sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.[ControlMaximizeEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"Control Maximizing event is raised\")]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Displays the docked control name]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name)]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [arg.Cancel=][True]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p98}[]{#_ControlMinimized_Event}3.2.3.8.4.3 ControlMinimized Event {#controlminimized-event style="tab-stops: 0pt"}

[] 

This event is fired after the control is minimized using the minimize option available for the docked control. This event can display the control name using the Control parameter available for the ControlMinimizedEventHandler.

[] 


  --------- --------------------------------------------------
  Members   Description
  Control   Specifies the docked control which is minimized.
  --------- --------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [private void ][dockingManager1_ControlMinimized(][object ][sender, ControlMinimizedEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [// You can see the below line in output window during runtime.]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine(\"Control Minimized event is raised\");]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [Displays the docked control name]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub ][dockingManager1_ControlMinimized(][ByVal][ sender [As] [Object], [ByVal] arg [As] [ControlMinimizedEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine(\"Control Minimized event is raised\")]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Displays the docked control name]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine(\"Control Name : \"+arg.Control.Name);]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p99}[]{#_ControlRestored_Event}3.2.3.8.4.4 ControlRestored Event {#controlrestored-event style="tab-stops: 0pt"}

[[[]]]{.underline} 

This event occurs after the control is restored to its original position. This event can give the previous state of the control using the PreviousSizeState property available for the handler.

**[]** 

Event Data

**[]** 

The event handler receives an argument of type ControlRestoredEventArgs containing data related to this event. The following ControlRestoredEventArgs properties provide information specific to this event.

[] 


  ------------------- --------------------------------------------------
  Member              Description
  PreviousSizeState   Returns previous size state of changing control.
  ------------------- --------------------------------------------------


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [private void ][dockingManager1_ControlRestored(][object ][sender, ControlRestoredEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                         |
| [// You can see the below line in output window during runtime.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine(\"Control Restored event is raised\");]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [//Displays the previous state]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\"Control Name : \"]+arg.PreviousSizeState.ToString());]                                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private Sub ][dockingManager1_ControlRestored(][ByVal][ sender [As] [Object], [ByVal] arg [As] [ControlRestoredEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine(\"Control Restored event is raised\")]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\'Displays the previous state]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Console][.WriteLine([\"Control Name : \"]+arg.PreviousSizeState.ToString());]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

