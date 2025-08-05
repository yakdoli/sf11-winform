---
title: clientsideobjectmodel9.md
original_path: WinForms_Docs/99_Uncategorized/clientsideobjectmodel9.md
created_at: 2025-08-05
---






##### ClientSide Object Model {#clientside-object-model style="tab-stops: 0pt"}

[] 

Methods

[] 


+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                    | Type                  | Description                                                                                                                                                                                                              |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Refresh                   | string                | For .NET Framework version 2.0 only. Sends callback to server without page refreshing and triggers CallbackRefresh server side GroupBar event. To perform callback the **EnableCallbacks** property must be set to true. |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetExpandDuration         | int                   | Sets a value indicating the duration of expand animation, in milliseconds.                                                                                                                                               |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetExpandDuration         | \-                    | Gets a value indicating duration of expand animation, in milliseconds.                                                                                                                                                   |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetCollapseDuration       | int                   | Sets a value indicating duration of collapse animation, in milliseconds.                                                                                                                                                 |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetCollapseDuration       | \-                    | Gets a value indicating duration of collapse animation, in milliseconds.                                                                                                                                                 |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetExpandType             | int                   | Sets a value indicating the type of slide effect to use during expand animation.                                                                                                                                         |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | Parameter takes one of the following values.                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 0 - None                                                                                                                                                                                                                 |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 1 - Constant                                                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 2 - Accelerate                                                                                                                                                                                                           |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 3 - Decelerate                                                                                                                                                                                                           |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetExpandType             | \-                    | Gets a value indicating the type of slide effect to use during expand animation.                                                                                                                                         |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetCollapseType           | int                   | Sets a value indicating the type of slide effect to use during collapse animation.                                                                                                                                       |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | Parameter takes one of the following values.                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 0 - None                                                                                                                                                                                                                 |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 1 - Constant                                                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 2 - Accelerate                                                                                                                                                                                                           |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 3 - Decelerate                                                                                                                                                                                                           |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetCollapseType           | \-                    | Gets a value indicating the type of slide effect to use during collapse animation.                                                                                                                                       |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetExpandTransition       | int                   | Sets a value indicating the visual effect to use during expand animation.                                                                                                                                                |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | Parameter takes one of the following values.                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | -1 - TransitionNone                                                                                                                                                                                                      |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 0 - TransitionFade                                                                                                                                                                                                       |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 1 - TransitionDissolve                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 2 - TransitionPixelate                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 3 - TransitionWipeDown                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 4 - TransitionWipeLeft                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 5 - TransitionWipeRight                                                                                                                                                                                                  |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 6 - TransitionWipeUp                                                                                                                                                                                                     |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetExpandTransition       | \-                    | Gets a value indicating the visual effect to use during expand animation.                                                                                                                                                |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetCollapseTransition     | int                   | Sets a value indicating the visual effect to use during collapse animation.                                                                                                                                              |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | Parameter takes one of the following values.                                                                                                                                                                             |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | -1 - TransitionNone                                                                                                                                                                                                      |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 0 - TransitionFade                                                                                                                                                                                                       |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 1 - TransitionDissolve                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 2 - TransitionPixelate                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 3 - TransitionWipeDown                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 4 - TransitionWipeLeft                                                                                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 5 - TransitionWipeRight                                                                                                                                                                                                  |
|                           |                       |                                                                                                                                                                                                                          |
|                           |                       | 6 - TransitionWipeUp                                                                                                                                                                                                     |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetCollapseTransition     | \-                    | Gets a value indicating the visual effect to use during collapse animation.                                                                                                                                              |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetExpandSingleGroup      | bool                  | Sets a value indicating whether it expands only a single group item, at a time.                                                                                                                                          |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetExpandSingleGroup      | \-                    | Gets a value indicating whether it expands only a single group item, at a time.                                                                                                                                          |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetAutoPostBackOnSelect   | bool                  | Sets a value indicating whether to trigger a postback, on item select.                                                                                                                                                   |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetAutoPostBackOnSelect   | \-                    | Gets a value indicating whether to trigger a postback, on item select.                                                                                                                                                   |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetAutoPostBackOnExpand   | bool                  | Sets a value indicating whether to trigger a postback, on item expand.                                                                                                                                                   |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetAutoPostBackOnExpand   | \-                    | Gets a value indicating whether to trigger a postback, on item expand.                                                                                                                                                   |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetAutoPostBackOnCollapse | bool                  | Sets a value indicating whether to trigger a postback, on item collapse.                                                                                                                                                 |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetAutoPostBackOnCollapse | \-                    | Gets a value indicating whether to trigger a postback, on item collapse.                                                                                                                                                 |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetMultiPageID            |                       | Gets a value that specifies the id of the multipage control to be integrated with groupbar.                                                                                                                              |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetMultiPageID            | string                | Sets a value that specifies the id of the multipage control to be integrated with groupbar.                                                                                                                              |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

ClientEventData

[] 


  ---------------- ------------- -----------------------------------------------------------------------------------
  Property         Parameter     Description
  ID               string        Specifies the client side item identifier.
  Text             string        Specifies the item text.
  Tooltip          string        Specifies the help message that showing when user moves mouse over GroupBar item.
  NavigateUrl      string        Specifies the item\'s target URL.
  Selected         bool          Specifies whether item is selected.
  Disabled         bool          Specifies whether item is disabled.
  Checked          bool          Specifies whether item is checked.
  Expanded         bool          Specifies whether item is expanded.
  HasSubNodes      bool          Specifies whether item has child nodes.
  Selectable       bool          Specifies whether item is selectable.
  HtmlID           string        Specifies the client side GroupBar identifier.
  Element          HTMLElement   Represents HTML item element.
  ParentGroupBar   object        Represents GroupBar client-side object.
  Event            object        Represents event.
  ---------------- ------------- -----------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[J][avaScript[\]]]**                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                      |
| [function][ OnItemSelect( EventData )]                                                          |
|                                                                                                                                                                                      |
| [{]                                                                                                                                              |
|                                                                                                                                                                                      |
| [      [var] sText = [\"You selected item \'\"] + EventData.Text + [\"\'\"];] |
|                                                                                                                                                                                      |
| [      alert( sText );]                                                                                                                          |
|                                                                                                                                                                                      |
| [}]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

