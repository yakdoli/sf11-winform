---
title: howtodynamicallyaddconfigurationsettingsatruntime.md
original_path: WinForms_Docs/99_Uncategorized/howtodynamicallyaddconfigurationsettingsatruntime.md
created_at: 2025-08-05
---








  









## How To Dynamically Add Configuration Settings At Runtime {#how-to-dynamically-add-configuration-settings-at-runtime style="tab-stops: 0pt"}

 

The following code snippet illustrates how to create Custom Formats and define ConfigLexems that belong to those Formats.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Create a format and set its attributes]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [ISnippetFormat][ formatMethod = [this].editControl1.Language.Add([\"MethodName\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [formatMethod.FontColor = [Color].HotPink;]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [formatMethod.Font = [new] Font([\"Garamond\"],12);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Create a lexem that belongs to this format]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| [ConfigLexem][ configLex = [new] [ConfigLexem]([\"Method\[0-9\]\*\"], [\"\"], [FormatType].Custom, [false]);] |
|                                                                                                                                                                                                                                                                                                                                      |
| [configLex.IsBeginRegex = [true];]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [configLex.FormatName = [\"MethodName\"];]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Add it to the current language\'s lexems collection]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.Language.Lexems.Add(configLex);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.Language.ResetCaches();]                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [\' Create a format and set its properties]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ formatMethod [As] ISnippetFormat = [Me].editControl1.Language.Add([\"MethodName\"])]                                                     |
|                                                                                                                                                                                                                                                                                                       |
| [formatMethod.FontColor = Color.HotPink]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                       |
| [formatMethod.Font = [New] Font([\"Garamond\"], 12)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [\' Create a lexem that belongs to this format]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ configLex [As] [New] ConfigLexem([\"Method\[0-9\]\*\"], [\"\"], FormatType.Custom, [False])] |
|                                                                                                                                                                                                                                                                                                       |
| [configLex.IsBeginRegex = [True]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                       |
| [configLex.FormatName = [\"MethodName\"]]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                       |
| [\' Add it to the current language\'s lexems collection]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                       |
| [Me][.editControl1.Language.Lexems.Add(configLex)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                       |
| [Me][.editControl1.Language.ResetCaches()]                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p189} 

[]{#related-topics}

