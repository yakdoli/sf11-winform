---
title: pinpointevents1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pinpointevents1.md
created_at: 2025-07-03
---






##### PinPoint Events {#pinpoint-events style="tab-stops: 0pt"}

[] 

 When changing the node\'s location, the pinpoint of the node will be reset. The below table contains pinpoint events and descriptions.

[] 


  ------------------- -------------------------------------------------------
  DocumentEventSink   Description
  PinOffsetChanged    Triggered after the offset of the pinpoint is reset.
  PinOffsetChanging   Triggered when the offset of the pinpoint is changed.
  PinPointChanged     Triggered after the pinpoint is repositioned.
  PinPointChanging    Triggered when the pinpoint is moved.
  ------------------- -------------------------------------------------------


[] 

Data can be retrieved or set using the following members.

[] 


  -------------------------------------------- ----------------------------------------------------------
  PinPoint / PinPointOffset EventArgs Member   Description
  Cancel                                       Cancels the PinPoint Changing events.
  NodeAffected                                 Returns the node\'s name by which the node was affected.
  Offset                                       Returns the X and Y values.
  -------------------------------------------- ----------------------------------------------------------


[] 

[] 

Programmatically the events are written as follows,

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [public][ [void] Form1_Load([object] sender, [EventArgs] e)]                                                     |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    ((DocumentEventSink)model4.EventSink).PinOffsetChanged += [new] PinOffsetChangedEventHandler(Form1_PinOffsetChanged);]                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [    ((DocumentEventSink)model4.EventSink).PinOffsetChanging += [new] PinOffsetChangingEventHandler(Form1_PinOffsetChanging);]                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    ((DocumentEventSink)model4.EventSink).PinPointChanged += [new] PinPointChangedEventHandler(Form1_PinPointChanged);]                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [    ((DocumentEventSink)model4.EventSink).PinPointChanging += [new] PinPointChangingEventHandler(Form1_PinPointChanging);]                                                                                 |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    [// Circle]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [    Syncfusion.Windows.Forms.Diagram.Ellipse circle = [new] Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72);]                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [    circle.Name = [\"Circle\"];]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                      |
| [    circle.FillStyle.Type = FillStyleType.LinearGradient;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [    circle.FillStyle.ForeColor = [Color].AliceBlue;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [    circle.ShadowStyle.Visible = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [    model4.AppendChild(circle);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [void][ Form1_PinPointChanging(PinPointChangingEventArgs evtArgs)]                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [MessageBox].Show([\"PinpointChanging event is fired\"] + [\"\\n\"] + [\"Node name: \"] + evtArgs.NodeAffected.Name.ToString());] |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [void][ Form1_PinPointChanged(PinPointChangedEventArgs evtArgs)]                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [MessageBox].Show([\"PinPointChanged event is fired\"] + [\"\\n\"] + [\"Offset values: \"] + evtArgs.Offset.ToString());]         |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [void][ Form1_PinOffsetChanging(PinOffsetChangingEventArgs evtArgs)]                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [MessageBox].Show([\"PinOffsetChanging event is fired\"] + [\"\\n\"] + [\"Node name: \"] + evtArgs.NodeAffected.Name);]           |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [void][ Form1_PinOffsetChanged(PinOffsetChangedEventArgs evtArgs)]                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [MessageBox].Show([\"PinOffsetChanged event is fired\"] + [\"\\n\"] + [\"Offset values: \"] + evtArgs.Offset.ToString());]        |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Public][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model4.EventSink, DocumentEventSink).PinOffsetChanged, [AddressOf] Form1_PinOffsetChanged]                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model4.EventSink, DocumentEventSink).PinOffsetChanging, [AddressOf] Form1_PinOffsetChanging]                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model4.EventSink, DocumentEventSink).PinPointChanged, [AddressOf] Form1_PinPointChanged]                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model4.EventSink, DocumentEventSink).PinPointChanging, [AddressOf] Form1_PinPointChanging]                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [    [\' Circle]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [    [Dim] circle [As] [New] Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72)]                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [    circle.Name = [\"Circle\"]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [    circle.FillStyle.Type = FillStyleType.LinearGradient]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [    circle.FillStyle.ForeColor = Color.AliceBlue]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [    circle.ShadowStyle.Visible = [True]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [    model4.AppendChild(circle)]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_PinPointChanging([ByVal] evtArgs [As] PinPointChangingEventArgs)]                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"PinpointChanging event is fired\"] & vbLf & [\"Node name: \"]) + evtArgs.NodeAffected.Name.ToString())]                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_PinPointChanged([ByVal] evtArgs [As] PinPointChangedEventArgs)]                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"PinPointChanged event is fired\"] & vbLf & [\"Offset values: \"]) + evtArgs.Offset.ToString())]                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_PinOffsetChanging([ByVal] evtArgs [As] PinOffsetChangingEventArgs)]                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"PinOffsetChanging event is fired\"] & vbLf & [\"Node name: \"]) + evtArgs.NodeAffected.Name)]                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_PinOffsetChanged([ByVal] evtArgs [As] PinOffsetChangedEventArgs)]                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"PinOffsetChanged event is fired\"] & vbLf & [\"Offset values: \"]) + evtArgs.Offset.ToString())]                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagrams are as follows,

**[]** 

{border="0"}

**[]** 

Figure 105: Pinpoint Changing Event

**[]** 

{border="0"}

**[]** 

Figure 106: Pinpoint Changed Event

 

[]{#p63} 

 

[]{#related-topics}

