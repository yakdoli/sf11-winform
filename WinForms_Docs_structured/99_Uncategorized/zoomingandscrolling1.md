---
title: zoomingandscrolling1.md
original_path: WinForms_Docs/99_Uncategorized/zoomingandscrolling1.md
created_at: 2025-08-05
---






#### Zooming and Scrolling {#zooming-and-scrolling style="tab-stops: 0pt"}

Essential Chart supports the interactive zooming features along the x and y axis. During runtime, the user can select the zooming range by using the mouse and the chart's zoom-in factor accordingly. The scrollbars will be activated to browse the hidden areas on the zoomed in area.

[] 

{border="0"}

Figure 314: Chart Structure - While Zooming

{border="0"}

Figure 315: Chart Structure - After Zooming

Properties

The following table lists the properties that are used for zooming:

 

 


+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| Property         | Description                                      | Property Type                                           | Value it Accepts              | Any Other Dependencies/Sub-properties Associated |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| EnableXZooming   | Enables or disables the x-axis zoom.             | [bool]                             | [True]   | [NA]                     |
|                  |                                                  |                                                         |                               |                                                  |
|                  |                                                  |                                                         | []       |                                                  |
|                  |                                                  |                                                         |                               |                                                  |
|                  |                                                  |                                                         | [false]  |                                                  |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| EnableYZooming   | Enables or disables the y-axis zoom.             | [bool]                             |                               | [NA]                     |
|                  |                                                  |                                                         |                               |                                                  |
|                  |                                                  |                                                         | [True]   |                                                  |
|                  |                                                  |                                                         |                               |                                                  |
|                  |                                                  |                                                         | []       |                                                  |
|                  |                                                  |                                                         |                               |                                                  |
|                  |                                                  |                                                         | [false ] |                                                  |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| ZoomOutIncrement | Sets the zoom out value for every reset.         | [double]                           | [double] | [NA]                     |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| ZoomPosition     | Sets the minimal value of the axis to be zoomed. | [double][] | [double] | [NA]                     |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+
| ZoomFactor       | Sets the value for the Zoom Factor.              | [double][] | [double] | [NA]                     |
+------------------+--------------------------------------------------+---------------------------------------------------------+-------------------------------+--------------------------------------------------+


 

Scrolling

Scrolling and panning are used to view the visible area on the chart, after zooming.

You can scroll vertically inside the ChartArea by using the mouse wheel. You can scroll horizontally by holding and pressing the spacebar key and moving the mouse wheel.

Scrolling will be automatically enabled while enabling zooming. You can disable the scrollbars by setting the ShowScrollBars property to true. Even though, you disable the scrollbars, you can scroll by using the mouse wheel.

 

Scrolling by Using the Keyboard

The following keys enable scrolling inside the ChartArea:

 


  ------------- ---------------------------------------
  Keys          Action
  Up arrow      Scroll upwards in the ChartArea.
  Down arrow    Scroll downwards in the ChartArea.
  Left arrow    Scroll to the left in the ChartArea.
  Right arrow   Scroll to the right in the ChartArea.
  ------------- ---------------------------------------


[] 

Properties

The following table lists the properties that are used for scrolling:

 


+---------------------------+----------------------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| Property                  | Description                                                          | Property Type               | Value it Accepts             | Any Other Dependencies/Sub-properties Associated |
+---------------------------+----------------------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| ShowScrollBars            | Enables or disables the visibility of the scrollbars.                | [bool] | [True]  | [NA]                     |
|                           |                                                                      |                             |                              |                                                  |
|                           |                                                                      |                             | []      |                                                  |
|                           |                                                                      |                             |                              |                                                  |
|                           |                                                                      |                             | [false] |                                                  |
+---------------------------+----------------------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| ShowScrollBarsResetButton | Enables or disables the visibility of the scrollbar\'s Reset button. | [bool] | [True]  | [NA]                     |
|                           |                                                                      |                             |                              |                                                  |
|                           |                                                                      |                             | []      |                                                  |
|                           |                                                                      |                             |                              |                                                  |
|                           |                                                                      |                             | [false] |                                                  |
+---------------------------+----------------------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+


[] 

Chart with the zooming feature can be created through two ways:

[·      ]Builder

[·      ]ChartModel

More:







