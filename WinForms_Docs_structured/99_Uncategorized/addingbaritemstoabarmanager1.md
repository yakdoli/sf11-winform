---
title: addingbaritemstoabarmanager1.md
original_path: WinForms_Docs/99_Uncategorized/addingbaritemstoabarmanager1.md
created_at: 2025-08-05
---






##### Adding Bar Items to a BarManager {#adding-bar-items-to-a-barmanager style="tab-stops: 0pt"}

[] 

To programmatically add bar items to a BarManager, perform the below steps.

[] 

1.   Include the required namespaces.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                                        |
| **[]**                                                                               |
|                                                                                                                                        |
| [using][ Syncfusion.Windows.Forms.Tools;]         |
|                                                                                                                                        |
| [using][ Syncfusion.Windows.Forms.Tools.XPMenus;] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                      |
|                                                                                                                                         |
| **[]**                                                                                |
|                                                                                                                                         |
| [Imports][ Syncfusion.Windows.Forms.Tools]         |
|                                                                                                                                         |
| [Imports][ Syncfusion.Windows.Forms.Tools.XPMenus] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of MainFrameBarManager.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager mainFrameBarManager1;]                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [this][.mainFrameBarManager1 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager([this].components, [this]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ mainFrameBarManager1 [As] Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager]                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ [Me].mainFrameBarManager1 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager([Me].components, [Me])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Add category to the MainFrameBarManager.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| **[]**                                                                                         |
|                                                                                                                                                  |
| [this][.mainFrameBarManager1.Categories.Add(\"MainMenu\");] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [Me][.mainFrameBarManager1.Categories.Add([\"MainMenu\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create an instances for ParentBarItem(File) and BarItems(New,Open and Close).

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem parentBarItem1;]                             |
|                                                                                                                                                                                                   |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem1;]                                         |
|                                                                                                                                                                                                   |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem2;]                                         |
|                                                                                                                                                                                                   |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem3;]                                         |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [this][.parentBarItem1 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem();] |
|                                                                                                                                                                                                   |
| [this][.barItem1 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();]             |
|                                                                                                                                                                                                   |
| [this][.barItem2 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();]             |
|                                                                                                                                                                                                   |
| [this][.barItem3 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();]             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [Private][ parentBarItem1 [As] Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem] |
|                                                                                                                                                                                                |
| [Private][ barItem1 [As] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem]             |
|                                                                                                                                                                                                |
| [Private][ barItem2 [As] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem]             |
|                                                                                                                                                                                                |
| [Private][ barItem3 [As] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem]             |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Me][.parentBarItem1 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem()] |
|                                                                                                                                                                                                |
| [Me][.barItem1 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()]             |
|                                                                                                                                                                                                |
| [Me][.barItem2 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()]             |
|                                                                                                                                                                                                |
| [Me][.barItem3 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()]             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Add BarItems to the MainFrameBarManager.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [this][.mainFrameBarManager1.Items.AddRange([new] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem\[\] {]              |
|                                                                                                                                                                                                                                |
| [this][.parentBarItem1,[this].barItem1,[this].barItem2,[this].barItem3});] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.mainFrameBarManager1.Items.AddRange([New] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem() { [Me].parentBarItem1,[Me].barItem1,[Me].barItem2,[Me].barItem3})] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[ Refer ]Adding Toolbars and Populating the Bar Items[ ][to add toolbar and populate menus.]

[]{#related-topics}

