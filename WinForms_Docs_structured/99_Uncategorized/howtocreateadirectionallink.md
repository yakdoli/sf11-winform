---
title: howtocreateadirectionallink.md
original_path: WinForms_Docs/99_Uncategorized/howtocreateadirectionallink.md
created_at: 2025-08-05
---








  









## How To Create a Directional Link {#how-to-create-a-directional-link style="tab-stops: 0pt"}

[] 

Links can be provided with end point decorators to convey the direction. The following code snippet shows how to create a directional link by adding a \'Filled Arrow\' end point visual to the head port edge of the link.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                               |
|                                                                                                                                                                   |
| [// Create a directional link.]                                                                                 |
|                                                                                                                                                                   |
| [Link][ link = [new] [Link](pts);] |
|                                                                                                                                                                   |
| [EndPointDecoratorModel decoratorMdl = Global.EndPointDecoratorPalette\[[\"Filled Arrow\"]\];]         |
|                                                                                                                                                                   |
| [if][ (decoratorMdl != [null])]                         |
|                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                   |
| [ link.EndPoints.LastEndPointDecorator = decoratorMdl.CreateInstance();]                                                      |
|                                                                                                                                                                   |
| [}]                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [\' Create a directional link.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [Dim][ link [As] [New] LinkLabel.Link(pts)]                                                                                     |
|                                                                                                                                                                                                                                                                |
| [Dim][ decoratorMdl [As] EndPointDecoratorModel = [Global].EndPointDecoratorPalette([\"Filled Arrow\"])] |
|                                                                                                                                                                                                                                                                |
| [If][ [Not] (decoratorMdl [Is] [Nothing]) [Then]]                                     |
|                                                                                                                                                                                                                                                                |
| [ link.EndPoints.LastEndPointDecorator = decoratorMdl.CreateInstance()]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p79} 

 

[]{#related-topics}

