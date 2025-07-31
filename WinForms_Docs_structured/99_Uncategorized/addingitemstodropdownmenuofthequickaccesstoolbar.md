---
title: addingitemstodropdownmenuofthequickaccesstoolbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingitemstodropdownmenuofthequickaccesstoolbar.md
created_at: 2025-07-03
---






#### Adding Items to Drop-Down Menu of the Quick Access Toolbar {#adding-items-to-drop-down-menu-of-the-quick-access-toolbar style="tab-stops: 0pt"}

[] 

You can add items to the drop-down menu of the Quick Access Toolbar by using the QATMenuItems property of the the QuickAccessToolbar. The following code example illustrates how to add items to the drop-down menu of the Quick Access Toolbar by using this property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][Ribbon.QuickAccessToolBar][\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][QuickAccessToolBar][\>]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][syncfusion][:][QuickAccessToolBar.QATMenuItems][\>]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][RibbonButton][ Label][=\"Testing1\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][RibbonButton][ Label][=\"Testing2\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\</][syncfusion][:][QuickAccessToolBar.QATMenuItems][\>]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][QuickAccessToolBar][\>]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can also dynamically add items to the drop-down menu of the Quick Access Toolbar by using the Add method of the the QATMenuItems. The following code example illustrates how to add items to the drop-down menu of the Quick Access Toolbar by using this method.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [RibbonButton][ button1 = [new] [RibbonButton]();] |
|                                                                                                                                                                                                                         |
| [button1.Label = [\"Testing1\"];]                                                                                                           |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [RibbonButton][ button2 = [new] [RibbonButton]();] |
|                                                                                                                                                                                                                         |
| [button2.Label = [\"Testing2\"];]                                                                                                           |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [this][.ribbon1.QuickAccessToolBar.QATMenuItems.Add(button1);]                                     |
|                                                                                                                                                                                                                         |
| [this][.ribbon1.QuickAccessToolBar.QATMenuItems.Add(button2);]                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 847: Items Added to the Drop-Down Menu of the Quick Access Toolbar

[] 

See Also

[] 

[]{.UGHyperlink}

 

[]{#p446} 

[]{#related-topics}

