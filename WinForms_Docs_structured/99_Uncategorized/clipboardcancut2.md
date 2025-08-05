---
title: clipboardcancut2.md
original_path: WinForms_Docs/99_Uncategorized/clipboardcancut2.md
created_at: 2025-08-05
---






##### ClipboardCanCut {#clipboardcancut style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This event is triggered when some grid data is about to be moved to the clipboard. Inside this event handler, you can check for the data and range of cells going to be moved and cancel the operation if you do not want to move the data. It receives an argument of type **GridCutCopyPasteEventArgs** containing data related to this event. The following are the event argument properties.

 

Properties*[]*

  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------
  **[Property]**                         **[Description][]**
  DataObject[]   Data to be moved.[]
  RangeList                                                    List of cell ranges that are selected for moving.
  Handled                                                      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

