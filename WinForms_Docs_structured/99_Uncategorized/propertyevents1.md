---
title: propertyevents1.md
original_path: WinForms_Docs/99_Uncategorized/propertyevents1.md
created_at: 2025-08-05
---






##### Property Events {#property-events style="tab-stops: 0pt"}

[] 

Each node has different properties (Name,Color,Size etc). The below events are handled when changing these properties.

 

Property Events are as follows.

[] 


  ------------------- ------------------------------------------------------
  DocumentEventSink   Description
  PropertyChanged     Triggered after the property of any node is changed.
  PropertyChanging    Triggered when the property value is changed.
  ------------------- ------------------------------------------------------


[] 

Data can be retrieved or set using the following members.

[] 


  ----------------------------------- ------------------------------------------------------
  PropertyChanging EventArgs Member   Description
  Cancel                              Cancels the PropertyChanged event.
  NewValue                            Returns the new value assigned to the property.
  PropertyContainer                   Returns the container for the property.
  PropertyName                        Returns name of the property whose value is changed.
  ----------------------------------- ------------------------------------------------------


[] 


  ---------------------------------- ----------------------------------------------------------
  PropertyChanged EventArgs Member   Description
  NodeAffected                       Returns the name of the node whose property is changed.
  PropertyName                       Returns the name of the property whose value is changed.
  ---------------------------------- ----------------------------------------------------------


[] 

Programmatically the events are written as follows,

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [public][ [void] Form1_Load([object] sender, [EventArgs] e)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [    ((DocumentEventSink)model1.EventSink).PropertyChanged += [new] Syncfusion.Windows.Forms.Diagram.PropertyChangedEventHandler]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [        (Form1_PropertyChanged);]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [    ((DocumentEventSink)model1.EventSink).PropertyChanging += [new] [PropertyChangingEventHandler](Form1_PropertyChanging);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [private][ [void] Form1_PropertyChanged(Syncfusion.Windows.Forms.Diagram.PropertyChangedEventArgs evtArgs)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [    [MessageBox].Show([\"PropertyChanged event is fired\"] + [\"\\n\"] + [\"Property Name: \"] + evtArgs.PropertyName);]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [private][ [void] Form1_PropertyChanging(Syncfusion.Windows.Forms.Diagram.PropertyChangingEventArgs eprop)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [    [MessageBox].Show([\"PropertyChanging event is fired\"] + [\"\\n\"] + [\"Property Name: \"] + eprop.PropertyName + [\"\\n\"] + [\"new                      Value: \"] + eprop.NewValue);] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
| [Public][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).PropertyChanged, [AddressOf] Form1_PropertyChanged]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                           |
| [    [AddHandler] [DirectCast](model1.EventSink, DocumentEventSink).PropertyChanging, [AddressOf] Form1_PropertyChanging]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] Form1_PropertyChanged([ByVal] evtArgs [As] Syncfusion.Windows.Forms.Diagram.PropertyChangedEventArgs)]                                                               |
|                                                                                                                                                                                                                                                                                                                                           |
| [    MessageBox.Show(([\"PropertyChanged event is fired\"] & vbLf & [\"Property Name: \"]) + evtArgs.PropertyName)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] Form1_PropertyChanging([ByVal] eprop [As] Syncfusion.Windows.Forms.Diagram.PropertyChangingEventArgs)]                                                               |
|                                                                                                                                                                                                                                                                                                                                           |
| [    MessageBox.Show((([\"PropertyChanging event is fired\"] & vbLf & [\"Property Name: \"]) + eprop.PropertyName & vbLf & [\"new \"] & vbTab & vbTab & vbTab & vbTab & [\"Value: \"]) + eprop.NewValue)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagrams are as follows.

**[]** 

{border="0"}

**[]** 

Figure 115: Property Changing Event

**[]** 

{border="0"}

**[]** 

Figure 116: Property Changed Event

 

[]{#p67} 

 

[]{#related-topics}

