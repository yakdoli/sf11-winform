---
title: howtouseothercontrolsinsidethedialogeditortemplate.md
original_path: WinForms_Docs/04_Controls/Editors/howtouseothercontrolsinsidethedialogeditortemplate.md
created_at: 2025-08-05
---








  









## How to Use Other Controls Inside the DialogEditorTemplate? {#how-to-use-other-controls-inside-the-dialogeditortemplate style="tab-stops: 0pt"}

Essential Grid allows you to use other controls inside the DialogEditorTemplate. You need to make a note on the setting of z-*index* property for the control while using the controls inside the DialogEditorTemplate. In some cases, the control may set behind the Dialog. To make the control visible, you have to set the z-*index* for the control using their appropriate CSS classes. For example, when using the UploadBox and AutoCompleteTextBox controls inside the DialogEditorTemplate, you have to set the z-*index* as illustrated in the following code examples.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                   |
| []                                                                                                            |
|                                                                                                                                                   |
| [// For UploadBox]                                                                                            |
|                                                                                                                                                   |
| [   .uploadbox][ [.sf_uploadinput]] |
|                                                                                                                                                   |
| [    {]                                                                                                       |
|                                                                                                                                                   |
| [        [z-index]: [9999] [!important];]       |
|                                                                                                                                                   |
| [    }]                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                             |
| []                                                                                                      |
|                                                                                                                                             |
| [// For AutoCompleteTextBox]                                                                            |
|                                                                                                                                             |
| [    [.Autocomplete_SuggestionList] ]                                            |
|                                                                                                                                             |
| [    {]                                                                                                 |
|                                                                                                                                             |
| [        [z-index]: [9999] [!important];] |
|                                                                                                                                             |
| [    }]                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

