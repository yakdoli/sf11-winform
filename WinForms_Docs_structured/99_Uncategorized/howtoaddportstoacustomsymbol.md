---
title: howtoaddportstoacustomsymbol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddportstoacustomsymbol.md
created_at: 2025-07-03
---








  









## How To Add Ports To A Custom Symbol {#how-to-add-ports-to-a-custom-symbol style="tab-stops: 0pt"}

[] 

The following code snippet illustrates how ports can be added to a custom symbol.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [private][ CirclePort leftport;]                                                                                  |
|                                                                                                                                                                                                        |
| [private][ CirclePort rightport;]                                                                                 |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [//Add these lines to MySymbol\'s Constructor]                                                                                                       |
|                                                                                                                                                                                                        |
| [//Port locations]                                                                                                                                   |
|                                                                                                                                                                                                        |
| [leftport = [new] CirclePort([new] PointF(0, [this].Height / 2));]                                  |
|                                                                                                                                                                                                        |
| [rightport = [new] CirclePort([new] PointF([this].Width, [this].Height / 2));] |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [//Append CirlePorts to MySymbol]                                                                                                                    |
|                                                                                                                                                                                                        |
| [AppendChild(leftport);]                                                                                                                                           |
|                                                                                                                                                                                                        |
| [AppendChild(rightport);]                                                                                                                                          |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [//Make CenterPort visible]                                                                                                                          |
|                                                                                                                                                                                                        |
| [this][.CenterPort.Visible = [true];]                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [Private][ leftport [As] CirclePort]                                                    |
|                                                                                                                                                                                                   |
| [Private][ rightport [As] CirclePort]                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [\'Add these lines to MySymbol\'s Constructor]                                                                                                  |
|                                                                                                                                                                                                   |
| [\'Port locations]                                                                                                                              |
|                                                                                                                                                                                                   |
| [leftport = [New] CirclePort([New] PointF(0, [Me].Height / 2))]                                |
|                                                                                                                                                                                                   |
| [rightport = [New] CirclePort([New] PointF([Me].Width, [Me].Height / 2))] |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [\'Append CirlePorts to MySymbol]                                                                                                               |
|                                                                                                                                                                                                   |
| [AppendChild(leftport)]                                                                                                                                       |
|                                                                                                                                                                                                   |
| [AppendChild(rightport)]                                                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [\'Make CenterPort visible]                                                                                                                     |
|                                                                                                                                                                                                   |
| [Me][.CenterPort.Visible = [True]]                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p71} 

 

[]{#related-topics}

