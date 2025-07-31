---
title: outliningcollapseevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\outliningcollapseevent.md
created_at: 2025-07-03
---






#### OutliningCollapse Event {#outliningcollapse-event style="tab-stops: 0pt"}

 

This event is raised when a region collapses.

 

The event handler receives an argument of type **CollapseEventArgs**. The following CollapseEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------
  Member          Description
  CollapsedText   Gets / sets collapsed text.
  CollapseName    Gets / sets collapse name.
  Collapser       Gets / sets collapser.
  --------------- -----------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [private][ [void] editControl1_OutliningCollapse([object] sender, Syncfusion.Windows.Forms.Edit.[CollapseEventArgs] e)] |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Console][.WriteLine([\" OutliningCollapse event is raised \"]);]                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] editControl1_OutliningCollapse([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.[Forms.Edit.CollapseEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\" OutliningBeforeCollapse event is raised \"])]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p153} 

[]{#related-topics}

