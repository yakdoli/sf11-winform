---
title: unreachabletextfoundevent.md
original_path: WinForms_Docs/99_Uncategorized/unreachabletextfoundevent.md
created_at: 2025-08-05
---








  









### UnreachableTextFound Event {#unreachabletextfound-event style="tab-stops: 0pt"}

 

This event occurs when text in a hidden block is found and this block can\'t be expanded due to user\'s canceling.

 

The event handler receives an argument of type **UnreachableTextFoundEventArgs**. The following UnreachableTextFoundEventArgs members provide information, specific to this event.

[] 


  ---------------- ---------------------------------------------
  Member           Description
  ContinueSearch   Indicates whether search must be continued.
  Point            Point of the location of unreachable text.
  Text             Searched text.
  ---------------- ---------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_UnreachableTextFound([object] sender, Syncfusion.Windows.Forms.Edit.[UnreachableTextFoundEventArgs] e)] |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [Console][.WriteLine([\" UnreachableTextFound event is raised \"]);]                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] editControl1_UnreachableTextFound([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.UnreachableTextFoundEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\" UnreachableTextFound event is raised \"])]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p175} 

[]{#related-topics}

