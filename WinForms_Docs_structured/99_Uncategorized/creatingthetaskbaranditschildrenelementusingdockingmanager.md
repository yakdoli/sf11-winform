---
title: creatingthetaskbaranditschildrenelementusingdockingmanager.md
original_path: WinForms_Docs/99_Uncategorized/creatingthetaskbaranditschildrenelementusingdockingmanager.md
created_at: 2025-08-05
---






#### Creating the Taskbar and its children element using Docking Manager {#creating-the-taskbar-and-its-children-element-using-docking-manager style="tab-stops: 0pt"}

There are two possible ways to create a simple TaskBar control.

[] 

Through Designer

To create the TaskBar control through designer, do the following steps:

 

1.   Drag the TaskBar control from the toolbox onto your WPF application.

[] 

{border="0"}

[] 

Figure 1040: Dragging TaskBar Control from the Toolbox

***[]*** 

2.   Set the properties for the TaskBar in design mode by using the Smart Tag feature.

 

Programmatically

[] 

TaskBar control is created by using either XAML or C# code. The following lines of code can be used to create a TaskBar control.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<!\-- Adding TaskBar \--\>]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][TaskBar][ Name][=\"taskBar\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][TaskBar][\>]                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                                               |
| [//Creating an instance for TaskBar]                                                                                                        |
|                                                                                                                                                                                                               |
| [TaskBar][ taskBar = [new] [TaskBar]();] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [//Adding TaskBar as content of window]                                                                                                     |
|                                                                                                                                                                                                               |
| [this][.Content = taskBar; ]                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To display the TaskBar by using C# code, you must already have a panel in which you are going to add the control. Otherwise, the control cannot be displayed.

 


The following screen shot shows the TaskBar control.

 

{border="0"}

*[]* 

Figure 1041:TaskBar Control

 

[]{#p555} 

[]{#related-topics}

