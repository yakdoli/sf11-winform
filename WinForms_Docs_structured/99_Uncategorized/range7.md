---
title: range7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\range7.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Range {#range style="tab-stops: 0pt"}

This feature allows you to set the minimum, maximum and the increment values of the ProgressBar.

The Minimum value specifies the value at which the progress bar shows the process to have started.

The Maximum value specifies the value at which the progress bar shows the process to have completed.

The Step value specifies the value at which the progress bar shows the next step of the process to have started---it is an increment value.

The Value property specifies the current value of the Progress Bar.

Properties

  ----------- ----------------------------------------------------------------------------- ------------------ ------------------- ------------
  Name        Description                                                                   Type of property   Value it accepts    Dependency
  Minimum     Sets the minimum allowable value.                                             int                0 to int.MaxValue   NA
  Maximum     Sets the maximum allowable value.                                             int                0 to int.MaxValue   NA
  StepValue   Sets the step value by which the progress bar value increases or decreases.   int                0 to int.MaxValue   NA
  Value       Sets the value of the progress bar when loading.                              int                0 to int.MaxValue   NA
  ----------- ----------------------------------------------------------------------------- ------------------ ------------------- ------------

 

You can implement the range of the progress bar in the following ways:

More:







