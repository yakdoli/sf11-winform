---
title: resizingasinglenodeonmultipleselection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\resizingasinglenodeonmultipleselection.md
created_at: 2025-07-03
---






#### Resizing a Single Node on Multiple Selection {#resizing-a-single-node-on-multiple-selection style="tab-stops: 0pt"}

 

Multiple items on the drawing area can be selected.

 

Multiple selections can be performed by the following steps.

[] 

[·      ]Items on the drawing area are selected only if they fall within the bounds of the drag adorner.

[·      ]The drag adorner is displayed when the user clicks anywhere on the page and starts dragging the pointer.

[·      ]The rectangle is formed with the drag start-point as one of its points, and the point where the mouse button was released as its second point, defines the drag adorner\'s bounds.

[·      ]Nodes connected to one or more nodes are selected only if one of the connected nodes is also within the drag adorner bounds. The nodes and the connector connecting them act as a single selection.

[] 


{border="0"}Note: Resizing or moving any one item affects the other items by the same factor. However, rotating affects only the current node.


[] 

{border="0"}

Figure 36: Multiple Selections**[]**

 

[]{#p29} 

[]{#related-topics}

