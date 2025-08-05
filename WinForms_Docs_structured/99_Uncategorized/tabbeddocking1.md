---
title: tabbeddocking1.md
original_path: WinForms_Docs/99_Uncategorized/tabbeddocking1.md
created_at: 2025-08-05
---






##### Tabbed Docking {#tabbed-docking style="tab-stops: 0pt"}

[] 

This section will discuss how the docked controls inside a container can be tabbed.

[] 

At Design Time

[] 

The docked controls can be tabbed in the designer, by just dragging and dropping into one another. DockingManager helps you in doing this using different DragProviderStyle.

[] 

{border="0"}

[] 

Figure 47: Docked controls tabbed in the Designer

[] 

At RunTime

[] 

DockingManager helps you in dragging and dropping the docked controls at run time, using different DragProviderStyle. This styles display prediction Bands, which lets you decide whether you can drop the control in that location.

[] 

{border="0"}

[] 

Figure 48: Docking a control with tabbed style into another Control

[] 

Runtime Example

[] 

The below code lets you tab two docked controls (Panel1 and Panel2).

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.dockingManager.DockControl([this].[Panel1], [this].[Panel2], Syncfusion.Windows.Forms.Tools.[DockingStyle].Tabbed, 200, [true]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [Me][.dockingManager.DockControl([Me].Panel1, [Me].Panel2, Syncfusion.Windows.Forms.Tools.DockingStyle.Tabbed, 200, [True])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: In the Tabbed style, the control is docked as a tabbed window along with the dock target. This style is not applicable when the dock target is the host form / user control.


[] 

Context Menu for Tabbed Controls

[] 

The tabbed control can display context menu when the user right clicks on the tabs. See Context Menu.

[] 

Aligning the Tabs

[] 

The alignment of the tabs can be specified using DockTabAlignment property.

[] 

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
| DockingManager Property           | Description                                                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
| DockTabAlignment                  | Property which sets the value indicating the alignment of the dock tabs. The different alignment options are, |
|                                   |                                                                                                               |
|                                   |                                                                                                               |
|                                   |                                                                                                               |
|                                   | *Top,*                                                                                                        |
|                                   |                                                                                                               |
|                                   | *Bottom,*                                                                                                     |
|                                   |                                                                                                               |
|                                   | *Left and*                                                                                                    |
|                                   |                                                                                                               |
|                                   | *Right.*                                                                                                      |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------+


[] 


{border="0"} Note: This property can also be set easily using Task Window.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [this][.dockingManager.DockTabAlignment = Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Me][.dockingManager.DockTabAlignment = Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 49: Tabs aligned to \"Right\"

**[]** 

Methods related to Tabbed Docking

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DockingManager Property           | Description                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsSameTabbedGroup                 | Determines whether the second control is under the same group of the first control.                                                                                  |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   | *Ctrl1* - Indicates the first control.                                                                                                                               |
|                                   |                                                                                                                                                                      |
|                                   | *Ctrl2* - Indicates the second control.                                                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetTabPosition                    | Returns the tab position of the specified control among a tab group. An integer value will be returned indicating the tab position. The parameter is,                |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   | *Ctrl[ ]*- Indicates the docking window.                                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetTabbedSiblings                 | Returns all the siblings of the specified control in a tabbed group or it returns the array of controls which are tabbed with the given control. The parameters are, |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   | *Ctrl[ ]*- Instance of control whose tabbed siblings are to be returned.                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsTabbed                          | Returns whether the specified control is tabbed or not. The parameter is,                                                                                            |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   | *Ctrl[ ]*- Indicates the docking window.                                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [this][.dockingManager.IsSameTabbedGroup([this].listBox1,[this].checkedListBox1);] |
|                                                                                                                                                                                                                   |
| [this][.dockingManager1.GetTabPosition([this].listBox1);]                                               |
|                                                                                                                                                                                                                   |
| [this][.dockingManager1.GetTabbedSiblings([this].listView1);]                                           |
|                                                                                                                                                                                                                   |
| [this][.dockingManager1.IsTabbed([this].listBox1);]                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [Me][.dockingManager.IsSameTabbedGroup([this].listBox1,[this].checkedListBox1)] |
|                                                                                                                                                                                                                |
| [Me][.dockingManager1.GetTabPosition([Me].listBox1)]                                                 |
|                                                                                                                                                                                                                |
| [Me][.dockingManager1.GetTabbedSiblings([Me].listView1)]                                             |
|                                                                                                                                                                                                                |
| [Me][.dockingManager1.IsTabbed([this][.]listBox1)]                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[Getting Started]{.UGHyperlink}[, ]{.UGHyperlink}[DockAllow Event]{.UGHyperlink}[, ]{.UGHyperlink}[Dock Arrow Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

