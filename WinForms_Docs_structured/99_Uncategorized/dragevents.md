---
title: dragevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dragevents.md
created_at: 2025-07-03
---






##### Drag Events {#drag-events style="tab-stops: 0pt"}

[] 

This section covers the following events:

[] 

###### 3.2.3.8.7.1 DragAllow Event[]{#p110} {#dragallow-event style="tab-stops: 0pt"}

[] 

The DragAllow event is triggered when a docking window is about to be dragged. Whenever the user wants to dock a control, he will try to drag the control, to dock it to a particular target. This event will be raised, when this dragging process starts.

[] 

Event Data

[] 

DragAllowEventHandler receives an argument of type DragAllowEventArgs containing data related to this event. The following DragAllowEventArgs properties provides information specific to this event.

[] 


  --------- --------------------------------------------------------------------------------------
  Members   Description
  Cancel    This property gets / sets the value indicating whether the event should be canceled.
  Control   The control that is about to be dragged.
  --------- --------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [//The DragAllow event occurs when a docking window is about to be dragged.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| [private void ][dockingManager1_DragAllow(][object ][sender, Syncfusion.Windows.Forms.Tools.DragAllowEventArgs arg)] |
|                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine(\"DragAllow Event has been triggered\");]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| [//arg.Control property gives the reference to be dragged.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                            |
| [if][(arg.Control==][this][.panel1)]                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [//arg.Cancel is the property used to cancel the drag operation when it\'s in true state.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| [arg.Cancel=][true][;]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\'The DragAllow event occurs when a docking window is about to be dragged.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] dockingManager1_DragAllow([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DragAllowEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\"DragAllow Event has been triggered\"])]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\'arg.Control property gives the reference to be dragged.]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [If][ arg.Control = [Me].panel1 [Then]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\'arg.Cancel is the property used to cancel the drag operation when it\'s in true state.]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [arg.Cancel = [True]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p111}[]{#_DragFeedbackStart_Event}3.2.3.8.7.2 DragFeedbackStart Event {#dragfeedbackstart-event style="tab-stops: 0pt"}

 

The DragFeedbackStart event is fired just before the start of the feedback of a drag operation. When the docked control is dragged from its position to locate some position, this event will be raised.

[] 


  --------- -------------------------------------------------------
  Member    Description
  Control   Gets the docked control which is about to be dragged.
  --------- -------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [//The DragFeedbackStart event occurs just before the start of feedback of a drag operation.]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                 |
| [//It occurs after the DragAllow Event.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                 |
| [private void ][dockingManager1_DragFeedbackStart(][object ][sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"DragFeedbackStart Event has been \");]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                 |
| [//The following code is used to display all control names which are in the Docking Manager.]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                 |
| [Syncfusion.Windows.Forms.Tools.DockingManager ctrl=sender ][as]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [Syncfusion.Windows.Forms.Tools.DockingManager;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                 |
| [IEnumerator ienum = ctrl.Controls;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [ArrayList dockedctrls = ][new ][ArrayList();]                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [while][(ienum.MoveNext())]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| [dockedctrls.Add(ienum.Current);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [foreach][(Control c ][in ][dockedctrls)]                                                 |
|                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine(\"Control Name :\" + c.Name);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] dockingManager1_DragFeedbackStart([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"DragFeedbackStart Event has been \"])]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ ctrl [As] Syncfusion.Windows.Forms.Tools.DockingManager = [CType](ConversionHelpers.AsWorkaround(sender, [GetType](Syncfusion.Windows.Forms.Tools.DockingManager)), Syncfusion.Windows.Forms.Tools.DockingManager)] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ ienum [As] IEnumerator = ctrl.Controls]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ dockedctrls [As] ArrayList = [New] ArrayList]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [While][ ienum.MoveNext]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [dockedctrls.Add(ienum.Current)]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [While]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [For][ [Each] c [As] Control [In] dockedctrls]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Control Name :\"] + c.Name)]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Next]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p112}[]{#_DragFeedbackStop_Event}3.2.3.8.7.3 DragFeedbackStop Event {#dragfeedbackstop-event style="tab-stops: 0pt"}

[] 

The DragFeedbackStop event occurs immediately after the end of the feedback of a drag operation. When the docked control is dragged from its position and locates another position, this event will be raised. Whenever the mouse click is released from dragging, the drag feedback is stopped and DragFeedbackStop event will be triggered.

[] 


  --------- -------------------------------------------
  Member    Description
  Control   Gets the docked control which is dragged.
  --------- -------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [//The DragFeedbackStop event occurs immediately after the end of feedback of a drag operation.]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [private void ][dockingManager1_DragFeedbackStop(][object ][sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine(\"DragFeedbackStop Event is raised\");]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| [\'The DragFeedbackStop event occurs immediately after the end of feedback of a drag operation.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] dockingManager1_DragFeedbackStop([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine([\"DragFeedbackStop Event is raised\"])]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

