---
title: visualinheritancesupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\visualinheritancesupport.md
created_at: 2025-07-03
---






#### Visual Inheritance Support {#visual-inheritance-support style="tab-stops: 0pt"}

[] 

XP Menus supports Visual Inheritance during design-time, which means you can set up XP Menus in a form and also continue to set up in the form derived from it. The corresponding components like the BarManager and toolbar should however be protected or public for this to be supported. In the derived form\'s designer, you can add new bar items to the bar manager and then add these items to the toolbar, submenu etc.

 

These are things you can do in a derived form in Visual Inheritance mode.

[] 

[·      ]Add new BarItems created in the derived form to any toolbar, ParentBarItem, anywhere.

[·      ]Reposition the existing BarItems within a toolbar or ParentBarItem.

[·      ]Remove an existing group setting and add a new group setting.

[] 

These are the **limitations** of Visual Inheritance mode.

[] 

[·      ]Cannot add menu items created in a base form to any bars/submenus in a derived form.

[·      ]When the items in a base form\'s toolbar/submenu are repositioned, any previous repositioning that occurred in the derived form will be lost and the results may be unpredictable.

[]{#related-topics}

