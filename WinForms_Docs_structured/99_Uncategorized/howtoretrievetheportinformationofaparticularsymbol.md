---
title: howtoretrievetheportinformationofaparticularsymbol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoretrievetheportinformationofaparticularsymbol.md
created_at: 2025-07-03
---








  









## How To Retrieve the Port Information Of a Particular Symbol {#how-to-retrieve-the-port-information-of-a-particular-symbol style="tab-stops: 0pt"}

[] 

You can retrieve port information of a particular symbol using the **HandlesHitTesting.GetConnectionPointAtPoint(Node, Point)** method.

 

This method has two parameters: *Node* and *Port*.

[] 

[·      ]Node specifies the symbol in which the port resides

[·      ]Point specifies the Point object that holds the location of the port.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [ConnectionPoint][ port = [HandlesHitTesting].GetConnectionPointAtPoint(circle, [new] [Point](120, 120)); ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [Dim][ port [As] ConnectionPoint = HandlesHitTesting.GetConnectionPointAtPoint(circle, [New] Point(120, 120))] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p94} 

 

[]{#related-topics}

