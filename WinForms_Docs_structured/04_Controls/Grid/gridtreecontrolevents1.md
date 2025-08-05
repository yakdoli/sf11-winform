---
title: gridtreecontrolevents1.md
original_path: WinForms_Docs/04_Controls/Grid/gridtreecontrolevents1.md
created_at: 2025-08-05
---








  









### GridTree Control Events {#gridtree-control-events style="tab-stops: 0pt"}

Here is the list of events exposed in GridTree control. Additionally, you have access to all the GridControl events exposed on the GridTreeControl.InternalGrid.

 

Table 51: GridTree control Event


  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GridTree control Event   Description
  ModelLoaded              Handled once the InternalGrid is created and after the template is applied to the GridTree control. This is the correct place to set the properties and subscribe to events on the InternalGrid.
  RequestTreeItems         Required event that is used to provide the underlying data to the GridTree control on demand. This event is discussed earlier in this document.
  RequestNodeImage         By handling this event, you can provide an image to be used in the expand cell. This event is discussed earlier in this document.
  ExpandStateChanging      This is a cancelable event that is handled just prior to a node being expanded by the user.
  ExpandStateChanged       This is a notification event that is handled once a node has been expanded by the user.
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 


{border="0"}Note: Additionally, you have access to all the Grid control events exposed on the GridTreeControl.InternalGrid.


[]{#related-topics}

