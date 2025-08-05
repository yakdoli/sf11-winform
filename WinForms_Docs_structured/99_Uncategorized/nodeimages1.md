---
title: nodeimages1.md
original_path: WinForms_Docs/99_Uncategorized/nodeimages1.md
created_at: 2025-08-05
---






##### Node Images {#node-images style="tab-stops: 0pt"}

You can display an image next to the expand glyph in the expand cell of the Grid Tree by setting the GridTreeControl.SupportNodeImages property to true. When this property is set to true, the Grid Tree will raise the RequestNodeImage event that allows you to provide an image for a given node. The EventArgs will provide you with the GridTreeNode object, and then the image can be set using the NodeImage property based on the given tree node.

 

The following code example illustrates how to handle the RequestNodeImage event.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [void][ treeGrid_RequestNodeImage([object] sender, [GridTreeRequestNodeImageEventArgs] args)] |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [args.NodeImage = employees.GetItemBitmap(args.Item [as] Employee);]                                                                                                   |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Here is a screen shot that shows custom glyphs and node images.

 

{border="0"}

Figure 262: Custom Glyphs and Node Images

 

 

 

[]{#related-topics}

