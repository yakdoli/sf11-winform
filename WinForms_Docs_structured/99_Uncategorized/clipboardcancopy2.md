---
title: clipboardcancopy2.md
original_path: WinForms_Docs/99_Uncategorized/clipboardcancopy2.md
created_at: 2025-08-05
---






##### ClipboardCanCopy {#clipboardcancopy style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This event is triggered when some grid data is about to be copied to the clipboard. Inside this event handler, you can check for the data and range of cells that are going to be copied, and cancel the operation if you don't want to copy the data.

1.   The grid cell data and range of cells that are going to be moved to the clipboard can be accessed by using the **DataObject** and **RangeList** properties.

2.   If you don't want to move the data to the clipboard, you can cancel the operation by setting **e.Cancel** to **true**.

 

Properties

  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------
  **[Property]**                         **[Description][]**
  DataObject[]   Data to be copied.[]
  RangeList                                                    List of cell ranges that are selected for copying.
  Handled                                                      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

