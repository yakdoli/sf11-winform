---
title: contextmenu5.md
original_path: WinForms_Docs/99_Uncategorized/contextmenu5.md
created_at: 2025-08-05
---








  









## Context Menu {#context-menu style="tab-stops: 0pt"}

Essential Schedule provides support for adding, editing, deleting, and printing an appointment by clicking the menu item in the Context menu.  To show the context menu on the Schedule control, you must set the ShowContextMenu property to True.  It also provides options to add custom menu items.

Context menus are defined in the collections by using the Menu ID, Menu Name, and Command Name fields. Command name field is used to differentiate default Context menu items and custom Context menu items.

Essential Schedule will automatically process items with the following predefined values.

Appointment context menu default items are:

[·      ]Open appointment

[·      ]Delete Appointment

[·      ]Quick Print

Cell context menu default items are:

[·      ]New appointment

[·      ]New Recurring Appointment

[·      ]Go to Today

[] 

Properties

Table 22: Context Menu Properties**[]**

**[]** 


+------------------+-------------------------------------+----------------------+---------------------------------------------------+-------------+
| Property         | Description                         | Type of the property | Value it accepts                                  | Dependency  |
+------------------+-------------------------------------+----------------------+---------------------------------------------------+-------------+
| ContextMenuItems | Used to add Menu items for Schedule | List                 | [List\<ContextMenuItem\>] | NA          |
|                  |                                     |                      |                                                   |             |
|                  |                                     |                      | []                        |             |
+------------------+-------------------------------------+----------------------+---------------------------------------------------+-------------+


[] 

More:





