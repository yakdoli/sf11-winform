---
title: settingtablistcontextmenuandtabitemcontextmenufortabitem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingtablistcontextmenuandtabitemcontextmenufortabitem.md
created_at: 2025-07-03
---






#### Setting TabListContextMenu and TabItemContextMenu For Tab Item {#setting-tablistcontextmenu-and-tabitemcontextmenu-for-tab-item style="tab-stops: 0pt"}

[] 

In TabControlExt, context menu can be displayed for the Tab Items by setting the **ShowTabItemContextMenu** property to **True**. This is a dependency property which is used to enable or disable the context menu for the Tab Item.

 

The context menu of the Tab Item has the following menu items.

[] 

[·      ]Close

[·      ]Close All But This

[·      ]Close All

 

To enable the Tab Item context menu, use the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<!\-- Adding TabControlExt  \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][TabControlExt][ Name][=\"tabControlExt\"][ ShowTabItemContextMenu][=\"True\"\>]                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt1\"][ Header][=\"TabItemExt1\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\</][syncfusion][:][TabItemExt][\>]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt2\"][ Header][=\"TabItemExt2\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\</][syncfusion][:][TabItemExt][\>]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][syncfusion][:][TabControlExt][\>]                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Creating instance of the TabControlExt control]                                                                                                           |
|                                                                                                                                                                                                                                 |
| [TabControlExt][ tabControlExt = [new] [TabControlExt]();] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [//Creating the instance of StackPanel]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [StackPanel][ stackPanel = [new] [StackPanel]();]          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Creating instance of the TabItemExt ]                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [TabItemExt][ tabItemExt1 = [new] [TabItemExt]();]         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Setting header of the TabItemExt]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [tabItemExt1.Header = [\"TabItemExt1\"];]                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Adding TabItemExt to TabControlExt]                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [tabControlExt.Items.Add(tabItemExt1);            ]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Changing the Visibility of Scroll button ]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [tabControlExt.ShowTabItemContextMenu = [true]; ]                                                                                                      |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Adding control to the StackPanel]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [stackPanel.Children.Add(tabControlExt);]                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

*[Figure ][1005][: ShowTabItemContextMenu = \"True\"]*

[] 

Tab Item Context Menu Events

[] 

OnCloseOtherTabs Event

[] 

This event is handled when the \'Close All But This\' menu item in the TabItemContextMenu is clicked.

[] 

**OnCloseAllTabs Event**

[] 

This event is handled when the \'Close All\' menuitem in TabItemContextMenu is clicked.

[] 

OnCloseButtonClick Event

 

This event is handled when the \'Close\' menu item in TabItemContextMenu is clicked.

[] 

See Also

[] 

[]{.UGHyperlink}

 

[]{#p531} 

[]{#related-topics}

