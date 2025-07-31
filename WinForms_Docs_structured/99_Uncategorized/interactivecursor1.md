---
title: interactivecursor1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\interactivecursor1.md
created_at: 2025-07-03
---








  









### Interactive Cursor {#interactive-cursor style="tab-stops: 0pt"}

[] 

The Interactive Cursor feature allows you to position the mouse pointer on a specific data point in a series and provides you a hint on its x and y values by a horizontal and vertical line passing through the data point and intersecting the x and y axis. These lines can be dragged around to position them at specific data points.

Interactive Cursor can be implemented by creating an instance of ChartInteractiveCursor with the **ChartSeries** as its input. Then, add the instance to the Interactive Cursors collection, as shown below.

Features

You can click and drag the Interactive cursor to the point for which you want to identify the corresponding xvalue or yvalue even after zooming.

[] 

Properties:

For Chart Interactive Cursor, in the server-side the following properties are available, to set the color, x position, and yposition properties of the interactive cursor:

[  ]


+-------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+---------------------------------------------------+
| Property    | Description                                                                                                                         | Property Type                                  | Value it Accepts                               | Any Other Dependencies/Sub-properties Associated  |
+=============+=====================================================================================================================================+================================================+================================================+===================================================+
| Color       | It specifies the Interactive cursor color that is to be rendered.                                                                   | System.Drawing.[Color] | System.Drawing.[Color] | Dependent on the ShowInteractiveCursors property. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+---------------------------------------------------+
| XPosition   | It selects the X -- Index from the sorted points (sorting by using XValues) and also changes the YPosition according to this value. | [int]                     | [int]                     | Dependent on the ShowInteractiveCursors property. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+---------------------------------------------------+
| YPosition   | It selects the Y -- Index from the sorted points (sorting by using YValues) and also changes the XPosition according to this value. | [int]                     | [int]                     | Dependent on the ShowInteractiveCursors property. |
|             |                                                                                                                                     |                                                |                                                |                                                   |
|             |                                                                                                                                     |                                                |                                                |                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------+---------------------------------------------------+


 

Client-side Methods:

**[]** 

Chart MVC also provides the client-side function to set the Interactive cursor properties such as color, style, and width and to also get these properties.

[] 

[] 


  Name                      Parameters                                                           Return Type   Description[]
  ------------------------- -------------------------------------------------------------------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  get_InterCursorProperty   InteractiveCursorIndex -- int(datatype)                              Jsondata      It is used to get the specified interactive Cursor properties such as color, style, and width.
  cursorColor               Color -- string(datatype), InteractiveCursorIndex -- int(datatype)   None          It is used to set the specified interactive cursor color.
  cursorWidth               Width -- int(datatype), InteractiveCursorIndex -- int(datatype)      none          It is used to set the specified Interactive cursor width
  cursorStyle               Style -- string(datatype), InteractiveCursorIndex -- int(datatype)   none          It is used to set the specified Interactive cursor style.
  horizontalNext            InteractiveCursorIndex                                               none          It is used to move the specified Interactive Cursor horizontally to the next position, i.e., right.
  horizontalPrev            InteractiveCursorIndex                                               none          It is used to move the specified Interactive Cursor horizontally to the previous position, i.e., left.
  verticalNext              InteractiveCursorIndex                                               none          It is used to move the specified Interactive Cursor vertically to the next position, i.e., up.
  verticalPrev              InteractiveCursorIndex                                               none          It is used to move the specified Interactive Cursor vertically to the previous position, i.e., down.
  CursorAreaPointTally      InteractiveCursorIndex                                               none          If the Interactive cursor is in an invisible region of the ChartArea, then this function moves the ChartArea to the position where the specified Interactive cursor is present.


[] 

The following are the uses of the get_InterCursorproperty function. It returns jsondata, which contains the CursorStyle, CursorWidth, and CursorColor properties. By this you can get all the Interactive cursor properties.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [                ][var][ chart = \$find([\"Chart_Model\"]);] |
|                                                                                                                                                                                                                        |
| [                [var] Property = chart.get_InterCursorProperty(InteractiveCursorIndex);]                                                                     |
|                                                                                                                                                                                                                        |
| [                \$([\'#CursorStyle\']).val(Property.CursorStyle);]                                                                                        |
|                                                                                                                                                                                                                        |
| [                \$([\'#CursorWidth\']).val(Property.CursorWidth);]                                                                                        |
|                                                                                                                                                                                                                        |
| [                \$([\'#Color\']).val(Property.CursorColor);]                                                                                              |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following are the uses of the cursorColor, cursorWidth, and cursorStyle functions. These functions change the **color, width,** and **style** of the Interactive Cursor in the **chart** object respectively.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                                                 |
|                                                                                                                                                                        |
| [                [var] color = \$get([\"Color\"]);]                                   |
|                                                                                                                                                                        |
| [                var][ Width = \$get([\"CursorWidth\"]);] |
|                                                                                                                                                                        |
| [                var][ Style = \$get([\"CursorStyle\"]);] |
|                                                                                                                                                                        |
| [                [var] chart = \$find([\"Chart_Model\"]);]                            |
|                                                                                                                                                                        |
| [                chart.cursorColor(color.value, InteractiveCursorIndex);]                                                          |
|                                                                                                                                                                        |
| [                chart.cursorWidth(Width.value, InteractiveCursorIndex);]                                                          |
|                                                                                                                                                                        |
| [                chart.cursorStyle(Style.value, InteractiveCursorIndex);]                                                          |
|                                                                                                                                                                        |
| []                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The following are the uses of the horizontalNext function, which moves the specified Interactive Cursor horizontally to the next position, i.e., right.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                      |
|                                                                                                                                             |
| [                [var] chart = \$find([\"Chart_Model\"]);] |
|                                                                                                                                             |
| [                chart.horizontalNext(InteractiveCursorIndex);]                                         |
|                                                                                                                                             |
| []                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following are the uses of the horizontalPrev function, which moves the specified Interactive Cursor horizontally to the previous position, i.e., left.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                                                                     |
|                                                                                                                                                                                            |
| [           ][     [var] chart = \$find([\"Chart_Model\"]);] |
|                                                                                                                                                                                            |
| [                chart.horizontalPrev(InteractiveCursorIndex);][]                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following are the uses of the verticalNext function, which moves the specified Interactive Cursor vertically to the next position, i.e., up.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                      |
|                                                                                                                                             |
| [                [var] chart = \$find([\"Chart_Model\"]);] |
|                                                                                                                                             |
| [                chart.verticalNext(InteractiveCursorIndex);]                                           |
|                                                                                                                                             |
| []                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following are the uses of the verticalPrev function, which moves the specified Interactive Cursor vertically to the previous position, i.e., right.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\][]                                                                                                                 |
|                                                                                                                                                  |
| [                [var] chart = \$find([\"Chart_Model\"]);]      |
|                                                                                                                                                  |
| [                chart.verticalPrev(InteractiveCursorIndex);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following are the uses of the CursorAreaPointTally function, which moves the ChartArea to the position where the Interactive cursor is present.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| \[js\]                                                                                                                                      |
|                                                                                                                                             |
| [                [var] chart = \$find([\"Chart_Model\"]);] |
|                                                                                                                                             |
| [                chart.CursorAreaPointTally(InteractiveCursorIndex);]                                   |
|                                                                                                                                             |
| []                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The Interactive Cursor can be added to the ChartModel through two ways:

[·      ]Builder

[·      ]ChartModel

[] 

[] 

More:







