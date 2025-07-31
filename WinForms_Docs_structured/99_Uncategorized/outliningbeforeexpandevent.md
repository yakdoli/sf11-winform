---
title: outliningbeforeexpandevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\outliningbeforeexpandevent.md
created_at: 2025-07-03
---






#### OutliningBeforeExpand Event {#outliningbeforeexpand-event style="tab-stops: 0pt"}

 

This event is raised before a region is about to expand.

 

The event handler receives an argument of type **OutliningEventArgs**. The following OutliningEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------------------------------------------------------
  Member          Description
  Cancel          Gets / sets value indicating whether the user cancels the underlying event.
  CollapsedText   Gets / sets collapsed text.
  CollapseName    Gets / sets collapse name.
  Collapser       Gets / sets collapser.
  --------------- -----------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [private][ [void] editControl1_OutliningBeforeExpand([object] sender, Syncfusion.Windows.Forms.Edit.[OutliningEventArgs] e)] |
|                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [Console][.WriteLine([\" OutliningBeforeExpand event is raised \"]);]                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_OutliningBeforeExpand([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.OutliningEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\" OutliningBeforeExpand event is raised \"])]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p152} 

[]{#related-topics}

