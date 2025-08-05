---
title: graphics.md
original_path: WinForms_Docs/99_Uncategorized/graphics.md
created_at: 2025-08-05
---






#### Graphics {#graphics style="tab-stops: 0pt"}

[]{#p34} 

Primitives

[] 

The general class **PdfGraphics** enables to draw a wide range of primitives like lines, curves, paths and text. For each such operation there is a set of methods called **Draw\<primitive\>()** (e.g. DrawLine). Each set of methods accepts parameters specific to each primitive type (for example: pen, brush, boundaries, etc). If pen is used, the primitive is drawn, and if brush is used, the primitive is filled. You can also use Null value instead of pen or brush.

[] 

The following are the public members exposed by the PdfGraphics class.

[] 

Methods

[] 


  ----------------------------- -----------------------------------------------------------------------------------------------------
  Name                          Description
  CheckCorrectLayoutRectangle   Creates laid
  ClipTranslateMargins          Sets the drawing area and translates the origin
  DrawArc                       Draws an arc
  DrawBezier                    Draws a Bezier curve
  DrawEllipse                   Draws an ellipse
  DrawImage                     Inserts an image
  DrawLine                      Draws a line
  DrawPath                      Draws a path
  DrawPdfTemplate               Draws a PDF template
  DrawPie                       Draws a Pie
  DrawPolygon                   Draws a Polygon shape
  DrawRectangle                 Draws a rectangle shape
  DrawString                    Draws the text
  DrawStringLayoutResult        Draws a layout result
  GetBezierArcPoints            Gets the Bezier points for arc constructing
  GetLineBounds                 Returns bounds of the line info
  GetTextVerticalAlignShift     Calculates shift value if the text is vertically aligned
  InitializeCoordinates         Initializes coordinate system
  MultiplyTransform             Multiplies the world transformation of the Graphics and specifies the Matrix
  PutComment                    Puts a comment line
  Reset                         Clears instances
  Restore                       Restores the state of the Graphics to the state represented by a GraphicsState or to the last state
  RotateTransform               Rotates coordinate system in counterclockwise direction
  Save                          Saves the current state of the Graphics and identifies the saved state with a GraphicsState
  ScaleTransform                Scales coordinates by specified coordinates
  SetBBox                       Sets the BBox entry of the graphics dictionary
  SetClip                       Modifying the current clipping path by intersecting it with the current path
  SetLayer                      Sets the layer for the graphics
  SetTransparency               Sets transparency
  SkewTransform                 Skews coordinate system axes
  TranslateTransform            Translates coordinates by specified coordinates
  ----------------------------- -----------------------------------------------------------------------------------------------------


 

Properties

 


  ----------------- ----------------------------------------------------------------------------------------------------
  Name              Description
  AutomaticFields   Gets the automatic fields
  ClientSize        Gets a SizeF structure that binds the region of the Graphics reduced by margins and page templates
  ColorSpace        Gets or sets the current color space
  Layer             Gets the layer for the graphics, if exists
  Matrix            Gets the matrix reflecting current transformation
  Page              Gets the page for this graphics, if exists
  Size              Gets the size of the canvas
  StreamWriter      Gets the stream writer
  ----------------- ----------------------------------------------------------------------------------------------------


 

Units, Size and Co-ordinate System

 

The co-ordinate system is either Top or Left. Origin is translated depending on the margins and page templates. The measure units are points (1/72 inch). The **PdfUnitConvertor** class enables to convert different measure units.

 

**Size** property of PdfGraphics returns the size of the canvas. Also, **ClientSize** property returns a client area of the canvas, which might be smaller. Any output of the client area will not be visible.

 

Graphics State and Co-ordinate System Manipulation

[] 

Also, PdfGraphics class allows manipulating with graphics state (save, restore) and coordinate system (rotate, translate, etc). **Save** and **Restore** methods can be used for manipulating with graphics state, while TranslateTransform, RotateTransform, etc., can be used for co-ordinates manipulating. Also, clip regions can be set using the **SetClip** method.

[] 

You may save the current graphics state, translate the origin, rotate and draw some primitives, restore the graphics state and continue drawing with the restored coordinate system.

[] 

Transparency

 

You may specify transparency for pen operations (for example: drawing lines), brush operations (for example: filling shapes), and for both of them simultaneously.

 

Also, you may specify the method of the resulting color calculation. Transparency is set by using the **SetTransparency** method of PdfGraphics. It includes the following blend modes:

 

[·      ]Normal

[·      ]Multiply

[·      ]Screen

[·      ]Overlay

[·      ]Darken

[·      ]Lighten

[·      ]ColorDodge

[·      ]ColorBurn

[·      ]HardLight

[·      ]SoftLight

[·      ]Difference

[·      ]Exclusion

 

Text Output

 

There are plenty of **DrawString** methods in PdfGraphics that allow text printing. The format of the methods are similar to the System.Drawing.Graphics.DrawString methods.

 

**PdfPen** as well as **PdfBrush** are used to print the text. You can use either object, or even both pen and brush for the text output. PdfPen sets the text boundaries while PdfBrush fills the internal area of the text.

 

If the coordinates are used for the text output only, it will be printed despite the graphics boundaries. New lines symbols split the text by lines only. If the bound (RectangleF structure) of the text is set, the text will be laid out to fit the boundaries. If the width of the boundaries is set to 0 or less, the text will not be limited horizontally. If the height of the boundaries is set to 0 or less, the text will be limited by the boundaries of the PdfGraphics.

 

Text Output Settings

 

To apply different settings to text output, **PdfStringFormat** class is used. It contains variety of properties that allow to set different text output settings.

 


Note:[ ]You must add the Syncfusion.Pdf.Graphics namespace to work with Graphics and graphic elements.

 

 


More:















