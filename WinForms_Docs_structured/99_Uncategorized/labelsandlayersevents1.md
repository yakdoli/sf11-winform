---
title: labelsandlayersevents1.md
original_path: WinForms_Docs/99_Uncategorized/labelsandlayersevents1.md
created_at: 2025-08-05
---






##### Labels And Layers Events {#labels-and-layers-events style="tab-stops: 0pt"}

[] 

The below mentioned events are fired, when adding or removing the labels and layers to or from the diagram.

 

The following table shows the label events:

[] 


  ------------------- -----------------------------------------------
  DocumentEventSink   Description
  LabelsChanged       Triggered when labels are added.
  LayersChanged       Triggered when layers are added to the model.
  ------------------- -----------------------------------------------


[] 

Data can be retrieved or set using the following members.

[] 


+-----------------------------------+-------------------------------------------------------------------------------+
| Label / Layers EventArgs Member   | Description                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| Cancel                            | Cancels the LabelChanging event.                                              |
+-----------------------------------+-------------------------------------------------------------------------------+
| ChangeType                        | It returns the following possible values:                                     |
|                                   |                                                                               |
|                                   | [·      ]Insert-Whether the label is inserted    |
|                                   |                                                                               |
|                                   | [·      ]Remove--Whether the label is removed    |
+-----------------------------------+-------------------------------------------------------------------------------+
| Element                           | Returns whether the head or tail end is moved.                                |
+-----------------------------------+-------------------------------------------------------------------------------+
| Elements                          | Returns the elements collection on which the event occurs.                    |
+-----------------------------------+-------------------------------------------------------------------------------+
| Index                             | Returns the zero-based index into the collection on which the event occurred. |
+-----------------------------------+-------------------------------------------------------------------------------+
| Owner                             | Returns the owner object.                                                     |
+-----------------------------------+-------------------------------------------------------------------------------+


[] 

Label Events

[] 

Whenever labels are added to the label collection, this event will be triggered.

 

Programmatically, the events are written as follows:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                         |
|                                                                                                                                                                                                                  |
| [public][ [void] Form1_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [    ((DocumentEventSink)model1.EventSink).LabelsChanged += [new] CollectionExEventHandler(Form1_LabelsChanged);]                                       |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [void][ Form1_LabelsChanged(CollectionExEventArgs evtArgs)]                                                                 |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [    [MessageBox].Show([\"LabelsChanged event is fired\"] + evtArgs.ChangeType.ToString() + evtArgs.Owner.ToString());]          |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [Public][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).LabelsChanged, [AddressOf] Form1_LabelsChanged]                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_LabelsChanged([ByVal] evtArgs [As] CollectionExEventArgs)]                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"LabelsChanged event is fired\"] & evtArgs.ChangeType.ToString()) + evtArgs.Owner.ToString())]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Layers Events

[] 

Programmatically, the events are written as follows:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [public][ [void] Form1_Load([object] sender, [EventArgs] e)]                                   |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    ((DocumentEventSink)model1.EventSink).LayersChanged += [new] CollectionExEventHandler(Form1_LayersChanged);]                                                                         |
|                                                                                                                                                                                                                                                    |
| [    Layer layer0 = [new] Layer();]                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [    [this].diagram1.Model.Layers.Add(layer0);]                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [    layer0.Enabled = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    layer0.Visible = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [void][ Form1_LayersChanged(CollectionExEventArgs evtArgs)]                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    [MessageBox].Show([\"LayersChanged event is fired.\"] + [\"\\n\"] + [\"Owner: \"] + evtArgs.Owner.ToString());] |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [Public][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                        |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).LayersChanged, [AddressOf] Form1_LayersChanged]                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [    [Dim] layer0 [As] [New] Layer()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [    [Me].diagram1.Model.Layers.Add(layer0)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [    layer0.Enabled = [True]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [    layer0.Visible = [True]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] Form1_LayersChanged([ByVal] evtArgs [As] CollectionExEventArgs)]                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show(([\"LayersChanged event is fired.\"] & vbLf & [\"Owner: \"]) + evtArgs.Owner.ToString())]                                                                                                       |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagram is as follows,

**[]** 

{border="0"}

**[]** 

Figure 117: LayersChanged Event

 

[]{#p68} 

[]{#related-topics}

