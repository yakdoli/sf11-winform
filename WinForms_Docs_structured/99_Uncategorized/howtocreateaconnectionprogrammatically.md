---
title: howtocreateaconnectionprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/howtocreateaconnectionprogrammatically.md
created_at: 2025-08-05
---








  









## How To Create a Connection Programmatically {#how-to-create-a-connection-programmatically style="tab-stops: 0pt"}

[] 

Typically, symbols and links are connected together using the interactive **LinkTool** UI tool or the **LinkCmd** command class. Sometimes, it is useful to create connections programmatically. For example, you might be generating a diagram from the data in a database or possibly even writing your own custom link tool. You might even create a connection between two symbols directly without having a link in between.

[] 

The following code creates a link and connects it to the center ports of two symbols.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [public][ [Link] LinkSymbols([Symbol] sym1, [Symbol] sym2)] |
|                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [    [Link] link = [new] [Link]([Link].Shapes.Line);]                                   |
|                                                                                                                                                                                                                 |
| [    sym1.Connect(sym1.CenterPort, link.TailPort);]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [    sym2.Connect(link.HeadPort, sym2.CenterPort);]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [    [return] link;]                                                                                                                                   |
|                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Public][ [Function] LinkSymbols([ByVal] sym1 [As] Syncfusion.Windows.Forms.Diagram.Symbol, [ByVal] sym2 [As] Syncfusion.Windows.Forms.Diagram.Symbol) [As] LinkLabel.Link] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ link [As] LinkLabel.Link = [New] LinkLabel.Link(link.Shapes.Line)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [sym1.Connect(sym1.CenterPort, link.TailPort)]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [sym2.Connect(link.HeadPort, sym2.CenterPort)]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Return][ link]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Function]]                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p77} 

 

[]{#related-topics}

