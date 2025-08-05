---
title: autolabelevent.md
original_path: WinForms_Docs/99_Uncategorized/autolabelevent.md
created_at: 2025-08-05
---






##### AutoLabel Event {#autolabel-event style="tab-stops: 0pt"}

[] 

A detailed explanation about the **PropertyChanged** event is given in the following section.

[] 


  ----------------- ---------------------------------------------------------------------------------
  AutoLabel Event   Description
  PropertyChanged   This event is fired when the LabeledControl, Gap or Position properties change.
  ----------------- ---------------------------------------------------------------------------------


###### []{#p752}3.3.10.1.4.1        PropertyChanged Event {#propertychanged-event style="tab-stops: 0pt"}

[] 

This event is fired when the **LabeledControl**, **Gap** or **Position** properties of this class change.

 

The event handler receives an argument of type **SyncfusionPropertyChangedEventArgs** containing data related to this event.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [private][ [void] autoLabel1_PropertyChanged([object] sender, Syncfusion.ComponentModel.[SyncfusionPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\" PropertyChanged event is raised\"]);]                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] autoLabel1_PropertyChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.ComponentModel.SyncfusionPropertyChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine([\" PropertyChanged event is raised\"])]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

