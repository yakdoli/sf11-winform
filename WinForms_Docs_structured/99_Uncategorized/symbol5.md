---
title: symbol5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbol5.md
created_at: 2025-07-03
---






#### Symbol {#symbol style="tab-stops: 0pt"}

[]{#p61} 

**WSymbol** class represents a symbol in the Word document. To insert a symbol, open the **Insert** menu and click **Symbol** in Microsoft Word.

 

{border="0"}

Figure 66: Symbol Option in Insert Menu

 

 

 

{border="0"}

Figure 67: Symbol Dialog Box

 

 

You can use the **AppendSymbol** function of WParagraph to insert a symbol by using DocIO.

 

Also, you can use the **CharacterCode** property to set or get the symbol from the WSymbol class, and the **CharacterFormat** property to set or get the character formatting of the symbol.

 

**Class Hierarchy**

 

ParagraphItem

            \|

            WSymbol

 

**Public Constructor**

 


  --------------------------------- ----------------------------------------------------
  Name                              Description
  WSymbol.WSymbol (IWordDocument)   Initializes a new instance of the WSymbol class.  
  --------------------------------- ----------------------------------------------------


 

Public Properties

 


  ----------------- ------------------------------------------
  Name              Description
  CharacterCode     Gets or sets symbol\'s character code.  
  CharacterFormat   Gets character format for the symbol.  
  EntityType        Gets the type of the entity.  
  FontName          Gets or sets symbol font name.  
  ----------------- ------------------------------------------


 

The following example illustrates how to use the WSymbol class.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                                       |
|                                                                                                                                                                                |
| [IWordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                                |
| [IWSection][ section = doc.AddSection();]                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [IWParagraph][ paragraph = section.AddParagraph();]                                       |
|                                                                                                                                                                                |
| [paragraph.AppendText([\"Testing symbols\"]);]                                                                      |
|                                                                                                                                                                                |
| [WSymbol][ symbol = paragraph.AppendSymbol(140);]                                         |
|                                                                                                                                                                                |
| [symbol.FontName = [\"Wingdings\"];]                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [doc.Save([\"Symbol.doc\"]);]                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                                             |
|                                                                                                                                                                                      |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()] |
|                                                                                                                                                                                      |
| [Dim][ section [As] IWSection = doc.AddSection()]                          |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]                |
|                                                                                                                                                                                      |
| [paragraph.AppendText([\"Testing symbols\"])]                                                                             |
|                                                                                                                                                                                      |
| [Dim][ symbol [As] WSymbol = paragraph.AppendSymbol(140)]                  |
|                                                                                                                                                                                      |
| [symbol.FontName = [\"Wingdings\"]]                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                |
|                                                                                                                                                                                      |
| [doc.Save([\"Symbol.doc\"])]                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

