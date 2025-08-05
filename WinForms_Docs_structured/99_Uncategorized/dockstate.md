---
title: dockstate.md
original_path: WinForms_Docs/99_Uncategorized/dockstate.md
created_at: 2025-08-05
---






##### Dock State {#dock-state style="tab-stops: 0pt"}

[] 

This section covers the following events:

[] 

###### 3.2.3.8.5.1 DockStateChanged Event {#dockstatechanged-event style="tab-stops: 0pt"}

[]{#p101}[] 

When the user changes the dock state of the control, DockStateChanged event will be raised immediately after this dock state change operation.

[] 

Event Data

**[]** 

The event handler receives an argument of type DockStateChangeEventArgs containing data related to this event. The following DockStateChangeEventArgs property provides information specific to this event.

[] 


  --------- ---------------------------------------------------------------------
  Member    Description
  Control   Gets the collection of controls undergoing the dock state transfer.
  --------- ---------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [//The DockStateChanged event occurs immediately after a dock operation.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                         |
| [private void ][dockingManager1_DockStateChanged(][object ][sender, Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine(\"DockStateChanged Event has occurred\");]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine(\"Total Number of controls in a group : \" +]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| [arg.Controls.Length.ToString());]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [//arg.Controls Gets the collection of controls undergoing the dockstate transfer.]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                         |
| [Control\[\] ctrls = arg.Controls;]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [int ][i=1;]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [//Here display all the controls in arg.Controls group.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [foreach][(Control ctrl ][in ][ctrls)]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine(\"Control\"+ i + \" Name : \" + ctrl.Name);]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [i++;]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\'The DockStateChanged event occurs immediately after a dock operation.]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] dockingManager1_DockStateChanged([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\"DockStateChanged Event has occurred\"])]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\"Total Number of controls in a group : \"] + arg.Controls.Length.ToString)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\'arg.Controls Gets the collection of controls undergoing the dockstate transfer.]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ ctrls [As] Control() = arg.Controls]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ i [As] [Integer] = 1]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\'Here display all the controls in arg.Controls group.]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [For][ [Each] ctrl [As] Control [In] ctrls]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\"Control\"] + i + [\" Name : \"] + ctrl.Name)]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [System.Math.Min(System.Threading.Interlocked.Increment(i), i - 1)]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Next]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p102}[]{#_DockStateChanging_Event}3.2.3.8.5.2 DockStateChanging Event {#dockstatechanging-event style="tab-stops: 0pt"}

[] 

DockStateChanging event will be triggered just before a dock operation takes place.

**[]** 

Event Data

[] 

The event handler receives an argument of type DockStateChangeEventArgs containing data related to this event. The following DockStateChangeEventArgs property provides information specific to this event.

[] 


+-----------------------------------+--------------------------------------------+
| Member                            | Description                                |
+-----------------------------------+--------------------------------------------+
| Control                           | Gets the collection of controls undergoing |
|                                   |                                            |
|                                   | the dockstate transfer.                    |
+-----------------------------------+--------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| **[/]**[/The DockStateChanging event occurs just before a dock operation takes place.]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [private void ][dockingManager1_DockStateChanging(][object ][sender, Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"DockStateChanging Event has occurred\");]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Total Number of controls in a group : \"+arg.Controls.Length.ToString());]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| [//arg.Controls gives the collection of controls which are in Docked Area.]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                          |
| [Control\[\] ctrls = arg.Controls;]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [int ][i=1;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Here display all the controls in arg.Controls group.]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [foreach][(Control ctrl ][in ][ctrls)]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Control\"+ i + \" Name : \" + ctrl.Name);]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| [i++;]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'The DockStateChanging event occurs just before a dock operation takes place.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] dockingManager1_DockStateChanging([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"DockStateChanging Event has occurred\"])]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Total Number of controls in a group : \"] + arg.Controls.Length.ToString)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'arg.Controls gives the collection of controls which are in Docked Area.]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ ctrls [As] Control() = arg.Controls]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ i [As] [Integer] = 1]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'Here display all the controls in arg.Controls group.]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [For][ [Each] ctrl [As] Control [In] ctrls]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Control\"] + i + [\" Name : \"] + ctrl.Name)]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [System.Math.Min(System.Threading.Interlocked.Increment(i), i - 1)]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Next]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p103}[]{#_DockStateUnavailable_Event}3.2.3.8.5.3 DockStateUnavailable Event {#dockstateunavailable-event style="tab-stops: 0pt"}

[] 

The DockStateUnavailable event occurs if serialized information is not available for a dockable control when loading a persisted dock state.

**[]** 

Event Data

**[]** 

The event handler receives an argument of type DockStateUnavailableEventArgs containing data related to this event. The following DockStateUnavailableEventArgs property provides information specific to this event.

[] 


  --------- -----------------------------------
  Member    Description
  Control   The name property of the control.
  --------- -----------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//The DockStateUnavailable event occurs if serialized information is not available]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//for a dockable control when loading a persisted dock state.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| [private void ][dockingManager1_DockStateUnavailable(][object ][sender, Syncfusion.Windows.Forms.Tools.DockStateUnavailableEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine(\"DockStateUnavailable Event has been fired\");]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine(\"Dock state unavailable for the Control is :]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\"+arg.Control.Name);]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'The DockStateUnavailable event occurs if serialized information is not available]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'for a dockable control when loading a persisted dock state.]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] dockingManager1_DockStateUnavailable([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockStateUnavailableEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\"DockStateUnavailable Event has been fired\"])]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\"Dock state unavailable for the Control is : \"] + arg.Control.Name)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p104}[]{#_NewDockStateBeginLoad_Event}3.2.3.8.5.4 NewDockStateBeginLoad Event {#newdockstatebeginload-event style="tab-stops: 0pt"}

[] 

The NewDockStateBeginLoad event occurs just before a new dock state is loaded. Whenever an application with one or more docked controls is going to be loaded, this event will be triggered.

[] 


  --------- ---------------------------------------------------------------------------
  Member    Description
  Control   Gets the docked control for which a new dock state is going to be loaded.
  --------- ---------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [//The NewDockStateBeginLoad event occurs just before a new dock state is loaded.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [private void ][dockingManager1_NewDockStateBeginLoad(][object ][sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [Console.WriteLine(\"NewDockStateBeginLoad Event occurred\");]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| [//This will show until you click on the OK button.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [//So The new state will be loaded after finishing this statement.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [MessageBox.Show(\"This is NewDockStateBeginLoad Event Message Box\");]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] dockingManager1_NewDockStateBeginLoad([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\"NewDockStateBeginLoad Event occurred\"])]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                           |
| [\'This will show until you click on the OK button.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                           |
| [\'So The new state will be loaded after finishing this statement.]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                           |
| [MessageBox.Show([\"This is NewDockStateBeginLoad Event Message Box\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p105}[]{#_NewDockStateEndLoad_Event}3.2.3.8.5.5 NewDockStateEndLoad Event {#newdockstateendload-event style="tab-stops: 0pt"}

 

The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded. Whenever an application with one or more docked controls is loaded, this event will be triggered.

[] 


  --------- ---------------------------------------------------------------------
  Member    Description
  Control   Gets the docked control for which a new dock state has been loaded.
  --------- ---------------------------------------------------------------------


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [//The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [private void ][dockingManager1_NewDockStateEndLoad(][object ][sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"NewDockstateEndLoad Event occurred\");]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| [//This will show until you click on the OK button.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [//So The new state will be loaded after finishing this statement.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [MessageBox.Show(\"This is NewDockStateEndLoad Event Message Box\");]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [\'The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] dockingManager1_NewDockStateEndLoad([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"NewDockstateEndLoad Event occurred\"])]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [\'This will show until you click on the OK button.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [\'So The new state will be loaded after finishing this statement.]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                         |
| [MessageBox.Show([\"This is NewDockStateEndLoad Event Message Box\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

