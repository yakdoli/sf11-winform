---
title: drawingtools.md
original_path: WinForms_Docs/99_Uncategorized/drawingtools.md
created_at: 2025-08-05
---








  









### DrawingTools {#drawingtools style="tab-stops: 0pt"}

This feature enables you to draw different shapes and lines. The drawn shapes and lines will be converted into Node and LineConnector respectively.

The following shapes and lines are available in DrawingTools:

 

1.   Ellipse

2.   Rectangle

3.   Rounded Rectangle

4.   Polygon

5.   Straight Line

6.   Bezier Line

7.   Orthogonal Line

 

 Use Case Scenarios

DrawingTools such as Microsoft Paint and Expression Blend support drawing a particular shape continually on a page. This feature too, enables you to draw a shape repeatedly without selecting it manually each time.

Properties

Table 13: DrawingToolsProperty**[ ]**Table


+--------------------+---------------------------------------------------------------------------------------+---------------------+-----------------------------------------------+------------------------------+
| Property           | Description                                                                           | Type                | Data Type                                     | Reference Link               |
+--------------------+---------------------------------------------------------------------------------------+---------------------+-----------------------------------------------+------------------------------+
| EnableDrawingTools | Gets or sets a value indicating whether   EnableDrawingTools is enabled or dis abled. | Dependency property | Boolean(True/False)[] | NA[] |
+--------------------+---------------------------------------------------------------------------------------+---------------------+-----------------------------------------------+------------------------------+
| DrawingTools       | Gets or sets the ShapeType to be used.                                                | Dependency property | Enum                                          | NA                           |
|                    |                                                                                       |                     |                                               |                              |
|                    | Default value is                                                                      |                     | DrawingTools.Ellipse                          |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    | DrawingTools.Ellipse                                                                  |                     | DrawingTools.Rectangle                        |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTool.RoundedRectangle                  |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTools.Polygon                          |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTools.StraightLine                     |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTools.BezierLine                       |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTools.OrthogonalLine                   |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     | DrawingTools.PolyLine                         |                              |
|                    |                                                                                       |                     |                                               |                              |
|                    |                                                                                       |                     |                                               |                              |
+--------------------+---------------------------------------------------------------------------------------+---------------------+-----------------------------------------------+------------------------------+


 

 

Sample Link[]

 To view a sample:

1.   Open the Silverlight sample browser from the dashboard.

2.   Navigate to SL Diagram -\> Product Showcase -\> Diagram Builder

[] 

More:









