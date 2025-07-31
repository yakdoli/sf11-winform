---
title: howtosetthegroupviewcontrolwithnoitemsselectedwhenthebuttonviewissettotrue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthegroupviewcontrolwithnoitemsselectedwhenthebuttonviewissettotrue.md
created_at: 2025-07-03
---






##### How to set the GroupView control with no Items selected when the Button View is set to True {#how-to-set-the-groupview-control-with-no-items-selected-when-the-button-view-is-set-to-true style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

When ButtonView is set to \'True\', the user cannot set the selected index to -1 to make it as not selected. As an alternative, set the Button View to \'False\' as a default and in the GroupView\'s **MouseDown** event or **GroupViewItemSelected** event, set the Button View to \'True\'.

 

The following code snippet illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Set Button View in the MouseDown event.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| [private][ [void] groupView1_MouseDown([object] sender, System.Windows.Forms.[MouseEventArgs] e) ] |
|                                                                                                                                                                                                                                                        |
| [{ ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [this][.groupView1.ButtonView = [true]; ]                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [} ]                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                             |
| [\' Set Button View in the MouseDown event. ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] groupView1_MouseDown([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.MouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                             |
| [Me][.groupView1.ButtonView = [True]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p662} 

 

[]{#related-topics}

