---
title: usingpropertiesmodel11.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel11.md
created_at: 2025-08-05
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps guide in the customization of node labels through the properties model.

1.   In the **controller**, create object for Node class and set the **LabelFontColor, LabelBorderColor,** etc., properties.

2.   Create an object for the **DiagramPropertiesModel** class and set the **Nodes** property. Pass this model class to the **view data**.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                |
|                                                                                                                                                                      |
| [            ]                                                                                                  |
|                                                                                                                                                                      |
| [            [Node] node = [new] [Node]()] |
|                                                                                                                                                                      |
| [            {]                                                                                                 |
|                                                                                                                                                                      |
| [                Name = Node1,]                                                                                 |
|                                                                                                                                                                      |
| [                Label = Node1,]                                                                                |
|                                                                                                                                                                      |
| [                LabelBackground = \"#fcb\",]                                                                   |
|                                                                                                                                                                      |
| [                LabelBorderColor = \"#bcf\",]                                                                  |
|                                                                                                                                                                      |
| [                LabelBorderWidth = 1,]                                                                         |
|                                                                                                                                                                      |
| [                LabelFontColor = \"#aad\",]                                                                    |
|                                                                                                                                                                      |
| [                LabelFontFamily = \"Arial\",]                                                                  |
|                                                                                                                                                                      |
| [                LabelFontSize = 12,]                                                                           |
|                                                                                                                                                                      |
| [                LabelHeight = 30,]                                                                             |
|                                                                                                                                                                      |
| [                LabelWidth = 100,]                                                                             |
|                                                                                                                                                                      |
| [                LabelHorizontalAlignment = [Horizontal].Center,]                       |
|                                                                                                                                                                      |
| [                LabelVerticalAlignment = [Vertical].Middle,]                           |
|                                                                                                                                                                      |
| [                LabelFontColor = [\"red\"],]                                           |
|                                                                                                                                                                      |
| [                LabelFontSize = 16,]                                                                           |
|                                                                                                                                                                      |
| [                LabelFontFamily = [\"Times New Roman]]                                 |
|                                                                                                                                                                      |
| [            }; ]                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In the **view**, invoke the **Diagram** helper with the control ID which is same as the **viewdata** name.

 

+---------------------------------------------------------------------------------------+
| **[View]**[ ] |
|                                                                                       |
| ```                                                      |
| <%{                                                                                   |
| ```                                                                                   |
|                                                                                       |
| ```                                                      |
|       Html.Syncfusion().Diagram("FlatDiagram")                                        |
| ```                                                                                   |
|                                                                                       |
| [          .Render();]                            |
|                                                                                       |
| ```                                                      |
|   }                                                                                   |
| ```                                                                                   |
|                                                                                       |
| [%\>][] |
+---------------------------------------------------------------------------------------+

 

4.   Build and run the application.

[] 

The following output is generated using the code snippets above.

 

{border="0"}

Figure 50: Customized Label[]

 

[]{#related-topics}

