---
title: graphicelements.md
original_path: WinForms_Docs/99_Uncategorized/graphicelements.md
created_at: 2025-08-05
---






##### Graphic Elements {#graphic-elements style="tab-stops: 0pt"}

[] 

These include the basic functionality of drawing elements on the canvas (PdfGraphics). As a result, you can draw such objects on pages or any other object that has graphics context (PdfTemplate etc). Graphics elements are simple and does not span several pages.

 

Layout

 

**PdfLayoutElement** class provides an ability to draw contents on several pages. This functionality is described in the  section.

[] 

Shapes

[] 

**PdfShapeElement** class provides the basic functionality of simple graphics primitives (like lines, rectangles, etc.). It is derived from LayoutElement, which enables every shape to span several pages. The basic graphics primitives are as follows:

[] 

[·      ]Line

[·      ]Rectangle

[·      ]Polygon

[·      ]Arc

[·      ]Bezier Curve

[·      ]Ellipse

[·      ]Path

[·      ]PdfTemplate

[·      ]Pie

[·      ]Image

[] 

Each shape can be drawn by its own **Draw** method or by using an appropriate method of the **PdfGraphics** class (like DrawLine, DrawRectangle, etc.). Each shape has its own coordinate system (which is equal to a page coordinate system). Coordinates of the shape are set in that coordinate system. When the shape is going to be drawn by using its **Draw** method, its coordinate system is translated by the coordinates set to the Draw method. So, whenever the shape is going to be drawn, take its own coordinate system into consideration.

 

The following screen shot illustrates the shape drawing behavior.

 

{border="0"}

Figure 26: Shape drawing behavior

 

[]{#related-topics}

