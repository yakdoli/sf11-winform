---
title: serversideevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serversideevents.md
created_at: 2025-07-03
---






#### Server-Side Events {#server-side-events style="tab-stops: 0pt"}

[] 

DiagramWebControl has the following server-side events.

[] 

[·      ]CallbackRefresh

[·      ]CanvaClick

[·      ]DiagramZoom

[·      ]Disposed

[·      ]ImageGridCellUpdating

[·      ]Init

[·      ]KeyDown

[·      ]KeyPress

[·      ]LayoutUpdated

[·      ]Load

[·      ]PostbackDescriptors

[·      ]PreRender

[·      ]Unload

[·      ]DataBinding

[·      ]NodeChangeText

[·      ]NodeClick

[·      ]NodeDoubleClick

[·      ]NodeDrop

[·      ]NodeDropFromPalette

[·      ]NodeResize

[·      ]NodeUpdate

[] 

CallbackRefresh Event

[] 

This is a server-side event that is triggered with the client-side args, after calling client object Refresh( sArg ) method.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Shared.CallbackEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Shared.CallbackEventArgs member provides information specific to this event.

[] 


+-----------------------------------+-----------------------------------+
|                                   |                                   |
|                                   |                                   |
| Member                            | Description                       |
+-----------------------------------+-----------------------------------+
| CallbackArgument                  | The arguments sent by the client. |
+-----------------------------------+-----------------------------------+


[] 

CanvaClick Event

[] 

This is a server-side event that is triggered after a canva is clicked.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.CanvaClickEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.CanvaClickEventArgs members provide information specific to this event.

[] 


+-----------------------------------+-----------------------------------------------------------------+
|                                   |                                                                 |
|                                   |                                                                 |
| Member                            | Description                                                     |
+-----------------------------------+-----------------------------------------------------------------+
| AltKey                            | Indicates whether the ALT key was pressed.                      |
+-----------------------------------+-----------------------------------------------------------------+
| CtrlKey                           | Indicates whether the CTRL key was pressed.                     |
+-----------------------------------+-----------------------------------------------------------------+
| DiagramWebControl                 | Current DiagramWebControl                                       |
+-----------------------------------+-----------------------------------------------------------------+
| MouseXInModel                     | Mouse X position in current model.                              |
+-----------------------------------+-----------------------------------------------------------------+
| MouseYInModel                     | Mouse Y position in current model.                              |
+-----------------------------------+-----------------------------------------------------------------+
| PosX                              | Mouse X position in current DiagramWebControl for current view. |
+-----------------------------------+-----------------------------------------------------------------+
| PosY                              | Mouse Y position in current DiagramWebControl for current view. |
+-----------------------------------+-----------------------------------------------------------------+
| ScrollLeft                        | Left scroll position in current DiagramWebControl.              |
+-----------------------------------+-----------------------------------------------------------------+
| ScrollTop                         | Top scroll position in current DiagramWebControl.               |
+-----------------------------------+-----------------------------------------------------------------+
| ShiftKey                          | Indicates whether the SHIFT key was pressed.                    |
+-----------------------------------+-----------------------------------------------------------------+


[] 

DiagramZoom Event

[] 

This is a server-side event that is triggered after the diagram zoom operation.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.DiagramZoomEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.DiagramZoomEventArgs members provide information specific to this event.

 


  ------------------- ----------------------------------------------------
  Member              Description
  DiagramWebControl   Current DiagramWebControl
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  Zoom                Current zoom value in current DiagramWebControl.
  ------------------- ----------------------------------------------------


[] 

ImageGridCellUpdating Event

[] 

This is a server-side event that is triggered when the client\'s image grid image needs to be updated.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.ImageGridCellUpdatingEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.ImageGridCellUpdatingEventArgs members provide information specific to this event.

[] 


  --------------- ----------------------------------------
  Member          Description
  Graphics        Graphics to draw on.
  ImageOrigin     Image origin in document.
  Magnification   DiagramWebControl magnification value.
  --------------- ----------------------------------------


[] 

KeyDown Event

[] 

This is a server-side event that is triggered in response to a key down event.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs members provide information specific to this event.

[] 


  ------------------- ----------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- ----------------------------------------------------


[] 

KeyPress Event

[] 

This is a server-side event that is triggered in response to a key press event.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs members provide information specific to this event.

[] 


  ------------------- ----------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- ----------------------------------------------------


[] 

KeyUp Event

[] 

This is a server-side event that is triggered in response to a key press event.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.KeybEventArgs members provide information specific to this event.

[] 


  ------------------- ----------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- ----------------------------------------------------


[] 

NodeChangeText Event

[] 

This is a server-side event that is triggered when the node text is changed.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeChangeTextEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeChangeTextEventArgs members provide information specific to this event.

[] 


  ------------------- --------------------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl.
  KeyCode             Unicode key character.
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  NewText             New node text
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X offset
  OffsetY             Y offset
  OldText             Old node text
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- --------------------------------------------------------------


[] 

NodeClick Event

[] 

This is a server-side event that is triggered after a node is clicked.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeClickEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeClickEventArgs members provide information specific to this event.

[] 


  Member              Description
  ------------------- --------------------------------------------------------------
  AltKey              Indicates whether the ALT key was pressed.
  ControlPoint        Gets active ControlPoint.
  ControlPointId      Gets ControlPoint id.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl.
  EndPoint            Gets active EndPoint.
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X Offset
  OffsetY             Y Offset
  PathNode            Gets PathNode.
  PathPoint           Gets active ControlPoint in local coordinates.
  PathPointId         Gets PathPointId.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.


[] 

The following code example illustrates how to change the properties of a diagram node when the mouse is clicked over the node.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [this][.DiagramWebControl1.NodeClick += [new] [NodeClickEventHandler](DiagramWebControl1_NodeClick);]           |
|                                                                                                                                                                                                                                                   |
| [protected][ [void] DiagramWebControl1_NodeClick([object] sender, [NodeClickEventArgs] e)] |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.Color = System.Drawing.[Color].SaddleBrown;]                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.ColorAlphaFactor = 100;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.ForeColor = System.Drawing.[Color].SteelBlue;]                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.ForeColorAlphaFactor = 70;]                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.Type = [FillStyleType].PathGradient;]                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.PathBrushStyle = [PathGradientBrushStyle].RectangleLeftBottom;]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.Type = [FillStyleType].Hatch;]                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.GradientAngle = 95;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [ellipse.FillStyle.GradientCenter = 0.5f;]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 71: NodeClick Event

[] 

NodeDoubleClick Event

[] 

This is a server-side event that is triggered after a node is double-clicked.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeDoubleClickEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeDoubleClickEventArgs members provide information specific to this event.

[] 


  ------------------- --------------------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X Offset
  OffsetY             Y Offset
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- --------------------------------------------------------------


[] 

NodeDrop Event

[] 

This is a server-side event that is triggered after a node drop operation.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeDropEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeDropEventArgs members provide information specific to this event.

[] 


  ------------------- --------------------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X Offset
  OffsetY             Y Offset
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- --------------------------------------------------------------


[] 

NodeDropFromPalette Event

[] 

This is a server-side event that is triggered when a node is dragged from the PaletteGroupBar to the DiagramWebControl.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeDropFromPaletteEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeDropFromPaletteEventArgs members provide information specific to this event.

[] 


  ------------------- ---------------------------------------------------------------------------------
  Member              Description
  DiagramWebControl   Current DiagramWebControl.
  GroupBarId          Gets GroupBar id.
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  Node                Gets dragged node.
  NodeId              Gets Node id in the palette.
  Palette             Gets the Symbol Palette from which the node has been dragged.
  PaletteGroupBar     Gets reference to PaletteGroupBar control from which the node has been dragged.
  PaletteId           Gets palette id.
  PosX                Gets node insert position on X.
  PosY                Gets node insert position on Y.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ------------------- ---------------------------------------------------------------------------------


[] 

NodeResize Event

[] 

This is a server-side event that is triggered after a node is resized.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeResizeEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeResizeEventArgs members provide information specific to this event.

[] 


  ------------------- --------------------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  NewHeight           Gets new height of node.
  NewWidth            Gets new width of node.
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X Offset
  OffsetY             Y Offset
  ResizeCorner        Gets node resize corner.
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  ------------------- --------------------------------------------------------------


[] 

NodeUpdate Event

[] 

This is a server-side event that is triggered after a node is updated.

 

The event handler receives an argument of type **Syncfusion.Web.UI.WebControls.Diagram.NodeUpdateEventArgs** containing data related to this event. The following Syncfusion.Web.UI.WebControls.Diagram.NodeUpdateEventArgs members provide information specific to this event.

[] 


  ------------------- --------------------------------------------------------------
  Member              Description
  AltKey              Indicates whether the ALT key was pressed.
  CtrlKey             Indicates whether the CTRL key was pressed.
  DiagramWebControl   Current DiagramWebControl
  KeyCode             Unicode key character
  MouseXInModel       Mouse X position in current model.
  MouseYInModel       Mouse Y position in current model.
  Node                Node on which some action has been effectuated.
  NodeFullName        Full name of node on which some action has been effectuated.
  NodeName            Name of node on which some action has been effectuated.
  NodeUnderMouse      Node which is under the mouse cursor.
  OffsetX             X Offset
  OffsetY             Y Offset
  ScrollLeft          Left scroll position in current DiagramWebControl.
  ScrollTop           Top scroll position in current DiagramWebControl.
  ShiftKey            Indicates whether the SHIFT key was pressed.
  UserArguments       Gets user arguments for the event.
  ------------------- --------------------------------------------------------------


[] 

Example

[] 

To display a rectangle when the user clicks on the DiagramWebControl

[] 

1.   Drag the DiagramWebControl onto the web page.

2.   Right-click on the **DiagramWebControl**.

3.   Select **Properties** option in the pop-up menu that is displayed.

4.   Click **Events** in the properties menu.

5.   Double-click the **CanvaClick** event. This opens the aspx.cs file.

[] 

Include the following code snippet in the aspx.cs file to create a rectangle.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [protected][ [void] DiagramWebControl1_CanvaClick([object] sender, Syncfusion.Web.UI.WebControls.Diagram.[CanvaClickEventArgs] e)] |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] rectangle = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](20, 20, 50, 30);]                                                   |
|                                                                                                                                                                                                                                                                                           |
| [rectangle.Name = [\"My first rectangle\"];]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [DiagramWebControl1.Model.AppendChild(rectangle);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. Click on the DiagramWebControl canva to view the rectangle.

[] 

{border="0"}

[] 

Figure 72: CanvaClick Event Sample

[]{#related-topics}

