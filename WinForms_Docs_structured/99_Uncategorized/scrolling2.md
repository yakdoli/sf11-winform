---
title: scrolling2.md
original_path: WinForms_Docs/99_Uncategorized/scrolling2.md
created_at: 2025-08-05
---








  









### Scrolling {#scrolling style="tab-stops: 0pt"}

Essential Grid now allows you to specify the required width and height for a grid. You can scroll through the grid manually. Also, the width property in the ColumnBuilder can be used to set the width for individual grid columns in both design time and run time.

Properties

 

 


  -------------------------- ----------------------------------------------------------- ------------------ ------------------ --------------------------------------------------
  Property                   Description                                                 Type of property   Value it accepts   Any other dependencies/sub-properties associated
  AllowScrolling             Enables/disables the scroll bars in a grid.                 Boolean            True/False         NA
  Width                      Gets or sets the width of grid.                             Integer                               NA
  Height                     Gets or sets the height of grid.                            Integer                               NA
  IGridColumnBuilder.Width   Gets or sets the width of individual column in view page.   Integer                               NA
  -------------------------- ----------------------------------------------------------- ------------------ ------------------ --------------------------------------------------


 

Methods

 

 


  ---------------------- ------------ ------------------------- ---------------------------------------------------
  Method                 Parameters   Return type               Description
  AllowScrolling(bool)   bool         IScrollingBuilder         Used to enable/disable the scroll bars in a grid.
  Width(int)             integer      IScrollingBuilder         Used to  set the grid width.
  Height(int)            integer      IScrollingBuilder         Used to set the gridcontent height.
  width(int)             integet      IGridColumnBuilder\<T\>   Used to set the column width.
  ---------------------- ------------ ------------------------- ---------------------------------------------------


 

Essential Grid's scrolling feature allows you to scroll through the grid manually.

Another feature that we have implemented under scrolling is that of virtual scrolling.

More:







