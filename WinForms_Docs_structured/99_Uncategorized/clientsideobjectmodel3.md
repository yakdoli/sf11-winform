---
title: clientsideobjectmodel3.md
original_path: WinForms_Docs/99_Uncategorized/clientsideobjectmodel3.md
created_at: 2025-08-05
---






##### Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 


  --------------- ------------ ------------- ----------------------------------------------
  Method          Parameters   Return Type   Description
  IsPopupShown    \-           bool          Specifies whether popup container is shown.
  IsPopupHidden   \-           bool          Specifies whether popup container is hidden.
  ShowPopup       \-           \-            Shows popup container.
  HidePopup       \-           \-            Hides popup container.
  SetText         string       \-            Sets the control text.
  GetText         \-           string        Gets the control text.
  --------------- ------------ ------------- ----------------------------------------------


[] 

ClienEventData Object Properties

[] 


  ---------- ------------- -----------------------------------------------------------------------------------------------------------------
  Property   Type          Description
  TextEl     HTMLElement   Represents HTML text box element.
  PopupEl    HTMLElement   Represents HTML popup container.
  Button     HTMLElement   Represents HTML button element.
  Instance   object        Represents MultiColumnDropDownCombo client-side object.
  Event      object        Represents event.
  Text       string        Specifies the text in textbox.
  OldText    string        Specifies the old text in textbox before change (it is only for **ClientSideOnTextChanged** client side event).
  ---------- ------------- -----------------------------------------------------------------------------------------------------------------


 

[]{#related-topics}

