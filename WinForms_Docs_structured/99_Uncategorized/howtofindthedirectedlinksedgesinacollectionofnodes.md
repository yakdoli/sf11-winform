---
title: howtofindthedirectedlinksedgesinacollectionofnodes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtofindthedirectedlinksedgesinacollectionofnodes.md
created_at: 2025-07-03
---








  









## How to find the directed links (edges) in a collection of nodes?[] {#how-to-find-the-directed-links-edges-in-a-collection-of-nodes style="tab-stops: 0pt"}

[] 

Every link realizes the IEndPointContainer interface (Syncfusion.Windows.Forms.Diagram.IEndPointContainer). To find links, simply compare all nodes to the IEndPointContainer interface.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [foreach][ ([Node] node [in] DiagramWebControl1.Model.Nodes)] |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [      [if] (node [is] [IEndPointContainer])]                                             |
|                                                                                                                                                                                              |
| [      {]                                                                                                                                                |
|                                                                                                                                                                                              |
| [            [// node is a link]]                                                                                                  |
|                                                                                                                                                                                              |
| [      }]                                                                                                                                                |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [For][ [Each] node [As] Node [In] DiagramWebControl1.Model.Nodes ] |
|                                                                                                                                                                                                                        |
| [\' node is a link ]                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [    [If] [TypeOf] node [Is] IEndPointContainer [Then] ]                                       |
|                                                                                                                                                                                                                        |
| [    [End] [If] ]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [Next][ ]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

If the node is an IEndPointContainer, you can check it to the **LineConnector or OrthogonalConnector**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [foreach][ ([Node] node [in] DiagramWebControl1.Model.Nodes)] |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [      [if] (node [is] [IEndPointContainer])]                                             |
|                                                                                                                                                                                              |
| [      {]                                                                                                                                                |
|                                                                                                                                                                                              |
| [            [if] (node [is] [LineConnector])]                                            |
|                                                                                                                                                                                              |
| [            {]                                                                                                                                          |
|                                                                                                                                                                                              |
| [                  [// LineConnector]]                                                                                             |
|                                                                                                                                                                                              |
| [            }]                                                                                                                                          |
|                                                                                                                                                                                              |
| [            [else]]                                                                                                                |
|                                                                                                                                                                                              |
| [            {]                                                                                                                                          |
|                                                                                                                                                                                              |
| [                  [if] (node [is] [OrthogonalConnector])]                                |
|                                                                                                                                                                                              |
| [                  {]                                                                                                                                    |
|                                                                                                                                                                                              |
| [                        [// OrthogonalConnector]]                                                                                 |
|                                                                                                                                                                                              |
| [                  }]                                                                                                                                    |
|                                                                                                                                                                                              |
| [            }]                                                                                                                                          |
|                                                                                                                                                                                              |
| [      }]                                                                                                                                                |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [For][ [Each] node [As] Node [In] DiagramWebControl1.Model.Nodes ] |
|                                                                                                                                                                                                                        |
| [    [If] [TypeOf] node [Is] IEndPointContainer [Then] ]                                       |
|                                                                                                                                                                                                                        |
| [\' LineConnector ]                                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [        [If] [TypeOf] node [Is] LineConnector [Then] ]                                        |
|                                                                                                                                                                                                                        |
| [        [Else] ]                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [\' OrthogonalConnector ]                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [            [If] [TypeOf] node [Is] OrthogonalConnector [Then] ]                              |
|                                                                                                                                                                                                                        |
| [            [End] [If] ]                                                                                                                |
|                                                                                                                                                                                                                        |
| [        [End] [If] ]                                                                                                                    |
|                                                                                                                                                                                                                        |
| [    [End] [If] ]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [Next]                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

LineConnector may be a directed link. To verify that, simply check **TailDecorator** and **HeadDecorator**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [if][ (node [is] [LineConnector])]     |
|                                                                                                                                                                       |
| [{]                                                                                                                               |
|                                                                                                                                                                       |
| [      [if](]                                                                                                |
|                                                                                                                                                                       |
| [      ((([LineConnector])node).HeadDecorator.DecoratorShape != [DecoratorShape].None)] |
|                                                                                                                                                                       |
| [      \|\|]                                                                                                                      |
|                                                                                                                                                                       |
| [      ((([LineConnector])node).TailDecorator.DecoratorShape != [DecoratorShape].None)] |
|                                                                                                                                                                       |
| [      )]                                                                                                                         |
|                                                                                                                                                                       |
| [      {]                                                                                                                         |
|                                                                                                                                                                       |
| [            [// Directed link]]                                                                            |
|                                                                                                                                                                       |
| [      }     ]                                                                                                                    |
|                                                                                                                                                                       |
| [      [else]]                                                                                               |
|                                                                                                                                                                       |
| [      {]                                                                                                                         |
|                                                                                                                                                                       |
| [            [// Not directed link]]                                                                        |
|                                                                                                                                                                       |
| [      }]                                                                                                                         |
|                                                                                                                                                                       |
| [}]                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [If][ [TypeOf] node [Is] LineConnector [Then] ]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [\' Directed link ]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [If] ([DirectCast](node, LineConnector).HeadDecorator.DecoratorShape \<\> DecoratorShape.None) [OrElse] ([DirectCast](node, LineConnector).TailDecorator.DecoratorShape \<\> DecoratorShape.None) [Then] ] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [\' Not directed link ]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [Else] ]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [If] ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

