---
title: drawinginteractivecursorseparatelyeitherhorizontallyorverticallyorboth.md
original_path: WinForms_Docs/99_Uncategorized/drawinginteractivecursorseparatelyeitherhorizontallyorverticallyorboth.md
created_at: 2025-08-05
---






#### Drawing Interactive Cursor Separately -- Either Horizontally or Vertically or Both {#drawing-interactive-cursor-separately-either-horizontally-or-vertically-or-both style="tab-stops: 0pt"}

 

An Interactive cursor is used to indicate the x-axis and y-axis values of a data point. The interactive cursor can be drawn in different orientations namely Horizontal, Vertical and in both directions. The cursor color can also be changed according to requirements. The default color is set at the initial stage and this can be changed according to orientation or a common color can be set for both orientations as the parent color.

 

 Use Case Scenarios[]

 

The purpose of using Chart Interactive Cursor is to indicate the x-axis and y-axis values for a specified data point.  You can accurately locate the position of the point on the axes. You can use it as per your requirement i.e. horizontal, vertical or both accordingly.

The following screen shot shows the Interactive cursor, which is drawn in horizontal orientation:

{border="0"}[]

Figure 307: Interactive Cursor with Horizontal Orientation

 

 

Properties[]

**[]** 

+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+
| Property              | Description                                                                                              | Data Type             |
+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+
| CursorOrientation     | Indicates the orientation in which the Interactive Cursor is to be drawn. The options are :              | Enum                  |
|                       |                                                                                                          |                       |
|                       | [·      ]Horizontal                                                         |                       |
|                       |                                                                                                          |                       |
|                       | [·      ]Vertical                                                           |                       |
|                       |                                                                                                          |                       |
|                       | [·      ]Both                                                               |                       |
+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+
| HorizontalCursorColor | Specifies the color, which is to be used when Horizontal Interactive Cursor is drawn                     | Color                 |
+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+
| VerticalCursorColor   | Specifies the color, which is to be used when Vertical  Interactive Cursor is drawn                      | Color                 |
+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+
| Color                 | Specifies the base color, which is to be used other than the default color. This acts as a parent color. | Color                 |
+-----------------------+----------------------------------------------------------------------------------------------------------+-----------------------+

[] 

 

 

Drawing Interactive Cursor in a Chart Application[]

[] 

To add Interactive Cursor to the Chart control:

1.   Add a Interactive cursor to the **Chart** control.

2.   Set the orientation to horizontal or vertical or both.

3.   Choose the color.

 

Refer to the following code snippets to draw the interactive cursor separately.

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]][]**                                                                                          |
|                                                                                                                                                                                     |
| [cursor1 = [new] [ChartInteractiveCursor]([this].chartControl1.Series\[0\]);] |
|                                                                                                                                                                                     |
| [this][.chartControl1.ChartArea.InteractiveCursors.Add(cursor1);           ]                   |
|                                                                                                                                                                                     |
| [cursor1.CursorOrientation = [InteractiveCursorOrientation].Horizontal;]                                                |
|                                                                                                                                                                                     |
| [cursor1.HorizontalCursorColor = [Color].Red;][]                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                           |
|                                                                                                                                                      |
| **[]**                                                                                                           |
|                                                                                                                                                      |
| [cursor1 = [New] ChartInteractiveCursor([Me].chartControl1.Series(0))] |
|                                                                                                                                                      |
| [      [Me].chartControl1.ChartArea.InteractiveCursors.Add(cursor1)]                        |
|                                                                                                                                                      |
| [      cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal]                                      |
|                                                                                                                                                      |
| [      cursor1.HorizontalCursorColor = Color.Red][]                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The interactive cursor as described earlier can be set in three different orientations.

To draw the interactive cursor in horizontal orientation, you need to set the cursor orientation to "Horizontal" as shown in the following code snippets:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]][]**                                                                                 |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [cursor1.CursorOrientation = [InteractiveCursorOrientation].Horizontal;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                 |
|                                                                                                                                            |
| **[]**                                                                                                 |
|                                                                                                                                            |
| [      cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal][] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The same step is repeated for "vertical" and "both" cursor orientations except for the naming "Vertical" and "Both" respectively.

You can also add color(s) to individual interactive cursor. The default color (base color) is Red. You can change the default color by using Color, HorizontalCursorColor, and VerticalCursorColor properties. When you use the Color property, the interactive cursor will be drawn based on the color specified by the Color property (assuming this as base/parent color) regardless of the colors specified for Horizontal and Vertical cursor orientations. This is shown in the following code snippets:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]][]**                                                       |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [      cursor1.CursorOrientation = [InteractiveCursorOrientation].Both ;]            |
|                                                                                                                                                  |
| [      cursor1.Color = [Color].Blue;]                                                |
|                                                                                                                                                  |
| [      cursor1.VerticalCursorColor = [Color].Green;]                                 |
|                                                                                                                                                  |
| [cursor1.HorizontalCursorColor = [Color].Red;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                       |
|                                                                                                                                                  |
| [      ]                                                                                                     |
|                                                                                                                                                  |
| [       cursor1.CursorOrientation = InteractiveCursorOrientation.Both][] |
|                                                                                                                                                  |
| [       cursor1.Color = Color.Blue]                                                                          |
|                                                                                                                                                  |
| [       cursor1.VerticalCursorColor = Color.Green]                                                           |
|                                                                                                                                                  |
| [       cursor1.HorizontalCursorColor = Color.Red][]                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Now, the default color would be replaced with blue color at both the orientations as it is the parent color.

 

{border="0"}

Figure 308: Interactive Cursor with Parent Color Set to Blue

 

The following code snippets draw interactive cursor in different colors:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]][]**                                                       |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [      cursor1.CursorOrientation = [InteractiveCursorOrientation].Both ;]            |
|                                                                                                                                                  |
| [      cursor1.VerticalCursorColor = [Color].Green;]                                 |
|                                                                                                                                                  |
| [cursor1.HorizontalCursorColor = [Color].Red;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                       |
|                                                                                                                                                  |
| [      ]                                                                                                     |
|                                                                                                                                                  |
| [       cursor1.CursorOrientation = InteractiveCursorOrientation.Both][] |
|                                                                                                                                                  |
| [       cursor1.VerticalCursorColor = Color.Green]                                                           |
|                                                                                                                                                  |
| [       cursor1.HorizontalCursorColor = Color.Red][]                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[] 

{border="0"}

Figure 309 : Interactive Cursor with Horizontal Cursor Color Red and Vertical Cursor Color Green.[]

 

 

[]{#related-topics}

