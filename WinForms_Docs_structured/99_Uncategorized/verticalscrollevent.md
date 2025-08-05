---
title: verticalscrollevent.md
original_path: WinForms_Docs/99_Uncategorized/verticalscrollevent.md
created_at: 2025-08-05
---






#### VerticalScroll Event {#verticalscroll-event style="tab-stops: 0pt"}

 

This event is raised when the user scrolls the window vertically.

 

The event handler receives an argument of type **ScrollEventArgs**. The following ScrollEventArgs members provide information specific to this event.

 


  ------------------- -----------------------------------------------------------------------------
  Member              Description
  NewValue            Gets / sets the new System.Windows.Forms.ScrollBar.Value for the scrollbar.
  OldValue            Gets / sets the old System.Windows.Forms.ScrollBar.Value for the scrollbar.
  ScrollOrientation   Gets the scrollbar orientation that raised the scroll event.
  Type                Gets the type of scroll event that occurred.
  ------------------- -----------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [private][ [void] editControl1_VerticalScroll([object] sender, [ScrollEventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [Console][.WriteLine([\" VerticalScroll event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] editControl1_VerticalScroll([ByVal] sender [As] [Object], [ByVal] e [As] ScrollEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\" VerticalScroll event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p169} 

[]{#related-topics}

