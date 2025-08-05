---
title: indicatormargindoubleclickevent.md
original_path: WinForms_Docs/99_Uncategorized/indicatormargindoubleclickevent.md
created_at: 2025-08-05
---






#### IndicatorMarginDoubleClick Event {#indicatormargindoubleclick-event style="tab-stops: 0pt"}

 

This event is raised when the user double-clicks on the indicator margin area.

 

The event handler receives an argument of type **IndicatorClickEventArgs**. The following IndicatorClickEventArgs members provide information, specific to this event.

 


  ----------- --------------------------------------------
  Member      Description
  Bookmark    Gets clicked custom bookmark if available.
  LineIndex   Gets clicked line index.
  ----------- --------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_IndicatorMarginDoubleClick([object] sender, Syncfusion.Windows.Forms.Edit.[IndicatorClickEventArgs] e)] |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [Console][.WriteLine([\" IndicatorMarginDoubleClick event is raised \"]);]                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_IndicatorMarginDoubleClick([ByVal] sender [As] [Object], [ByVal] e Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\" IndicatorMarginDoubleClick event is raised \"])]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p142} 

[]{#related-topics}

