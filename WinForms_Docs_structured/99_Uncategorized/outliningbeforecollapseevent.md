---
title: outliningbeforecollapseevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\outliningbeforecollapseevent.md
created_at: 2025-07-03
---






#### OutliningBeforeCollapse Event {#outliningbeforecollapse-event style="tab-stops: 0pt"}

 

This event is raised before a region is about to collapse.

 

The event handler receives an argument of type **OutliningEventArgs**. The following OutliningEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------------------------------------------------------
  Member          Description
  Cancel          Gets / sets value indicating whether the user cancels the underlying event.
  CollapsedText   Gets / sets collapsed text.
  CollapseName    Gets / sets collapse name.
  Collapser       Gets / sets collapser.
  --------------- -----------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [private][ [void] editControl1_OutliningBeforeCollapse([object] sender, Syncfusion.Windows.Forms.Edit.[OutliningEventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [Console][.WriteLine([\" OutliningBeforeCollapse event is raised \"]);]                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] editControl1_OutliningBeforeCollapse([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.OutliningEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine([\" OutliningBeforeCollapse event is raised \"])]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p151} 

[]{#related-topics}

