---
title: usingpropertiesmodel29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel29.md
created_at: 2025-07-03
---








  









### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to handle client-side events raised by the diagram through the properties model.

1.   Define the the **ClientSideOnLoad**, **ClientSideOnNodeClick**, **ClientSideOnNodeSelected**, and **ClientSideOnNodeUnSelected** properties and pass the instance through the **view-specific data** to the **view**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**[]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|            DiagramPropertiesModel model = new DiagramPropertiesModel()                                                                                                                                                                                                                                  |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|             {                                                                                                                                                                                                                                                                                           |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|             };                                                                                                                                                                                                                                                                                          |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorClick = ][\"OnConnectorClick\"][;]                   |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDeleted = ][\"OnConnectorDeleted\"][;]               |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDeleting = ][\"OnConnectorDeleting\"][;]             |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDoubleClick = ][\"OnConnectorDoubleClick\"][;]       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDragEnd = ][\"OnConnectorDragEnd\"][;]               |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDragging = ][\"OnConnectorDragging\"][;]             |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDragStart = ][\"OnConnectorDragStart\"][;]           |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorDrop = ][\"OnConnectorDrop\"][;]                     |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorLabelChanged = ][\"OnConnectorLabelChanged\"][;]     |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorSelected = ][\"OnConnectorSelected\"][;]             |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorStartLabelEdit = ][\"OnConnectorStartLabelEdit\"][;] |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnConnectorUnSelected = ][\"OnConnectorUnSelected\"][;]         |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnHeadNodeChanged = ][\"OnHeadNodeChanged\"][;]                 |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnLoad = ][\"OnLoad\"][;]                                       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeClick = ][\"OnNodeClick\"][;]                             |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDeleted = ][\"OnNodeDeleted\"][;]                         |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDeleting = ][\"OnNodeDeleting\"][;]                       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDoubleClick = ][\"OnNodeDoubleClick\"][;]                 |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDragEnd = ][\"OnNodeDragEnd\"][;]                         |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDragging = ][\"OnNodeDragging\"][;]                       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDragStart = ][\"OnNodeDragStart\"][;]                     |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeDrop = ][\"OnNodeDrop\"][;]                               |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeLabelChanged = ][\"OnNodeLabelChanged\"][;]               |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeResized = ][\"OnNodeResized\"][;]                         |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeResizing = ][\"OnNodeResizing\"][;]                       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeSelected = ][\"OnNodeSelected\"][;]                       |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeStartLabelEdit = ][\"OnNodeStartLabelEdit\"][;]           |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnNodeUnSelected = ][\"OnNodeUnSelected\"][;]                   |
|                                                                                                                                                                                                                                                                                                         |
| [            model.ClientSideOnTailNodeChanged = ][\"OnTailNodeChanged\"][;]                 |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|            model.DiagramMode = DiagramMode.SVG;                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|             ViewData["FlatDiagram"] = model;                                                                                                                                                                                                                                                            |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| ```                                                                                                                                                                                                                                                                        |
|             return View();                                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   In the **view**, add the following code snippet. 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                            |
|                                                                                                                                            |
| [\<%][{]     |
|                                                                                                                                            |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])         ] |
|                                                                                                                                            |
| [         .Render();]                                                                 |
|                                                                                                                                            |
| [  }]                                                                                 |
|                                                                                                                                            |
| [%\>][ ]     |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In JavaScript, define the handlers.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[JavaScript ]**[]                                                                                           |
|                                                                                                                                                                                                                         |
| [\<[script] [type]=\"text/javascript\"\>]                                                                               |
|                                                                                                                                                                                                                         |
| [       [function] [ClientSideOnConnectorClick](sender,args) {]                                                         |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDeleted](sender,args) {]         |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDeleting](sender,args) {]        |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDoubleClick](sender,args) {]     |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDragEnd](sender,args) {]         |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDragging] (sender,args) {]       |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDragStart] (sender,args) {]      |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorDrop] (sender,args) {]           |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorLabelChanged] (sender,args) {]   |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector]]                                                                            |
|                                                                                                                                                                                                                         |
| [            // \_OldLabelValue  -- old label of the connector;]                                                                                   |
|                                                                                                                                                                                                                         |
| [            //\_NewLabelValue   - new Label of the connector**;**][]         |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorSelected] (sender,args) {]       |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [   function][ [ClientSideOnConnectorStartLabelEdit] (sender,args) {]      |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnConnectorUnSelected] (sender,args) {]     |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id           - ID attribute of the current connector]]                                                               |
|                                                                                                                                                                                                                         |
| [            [//  \_Connector    - Details of the connector][]]                                                  |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnLoad] (sender,args) {]                    |
|                                                                                                                                                                                                                         |
| [           //inst - instance of diagram client-side object.][  []] |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeClick] (sender,args) {]               |
|                                                                                                                                                                                                                         |
| [            [//args:]]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDeleted] (sender,args) {]             |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDeleting] (sender,args) {]            |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDoubleClick] (sender,args) {]         |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDragEnd] (sender,args) {]             |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDragging] (sender,args) {]            |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDragStart] (sender,args) {]           |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeDrop] (sender,args) {]                |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeLabelChanged] (sender,args) {]        |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id            - ID attribute of the current node]]                                                                   |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes         - Details of the node]]                                                                                |
|                                                                                                                                                                                                                         |
| [            // \_OldLabelValue  -- old label of the node;]                                                                                        |
|                                                                                                                                                                                                                         |
| [            //\_NewLabelValue   - new Label of the node**;**][]              |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeResized] (sender,args) {]             |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeResizing] (sender,args) {]            |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeSelected] (sender,args) {]            |
|                                                                                                                                                                                                                         |
| [             //args:][]                                                                    |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeStartLabelEdit] (sender,args) {]      |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnNodeUnSelected] (sender,args) {]          |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnHeadNodeChanged] (sender,args) {]         |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [        function][ [ClientSideOnTailNodeChanged] (sender,args) {]         |
|                                                                                                                                                                                                                         |
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\</[script]\>]                                                                                                                             |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

After performing the above steps, you can observe the handlers being invoked when the corresponding events are triggered.

[]{#related-topics}

