---
title: stepsfordrawing1.md
original_path: WinForms_Docs/99_Uncategorized/stepsfordrawing1.md
created_at: 2025-08-05
---






#### Steps for Drawing {#steps-for-drawing style="tab-stops: 0pt"}

 You can draw on a page by click and drag on the page.

 Follow are the below steps to draw a shape or a line:

 

1.  Set the **EnableDrawingTools** property of DiagramView to **true**.

2.  Select the DrawingTool as required from DrawingTools option.

3.  Click and drag. Preview of the drawing will be displayed.

4.  Release the mouse. Shape or line will be drawn.

Note:[ ]These steps are common for all shapes and lines drawing, except Polygon and Polyline.

 

**Shape Drawing:**

Preview Ellipse -- while Drawing

 

 

{hspace="12" align="left"}[\
]

*[Figure ][167][:Ellipse Preview]*

*[]* 

Ellipse -- After Drawing.

*[]* 

*[{border="0"}]*

*[Figure ][168][:Ellipse(Node)]*

*[       ]*

**[Line Drawing:]**

Bezier Line Preview -- While Drawing

**[{border="0"}]**

*[Figure ][169][:Bezier Line Preview]*

Bezier Line -- After Drawing

{border="0"}

*[Figure ][170][:Bezier Line(Line Connector)]*

 

***Note:***

[·      ]***The drawn shape will be converted into a Node.***

[·      ]***The drawn line will be converted into a*** ***LineConnector.***

[·      ]***You can continually draw the selected shape.***

[·      ]***Lines cannot be drawn*** ***continually.***

 

 

 

**Steps for drawing a Polygon and Polyline Drawing:**

 

1.  Set the **EnableDrawingTools** property of DiagramView to be true.

2.  Select the DrawingTool as required from DrawingTools option.

3.  Click, where you want the first point for polygon (or) polyline.

4.  Drag the mouse pointer. Preview of the drawing will be displayed.

5.  Click, where you want to place the Intermediate points of Polygon (or) Polyline

6.  Right-click to complete the drawing.

 

Preview Polygon -- While Drawing

{border="0"}

*[Figure ][171][: Polygon Preview]*

[                             ]*[]*

Polygon -- After Drawing

{border="0"}

*[Figure ][172][: Polygon(Node)]*

                                      *[]*

[]{#_Freeze_Panes}Sample Link

To view a sample:

1\. Open the WPF sample browser from the dashboard.

2\. Navigate to WPF Diagram -\> Product Showcase -\>Features demo

[]{#related-topics}

