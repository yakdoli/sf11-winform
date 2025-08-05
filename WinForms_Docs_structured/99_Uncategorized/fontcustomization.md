---
title: fontcustomization.md
original_path: WinForms_Docs/99_Uncategorized/fontcustomization.md
created_at: 2025-08-05
---








  









### Font Customization {#font-customization style="tab-stops: 0pt"}

[] 

The font customization in the Edit Control works slightly different from the regular text processing the control. The font customization is done only at the **Formats** level, and not at a word level or selected text level. Edit Control is more of a text parsing / syntax highlighting control, and less of a text editing control. Edit Control supports customization of fonts both through the configuration file and dynamically through a run-time **Formats Editor** dialog.

 

The Edit Control supports customization of fonts through the configuration file, as shown in the below code snippet.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"Text\"][ ][Font][=\"Courier New, 10pt\"][ ][FontColor][=\"Black\"][ ][/\>]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"SelectedText\"][ ][Font][=\"Courier New, 10pt\"][ ][BackColor][=\"Highlight\"][ ][FontColor][=\"HighlightText\"][ ][/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"String\"][ ][Font][=\"Courier New, 10pt, style=Bold\"][ ][FontColor][=\"Red\"][ ][/\>]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"Whitespace\"][ ][Font][=\"Courier New, 10pt\"][ ][FontColor][=\"Black\"][ ][/\>]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"Operator\"][ ][Font][=\"Courier New, 10pt\"][ ][FontColor][=\"DarkCyan\"][ ][/\>]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][format][ ][name][=\"Number\"][ ][Font][=\"Courier New, 10pt, style=Bold\"][ ][FontColor][=\"Navy\"][ ][/\>][ ]                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 70: Formats Editor

[] 

The Edit Control supports font customization at run time through the use of the **frmFormatsConfig** dialog box which consists of three smaller controls like the ControlFormatSettings, ControlFormatsList, and the ControlLanguageSelector. The **ControlFormatSettings**[ ]dialog box contains the actual controls to customize all the rendering settings of the selected Format, including font settings. The **ControlFormatsList**[ ]dialog consists of the list of currently existing formats in the configuration file. Also, it provides support to create new formats or delete existing ones. The **ControlLanguageSelector**[ ]dialog has a Combo Box containing the list of configuration languages supported by the Edit Control. The list gets updated when a new configuration language is added or an existing one is removed. The following code illustrates how you can hook up these dialogs to the Edit Control.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [this][.controlLanguageSelector1.EditControl = [this].editControl1;]             |
|                                                                                                                                                                                            |
| [this][.controlFormatsList1.EditControl = [this].editControl1;]                  |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [this][.controlFormatsList1.LanguageSelector = [this].controlLanguageSelector1;] |
|                                                                                                                                                                                            |
| [this][.controlFormatsSettings1.FormatsSelector = [this].controlFormatsList1;]   |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Shows the font customization dialog.]                                                                                                |
|                                                                                                                                                                                            |
| [this][.editControl1.ShowFormatsCustomizationDialog();]                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [Me][.controlLanguageSelector1.EditControl = [Me].editControl1]             |
|                                                                                                                                                                                       |
| [Me][.controlFormatsList1.EditControl = [Me].editControl1]                  |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [Me][.controlFormatsList1.LanguageSelector = [Me].controlLanguageSelector1] |
|                                                                                                                                                                                       |
| [Me][.controlFormatsSettings1.FormatsSelector = [Me].controlFormatsList1]   |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [// Shows the font customization dialog.]                                                                                           |
|                                                                                                                                                                                       |
| [this][.editControl1.ShowFormatsCustomizationDialog();]                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Refer to the Font Customization Demo sample for more information in this regard.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\FontCustomizationDemo***

[]{#p103} 

[]{#related-topics}

