---
title: creatingtabcontrolextcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingtabcontrolextcontrol.md
created_at: 2025-07-03
---








  









### Creating TabControlExt control {#creating-tabcontrolext-control style="tab-stops: 0pt"}

[] 

There are two possible ways to create a simple TabControlExt control.

 

**Through Designer**

 

To create the TabControlExt control through designer, follow the below steps.

[] 

1.   Drag the TabControlExt control from the toolbox onto your WPF application.

2.   Set the properties for the TabControlExt in design mode by using the SmartTag feature.

[] 

{border="0"}

*[]* 

*[Figure ][991][: Design Time View of TabControlExt]*

*[]* 

Programmatically

[] 

TabControlExt control is created by using either XAML or C# code. The following lines of code can be used to create a TabControlExt control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\-- Adding TabControlExt \--\>]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][TabControlExt][ Name][=\"tabControlExt\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][TabControlExt][\>]                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [// Creating instance of the TabControlExt control]                                                                                                            |
|                                                                                                                                                                                                                                  |
| [TabControlExt][ tabControlExt = [new] [TabControlExt]();]  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [//Creating the instance of StackPanel]                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [StackPanel][ stackPanel = [new] [StackPanel]();          ] |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [//Adding control to the stackpanel]                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [stackPanel.Children.Add(tabControlExt); ]                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

*[Figure ][992][: TabControlExt Control]*

[] 


{border="0"}Note: To display the TabControlExt using C# code, you must already have a panel in which you are going to add the control. Otherwise, the control cannot be displayed.


 

[]{#p514} 

[]{#related-topics}

