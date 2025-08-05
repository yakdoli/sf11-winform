---
title: hidevertex.md
original_path: WinForms_Docs/99_Uncategorized/hidevertex.md
created_at: 2025-08-05
---






#### Hide Vertex {#hide-vertex style="tab-stops: 0pt"}

**[]** 

The user can hide the vertex of a line connector by setting the **IsVertexVisible** property to False.

[] 

  ----------------- -------------------------------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------
  Property          Description                                                                Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  IsVertexVisible   Gets or sets a value indicating whether this instance is vertex visible.   Dependency property    Bool(true/false)   No
  ----------------- -------------------------------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
| [LineConnector][ lc = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [lc.ConnectorType = [ConnectorType].Straight;]                                                                           |
|                                                                                                                                                                                      |
| [lc.StartPointPosition = [new] [Point](100, 100);]                                                  |
|                                                                                                                                                                                      |
| [lc.EndPointPosition = [new] [Point](300, 300);]                                                    |
|                                                                                                                                                                                      |
| [lc.IntermediatePoints.Add([new] [Point](200, 100));]                                               |
|                                                                                                                                                                                      |
| [lc.IntermediatePoints.Add([new] [Point](200, 300));]                                               |
|                                                                                                                                                                                      |
| [lc.IsVertexVisible = [false]; ]                                                                                            |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
| [Dim][ lc [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [lc.ConnectorType = ConnectorType.Straight]                                                                                                                |
|                                                                                                                                                                                                |
| [lc.StartPointPosition = [New] Point(100, 100)]                                                                                       |
|                                                                                                                                                                                                |
| [lc.EndPointPosition = [New] Point(300, 300)]                                                                                         |
|                                                                                                                                                                                                |
| [lc.IntermediatePoints.Add(New Point(200, 100))]                                                                                                           |
|                                                                                                                                                                                                |
| [lc.IntermediatePoints.Add(New Point(200, 300))]                                                                                                           |
|                                                                                                                                                                                                |
| [lc.IsVertexVisible = [False]]                                                                                                        |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

{border="0"}

Figure 63: Vertex Style not visible

[]{#related-topics}

