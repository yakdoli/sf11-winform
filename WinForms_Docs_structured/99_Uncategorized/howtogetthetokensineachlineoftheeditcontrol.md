---
title: howtogetthetokensineachlineoftheeditcontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtogetthetokensineachlineoftheeditcontrol.md
created_at: 2025-08-05
---








  









## How To Get the Tokens In Each Line Of the Edit Control {#how-to-get-the-tokens-in-each-line-of-the-edit-control style="tab-stops: 0pt"}

[] 

You can get the tokens present in a line of the Edit Control by getting hold of the **ILexemLine** object associated with that particular line, and then accessing its Lexems in the **LineLexems** collection. The following code snippet illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [ILexemLine][ lexemLine = [this].editControl1.GetLine([this].editControl1.CurrentLine); ] |
|                                                                                                                                                                                                                          |
| [foreach][ ([Lexem] lexem [in] lexemLine.LineLexems) ]                                    |
|                                                                                                                                                                                                                          |
| [{ ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [lexemArrayList.Add(lexem); ]                                                                                                                                                        |
|                                                                                                                                                                                                                          |
| [} ]                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [Dim][ lexemLine [As] ILexemLine = [Me].editControl1.GetLine([Me].editControl1.CurrentLine)] |
|                                                                                                                                                                                                                                                  |
| [Dim][ lexem [As] Lexem]                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [For][ [Each] lexem [In] lexemLine.LineLexems ]                                                                   |
|                                                                                                                                                                                                                                                  |
| [lexemArrayList.Add(lexem) ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| [Next][ ]                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p194} 

[]{#related-topics}

