---
title: paintusermarginevent.md
original_path: WinForms_Docs/99_Uncategorized/paintusermarginevent.md
created_at: 2025-08-05
---






#### PaintUserMargin Event {#paintusermargin-event style="tab-stops: 0pt"}

 

This event occurs when the user margin has to be painted.

 

The event handler receives an argument of type **PaintEventArgs**. The following PaintEventArgs members provide information, specific to this event.

 


  --------------- -----------------------------------------------
  Member          Description
  ClipRectangle   Gets the rectangle area to paint.
  Graphics        Gets the graphics that will be used to paint.
  --------------- -----------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [private][ [void] editControl1_PaintUserMargin([object] sender, [PaintEventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [Console][.WriteLine([\" PaintUserMargin event is raised \"]);]                                                              |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] editControl1_PaintUserMargin([ByVal] sender [As] [Object], [ByVal] e [As] PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\" PaintUserMargin event is raised \"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p180} 

[]{#related-topics}

