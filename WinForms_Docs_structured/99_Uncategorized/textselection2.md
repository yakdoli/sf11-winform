---
title: textselection2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textselection2.md
created_at: 2025-07-03
---








  









### TextSelection {#textselection style="tab-stops: 0pt"}

 

**TextSelection** represents selected text in the Word document with the following limitations.

 

[·      ]Selected Text must be complete (text selection does not represent split selections).

[·      ]Selected Text must be a single paragraph (text selection inside two or more paragraphs is ignored).

 

TextSelection uses the **Find** and **FindAll** methods to select text. For details, see [Find].

 

**Public Constructors**

 


  --------------------------------------------------- --------------------------------------------------------
  Name                                                Description
  TextSelection.TextSelection(WParagraph, int, int)   Initializes a new instance of the TextSelection class.
  --------------------------------------------------- --------------------------------------------------------


 

Public Properties

 


  -------------- ----------------------------------
  Name           Description
  Count          Gets the count of text chunks.  
  SelectedText   Gets the selected text.  
  -------------- ----------------------------------


 

Public Methods

 


  --------------- -----------------------------------------------------------
  Name            Description
  GetAsOneRange   Gets as one range.  
  GetEnumerator   Returns an enumerator that iterates through a collection.
  GetRanges       Gets the ranges.
  this\[int\]     Gets the System.String at the specified index.  
  --------------- -----------------------------------------------------------


 


{border="0"}Note: TextSelection and GetAsOneRange should not be used for text replacement.


 

The following example illustrates how to use the TextSelection class.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [docTemplate.Open( FINDTEMPLATE );]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [TextSelection][ rangesHolder1 = docSource1.Find( [\"The PlaceHolder1\"], [false], [false] );] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [docTemplate.Open(FINDTEMPLATE)]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ rangesHolder1 [As] TextSelection = docSource1.Find([\"The PlaceHolder1\"], [False], [False])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

