---
title: outliningexpandevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\outliningexpandevent.md
created_at: 2025-07-03
---






#### OutliningExpand Event {#outliningexpand-event style="tab-stops: 0pt"}

[] 

This event is raised when a region expands.

 

The event handler receives an argument of type **CollapseEventArgs**. The following CollapseEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------
  Member          Description
  CollapsedText   Gets / sets collapsed text.
  CollapseName    Gets / sets collapse name.
  Collapser       Gets / sets collapser.
  --------------- -----------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [private][ [void] editControl1_OutliningExpand([object] sender, Syncfusion.Windows.Forms.Edit.[CollapseEventArgs] e)] |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [Console][.WriteLine([\" OutliningExpand event is raised \"]);]                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] editControl1_OutliningExpand([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.[Forms.Edit.CollapseEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\" OutliningExpand event is raised \"])]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p154} 

[]{#related-topics}

