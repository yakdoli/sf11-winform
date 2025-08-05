---
title: outliningtooltipcloseevent.md
original_path: WinForms_Docs/99_Uncategorized/outliningtooltipcloseevent.md
created_at: 2025-08-05
---






#### OutliningTooltipClose Event {#outliningtooltipclose-event style="tab-stops: 0pt"}

 

This event is raised when the outlining tooltip is closed.

 

The event handler receives an argument of type **CollapseEventArgs**. The following CollapseEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------
  Member          Description
  CollapsedText   Gets / sets collapsed text.
  CollapseName    Gets / sets collapse name.
  Collapser       Gets / sets collapser.
  --------------- -----------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [private][ [void] editControl1_OutliningTooltipClose([object] sender, Syncfusion.Windows.Forms.Edit.[CollapseEventArgs] e)] |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\" OutliningTooltipClose event is raised \"]);]                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] editControl1_OutliningTooltipClose([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.[Forms.Edit.CollapseEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\" OutliningTooltipClose event is raised \"])]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p156} 

[]{#related-topics}

