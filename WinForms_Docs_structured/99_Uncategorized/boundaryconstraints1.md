---
title: boundaryconstraints1.md
original_path: WinForms_Docs/99_Uncategorized/boundaryconstraints1.md
created_at: 2025-08-05
---








  









### Boundary Constraints {#boundary-constraints style="tab-stops: 0pt"}

The **BoundaryConstraintsEnabled** property can be used to control the movement of the nodes on the page.  When this property is set to **true**, nodes cannot be dragged beyond the diagram area. When set to **false**, it will allow the nodes to go beyond the diagram area and a scrollbar will be displayed to access those nodes.

 

Property 

+----------------------------+-----------------------------------------------------------------------------------+----------------------+----------------------+--------------------------------------------------+
| Property                   | Description                                                                       | Type of the Property | Value it Accepts     | Any Other Dependencies/Sub-Properties Associated |
+----------------------------+-----------------------------------------------------------------------------------+----------------------+----------------------+--------------------------------------------------+
| BoundaryConstraintsEnabled | Gets or sets a value indicating whether boundary constraints are set on the page. | Dependency property  | Boolean (True/False) | No (This is not supported in SVG Mode)           |
|                            |                                                                                   |                      |                      |                                                  |
|                            | Default value: false                                                              |                      |                      |                                                  |
+----------------------------+-----------------------------------------------------------------------------------+----------------------+----------------------+--------------------------------------------------+

 

 This property can be set by the following two ways:

More:







