---
title: usingpropertiesmodel15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel15.md
created_at: 2025-07-03
---






#### Using Properties model {#using-properties-model style="tab-stops: 0pt"}

The following steps guide in the customization of connector labels through the properties model.

1.   In the **controller**, create an object for the **Connector** class and set the **LabelFontColor**, **LabelBorderColor**, etc., properties.

2.   Create object for the **DiagramPropertiesModel** class and set the **Connector** property. Pass this model class to **view data**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                          |
| [            ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            Line[Connector] line = [new] Line[Connector] ()]                                                  |
|                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [                Name = \"Line1\",]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [                Label = \"Line's Label\",]                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [                HeadNode = node1,]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [                TailNode = node2,]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [                LabelBackground = \"#fcb\",]                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| [                LabelBorderColor = \"#bcf\",]                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [                LabelBorderWidth = 1,]                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [                LabelFontColor = \"#aad\",]                                                                                                                                        |
|                                                                                                                                                                                                                                          |
| [                LabelFontFamily = \"Arial\",]                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [                LabelFontSize = 12,]                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [                LabelHeight = 30,]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [                LabelWidth = 100,]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [                LabelHorizontalAlignment = [Horizontal].Center,]                                                                                           |
|                                                                                                                                                                                                                                          |
| [                LabelVerticalAlignment = [Vertical].Middle,]                                                                                               |
|                                                                                                                                                                                                                                          |
| [                LabelFontColor = [\"red\"],]                                                                                                               |
|                                                                                                                                                                                                                                          |
| [                LabelFontSize = 16,]                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [                LabelFontFamily = [\"Times New Roman]]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [            }; ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [DiagramPropertiesModel diagramModel = new DiagramPropertiesModel()]                                                                                                                |
|                                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [         Width =  750,]                                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [         Height =  500,]                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [         DiagramMode = DiagramMode.SVG,]                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [         Connectors = new LinesCollection() { ][line ][ }] |
|                                                                                                                                                                                                                                          |
| [    };]                                                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

[] 

3.   In the **view**, invoke the **Diagram** helper with the control ID which is same as the **view data** name.

 

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

The following output is generated using the code snippets above:

 

{border="0"}

Figure 82: Customized Label[]

 

[]{#related-topics}

