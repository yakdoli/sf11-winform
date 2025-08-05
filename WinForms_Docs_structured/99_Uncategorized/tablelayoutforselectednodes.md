---
title: tablelayoutforselectednodes.md
original_path: WinForms_Docs/99_Uncategorized/tablelayoutforselectednodes.md
created_at: 2025-08-05
---






#### Table Layout for Selected Nodes {#table-layout-for-selected-nodes style="tab-stops: 0pt"}

[This feature enables you to apply the table layout on selected nodes instead of applying it to the entire diagram. ]This arranges selected nodes or a given node collection in a tabular structure based on specified intervals between them. The number of nodes in each row and column can be specified and the layout will be applied accordingly. []

 

Use Case Scenarios

[·      ]Users can easily make the layout with a specific collection of nodes called ordered nodes.

[·      ]Users can easily position the layout.

[·      ]Users can easily align the layout by using the layout alignment properties.

[·      ]Users can set a rectangle boundary around nodes by using the **Layout Bounds** property.

 

Properties

Table 14: Property Table


+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-----------------------------+------------------------------------------+
| **Property**                                                          | **Description**                                                                                         | **Type**                    | **Data Type**                            |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-----------------------------+------------------------------------------+
| OrderedNodes                                                          | This property is used to get or set the Collection of Nodes for table layout.[] | Dependency property         | List\<IShape\>[] |
|                                                                       |                                                                                                         |                             |                                          |
|                                                                       |                                                                                                         |                             |                                          |
|                                                                       |                                                                                                         |                             |                                          |
|                                                                       |                                                                                                         | []  |                                          |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-----------------------------+------------------------------------------+


[] 

[] 

Sample Link

To view a sample of this feature:

1.   Open **Dashboard**.

2.   Click **User Interface \> WFP**.

3.   Click **Run Samples**.

4.   Navigate to **Diagram \> Automatic Layout \> Table Layout**.

More:









