---
title: howtopreventthenodesfrombeingrotated.md
original_path: WinForms_Docs/99_Uncategorized/howtopreventthenodesfrombeingrotated.md
created_at: 2025-08-05
---








  









## How To Prevent the Nodes From Being Rotated {#how-to-prevent-the-nodes-from-being-rotated style="tab-stops: 0pt"}

[] 

This can be done by raising the **Diagram.Model.EventSink.RotationChanging** event and cancelling the operation.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [this][.diagram1.Model.EventSink.RotationChanging += [new] [RotationChangingEventHandler](EventSink_RotationChanging); ] |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [void][ EventSink_RotationChanging([RotationChangingEventArgs] evtArgs) ]                                                                     |
|                                                                                                                                                                                                                                                         |
| [{ ]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                         |
| [    evtArgs.Cancel = [true]; ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [Me][.diagram1.Model.EventSink.RotationChanging += [New] RotationChangingEventHandler(EventSink_RotationChanging) ]                                                     |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] EventSink_RotationChanging([ByVal] evtArgs [As] Syncfusion.Windows.Forms.Diagram.RotationChangingEventArgs)] |
|                                                                                                                                                                                                                                                                                   |
| [evtArgs.Cancel = [True]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p89} 

 

[]{#related-topics}

