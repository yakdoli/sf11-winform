---
title: howtogetalltheconfiglexemsinthecontentsoftheeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogetalltheconfiglexemsinthecontentsoftheeditcontrol.md
created_at: 2025-07-03
---








  









## How To Get All the ConfigLexems In the Contents Of the Edit Control {#how-to-get-all-the-configlexems-in-the-contents-of-the-edit-control style="tab-stops: 0pt"}

[] 

The following code snippet illustrates how to get all the ConfigLexems in the contents of the Edit Control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [private][ ArrayList GetLexems() ]                                                                             |
|                                                                                                                                                                                                     |
| [{  ]                                                                                                                                                           |
|                                                                                                                                                                                                     |
| [ArrayList configLexemList = [new] ArrayList(); ]                                                                                          |
|                                                                                                                                                                                                     |
| [for][ ([int] i=1; i\<=[this].editControl1.PhysicalLineCount; i++) ] |
|                                                                                                                                                                                                     |
| [{ ]                                                                                                                                                            |
|                                                                                                                                                                                                     |
| [ILexemLine line = [this].editControl1.GetLine(i); ]                                                                                       |
|                                                                                                                                                                                                     |
| [foreach][ (ILexem lexem [in] line.LineLexems) ]                                          |
|                                                                                                                                                                                                     |
| [{ ]                                                                                                                                                            |
|                                                                                                                                                                                                     |
| [IConfigLexem configLexem = lexem.Config; ]                                                                                                                     |
|                                                                                                                                                                                                     |
| [configLexemList.Add(configLexem);  ]                                                                                                                           |
|                                                                                                                                                                                                     |
| [} ]                                                                                                                                                            |
|                                                                                                                                                                                                     |
| [} ]                                                                                                                                                            |
|                                                                                                                                                                                                     |
| [return][ configLexemList; ]                                                                                   |
|                                                                                                                                                                                                     |
| [}]                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [Private][ [Function] GetLexems() [As] ArrayList]                                        |
|                                                                                                                                                                                                                         |
| [Dim][ configLexemList [As] ArrayList = [New] ArrayList()]                               |
|                                                                                                                                                                                                                         |
| [Dim][ i [As] [Integer]]                                                                 |
|                                                                                                                                                                                                                         |
| [For][ i = 1 [To] [Me].editControl1.PhysicalLineCount [Step] i + 1] |
|                                                                                                                                                                                                                         |
| [Dim][ line [As] ILexemLine = [Me].editControl1.GetLine(i)]                              |
|                                                                                                                                                                                                                         |
| [Dim][ lexem [As] ILexem]                                                                                     |
|                                                                                                                                                                                                                         |
| [For][ [Each] lexem [In] line.LineLexems]                                                |
|                                                                                                                                                                                                                         |
| [Dim][ configLexem [As] IConfigLexem = lexem.Config]                                                          |
|                                                                                                                                                                                                                         |
| [configLexemList.Add(configLexem)]                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [Next]                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [Next]                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [Return][ configLexemList]                                                                                                         |
|                                                                                                                                                                                                                         |
| [End][ [Function]]                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p193} 

 

[]{#related-topics}

