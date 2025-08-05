---
title: clipboardcopy1.md
original_path: WinForms_Docs/99_Uncategorized/clipboardcopy1.md
created_at: 2025-08-05
---






#####   ClipboardCopy {#clipboardcopy style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This event is fired when some grid data is being copied to the clipboard. Inside this event handler, you can check for the data and range of cells being copied and cancel the operation if you don't want to copy the data. You can also provide custom formatted data for copying to the clipboard. It receives an argument of type **GridCutCopyPasteEventArgs** containing data related to this event. The following are the event argument properties.

 

Properties

  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------
  **[Property]**                         **[Description][]**
  DataObject[]   Data to be copied.[]
  RangeList                                                    List of cell ranges that are selected for copying.
  Handled                                                      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

