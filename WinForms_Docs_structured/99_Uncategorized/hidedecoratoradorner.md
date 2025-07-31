---
title: hidedecoratoradorner.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hidedecoratoradorner.md
created_at: 2025-07-03
---






#### Hide Decorator Adorner {#hide-decorator-adorner style="tab-stops: 0pt"}

The user can hide the decorator adorner of a line connector by setting the **IsDecoratorVisible** property to False.

[] 

  -------------------- ------------------------------------------------------------------------------------- ---------------------- ------------------------ ---------------------------------------------------
  Property             Description                                                                           Type of the property   Value it accepts         Any other dependencies/ sub properties associated
  IsDecoratorVisible   Gets or sets a value indicating whether this instance is decorator adorner visible.   Dependency property    Boolean (true / false)   No
  -------------------- ------------------------------------------------------------------------------------- ---------------------- ------------------------ ---------------------------------------------------

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
| [lc.IsDecoratorVisible = [false]; ]                                                                                         |
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
| [lc.IsDecoratorVisible = [False]]                                                                                                     |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

{border="0"}

Figure 64:Decorator Adorner Style not visible

 

[]{#related-topics}

