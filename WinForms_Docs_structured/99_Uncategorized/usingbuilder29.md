---
title: usingbuilder29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder29.md
created_at: 2025-07-03
---








  









### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps describe how to handle client-side events raised by the diagram through the builder.

1.   In the **view**, create a **nodes** and **connectors**; invoke the **Diagram** helper with the control ID as the first argument, followed by the **ClientSideOnLoad**, **ClientSideOnNodeClick**, **ClientSideOnNodeSelected**, and **ClientSideOnNodeUnSelected** methods with the desired handlers as arguments. 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [\<%][{]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [  Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                        |
| [  [.ClientSideOnConnectorClick(][\"OnConnectorClick\"][)]]                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDeleted(][\"OnConnectorDeleted\"][)]               |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDeleting(][\"OnConnectorDeleting\"][)]             |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDoubleClick(][\"OnConnectorDoubleClick\"][)]       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDragEnd(][\"OnConnectorDragEnd\"][)]               |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDragging(][\"OnConnectorDragging\"][)]             |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDragStart(][\"OnConnectorDragStart\"][)]           |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorDrop(][\"OnConnectorDrop\"][)]                     |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorLabelChanged(][\"OnConnectorLabelChanged\"][)]     |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorSelected(][\"OnConnectorSelected\"][)]             |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorStartLabelEdit(][\"OnConnectorStartLabelEdit\"][)] |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnConnectorUnSelected(][\"OnConnectorUnSelected\"][)]         |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnHeadNodeChanged(][\"OnHeadNodeChanged\"][)]                 |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnLoad(][\"OnLoad\"][)]                                       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeClick(][\"OnNodeClick\"][)]                             |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDeleted(][\"OnNodeDeleted\"][)]                         |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDeleting(][\"OnNodeDeleting\"][)]                       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDoubleClick(][\"OnNodeDoubleClick\"][)]                 |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDragEnd(][\"OnNodeDragEnd\"][)]                         |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDragging(][\"OnNodeDragging\"][)]                       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDragStart(][\"OnNodeDragStart\"][)]                     |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeDrop(][\"OnNodeDrop\"][)]                               |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeLabelChanged(][\"OnNodeLabelChanged\"][)]               |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeResized(][\"OnNodeResized\"][)]                         |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeResizing(][\"OnNodeResizing\"][)]                       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeSelected(][\"OnNodeSelected\"][)]                       |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeStartLabelEdit(][\"OnNodeStartLabelEdit\"][)]           |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnNodeUnSelected(][\"OnNodeUnSelected\"][)]                   |
|                                                                                                                                                                                                                                                                                        |
| [  .ClientSideOnTailNodeChanged(][\"OnTailNodeChanged\"][)]                 |
|                                                                                                                                                                                                                                                                                        |
| [  .DiagramMode(][DiagramMode][.SVG)]                                       |
|                                                                                                                                                                                                                                                                                        |
| [  .Render();]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [  }]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                        |
| [%\>][ ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   In JavaScript, define the handlers.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\] ]**[]                                                                                       |
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
| [            //args:][]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Id          - ID attribute of the current node]]                                                                     |
|                                                                                                                                                                                                                         |
| [            [//  \_Nodes       - Details of the node][]]                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\</[script]\> ]                                                                                                                            |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

