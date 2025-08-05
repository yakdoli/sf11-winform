---
title: magnificationevent.md
original_path: WinForms_Docs/99_Uncategorized/magnificationevent.md
created_at: 2025-08-05
---






#### Magnification Event {#magnification-event style="tab-stops: 0pt"}

[] 

When the control is zoomed in or out, the magnification events will be fired displaying the old and new magnification factors.

[] 

Magnification Events are as follows:

[] 


+-----------------------------------+--------------------------------------------+
|                                   |                                            |
|                                   |                                            |
| DiagramViewerEventSink            | Description                                |
+-----------------------------------+--------------------------------------------+
| MagnificationChanged              | Fired when magnification value is changed. |
+-----------------------------------+--------------------------------------------+


[] 

Data can be retrieved or set using the following members.

[] 


+-----------------------------------+----------------------------------------------------------------+
|                                   |                                                                |
|                                   |                                                                |
| Magnification EventArgs Member    | Description                                                    |
+-----------------------------------+----------------------------------------------------------------+
| NewMagnification                  | Returns the new magnification value.                           |
+-----------------------------------+----------------------------------------------------------------+
| OriginalMagnification             | Returns the old magnification value before the event occurred. |
+-----------------------------------+----------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_Load([object] sender, [EventArgs] e)]                         |
|                                                                                                                                                                                                                                                                           |
| [{][]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| [    ((DiagramViewerEventSink)diagramWeb1.EventSink).MagnificationChanged += [new] ViewMagnificationEventHandler(Form1_MagnificationChanged);]                                                   |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [\[EventHandlerPriorityAttribute([true])\]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_MagnificationChanged(ViewMagnificationEventArgs evtArgs)]                                               |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [    [MessageBox].Show([\"Old Factor: \"] + evtArgs.OriginalMagnification.ToString() + [\"New Factor: \"] + evtArgs.NewMagnification.ToString());] |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                         |
| [    [AddHandler] [DirectCast](diagramWeb1.EventSink, DiagramViewerEventSink).MagnificationChanged, [AddressOf] Form1_MagnificationChanged]                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [\<EventHandlerPriorityAttribute([True])\> \_]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Form1_MagnificationChanged([ByVal] evtArgs [As] ViewMagnificationEventArgs)]                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [    MessageBox.Show(([\"Old Factor: \"] & evtArgs.OriginalMagnification.ToString() & [\"New Factor: \"]) + evtArgs.NewMagnification.ToString())]                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagram is as follows:

**[]** 

{border="0"}

[] 

Figure 52: Magnification Factor while Zoom In

**[]** 

{border="0"}

[] 

Figure 53: Magnification Factor while Zoom Out

[]{#related-topics}

