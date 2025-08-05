---
title: nodecontent1.md
original_path: WinForms_Docs/99_Uncategorized/nodecontent1.md
created_at: 2025-08-05
---








  









### Node Content {#node-content style="tab-stops: 0pt"}

Node is used to visually represent any UIElements using **Content** property. You can host any content inside the node using the **Content** property. Node supports control template too, by defined template for the nodes, business object can be assigned as Node's Content and the template will look after how to present the business object.

[] 


{border="0"} Note:[ ]A Node can have both Content and Shape at the same time, doing so Content will be placed over the Shape.


 

Table 18: Property Table**[]**

+----------------------------+----------------------------------------------------------+----------------------+-----------------------------+-----------------------------------------------------+
| Property                   | Description                                              | Type of the property | Value it Accept             | Any other dependencies/ sub properties associated   |
+----------------------------+----------------------------------------------------------+----------------------+-----------------------------+-----------------------------------------------------+
| Content                    | Gets or sets the node\'s content.                        | Dependency property  | object                      | No[] |
+----------------------------+----------------------------------------------------------+----------------------+-----------------------------+-----------------------------------------------------+
| HorizontalContentAlignment | Specifies the horizontal alignment for the node content. | Dependency property  | HorizontalAlignment.Center  | No                                                  |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | HorizontalAlignment.Left    |                                                     |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | HorizontalAlignment.Right   |                                                     |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | HorizontalAlignment.Stretch |                                                     |
+----------------------------+----------------------------------------------------------+----------------------+-----------------------------+-----------------------------------------------------+
| VerticalContentAlignment   | Specifies the vertical alignment for the node content.   | Dependency property  | VerticalAlignment.Bottom    | No                                                  |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | VerticalAlignment.Center    |                                                     |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | VerticalAlignment.Stretch   |                                                     |
|                            |                                                          |                      |                             |                                                     |
|                            |                                                          |                      | VerticalAlignment.Top       |                                                     |
+----------------------------+----------------------------------------------------------+----------------------+-----------------------------+-----------------------------------------------------+

 

More:







