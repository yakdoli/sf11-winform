---
title: addingitemtodropdown.md
original_path: WinForms_Docs/99_Uncategorized/addingitemtodropdown.md
created_at: 2025-08-05
---






#### Adding Item to Drop-down {#adding-item-to-drop-down style="tab-stops: 0pt"}

 

This feature enables you to add items to the SplitButton drop-down list.

[] 

You can add item using the *DropDownItems* property. The following code illustrates how to add items to the drop-down list:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                           |
|                                                                                                                                                     |
| [            [this].splitButton1.DropDownItems.Add([\"Item 1\"]);] |
|                                                                                                                                                     |
| [            [this].splitButton1.DropDownItems.Add([\"Item 2\"]);] |
|                                                                                                                                                     |
| [            ]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                       |
|                                                                                                                                                 |
| [           [Me].splitButton1.DropDownItems.Add([\"Item 1\"])] |
|                                                                                                                                                 |
| [           [Me].splitButton1.DropDownItems.Add([\"Item 2\"])] |
|                                                                                                                                                 |
| [                  ]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 1491: Item Added

 

 

 

Removing Item from Drop-Down List

You can also remove the added items if required. The following code illustrates how to remove items form drop-down list:

 

+-----------------------------------------------------------------------------------------------------------------------+
| C#                                                                                                                    |
|                                                                                                                       |
| [            [this].splitButton1.DropDownItems.RemoveAt(1);] |
+-----------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------+
| VB                                                                                                                  |
|                                                                                                                     |
| [            [Me].splitButton1.DropDownItems.RemoveAt(1);] |
+---------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 1492: Item Removed

 

 

[]{#related-topics}

