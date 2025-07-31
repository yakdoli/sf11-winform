---
title: clientsideevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

[] 

DiagramWebControl has the following client-side events.

[] 

[·      ]OnClientCanvaClick

[·      ]OnClientCanvaScroll

[·      ]OnClientDiagramZoom

[·      ]OnClientNodeChangeText

[·      ]OnClientNodeClick

[·      ]OnClientNodeDoubleClick

[·      ]OnClientNodeDrop

[·      ]OnClientNodeDropFromPalette

[·      ]OnClientNodeMouseDown

[·      ]OnClientNodeMouseMove

[·      ]OnClientNodeMouseOut

[·      ]OnClientNodeMouseOver

[·      ]OnClientNodeMouseUp

[] 

OnClientCanvaClick and OnClientCanvaScroll Events

[] 

The OnClientCanvaClick and OnClientCanvaScroll events include the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[] 

OnClientDiagramZoom Event

[] 

The OnClientDiagramZoom event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Zoom

[] 

OnClientNodeChangeText Event

[] 

The OnClientNodeChangeText event includes the following parameters.

[] 

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[·      ]OldText

[·      ]NewText

[] 

OnClientNodeClick Event

[] 

The OnClientNodeClick event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeDoubleClick Event

[] 

The OnClientNodeDoubleClick event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeDrop Event

[] 

The OnClientNodeDrop event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeDropFromPalette Event

[] 

The OnClientNodeDropFromPalette event includes the following parameters.

[] 

[·      ]GroupBarID

[·      ]PaletteID

[·      ]NodeID

[·      ]NodeName

[·      ]X (x coordinate position)

[·      ]Y (y coordinate position)

[] 

OnClientNodeMouseDown Event

[] 

The OnClientNodeMouseDown event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeMouseMove Event

[] 

The OnClientNodeMouseMove event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeMouseOut Event

[] 

The OnClientNodeMouseOut event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeMouseOver Event

[] 

The OnClientNodeMouseOver event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

OnClientNodeMouseUp Event

[] 

The OnClientNodeMouseUp event includes the following parameters.

[] 

[·      ]Event

[·      ]El (element)

[·      ]Node

[·      ]FromNode

[·      ]ToNode

[] 

Example

[] 

To show the scroll left and top position in the DiagramWebControl using client-side events

[] 

1.   Drag **DiagramWebControl** onto the web page and modify the code in the HTML tag as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][html][ [xmlns][=\"http://www.w3.org/1999/xhtml\"\>]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][head][ [id][=\"Head1\"] [runat][=\"server\"\>]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][title][\>][Untitled Page[\</][title][\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][script][ [language][=\"javascript\"] [type][=\"text/javascript\"\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [function][ ScrollPosition(oData)]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [var][ oDiagram = oData.El;]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [document.getElementById([\"LeftScrollPosition\"]).innerHTML = oDiagram.scrollLeft;]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [document.getElementById([\"TopScrollPosition\"]).innerHTML = oDiagram.scrollTop;]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][script][\>]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][head][\>]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][body][\>]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][form][ [id][=\"form2\"] [runat][=\"server\"\>]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][div][\>]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][div][\>]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][DiagramWebControl][ [ID][=\"DiagramWebControl2\"] [runat][=\"server\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [BoundaryConstraintsEnabled][=\"True\"][ ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [DocumentID][=\"808c2164-05ed-4e0f-a475-05f3d83f6165\"][ [Height][=\"500px\"] ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Width][=\"600px\"][ ]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [OnClientCanvaScroll][ [=] [\"ScrollPosition(this)\"] [/\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][span][ [id][=\"LeftScrollPosition\"\>]0[\</][span][\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][span][ [id][=\"TopScrollPosition\"\>]0[\</][span][\>]]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][form][\>]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][body][\>]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][html][\>]                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Run the application. Move the scroll bars to view the scroll bars position.

[] 

{border="0"} 

 

{border="0"}

[] 

Figure 73: Client-Side Event

[] 


{border="0"}Note: If the events are raised on callback, return False to cancel the callback.


 

 

[]{#related-topics}

