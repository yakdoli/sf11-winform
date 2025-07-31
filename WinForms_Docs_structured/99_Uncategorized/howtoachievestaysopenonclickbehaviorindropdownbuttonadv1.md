---
title: howtoachievestaysopenonclickbehaviorindropdownbuttonadv1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoachievestaysopenonclickbehaviorindropdownbuttonadv1.md
created_at: 2025-07-03
---






##### How to achieve "StaysOpenOnClick" behavior in DropDownButtonAdv? {#how-to-achieve-staysopenonclick-behavior-in-dropdownbuttonadv style="tab-stops: 0pt"}

The DropDown open state can be maintained, when we cancel the **DropDownClosing** event:

The following code snippet describes disabling the DropDown:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **\[C#\]**]                                                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [public][ MainPage()]                                                                                                                    |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [     InitializeComponent();]                                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [     button.DropDownClosing += [new] [CancelEventHandler](button_DropDownClosing);]                                                         |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [void][ button_DropDownClosing([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [     e.Cancel = [true];]                                                                                                                                            |
|                                                                                                                                                                                                                               |
| [     [//DropDown will not close.]]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

