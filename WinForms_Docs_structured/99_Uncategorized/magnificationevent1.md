---
title: magnificationevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\magnificationevent1.md
created_at: 2025-07-03
---






##### Magnification Event {#magnification-event style="tab-stops: 0pt"}

[] 

When the control is zoomed in or out, the magnification events will be fired displaying the old and new magnification factors.

[] 

Magnification Events are as follows,

[] 


  ------------------------ --------------------------------------------
  DiagramViewerEventSink   Description
  MagnificationChanged     Fired when magnification value is changed.
  ------------------------ --------------------------------------------


[] 

Data can be retrieved or set using the following members.

[] 


  -------------------------------- ----------------------------------------------------------------
  Magnification EventArgs Member   Description
  NewMagnification                 Returns the new magnification value.
  OriginalMagnification            Returns the old magnification value before the event occurred.
  -------------------------------- ----------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_Load([object] sender, [EventArgs] e)]                                         |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [    ((DiagramViewerEventSink)diagram1.EventSink).MagnificationChanged += [new] ViewMagnificationEventHandler(Form1_MagnificationChanged);]                                                      |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\[EventHandlerPriorityAttribute([true])\]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_MagnificationChanged(ViewMagnificationEventArgs evtArgs)]                                                               |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [    [MessageBox].Show([\"Old Factor: \"] + evtArgs.OriginalMagnification.ToString() + [\"New Factor: \"] + evtArgs.NewMagnification.ToString());] |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                         |
| [    [AddHandler] [DirectCast](diagram1.EventSink, DiagramViewerEventSink).MagnificationChanged, [AddressOf] Form1_MagnificationChanged]                                                             |
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

[  ]

Sample diagrams are as follows,

**[]** 

{border="0"}

**[]** 

Figure 101: Magnification Factor while Zoom In

**[]** 

{border="0"}

**[]** 

Figure 102: Magnification Factor while Zoom Out

 

[]{#p60} 

 

[]{#related-topics}

