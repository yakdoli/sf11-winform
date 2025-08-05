---
title: unfreezingpanes.md
original_path: WinForms_Docs/99_Uncategorized/unfreezingpanes.md
created_at: 2025-08-05
---






#### Unfreezing Panes {#unfreezing-panes style="tab-stops: 0pt"}

Use the following code snippet in client side to unfreeze the panes based on the current selection.

[] 


+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                              |
|                                                                                                                                       |
| **[]**                                                                                            |
|                                                                                                                                       |
| [    [var] grid = \$find([\"MyGrid\"]);] |
|                                                                                                                                       |
| [    **grid.unFreezePanes();**]**[   ]**         |
+---------------------------------------------------------------------------------------------------------------------------------------+


 

Unlock all the rows and columns to scroll through the entire grid.

{border="0"}

Figure 280: Before Calling unFreezePanes

{border="0"}

Figure 281: After Calling unFreezePanes

 

[]{#related-topics}

