---
title: autocompletesupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autocompletesupport.md
created_at: 2025-07-03
---








  









### AutoComplete Support {#autocomplete-support style="tab-stops: 0pt"}

 

Complete Word feature is a user-friendly functionality that can be used in conjunction with the Context Choice, and is analogous to the Complete Word feature in Visual Studio. This feature autocompletes the rest of the member name once you have entered enough characters to distinguish it. Type the first few letters of the member name, and then press ALT+RIGHT ARROW or CTRL+SPACEBAR keys to see this functionality.

 

**Example**

 

When the following text is typed - \"this.editControl1.\", it displays a Context Choice list with members in the following order

 

[·      ]New

[·      ]Word

[·      ]WordLeft

[·      ]WordRight

 

**Case 1**

 

If you type \"w\" after \"this.editControl1.\", such that it looks like - \"this.editControl1.w\", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first matching member name. In this case, it will be autocompleted as \"this.editControl1.Word\".

 

**Case 2**

 

If you type \"wordr\" after \"this.editControl1.\", such that it looks like - \"this.editControl1.wordr\", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first matching member name. In this case, it will be autocompleted as \"this.editControl1.WordRight\".

 

**Case 3**

 

If you type \"move\" after \"this.editControl1.\", such that it looks like - \"this.editControl1.move\", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first matching member name. In this case, there is no matching member name to autocomplete, and hence nothing will happen.

 

**Case 4**

 

If you type nothing after \"this.editControl1.\", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first member name in the Context Choice list. In this case, it should be autocompleted as \"this.editControl1.New\".

 

Note that the searching process for the first matching member is not case sensitive. For example, \"wordr\" and \"WordR\" will be treated in the same way.

 

Set the **UseAutocomplete** property associated with the **IContextChoiceController** to **True**, to enable this functionality while using Context Choice.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [private][ [void] editControl1_ContextChoiceOpen(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] controller)] |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [controller.UseAutocomplete = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] editControl1_ContextChoiceOpen([ByVal] controller [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController) [Handles] editControl1.ContextChoiceOpen] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.UseAutocomplete = [True]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[AutoReplace Triggers]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p30} 

[]{#related-topics}

