---
title: layoutspacing3.md
original_path: WinForms_Docs/99_Uncategorized/layoutspacing3.md
created_at: 2025-08-05
---








  









### Layout Spacing  {#layout-spacing style="tab-stops: 0pt"}

The following are general spacing properties used in many automatic layouts. Spacing refers to spaces between the nodes that lie at different levels of the tree layout, and the space between each node with their sibling.

 

Properties 

 

  ---------------------- ---------------------------------------------------- ---------------------- ------------------ --------------------------------------------------
  Property               Description                                          Type of the Property   Value it Accepts   Any Other Dependencies/Sub-Properties Associated
  VerticalSpacing        Gets or sets the vertical spacing between nodes.     CLR Property           Double             No
  HorizontalSpacing      Gets or sets the horizontal spacing between nodes.   CLR Property           Double             No
  SpaceBetweenSubTrees   Gets or sets the space between sub-trees.            CLR Property           Double             No
  ---------------------- ---------------------------------------------------- ---------------------- ------------------ --------------------------------------------------

  

The user can set the horizontal and the vertical distance between the nodes in a tree layout using the **HorizontalSpacing** and **VerticalSpacing** properties. The spaces between sub-trees are specified using the **SpaceBetweenSubTrees** property. 


{border="0"} Note: In case of a table layout, only the HorizontalSpacing and VerticalSpacing properties should be specified.  


The following code illustrates these settings: 

More:







