---
title: throughc1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughc1.md
created_at: 2025-07-03
---






#### Through C# {#through-c style="tab-stops: 0pt"}

To create a GroupBar control in C#, include the following namespace to the directives list.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                             |
| [using][ Syncfusion.Windows.Tools.Controls;] |
|                                                                                                                                                             |
|                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Next, create the GroupBar as follows.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                   |
| [       ][     [GroupBar] gBar = [new] [GroupBar]();]                                                                                      |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
| [            [GroupBarItem] gBarItem1 = [new] [GroupBarItem]() { HeaderText =[\"NewGroupBarItem1\"],                                   IsSelected = [true] };] |
|                                                                                                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                   |
| [            [GroupView] gView = [new] [GroupView]();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                   |
| [            [GroupViewItem] gViewItem = [new] [GroupViewItem]() { Text=[\"New GroupViewItem\"]};]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                   |
| [            gView.Items.Add(gViewItem);]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
| [            gBarItem1.Content = gView;]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| [            ]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                   |
| [            [GroupBarItem] gBarItem2 = [new] [GroupBarItem]() { HeaderText=[\"NewGroupBarItem2\"]};]                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
| [            [GroupBarItem] gBarItem3 = [new] [GroupBarItem]() { HeaderText=[\"NewGroupBarItem3\"]};]                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
| [            gBar.Items.Add(gBarItem1);]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| [            gBar.Items.Add(gBarItem2);]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| [            gBar.Items.Add(gBarItem3);]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

This will generate the following GroupBar control.

{border="0"}

Figure 540: GroupBarControl Created with C#

 

 

 

 

 

[]{#p337} 

[]{#related-topics}

