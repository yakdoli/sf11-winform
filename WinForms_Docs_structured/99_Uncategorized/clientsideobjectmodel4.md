---
title: clientsideobjectmodel4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideobjectmodel4.md
created_at: 2025-07-03
---






##### Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

Client-Side Object Methods

**[]** 


  --------------- ------------- ------------ ----------------------------------------------
  Method          Parameter     ReturnType   Description
  IsPopupShown    \-            bool         Specifies whether popup container is shown.
  SetChecked      oItem, bVal                Specifies whether item must be checked
  IsPopupHidden   \-            bool         Specifies whether popup container is hidden.
  ShowPopup       \-            \-           Shows popup container.
  HidePopup       \-            \-           Hides popup container.
  SetText         string        \-           Sets the control text.
  GetText         \-            string       Gets the control text.
  --------------- ------------- ------------ ----------------------------------------------


[] 

Client Event Data

[] 


  ---------- ------------- -------------------------------------------------------
  Property   Type          Description
  TextEl     HTMLElement   Represents HTML text box element
  PopupEl    HTMLElement   Represents HTML popup container.
  Button     HTMLElement   Represents HTML button element.
  Instance   object        Represents MultiselectionDropDown client-side object.
  Event      object        Represents event.
  Text       string        Specifies the text in textbox.
  OldText    string        Specifies the old text in textbox before change.
  ---------- ------------- -------------------------------------------------------


[] 

Sample

[] 

MultiSelectionDropDown.OnItemCheckChanged Event

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                              |
|                                                                                                                       |
| []                                                   |
|                                                                                                                       |
| [function OnItemChecked(Odata)]                                   |
|                                                                                                                       |
| [{ ]                                                              |
|                                                                                                                       |
| [    selIdx=\"CurrentItem Index:\"+Odata.CheckChangedItem.Index;] |
|                                                                                                                       |
| [    DisplayDatas(\"CheckedItem\",selIdx);]                       |
|                                                                                                                       |
| [    selText=\"Selected Books:\"+Odata.NewText;]                  |
|                                                                                                                       |
| [    DisplayDatas(\"TextItem\",selText);]                         |
|                                                                                                                       |
| [      ]                                                          |
|                                                                                                                       |
| [}]                                                               |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

