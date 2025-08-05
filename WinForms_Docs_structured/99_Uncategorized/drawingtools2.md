---
title: drawingtools2.md
original_path: WinForms_Docs/99_Uncategorized/drawingtools2.md
created_at: 2025-08-05
---








  









### Drawing Tools {#drawing-tools style="tab-stops: 0pt"}

This feature enables you to draw different shapes and lines. The drawn shapes and lines will be converted into Node and LineConnector respectively.

The following shapes and lines are available in DrawingTools:

1.   Ellipse

2.   Rectangle

3.   Rounded Rectangle

4.   Polygon

5.   Straight Line

6.   Bezier Line

7.   Orthogonal Line

8.   Polyline

 

Use Case Scenarios

DrawingTools such as Microsoft Paint and Expression Blend support drawing a particular shape continually on a page. This feature too, enables you to draw a shape repeatedly without selecting it manually each time.

 

Properties

Table 77: DrawingToolsProperty Table


+--------------------+---------------------------------------------------------------------------------+----------------------+-----------------------------------------------+---------------------------------------------------+
| Property           | Description                                                                     | Type of the Property | Value It Accepts                              | Any Other Dependencies/ Sub properties Associated |
+--------------------+---------------------------------------------------------------------------------+----------------------+-----------------------------------------------+---------------------------------------------------+
| EnableDrawingTools | Gets or sets a value indicating whether   EnableDrawingTools is enabled or not. | Dependency property  | Boolean(True/False)[] | No[]                      |
+--------------------+---------------------------------------------------------------------------------+----------------------+-----------------------------------------------+---------------------------------------------------+
| DrawingTools       | Gets or sets the ShapeType to be used.                                          | Dependency property  | DrawingTools.Ellipse                          | No                                                |
|                    |                                                                                 |                      |                                               |                                                   |
|                    | Default value is                                                                |                      | DrawingTools.Rectangle                        |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    | DrawingTools.Ellipse                                                            |                      | DrawingTool.RoundedRectangle                  |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    |                                                                                 |                      | DrawingTools.Polygon                          |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    |                                                                                 |                      | DrawingTools.StraightLine                     |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    |                                                                                 |                      | DrawingTools.BezierLine                       |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    |                                                                                 |                      | DrawingTools.OrthogonalLine                   |                                                   |
|                    |                                                                                 |                      |                                               |                                                   |
|                    |                                                                                 |                      | DrawingTools.PolyLine                         |                                                   |
+--------------------+---------------------------------------------------------------------------------+----------------------+-----------------------------------------------+---------------------------------------------------+


 

Sample Link

To view a sample:

1.   Open the WPF sample browser from the dashboard.

2.   Navigate to WPF Diagram \> Product Showcase \>Features demo

 

More:









