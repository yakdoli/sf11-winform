---
title: outliningtooltippopupevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\outliningtooltippopupevent.md
created_at: 2025-07-03
---






#### OutliningTooltipPopup Event {#outliningtooltippopup-event style="tab-stops: 0pt"}

 

This event is raised when the outlining tooltip is shown.

 

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
| [private][ [void] editControl1_OutliningTooltipPopup([object] sender, Syncfusion.Windows.Forms.Edit.[CollapseEventArgs] e)] |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\" OutliningTooltipPopup event is raised \"]);]                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] editControl1_OutliningTooltipPopup([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.[Forms.Edit.CollapseEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\" OutliningTooltipPopup event is raised \"])]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p157} 

[]{#related-topics}

