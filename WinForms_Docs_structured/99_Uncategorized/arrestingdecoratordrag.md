---
title: arrestingdecoratordrag.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\arrestingdecoratordrag.md
created_at: 2025-07-03
---






#### Arresting Decorator Drag {#arresting-decorator-drag style="tab-stops: 0pt"}

The user can disable the drag operation on the decorator adorner of a line connector by setting the **IsDecoratorMovable** property to False.

 

Table 5: Property Table[]

  -------------------- ----------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property             Description                                                                   Type of the property   Value it accepts        Any other dependencies/ sub properties associated
  IsDecoratorMovable   Gets or sets a value indicating whether this instance is decorator movable.   Dependency property    Boolean (true/ false)   No
  -------------------- ----------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

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
| [lc.IsDecoratorMovable = [false];]                                                                                          |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [lc.IsDecoratorMovable = [False]]                                                                                                     |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The decorator adorner drag of a line connector is arrested.

[]{#related-topics}

