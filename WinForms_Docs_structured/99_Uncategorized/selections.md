---
title: selections.md
original_path: WinForms_Docs/99_Uncategorized/selections.md
created_at: 2025-08-05
---






#### Selections {#selections style="tab-stops: 0pt"}

[] 

There are two type of selection architectures in a Grid Grouping control. One is designed specifically for the Grid Grouping control referred as **Record-Based Selection** and the other is inherited from GridControlBase named as **Model-Based Selection**.

 

If you use the Record-Based selection functionality, then whole records are selected and these selections function properly with nested tables, sorting, and so on. If you choose to use the inherited selection capability, you will be able to select cell ranges, but the selections will have no knowledge of nested tables, grouping or sorts and thus is limited in a Grid Grouping control.

 

To use the Grid Grouping control record selections, you must set **AllowSelections** to None and then set **ListBoxSelectionMode** to something other than None. To use the inherited selection capability, set AllowSelections to something other than None.

 

In this section, you will learn about the following topics.

[] 

 

[]{#p462} 

 

More:













