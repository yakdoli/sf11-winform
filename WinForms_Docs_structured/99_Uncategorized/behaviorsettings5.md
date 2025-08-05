---
title: behaviorsettings5.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings5.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Parent item settings

[] 

While expanding a groupbar parent item, you can set the control to collapse all the other open parent items, expanding only a single, currently selected parent item. To apply this behavior to the control, the **ExpandSingleGroup** property must be set to **True**.

[] 


  ------------------- ---------------------------------------------------------------------------------------
  GroupBar Property   Description
  ExpandSingleGroup   Specifies if only a single group should be expanded at a time. Default value is True.
  ------------------- ---------------------------------------------------------------------------------------


[] 

Space settings for parent items

[] 

To set default space between the parent items, the **DefaultTopItemSpacing** property can be set with the value which has to be applied as the space between the items.

[] 


  ----------------------- ------------------------------------------------------------
  GroupBar Property       Description
  DefaultTopItemSpacing   Specifies the default spacing between the top level items.
  ----------------------- ------------------------------------------------------------


[] 

Item States

[] 

The states of the items can be handled and customized as you require it to be displayed in the Designer dialog by setting it for the required items.

 

The **Expanded** property when set, expands that item by default. By setting the **Disabled** property, the item will not respond to the user actions. The **Selected** property when set for an item, it will be selected by default.

[] 


  ------------------------ ----------------------------------------------------------------------------------------
  GroupBar Item Property   Description
  Disabled                 Gets/sets the boolean value to disable the state of an item. Default value is false.
  Expanded                 Gets/sets the boolean value, to expand the groupbar structure. Default value is false.
  Selected                 Gets/sets the boolean value to set the focus on the item. Default value is false.
  ------------------------ ----------------------------------------------------------------------------------------


 

[]{#related-topics}

