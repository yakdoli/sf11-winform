---
title: howtodisablethedropdownpopup3.md
original_path: WinForms_Docs/99_Uncategorized/howtodisablethedropdownpopup3.md
created_at: 2025-08-05
---






##### How to disable the DropDown Popup? {#how-to-disable-the-dropdown-popup style="tab-stops: 0pt"}

The DropDown can be disabled by cancelling the event **DropDownOpening**.

The following code snippet describes disabling the DropDown:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **\[C#\]**]                                                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [public][ MainPage()]                                                                                                                    |
|                                                                                                                                                                                                                               |
| [{k]                                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [    InitializeComponent();]                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [    button.DropDownOpening += [new] [CancelEventHandler](button_DropDownOpening);]                                                          |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [void][ button_DropDownOpening([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [    e.Cancel = [true];]                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [    [//DropDown will not open.]]                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

