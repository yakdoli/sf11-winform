---
title: textboxsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textboxsettings.md
created_at: 2025-07-03
---






##### TextBox Settings {#textbox-settings style="tab-stops: 0pt"}

[] 

Editing Text

[] 

The selected text from the dropdown can be displayed in the MultiSelectionDropDown textbox, and it can be edited at run time by enabling the **AllowTextEditing** property.

[] 


  ------------------ ---------------------------------------------------------------------
  Property           Description
  AllowTextEditing   Specifies whether to allow editing the text. Default value is True.
  ------------------ ---------------------------------------------------------------------


[] 

PostBack

[] 

When text is edited, a postback can be optionally triggered by setting the **AutoPostBackOnTextChanged** property to **True**.

[] 


  --------------------------- -------------------------------------------------------------------------------------------
  Property                    Description
  AutoPostBackOnTextChanged   Specifies whether to postback the page, when the text is changed. Default value is False.
  --------------------------- -------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                        |
| []                                                                    |
|                                                                                                                                        |
| [multiSelectionDropDown1.AutoPostBackOnTextChanged = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                      |
|                                                                                                                                       |
| []                                                                                |
|                                                                                                                                       |
| [multiSelectionDropDown1.AutoPostBackOnTextChanged = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[CSS Styles]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

