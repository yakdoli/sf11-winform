---
title: groupingitemsinapopupmenu.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\groupingitemsinapopupmenu.md
created_at: 2025-07-03
---






##### Grouping Items in a Popup Menu {#grouping-items-in-a-popup-menu style="tab-stops: 0pt"}

[] 

This topic will guide on how to group the menu items by inserting separator(s), in a popup menu with and without BarManager.

 

If the ParentBarItem associated with the popup menu is contained within a BarManager, drop-down the popup menu from the Popup Form, right click on an item and select **Begin A Group** from the context menu.

[] 

{border="0"}

[] 

Figure 818: Adding Separator for a PopupMenu or Grouping item contained within a BarManager

[] 

If the ParentBarItem is not contained within a BarManager, edit the **SeparatorIndices** property of the ParentBarItem indicating the item indices in the items list where you want the separators to be introduced.

[] 

{border="0"}

**[]** 

Figure 819: Adding Separators through the SeparatorIndices Collection Editor when BarManager is Not Used

[] 

{border="0"}

[] 

Figure 820: Separators after BarItem2 and BarItem5

**[]** 

We can also group the items using BeginGroupAt and RemoveGroupAt methods. Click [here] to know more.

[] 

See Also

**[]** 

[[·      ]]{.UGHyperlink}[Associating Popup Menu To a Control]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Adding and filling a popup menu]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[How to programmatically begin a group or remove an existing group in a popup menu]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[How to programmatically show a Popup Menu]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

