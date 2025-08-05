---
title: clientsideevents15.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents15.md
created_at: 2025-08-05
---






##### Client-side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The Drag Drop Manager control supports rich client-side events. You can trigger the client-side functions whenever some actions (dragstart/drag/dragend) are performed on the dragged element by setting the following properties to the corresponding function names.

[] 


  ----------------------- ---------------------------------------------------------------------------------
  Property                Description
  ClientsideOnDrag        Specifies the client-side function to trigger on a drag operation.
  ClientSideOnDragEnd     Specifies the client-side function to trigger when drag operation is performed.
  ClientSideOnDragStart   Specifies the client-side function to trigger on start drag.
  ----------------------- ---------------------------------------------------------------------------------


[] 

To perform the client-side event:

[] 

1.   Define the various functions to be executed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [language][=\"javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [function][ OnDrag()]                                                                                                                     |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [   document.getElementById([\"div_event\"]).innerHTML=[\"Drag\"];]                                                                        |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [function][ OnDragStart()]                                                                                                                |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [   document.getElementById([\"div_event\"]).innerHTML=[\"DragStart\"];]                                                                   |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [function][ OnDragStart()]                                                                                                                |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [   document.getElementById([\"div_event\"]).innerHTML=[\"DragEnd\"];]                                                                     |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [\</][script][\>]                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Set the corresponding client-side events to the function name that should be executed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][DragDropManager][ [ID][=\"DragDropManager1\"] [ClientSideOnDragEnd][=\"OnDragEnd()\"] [ClientSideOnDrag][=\"OnDrag()\"] [ClientSideOnDragStart][=\"OnDragStart()\"] [runat][=\"server\"] [DragElementIDs][=\"img1,img2,img3,img4\"] [/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: When the drag element is dragged, the client side events trigger in the order mentioned below:


[] 

1.   DragStart

2.   Drag

3.   DragEnd

 

[]{#related-topics}

