---
title: rotationevents.md
original_path: WinForms_Docs/99_Uncategorized/rotationevents.md
created_at: 2025-08-05
---






#### Rotation Events[] {#rotation-events style="tab-stops: 0pt"}

[  ]

When the control is rotated horizontally or vertically, the rotation events will be fired displaying the rotation offsets.

 

The below table discusses the available rotation events with descriptions.

[] 


  ------------------------ ----------------------------------------------------------
  DocumentEventSink        Description
  FlipChanged              Triggered after the node is rotated using Flip property.
  FlipChanging             Triggered when the node is rotated using Flip property.
  RotationChanged          Triggered after the node is rotated.
  RotationChanging Event   Triggered on rotating the node in any direction.
  ------------------------ ----------------------------------------------------------


[] 

Data can be retrieved or set using the following members.

[] 


  --------------------------- ----------------------------------------------------------
  Rotation EventArgs Member   Description
  NodeAffected                Returns the node\'s name by which the node was affected.
  RotationOffset              Returns the angle by which the node was rotated.
  --------------------------- ----------------------------------------------------------


[] 


  ----------------------- ----------------------------------------------------------
  Flip EventArgs Member   Description
  Cancel                  Cancels the FlipChanging event.
  FlipAxis                Returns the axis around which the node was rotated.
  FlipValue               Returns the boolean value of the **Flip** property.
  NodeAffected            Returns the node\'s name by which the node was affected.
  ----------------------- ----------------------------------------------------------


[] 

Programmatically the events are written as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [public][ [void] Form1_Load([object] sender, [EventArgs] e)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    ((DocumentEventSink)model1.EventSink).FlipChanged += [new] FlipChangedEventHandler(Form1_FlipChanged);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    ((DocumentEventSink)model1.EventSink).FlipChanging += [new] FlipChangingEventHandler(Form1_FlipChanging);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    ((DocumentEventSink)model1.EventSink).RotationChanged += [new] RotationChangedEventHandler(Form1_RotationChanged);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    ((DocumentEventSink)model1.EventSink).RotationChanging += [new] RotationChangingEventHandler(Form1_RotationChanging);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [// Circle]]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    Syncfusion.Windows.Forms.Diagram.Ellipse circle = [new] Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    circle.Name = [\"Circle\"];]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    circle.FillStyle.Type = FillStyleType.LinearGradient;]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    circle.FillStyle.ForeColor = [Color].AliceBlue;]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    circle.ShadowStyle.Visible = [true];]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    model4.AppendChild(circle);]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [void][ Form1_RotationChanged(RotationChangedEventArgs evtArgs)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [MessageBox].Show([\"RotationChanged event is fired\"] + [\"\\n\"] + evtArgs.RotationOffset.ToString());]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [void][ Form1_FlipChanging(FlipChangingEventArgs evtArgs)]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [MessageBox].Show([\"FlipChanging event is fired\"]);]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString();]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [void][ Form1_FlipChanged(FlipChangedEventArgs evtArgs)]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [MessageBox].Show([\"FlipChanged event is fired\"] + [\"\\n\"] + [\"Flip Axis:\"] + evtArgs.FlipAxis.ToString() + [\"\\n\"] + [\"Node: \"] + evtArgs.NodeAffected.Name.ToString());] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    evtArgs.NodeAffected.EditStyle.Enabled = [false];]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Public][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).FlipChanged, [AddressOf] Form1_FlipChanged]                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).FlipChanging, [AddressOf] Form1_FlipChanging]                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).RotationChanged, [AddressOf] Form1_RotationChanged]                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).RotationChanging, [AddressOf] Form1_RotationChanging]                                                                           |
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
| [Private][ [Sub] Form1_RotationChanged([ByVal] evtArgs [As] RotationChangedEventArgs)]                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"RotationChanged event is fired\"] & vbLf) + evtArgs.RotationOffset.ToString())]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_FlipChanging([ByVal] evtArgs [As] FlipChangingEventArgs)]                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show([\"FlipChanging event is fired\"])]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString()]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_FlipChanged([ByVal] evtArgs [As] FlipChangedEventArgs)]                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show((([\"FlipChanged event is fired\"] & vbLf & [\"Flip Axis:\"]) + evtArgs.FlipAxis.ToString() & vbLf & [\"Node: \"]) + evtArgs.NodeAffected.Name.ToString())]              |
|                                                                                                                                                                                                                                                                                                        |
| [    evtArgs.NodeAffected.EditStyle.Enabled = [False]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

Sample diagram is as follows:

**[]** 

{border="0"}

[] 

Figure 58: Flip Changing Event

**[]** 

{border="0"}

[] 

Figure 59: Flip Changed Event

{border="0"}

[] 

Figure 60: Rotation Changing Event

**[{border="0"}][]**

[] 

[Rotation Changed Event]

[]{#related-topics}

