---
title: howtochangethelexemsdynamically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethelexemsdynamically.md
created_at: 2025-07-03
---








  









## How To Change the Lexems Dynamically {#how-to-change-the-lexems-dynamically style="tab-stops: 0pt"}

[] 

You can change the lexems dynamically by adding / removing the lexems by using the **Lexem.Add** and **Lexem.Remove** methods.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [//Removing Lexems from the language]                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [this][.editControl1.Language.Lexems.Remove(objconfigLex);]                                                                                               |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [//Changing the lexems]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [objconfigLex = [new] ConfigLexem([this].TextBox1.Text, [\"\"], [FormatType].Custom, [false]);] |
|                                                                                                                                                                                                                                                |
| [objconfigLex.IndentationGuideline = [true];]                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [objconfigLex.FormatName = [\"HighLight\"];]                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [//Add it to the current language\'s Lexems collection ]                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [this][.editControl1.Language.Lexems.Add(objconfigLex);]                                                                                                  |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [//Reset the current configuration language cache to reflect these changes.]                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [this][.editControl1.Language.ResetCaches();]                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [\'Removing Lexemes from the language]                                                                                                                             |
|                                                                                                                                                                                                                      |
| [Me][.editControl1.Language.Lexems.Remove(objconfigLex)]                                                                        |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\'Changing the lexems]                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [objconfigLex = [New] ConfigLexem([Me].TextBox1.Text, [\"\"], FormatType.Custom, [False])] |
|                                                                                                                                                                                                                      |
| [objconfigLex.IndentationGuideline = [True]]                                                                                                                |
|                                                                                                                                                                                                                      |
| [objconfigLex.FormatName = [\"HighLight\"]]                                                                                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [\' Add it to the current language\'s Lexemes collection ]                                                                                                         |
|                                                                                                                                                                                                                      |
| [Me][.editControl1.Language.Lexems.Add(objconfigLex)]                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [\' Reset the current configuration language cache to reflect these changes.]                                                                                      |
|                                                                                                                                                                                                                      |
| [Me][.editControl1.Language.ResetCaches()]                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p184} 

[]{#related-topics}

