---
title: supertooltipsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supertooltipsupport.md
created_at: 2025-07-03
---






##### SuperToolTip support {#supertooltip-support style="tab-stops: 0pt"}

[] 

The BarItems in XPMenus provides SuperToolTip support. Other than the usual tooltip, XPMenus now allows users to associate a SuperToolTip to the BarItems.

 

To associate a SuperTooltip to the BarItem (Menu Items), Drag and drop a SuperToolTip control on to the form in which the Menus are placed. Select the BarItem to which the SuperTooltip is to be added.

 

In the properties window, of the BarItem, we can see an extender property **ToolTip on superToolTip**. Click this to open the Tooltip Editor.

[] 

{border="0"}

[] 

Figure 827: Accessing ToolTip Editor using SuperTooltip property of a Bar Item

[] 

Customize the Tooltip using the Tooltip Editor.

[] 

{border="0"}

[] 

Figure 828: Setting ToolTip Text using ToolTipInfo.Body.Text Property

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| **[]**                                                                                                                    |
|                                                                                                                                                                             |
| [toolTipInfo1.Body.Text = [\"Save\"];]                                                                           |
|                                                                                                                                                                             |
| [this][.superToolTip1.SetToolTip([this].barItem2, toolTipInfo1);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [toolTipInfo1.Body.Text = [\"Save\"]]                                                                       |
|                                                                                                                                                                        |
| [Me][.superToolTip1.SetToolTip([Me].barItem2, toolTipInfo1)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 829: BarItem displaying Tooltip

**[]** 

A sample illustrating the supertooltip feature is available in the below sample installation location.

 

..\\My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Menus Package\\XPMenusSDI

[]{#related-topics}

