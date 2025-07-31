---
title: howtoaccessthetextassociatedwithindividuallinesintheselectedtextregionoftheeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccessthetextassociatedwithindividuallinesintheselectedtextregionoftheeditcontrol.md
created_at: 2025-07-03
---








  









## How To Access the Text Associated With Individual Lines In the Selected Text Region Of the Edit Control {#how-to-access-the-text-associated-with-individual-lines-in-the-selected-text-region-of-the-edit-control style="tab-stops: 0pt"}

 

The below given code snippet illustrates how you can access the text associated with individual lines in the selected text region of the Edit Control.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [string][ cleanedSQL = [\"\"]; ]                                           |
|                                                                                                                                                                                        |
| [if][ ([this].editControl1.SelectedText != [\"\"]) ]  |
|                                                                                                                                                                                        |
| [{ ]                                                                                                                                               |
|                                                                                                                                                                                        |
| [// Get the start and end points of the selection ]                                                                                  |
|                                                                                                                                                                                        |
| [CoordinatePoint start = [this].editControl1.Selection.Top; ]                                                                 |
|                                                                                                                                                                                        |
| [CoordinatePoint end = [this].editControl1.Selection.Bottom; ]                                                                |
|                                                                                                                                                                                        |
| [string][ lineText = [\"\"]; ]                                             |
|                                                                                                                                                                                        |
| [for][ ([int] i=start.VirtualLine; i\<=end.VirtualLine; i++) ]               |
|                                                                                                                                                                                        |
| [{ ]                                                                                                                                               |
|                                                                                                                                                                                        |
| [// Get the line object ]                                                                                                            |
|                                                                                                                                                                                        |
| [ILexemLine][ lexemLine = [this].editControl1.GetLine(i); ]                  |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [// Get the tokens in each line object and append them to get the line text ]                                                        |
|                                                                                                                                                                                        |
| [foreach][ ([ILexem] lexem [in] lexemLine.LineLexems) ] |
|                                                                                                                                                                                        |
| [{ ]                                                                                                                                               |
|                                                                                                                                                                                        |
| [lineText += lexem.Text;  ]                                                                                                                        |
|                                                                                                                                                                                        |
| [} ]                                                                                                                                               |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [// Store each of these line text  ]                                                                                                 |
|                                                                                                                                                                                        |
| [cleanedSQL += lineText + [\"\\n\"]; ]                                                                                      |
|                                                                                                                                                                                        |
| [lineText=[\"\"]; ]                                                                                                         |
|                                                                                                                                                                                        |
| [} ]                                                                                                                                               |
|                                                                                                                                                                                        |
| [} ]                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [Dim][ cleanedSQL [As] [String] = [\"\"]]                               |
|                                                                                                                                                                                                                               |
| [If][ [Me].editControl1.SelectedText \<\> [\"\"] [Then] ]               |
|                                                                                                                                                                                                                               |
| [\' Get the start and end points of the selection ]                                                                                                                         |
|                                                                                                                                                                                                                               |
| [Dim][ start [As] CoordinatePoint = [Me].editControl1.Selection.Top]                           |
|                                                                                                                                                                                                                               |
| [Dim][ [end] [As] CoordinatePoint = [Me].editControl1.Selection.Bottom  ] |
|                                                                                                                                                                                                                               |
| [Dim][ lineText [As] [String] = [\"\"]]                                 |
|                                                                                                                                                                                                                               |
| [Dim][ i [As] [Integer]]                                                                       |
|                                                                                                                                                                                                                               |
| [For][ i = start.VirtualLine [To] i\<- 1 [Step] =[end].VirtualLine ]      |
|                                                                                                                                                                                                                               |
| [\' Get the line object ]                                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [Dim][ lexemLine [As] ILexemLine = [Me].editControl1.GetLine(i)]                               |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [\' Get the tokens in each line object and append them to get the line text ]                                                                                               |
|                                                                                                                                                                                                                               |
| [Dim][ lexem [As] ILexem]                                                                                           |
|                                                                                                                                                                                                                               |
| [For][ [Each] lexem [In] lexemLine.LineLexems ]                                                |
|                                                                                                                                                                                                                               |
| [lineText += lexem.Text ]                                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [Next][ ]                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [\' Store each of these line text  ]                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [cleanedSQL += lineText + [\"\\n\"] ]                                                                                                                              |
|                                                                                                                                                                                                                               |
| [lineText=[\"\"] ]                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [Next][ ]                                                                                                                                |
|                                                                                                                                                                                                                               |
| [End][ [If] ]                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p183} 

[]{#related-topics}

