---
title: textbodyselection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textbodyselection.md
created_at: 2025-07-03
---








  









### TextBodySelection {#textbodyselection style="tab-stops: 0pt"}

 

**TextBodySelection** gives you an opportunity to select items in the TextBodyPart.

 

For example, you have the following text:

 

Text NEED [COPY]

  --- ---
       
       
  --- ---

 

THIS [TEXT] Other text

 

You may want to copy the \"NEED COPY\" table and \"THIS TEXT\", and paste in another location.

*[]* 

Objects Tree is as follows.

 

TextBody

[·      ]\[0\]Paragraph

[o  ]\[0\]TextRange -- \"Text\"

[o  ]\[1\]TextRange -- \"NEED\"

[o  ]\[2\]TextRange -- \"COPY\"

[·      ]\[1\]Table

[·      ]\[2\]Paragraph

[o  ]\[0\]TextRange -- \"THIS\"

[o  ]\[1\]TextRange -- \"TEXT\"

[o  ]\[2\]TextRange -- \"Other Text\"

 

The following code is used for this purpose.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [TextBodySelection][ bodySelection = ][new][ TextBodySelection( body, 0, 2, 1, 1 );] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

where, [ ]

0, 2, - paragraph starting index and ending index

1, - paragraph item starting index in first paragraph

1 - paragraph item ending index in last paragraph

 

**Public Constructors**

 


  --------------------------------------------------------------------- ------------------------------------------------------------
  **Name**                                                              **Description**
  TextBodySelection.TextBodySelection (ITextBody, int, int, int, int)   Initializes a new instance of the TextBodySelection class.
  TextBodySelection.TextBodySelection (ParagraphItem, ParagraphItem)    Initializes a new instance of the TextBodySelection class.
  --------------------------------------------------------------------- ------------------------------------------------------------


 

**Public Properties**

 


  ------------------------- -------------------------------------------------------
  Name                      Description
  ItemEndIndex              Gets or sets the end index of the text body item.  
  ItemStartIndex            Gets or sets the start index of the text body item.  
  ParagraphItemEndIndex     Gets or sets the end index of the paragraph item.  
  ParagraphItemStartIndex   Gets or sets the start index of the paragraph item.  
  TextBody                  Gets the text body.  
  ------------------------- -------------------------------------------------------


 

**Copy** and **Paste** methods of **TextBodyPart** of the **TextBodySelection** class are used to copy and paste the text and body element at any position in the document. The following code snippet illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [// Create TextBodySelection and select the items of interest.]                                                                                                                        |
|                                                                                                                                                                                                                                          |
| [TextBodySelection][ textSel = [new] [TextBodySelection](sec.Body, 0, lastItemIndex, 0, lastPItemIndex);] |
|                                                                                                                                                                                                                                          |
| [        ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [// Create TextBodyPart and copy the selected items.]                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [TextBodyPart][ replacePart = [new] [TextBodyPart](doc);]                                                 |
|                                                                                                                                                                                                                                          |
| [replacePart.Copy(textSel);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [// Paste the copied content at the end of the text body.]                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [replacePart.PasteAt(txtbdy,itemIndex);]                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [\' Create TextBodySelection and select the items of interest.]                                                                                                                              |
|                                                                                                                                                                                                                                                |
| [Dim][ textSel [As] TextBodySelection = [New] TextBodySelection(sec.Body, 0, lastItemIndex, 0, lastPItemIndex)] |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [\' Create TextBodyPart and copy the selected items.]                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [Dim][ replacePart [As] TextBodyPart = [New] TextBodyPart(doc)]                                                 |
|                                                                                                                                                                                                                                                |
| [replacePart.Copy(textSel)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [\' Paste the copied text at the end of the text body.]                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [replacePart.PasteAt(txtbdy,itemIndex)]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

