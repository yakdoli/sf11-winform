---
title: linebridging.md
original_path: WinForms_Docs/99_Uncategorized/linebridging.md
created_at: 2025-08-05
---








  









### Line Bridging {#line-bridging style="tab-stops: 0pt"}

[] 

Line bridging provides the visual effect such that the links jump over other links that are found in it\'s way with lower ZOrder, thereby avoiding the links from intersecting each other and providing a hassle-free view to clearly state the various connections between the nodes. This is done by enabling the LineBridgingEnabled property. Default value is ***false***.

[] 

{border="0"}

[] 

Figure 45:  Line Bridging

[] 

The below table lists the properties which controls the appearance of the bridge.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LineBridgeSize                    | Allows to set the size of the bridge when the links intersect each other. Default value is 16.                                                                                                                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BridgeStyle                       | Specifies the type of bridge to be applied. Default value is \'Arc\'. The value when set, applies to all the links that are drawn on the diagram. The links will bridge over the other link only when it\'s ZOrder value is high. The options include the following: |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | []                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Arc                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Gap                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Square                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side2                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side3                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side4                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side5                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side6                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                      |
|                                   | [·      ]Side7                                                                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically it can be set as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                             |
|                                                                                                                                                                 |
| [this][.diagram1.Model.LineBridgeSize = 5;]                                |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [//enabling for model]                                                                                        |
|                                                                                                                                                                 |
| [this][.diagram1.Model.LineBridgingEnabled = [true];] |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [//enabling for link object]                                                                                  |
|                                                                                                                                                                 |
| [link.LineBridgingEnabled = [true];]                                                                   |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [this][.diagram1.Model.BridgeStyle = BridgeStyle.Square;]                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                          |
|                                                                                                                                                              |
| [Me][.diagram1.Model.LineBridgeSize = 5]                                |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [\'enabling for model]                                                                                     |
|                                                                                                                                                              |
| [Me][.diagram1.Model.LineBridgingEnabled = [True]] |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [\'enabling for link object]                                                                               |
|                                                                                                                                                              |
| [link.LineBridgingEnabled = [True]]                                                                 |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [Me][.diagram1.Model.BridgeStyle = BridgeStyle.Square]                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: In the above code snippets, link refers to the instance of the Link node.


[]{#p28} 

[]{#related-topics}

