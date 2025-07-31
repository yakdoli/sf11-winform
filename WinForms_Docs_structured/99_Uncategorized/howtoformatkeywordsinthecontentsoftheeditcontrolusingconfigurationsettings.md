---
title: howtoformatkeywordsinthecontentsoftheeditcontrolusingconfigurationsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoformatkeywordsinthecontentsoftheeditcontrolusingconfigurationsettings.md
created_at: 2025-07-03
---








  









## How To Format Keywords In the Contents Of the Edit Control Using Configuration Settings {#how-to-format-keywords-in-the-contents-of-the-edit-control-using-configuration-settings style="tab-stops: 0pt"}

[] 

Handle the **ConfigurationChanged** event of the Edit Control and get all the tokens of the \"Format\" keyword. Then, handle the **OnCustomDraw** event of each of these tokens and perform string manipulation operations. The following code snippet illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [private][ [void] editControl1_ConfigurationChanged([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [foreach][( FormatManager lang [in] editControl1.Languages ) ]                                                                        |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [Format format = lang\[FormatType.KeyWord\] [as] Format;]                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [if][( format != [null] )]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [format.OnCustomDraw += [new] CustomSnippetDrawEventHandler(format_OnCustomDraw);]                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [private][ [void] format_OnCustomDraw([object] sender, CustomSnippetDrawEventArgs e)]                            |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [string][ text = e.Text;]                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [text = text.ToLower();]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [text = text\[0\].ToString().ToUpper() + text.Substring( 1, text.Length - 1 );]                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [e.Text = text;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_ConfigurationChanged([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] EditControl1.ConfigurationChanged] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ lang [As] FormatManager]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [For][ [Each] lang [In] editControl1.Languages]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ format [As] Format = lang(FormatType.KeyWord) [\']]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [If][ [Not] (format [Is] [Nothing]) [Then]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ format.OnCustomDraw, [AddressOf] format_OnCustomDraw]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Next][ lang]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub][  ]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] format_OnCustomDraw([ByVal] sender [As] [Object], [ByVal] e [As] CustomSnippetDrawEventArgs)]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ \[text\] [As] [String] = e.Text]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\[text\] = \[text\].ToLower()]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\[text\] = \[text\](0).ToString().ToUpper() + \[text\].Substring(1, \[text\].Length - 1)]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ e.Text = \[text\]]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Refer to the Keyword Formatting Demo sample for more information in this regard.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Text Formatting\\KeywordFormattingDemo***

 

[]{#p191} 

[]{#related-topics}

