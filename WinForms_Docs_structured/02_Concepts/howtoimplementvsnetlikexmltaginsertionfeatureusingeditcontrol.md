---
title: howtoimplementvsnetlikexmltaginsertionfeatureusingeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\howtoimplementvsnetlikexmltaginsertionfeatureusingeditcontrol.md
created_at: 2025-07-03
---








  









## How To Implement VS.NET-like XML Tag Insertion Feature Using Edit Control {#how-to-implement-vs.net-like-xml-tag-insertion-feature-using-edit-control style="tab-stops: 0pt"}

 

The VS.NET-like XML tag insertion feature can be used while editing XML language tags in Essential Edit. The cursor can be placed at any position of the line, and the nodes will be inserted exactly at the beginning and end of the current line.

 

This feature saves time while editing your XML documents by using Essential Edit. The following code snippet illustrates this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [private][ [void] menuItem_Click([object] sender, System.[EventArgs] e) ]                                                                                        |
|                                                                                                                                                                                                                                                                                                                      |
| [{ ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.inputDialog.ShowDialog(); ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [if][ ([this].accepted == [true]) ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [{ ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [if][([this].inputString.Equals([\"\"])) ]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                      |
| [{ ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [MessageBox][.Show([\"The node name cannot be empty\"]); ]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [} ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [else][ ]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [{ ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.MoveToLineStart(); ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.InsertText([this].editControl1.CurrentLine,([this].editControl1.CurrentColumn),[\" \"]); ]                                                |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.InsertTexthis.editControl1.CurrentLine,[this].editControl1.CurrentColumn ,[\"\<\"]+[this].inputString+[\"\>\"]); ] |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.InsertText([this].editControl1.CurrentLine,([this].editControl1.CurrentColumn),[\" \"]); ]                                                |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.AppendText([\"\</\"]+[this].inputString+[\"\>\"]); ]                                                                                    |
|                                                                                                                                                                                                                                                                                                                      |
| [}  ]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| [} ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [} ]                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] menuItem_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] menuItem12.Click] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.inputDialog.ShowDialog()]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [If][ [Me].accepted = [True] [Then]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [If][ [Me].inputString.Equals([\"\"]) [Then]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [MessageBox.Show([\"The node name cannot be empty\"])]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Else]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.MoveToLineStart()]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.InsertText([Me].editControl1.CurrentLine, ([Me].editControl1.CurrentColumn), [\" \"])]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.InsertText([Me].editControl1.CurrentLine, [Me].editControl1.CurrentColumn, [\"\<\"] + [Me].inputString + [\"\>\"])]                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.InsertText([Me].editControl1.CurrentLine, ([Me].editControl1.CurrentColumn), [\" \"])]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.AppendText([\"\</\"] + [Me].inputString + [\"\>\"])]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [If]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [If]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p195} 

[]{#related-topics}

