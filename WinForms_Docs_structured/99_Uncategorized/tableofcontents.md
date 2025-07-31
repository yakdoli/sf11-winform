---
title: tableofcontents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tableofcontents.md
created_at: 2025-07-03
---






#### Table Of Contents {#table-of-contents style="tab-stops: 0pt"}

 

The **TableOfContent** class represents the Table Of Contents (TOC) in the Word document.

To add the Table of Contents to the contents in the Word document, follow the steps listed below:

 

1.   Open the Insert menu and click Field.

2.   Then select the TOC field type.

 

You can use the **AppendTOC** method of the WParagraph class, to add a TOC to the DocIO document.

 

**UpperHeadingLevel** and **LowerHeadingLevel** define the number of heading levels to be displayed for the TOC. For example, if UpperHeadingLevel is set to 4 and LowerHeadingLevel is set to 3, then TOC will display heading levels from third to fourth.

 

**SetTOCLevelStyle** method sets the style for each TOC level. For example, **SetTOCLevelStyle**(1, \"Normal\") will set the **Normal** style for the first level of TOC.

 

**UpdatingTableOfContents** method of WordDocument class updates table of contents field in the word document. Internally Essential DocIO updates page number in table of contents using the Doc to PDF layout engine. Hence the limitations are similar to the limitation in Doc to PDF lay outing.

 


Note: Updating Table of Contents is not supported in Silverlight platform.


 

Known Limitations:

The following are the known limitations:

 

[·      ]Currently Auto shapes, foot note and end note, drawing canvas are not preserved in Doc to PDF lay outing, which may leads to updating of incorrect page number.

[·      ]Text wrapping support is partially handled in Doc to PDF lay outing, which may leads to updating of incorrect page number.

 

Class Hierarchy

 

ParagraphItem

            \|

            TableOfContent

 

Public Constructors

 


  ------------------------------------------------------- -----------------------------------------------------------
  Name                                                    Description
  TableOfContent.TableOfContent (IWordDocument)           Initializes a new instance of the TableOfContent class. 
  TableOfContent.TableOfContent (IWordDocument, string)   Initializes a new instance of the TableOfContent class.  
  ------------------------------------------------------- -----------------------------------------------------------


 

 

Public Properties

 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                              | Description                                                                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EntityType                        | Gets the type of the entity.                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IncludePageNumbers                | Gets or sets a value indicating whether to include page numbers in TOC. Default value is true.                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LowerHeadingLevel                 | Gets or sets lower heading level (in interger).                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RightAlignPageNumbers             | Gets or sets a value indicating whether to align page numbers on the right side. Default value is *true*.                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableID                           | Gets or sets the table ID (for TC fields).                                                                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UpperHeadingLevel                 | Gets or sets upper heading level (in interger).                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UseHeadingStyles                  | Gets or sets a value indicating whether to use base heading style (Heading 1...Heading 9).                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UseHyperlinks                     | Gets or sets a value indicating whether to insert TOC entries as hyperlinks.                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UseOutlineLevels                  | Gets or sets a value indicating whether to use outline levels.                                                                                                                       |
|                                   |                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UseTableEntryFields               | Gets or sets a value indicating whether the table will be built from TC fields. If the TableID property is defined, the table is built only from TC fields with the same identifier. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


Note: DocIO can\'t create Outline levels. However, enabling UseOutlineLevels property allow TOC creation from existing outline levels.


 

{border="0"}

Figure 69:Outline Levels

 

Public Methods

 


  ---------------------- --------------------------------------
  Name                   Description
  GetTOCLevelStyleName   Gets the style name for TOC level.  
  SetTOCLevelStyle       Sets the style for TOC level.
  ---------------------- --------------------------------------


 

The following code illustrates how to insert TOC, based on custom styles.

*[]* 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
|                                                                                                                                                                                                             |
|                                                                                                                                                                                                             |
| [WordDocument][ doc = [new] WordDocument();]                                                      |
|                                                                                                                                                                                                             |
| [doc.EnsureMinimal();]                                                                                                                                                  |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [WParagraph][ para = doc.LastParagraph;]                                                                               |
|                                                                                                                                                                                                             |
| [TableOfContent toc = para.AppendTOC(1, 1);]                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [toc.UseHeadingStyles = [false;]]                                                                                                                  |
|                                                                                                                                                                                                             |
| **[]**                                                                                                                                                     |
|                                                                                                                                                                                                             |
| [// Set the TOC level style based on which the TOC should be created.]                                                                                    |
|                                                                                                                                                                                                             |
| [toc. SetTOCLevelStyle(1, [\"MyStyle1\"]);]                                                                                                      |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [WSection][ section = doc.LastSection;]                                                                                |
|                                                                                                                                                                                                             |
| [WParagraph][ newPara = section.AddParagraph() [as] WParagraph;]                                  |
|                                                                                                                                                                                                             |
| [WTextRange][ text = newPara.AppendText([\"My Style1\"]) [as] WTextRange;] |
|                                                                                                                                                                                                             |
| [newPara.ApplyStyle(\"MyStyle1\");]                                                                                                                                     |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [//][ ][Updates the table of contents.]               |
|                                                                                                                                                                                                             |
| [doc.UpdateTableOfContents();][]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [Dim][ doc [As] [New] WordDocument()]                                                                            |
|                                                                                                                                                                                                                                                 |
| [doc.EnsureMinimal() ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [Dim][ para [As] WParagraph = doc.LastParagraph]                                                                                      |
|                                                                                                                                                                                                                                                 |
| [Dim][ toc [As] TableOfContent = para.AppendTOC(1, 1)]                                                                                |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [toc.UseHeadingStyles = [false]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [\' Set the TOC level style based on which the TOC should be created.]                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [toc.SetTOCLevelStyle(1, [\"MyStyle1\"]) ]                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [Dim][ section [As] WSection = doc.LastSection]                                                                                       |
|                                                                                                                                                                                                                                                 |
| [Dim][ newPara [As] WParagraph = [TryCast](section.AddParagraph(), WParagraph)]                                  |
|                                                                                                                                                                                                                                                 |
| [Dim][ text [As] WTextRange = [TryCast](newPara.AppendText([\"My Style1\"]), WTextRange)] |
|                                                                                                                                                                                                                                                 |
| [newPara.ApplyStyle(\"MyStyle1\")]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [\'][ ][Updates the table of contents.][]             |
|                                                                                                                                                                                                                                                 |
| [doc.UpdateTableOfContents()][]                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

