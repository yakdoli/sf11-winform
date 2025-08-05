---
title: indicatormarginclickevent.md
original_path: WinForms_Docs/99_Uncategorized/indicatormarginclickevent.md
created_at: 2025-08-05
---






#### IndicatorMarginClick Event {#indicatormarginclick-event style="tab-stops: 0pt"}

 

This event is raised when the user clicks on the indicator margin area.

 

The event handler receives an argument of type **IndicatorClickEventArgs**. The following IndicatorClickEventArgs members provide information, specific to this event.

 


  ----------- --------------------------------------------
  Member      Description
  Bookmark    Gets clicked custom bookmark if available.
  LineIndex   Gets clicked line index.
  ----------- --------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] editControl1_IndicatorMarginClick([object] sender, Syncfusion.Windows.Forms.Edit.[IndicatorClickEventArgs] e)] |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [Console][.WriteLine([\" IndicatorMarginClick event is raised \"]);]                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] editControl1_IndicatorMarginClick([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine([\" IndicatorMarginClick event is raised \"])]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p141} 

[]{#related-topics}

