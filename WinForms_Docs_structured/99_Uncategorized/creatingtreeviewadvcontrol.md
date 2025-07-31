---
title: creatingtreeviewadvcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingtreeviewadvcontrol.md
created_at: 2025-07-03
---








  









### Creating TreeViewAdv control {#creating-treeviewadv-control style="tab-stops: 0pt"}

[] 

There are two possible ways to create a simple TreeViewAdv control.

[] 

Through Designer

[] 

To create the TreeViewAdv control through designer, do the below steps

[] 

1.   Drag the TreeViewAdv control from the toolbox onto your WPF application.

[] 

{border="0"}

[] 

 Figure 1113:Dragging TreeViewAdv from the Toolbox

[] 

2.   Set the properties for the TreeViewAdv control by using the Smart Tag feature.

[] 

Programmatically

[] 

TreeViewAdv control is created by using either XAML or C# code. Use the below code to create a TreeViewAdv control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\-- Adding TreeViewAdv \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][TreeViewAdv][ Name][=\"treeViewAdv\"\>]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<!\-- Adding TreeViewItemAdv \--\>]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Marital Status\"\>]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Single\"/\>]                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Married\"/\>]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Married with Children\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\</][syncfusion][:][TreeViewItemAdv][\>]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Baby Vaccines\"\>]              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Hepatitis B\"/\>]           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Tetanus\"/\>]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Polio\"/\>]                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Measles\"/\>]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\</][syncfusion][:][TreeViewItemAdv][\>]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Country Information\"/\>]       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][TreeViewAdv][\>]                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Creating an instance of TreeViewAdv]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [TreeViewAdv][ treeViewAdv = [new] [TreeViewAdv]();]             |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Creating an instance of TreeViewItem]                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [TreeViewItemAdv][ treeViewItemAdv = [new] [TreeViewItemAdv]();] |
|                                                                                                                                                                                                                                       |
| [treeViewItemAdv.Header = [\"Marital Status\"];]                                                                                                          |
|                                                                                                                                                                                                                                       |
| [\...\...]                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| [\...\...]                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| [\...\...]                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Adding treeview item to TreeView]                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [treeViewAdv.Items.Add(treeViewItemAdv);]                                                                                                                                         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Adding content to the window]                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [this][.Content = treeViewAdv;]                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To display the TreeViewAdv using C# code, you must already have a panel in which you are going to add the control. Otherwise, the control cannot be displayed.


[] 

The following screen shot shows the TreeViewAdv control.

[] 

{border="0"}

*[]* 

 Figure 1114:TreeViewAdv Control

 

[]{#p574} 

[]{#related-topics}

