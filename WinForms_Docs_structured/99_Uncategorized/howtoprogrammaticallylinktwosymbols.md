---
title: howtoprogrammaticallylinktwosymbols.md
original_path: WinForms_Docs/99_Uncategorized/howtoprogrammaticallylinktwosymbols.md
created_at: 2025-08-05
---








  









## How To Programmatically Link Two Symbols {#how-to-programmatically-link-two-symbols style="tab-stops: 0pt"}

[] 

The **Syncfusion.Windows.Forms.Diagram.LinkCmd** command class can be used to programmatically link symbols.

 

The following code sample shows how to create a link between two symbols, symbol1 and symbol2.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                       |
|                                                                                                                                                           |
| [// Create a LinkCmd object.]                                                                           |
|                                                                                                                                                           |
| [LinkCmd linkcommand = [new] LinkCmd();]                                                         |
|                                                                                                                                                           |
| [linkcommand.Link = [new] [Link]([Link].Shapes.Line);] |
|                                                                                                                                                           |
| []                                                                                                                    |
|                                                                                                                                                           |
| [// Set up the Source and Target ports for the Link.]                                                   |
|                                                                                                                                                           |
| [linkcommand.SourcePort = symbol1.CenterPort;]                                                                        |
|                                                                                                                                                           |
| [linkcommand.TargetPort = symbol2.CenterPort;]                                                                        |
|                                                                                                                                                           |
| []                                                                                                                    |
|                                                                                                                                                           |
| [// Execute the command to connect the two symbols.]                                                    |
|                                                                                                                                                           |
| [this][.diagram.Controller.ExecuteCommand(linkcommand);]             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| ['Create a LinkCmd object.]                                                                                           |
|                                                                                                                                                                         |
| [Dim][ linkcommand [As] [New] LinkCmd()] |
|                                                                                                                                                                         |
| [linkcommand.Link = [New] Link(Link.Shapes.Line)]                                                              |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| ['Set up the Source and Target ports for the Link.]                                                                   |
|                                                                                                                                                                         |
| [linkcommand.SourcePort = symbol1.CenterPort]                                                                                       |
|                                                                                                                                                                         |
| [linkcommand.TargetPort = symbol2.CenterPort]                                                                                       |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| ['Execute the command to connect the two symbols.]                                                                    |
|                                                                                                                                                                         |
| [Me][.diagram.Controller.ExecuteCommand(linkcommand)]                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p92} 

 

[]{#related-topics}

