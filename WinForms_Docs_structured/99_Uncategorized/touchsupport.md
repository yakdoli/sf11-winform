---
title: touchsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\touchsupport.md
created_at: 2025-07-03
---








  









### Touch Support {#touch-support style="tab-stops: 0pt"}

Touch support for diagram view has the following features:

[·      ]Drag and Drop from the SymbolPalette

[·      ]Dragging the Node and LineConnector on DiagramView

[·      ]Panning

[·      ]Multiple selection

 

Steps for Dragging:

Dragging operation can be performed by

1.   Touch a particular element in the touch screen monitor.

2.   Start dragging the element to the desired location.

3.   Take the finger off from the screen after it is reached to the desired location.

This dragging gesture is used to perform the following operation.

Drag and Drop from the SymbolPalette

1.   Touch the SymbolPaletteItem for Drag and Drop.

2.   Drag the SymbolPaletteItem and Drop onto DiagramView by touching the finger in DiagramView.

 

Dragging the Node and LineConnector on DiagramView

1.   Touch the Node or Lineconnector for Dragging.

2.   The selected item can be moved around using your finger.

 

Panning

1.   Please enable the IsPanEnabled property of the DiagramView.

2.   Drag the finger over DiagramView, the DiagramView gets panned along the finger.

 

Multiple selections

1.   Touch the empty space of the DiagramView.

2.   Drag the finger in DiagramView, the Selection Adorner will be visible.

3.   Objects which are getting intersected while dragging will get selected.

{border="0"}

Figure 174: Drag

MultiTouch Support:

MultiTouch support has been provided to enable zoom the page and resizing a Node.

**Steps for Spreading and Pinching**

1.   Use two fingers to touch the monitor.

2.   Move the fingers away to perform spread operation.

3.   Move the fingers close to each other to perform pinch operation.

4.   Take the fingers off from the screen after the required size is achieved.

 

This spread and pinch gesture is used to perform, zooming and resizing operation.

[·      ]Zooming the DiagramView with two fingers can be done

[·      ]Resizing the Node with two fingers can be done

 

{border="0"}

Figure 175: Spread

 

 

{border="0"}

Figure 176: Pinch

{border="0"}

Steps for Zooming:

1.   Touch the DiagramView with two fingers.

2.   Pinch represents the ZoomOut.

3.   Spread represents the ZoomIn.

 

Steps for Resizing:

1.   Touch the Node for resizing with two Fingers.

2.   Pinch Represents - Increase the size of the Node.

3.   Spread Represents - Decrease the size of the Node.

[]{#related-topics}

