---
title: textbodypart.md
original_path: WinForms_Docs/99_Uncategorized/textbodypart.md
created_at: 2025-08-05
---








  









### TextBodyPart {#textbodypart style="tab-stops: 0pt"}

 

**TextBodyPart** class contains the collection of body items (it means that TextBodyPart can contain paragraphs, tables and even sections). TextBodyPart is usually used with the Bookmark Navigator.

 


{border="0"}Note:[ ]TextBodyPart contains the copy of objects from the documents (paragraph(s), table(s), section(s), etc). So if you modify the content of the TextBodyPart, it does not affect the objects inside the document.


 

[]{#DDE_LINK1}Public Constructors

 


  ----------------------------------------------- -------------------------------------------------------
  Name                                            Description
  TextBodyPart.TextBodyPart ()                    Initializes a new instance of the TextBodyPart class.
  TextBodyPart.TextBodyPart (TextBodySelection)   Initializes a new instance of the TextBodyPart class.
  TextBodyPart.TextBodyPart (TextSelection)       Initializes a new instance of the TextBodyPart class.
  TextBodyPart.TextBodyPart (WordDocument)        Initializes a new instance of the TextBodyPart class.
  ----------------------------------------------- -------------------------------------------------------


 

**Public Properties**

 


  ----------- ------------------------
  Name        Description
  BodyItems   Gets the body items.  
  ----------- ------------------------


 

**Public Methods**

 


  ------------ ------------------------------------------------------------
  Name         Description
  Clear        Clears this instance.
  Copy         Copies the specified item.
  PasteAfter   Pastes ParagraphItem or TextBodyItem after specified item.
  PasteAt      Pastes ITextBody at specified position.
  PasteAtEnd   Pastes ITextBody at end of textbody.  
  ------------ ------------------------------------------------------------


 

The following example illustrates how to use the TextBodyPart class.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                                      |
|                                                                                                                                                                                               |
| [WordDocument][ doc = [new] [WordDocument]( \"sample.doc\" );] |
|                                                                                                                                                                                               |
| [      ]                                                                                                                                                  |
|                                                                                                                                                                                               |
| [BookmarksNavigator][ bn = [new] [BookmarksNavigator](doc);]   |
|                                                                                                                                                                                               |
| [bn.MoveToBookmark([\"bookmark1\"]);]                                                                                              |
|                                                                                                                                                                                               |
| [TextBodyPart][ bodyPart = bn.GetBookmarkContent();]                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [Dim][ doc [As] WordDocument = [New] WordDocument([\"sample.doc\"])] |
|                                                                                                                                                                                                                            |
| [Dim][ bn [As] BookmarksNavigator = [New] BookmarksNavigator(doc)]                          |
|                                                                                                                                                                                                                            |
| [bn.MoveToBookmark([\"bookmark1\"])]                                                                                                                            |
|                                                                                                                                                                                                                            |
| [Dim][ bodyPart [As] TextBodyPart = bn.GetBookmarkContent()]                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

