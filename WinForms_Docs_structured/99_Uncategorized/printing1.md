---
title: printing1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\printing1.md
created_at: 2025-07-03
---








  









## Printing {#printing style="tab-stops: 0pt"}

Essential Chart supports the printing feature. This can be done by using the ServerSide properties and the client-side methods.

The printing functionality can be enabled in the server-side by using the **PrintButtonVisible** property.

**[]** 

Properties:

**[]** 


+----------------------+----------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| Property             | Description                                              | Property Type               | Value it Accepts             | Any Other Dependencies/Sub-properties Associated |
+----------------------+----------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| PrintButtonVisible   | Used to set the visibility of the Print button.          | [bool] | [True ] | [NA]                     |
|                      |                                                          |                             |                              |                                                  |
|                      |                                                          |                             | []      |                                                  |
|                      |                                                          |                             |                              |                                                  |
|                      |                                                          |                             | [False] |                                                  |
+----------------------+----------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| PrintButtonDraggable | Used to enable the dragging feature of the Print button. | [bool] | [True ] | [NA]                     |
|                      |                                                          |                             |                              |                                                  |
|                      |                                                          |                             | []      |                                                  |
|                      |                                                          |                             |                              |                                                  |
|                      |                                                          |                             | [False] |                                                  |
|                      |                                                          |                             |                              |                                                  |
|                      |                                                          |                             | []      |                                                  |
+----------------------+----------------------------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+


 

The printing functionality can be enabled in the client-side by using the **PrintingImage** function.

 

Client-side Methods

[] 


  --------------- -------------------------------------------------------- -------------------------------------------------------- -----------------------------------------------------------------------
  Name            Parameters                                               Return Type                                              Description[]
  PrintingImage   [None][]   [None][]   [This property is used for printing the chart.]
  --------------- -------------------------------------------------------- -------------------------------------------------------- -----------------------------------------------------------------------


[] 

The printing feature can be enabled in a chart through two ways:

[·      ]Builder

[·      ]ChartModel

More:







