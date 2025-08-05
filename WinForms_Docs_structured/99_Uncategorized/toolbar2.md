---
title: toolbar2.md
original_path: WinForms_Docs/99_Uncategorized/toolbar2.md
created_at: 2025-08-05
---








  









### ToolBar {#toolbar style="tab-stops: 0pt"}

Essential Chart for ASP.NET MVC supports the toolbar. The toolbar contains the following options:

[] 

[·      ]Save the chart

[·      ]Copy the chart

[·      ]Print the chart

[·      ]Zoom-in the chart

[·      ]Zoom-out the chart

[·      ]Change the ChartSeriesSkins

[·      ]Enable chart 3D effect

[·      ]Enable panning while zooming

 

The toolbar can be dragged. By default, the Toolbar dragging functionality is enabled. You can disable the dragging functionality of the toolbar by using the **IsToolBarDraggable** property.

 

Properties

[] 


+--------------------+-----------------------------------------------------------------------+-------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------+
| Property           | Description                                                           | Property Type                                         | Value it Accepts                                                     | Any Other Dependencies/Sub-properties Associated |
+--------------------+-----------------------------------------------------------------------+-------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------+
| ShowToolBar        | Set this property to true, to display the toolbar.                    | [bool]                           | [True]                                          | [NA]                     |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | []                                              |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [false]                                         |                                                  |
+--------------------+-----------------------------------------------------------------------+-------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------+
| IsToolBarDraggable | Set this property to true, to enable the dragging feature of Toolbar. | [bool]                           | [True]                                          | [NA]                     |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | []                                              |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [false]                                         |                                                  |
+--------------------+-----------------------------------------------------------------------+-------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------+
| ToolBarItem        | This property is used to add the toolbar items manually.              | [List][] | [ToolBarItem].ChartSeriesSkins               | [NA]                     |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].ChartTypes                     |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].Enable3D                       |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].Panning                        |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].Print                          |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].Save                           |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].ZoomIn                         |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       |                                                                      |                                                  |
|                    |                                                                       |                                                       | [ToolBarItem].ZoomOut[] |                                                  |
+--------------------+-----------------------------------------------------------------------+-------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------+


[] 

More:







