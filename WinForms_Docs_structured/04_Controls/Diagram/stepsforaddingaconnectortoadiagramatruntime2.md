---
title: stepsforaddingaconnectortoadiagramatruntime2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\stepsforaddingaconnectortoadiagramatruntime2.md
created_at: 2025-07-03
---






#### Steps for adding a connector to a diagram at run time {#steps-for-adding-a-connector-to-a-diagram-at-run-time style="tab-stops: 0pt"}

[] 

[·      ]First set the **EnableConnection** property of DiagramView to *True*. This has to be set to true every time the user makes a connection.

[·      ]Press the left mouse button while the pointer is over the node where the connection is to start. This acts as the head node for the connector.

[·      ]While the left button is pressed, drag the pointer to the node to where you want to create a link. The cursor will change to a cross while dragging.

[] 


{border="0"}Note: If a node is not hit while making a connection, then no connector gets added.

 


{border="0"}

Figure 52: Connector DragStart

[] 

[·      ]When you hit any node in the process, you can see an adorner showing what the link will look like if created.

[] 

{border="0"}

[] 

Figure 53: HitNode

[] 

[·      ]Release the left button over the target node where you want to connect. This acts as the tail node for the connector and hence the link is created.

 

[] 

{border="0"}

Figure 54: Connection Ended

 

The connector\'s path geometry is dynamically created based on the start and end points and the connector type.

 

It is also possible to drag-and-drop line connectors from the SymbolPalette. Three shapes of the line connectors have been added in a group named "Connectors". The desired line can be dragged onto the page. Initially, the headnode and the tail node will be null. The steps to be followed to add a line connector from SymbolPalette are as follows:

[] 

1.   Drag the desired line connector onto the page.

[] 

{border="0"}

Figure 55: Bezier Line added to the Page

[] 

2.   Then drag the head thumb of the line connector to the desired node to make a connection.

[] 

{border="0"}

Figure 56: Dragging the Head Thumb

[] 

3.   Similarly drag the tail thumb of the line connector to the desired node. Now, this creates a link between the two nodes.

[] 

{border="0"}

Figure 57: Dragging the Tail Thumb

[] 

[]{#related-topics}

