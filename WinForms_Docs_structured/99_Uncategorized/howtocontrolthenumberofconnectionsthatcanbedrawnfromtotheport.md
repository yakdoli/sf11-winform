---
title: howtocontrolthenumberofconnectionsthatcanbedrawnfromtotheport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocontrolthenumberofconnectionsthatcanbedrawnfromtotheport.md
created_at: 2025-07-03
---








  









## How To Control the Number Of Connections That Can Be Drawn From / To the Port {#how-to-control-the-number-of-connections-that-can-be-drawn-from-to-the-port style="tab-stops: 0pt"}

[] 

This can be done using the port\'s **ConnectionsLimit** property. ConnectionsLimit specifies the number of connections to be allowed. Default value is ***10***.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [Syncfusion.Windows.Forms.Diagram.ConnectionPoint cp = [new ]Syncfusion.Windows.Forms.Diagram.ConnectionPoint();] |
|                                                                                                                                                                            |
| [cp.ConnectionsLimit = 12;]                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [Dim][ cp[ As New ]Syncfusion.Windows.Forms.Diagram.ConnectionPoint()] |
|                                                                                                                                                                                  |
| [cp.ConnectionsLimit = 12]                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p74} 

 

[]{#related-topics}

