---
title: howtofindthataconnectionmadewasntsuccessful.md
original_path: WinForms_Docs/99_Uncategorized/howtofindthataconnectionmadewasntsuccessful.md
created_at: 2025-08-05
---








  









## How to find that a connection made wasn\'t successful? {#how-to-find-that-a-connection-made-wasnt-successful style="tab-stops: 0pt"}

[] 

We can use the **TailEndPoint.Port** and **HeadEndPoint.Port** for this purpose.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [if][ (link.TailEndPoint.Port != [null])] |
|                                                                                                                                                     |
| [{]                                                                                                             |
|                                                                                                                                                     |
| [// Connected ]                                                                                   |
|                                                                                                                                                     |
| [}]                                                                                                             |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [if][ (link.HeadEndPoint.Port != [null])] |
|                                                                                                                                                     |
| [{]                                                                                                             |
|                                                                                                                                                     |
| [// Connected]                                                                                    |
|                                                                                                                                                     |
| [}]                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Connected]                                                                                                                                            |
|                                                                                                                                                                                                             |
| [If][ link.TailEndPoint.Port [IsNot] [Nothing] [Then] ] |
|                                                                                                                                                                                                             |
| [End][ [If] ]                                                                                     |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Connected ]                                                                                                                                           |
|                                                                                                                                                                                                             |
| [If][ link.HeadEndPoint.Port [IsNot] [Nothing] [Then] ] |
|                                                                                                                                                                                                             |
| [End][ [If]]                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Link -- LineConnector

[] 

A connection can also be checked while trying to connect two nodes. If **TryConnect()** method returns \'True\', then the connection was successful and vice versa.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [private][ [void] ConnectNodes([Node] parent, [Node] child)]                                                      |
|                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [      [if] (parent != [null] && child != [null] && parent.EnableCentralPort && child.EnableCentralPort)]                                                          |
|                                                                                                                                                                                                                                                                       |
| [      {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [            [LineConnector] link = [new] [LineConnector]([PointF].Empty, [new] [PointF](10, 10));] |
|                                                                                                                                                                                                                                                                       |
| [            [this].DiagramWebControl1.Model.AppendChild(link);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            parent.CentralPort.TryConnect(link.TailEndPoint);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            child.CentralPort.TryConnect(link.HeadEndPoint);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [      }]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] ConnectNodes([ByVal] parent [As] Syncfusion.Windows.Forms.Diagram.Node, [ByVal] child [As] Syncfusion.Windows.Forms.Diagram.Node)]                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [If][ parent [IsNot] [Nothing] [AndAlso] child [IsNot] [Nothing] [AndAlso] parent.EnableCentralPort [AndAlso] child.EnableCentralPort [Then]] |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ link [As] [New] Syncfusion.Windows.Forms.Diagram.LineConnector(PointF.Empty, [New] PointF(10, 10))]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.DiagramWebControl1.Model.AppendChild(link)]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [parent.CentralPort.TryConnect(link.TailEndPoint)]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [child.CentralPort.TryConnect(link.HeadEndPoint)]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

