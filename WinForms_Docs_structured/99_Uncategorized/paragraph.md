---
title: paragraph.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\paragraph.md
created_at: 2025-07-03
---








  









## Paragraph {#paragraph style="tab-stops: 0pt"}

 

**WParagraph** class represents a single paragraph in a document. DocIO paragraph contains paragraph items inside. You can add paragraph items by using the Items property. This property returns the collection of paragraph items (object of ParagraphItemCollection type).

 

Each paragraph has a paragraph format. The format of the paragraph is set by using the **ParagraphFormat** property. This  property is used to define the paragraph border, style of texture, foreground and background color, paragraph spacing, and so on. For more details on Paragraph Formatting, see 

]]{.MsoHyperlink} 

**IsInCell**: defines whether current paragraph belongs to the table cell (is in the table cell)

[·      ]**IsEndOfSection**: defines whether the current paragraph is the last paragraph in the section

[·      ]**IsEndOfDocument**: defines whether the current paragraph is the last paragraph in the document

 

**Formatting Break Symbol**

 

**BreakCharacterFormat** property is used to set the character formatting for the break symbol.

 

{border="0"}

Figure 42: Formatted Break Symbol

 

**DocIO List**

 

DocIO paragraphs can also be displayed as a list by using the ListFormat property. This property returns the object of the WListFormat type. The WListFormat class defines the formatting for the list (applied list style, list level number and so on). For more details on WListFormat class, see 

 

**Adding Paragraph Items**

 

DocIO paragraph enables to add paragraph items to the end of the current paragraph by using the Append function. For example, the AppendText method, AppendBreak method, and so on, are used for this purpose.

 

Class Hierarchy

 

TextBodyItem

                 \|   

            WParagraph

 

**Public Constructor**

 


  --------------------------------------- ------------------------------------------------------
  Name                                    Description
  WParagraph.WParagraph (IWordDocument)   Initializes a new instance of the WParagraph class. 
  --------------------------------------- ------------------------------------------------------


 

**Public Properties**

 


+-----------------------------------+-----------------------------------------------------------------------------+
| **Name**                          | **Description**                                                             |
+-----------------------------------+-----------------------------------------------------------------------------+
| BreakCharacterFormat              | Gets character format for the break symbol.                                 |
+-----------------------------------+-----------------------------------------------------------------------------+
| ChildEntities                     | Gets the child entities.                                                    |
+-----------------------------------+-----------------------------------------------------------------------------+
| EntityType                        | Gets the type of the entity.                                                |
+-----------------------------------+-----------------------------------------------------------------------------+
| IsEndOfDocument                   | Gets a value indicating whether this paragraph is the end of document.      |
+-----------------------------------+-----------------------------------------------------------------------------+
| IsEndOfSection                    | Gets a value indicating whether this paragraph is the end of the section.   |
|                                   |                                                                             |
|                                   |                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------+
| IsInCell                          | Gets a value indicating whether this paragraph is in cell.                  |
+-----------------------------------+-----------------------------------------------------------------------------+
| Items                             | Gets paragraph items.                                                       |
+-----------------------------------+-----------------------------------------------------------------------------+
| ListFormat                        | Gets format of the list for the paragraph.                                  |
+-----------------------------------+-----------------------------------------------------------------------------+
| ParagraphFormat                   | Gets paragraph format.                                                      |
+-----------------------------------+-----------------------------------------------------------------------------+
| StyleName                         | Gets paragraph style name.                                                  |
+-----------------------------------+-----------------------------------------------------------------------------+
| Text                              | Gets or sets paragraph text.                                                |
+-----------------------------------+-----------------------------------------------------------------------------+


 

**Public Methods**

 


  ------------------------- -------------------------------------------------------------------
  **Name**                  **Description**
  AppendBookmarkEnd         Appends end of the bookmark with specified name into paragraph.
  AppendBookmarkStart       Appends start of the bookmark with specified name into paragraph.
  AppendBreak               Appends break to end of the paragraph.  
  AppendCheckBox            Appends checkbox to end of paragraph.
  AppendComment             Appends comment to end of paragraph.
  AppendDropDownFormField   Appends DropDown form field to end of paragraph.
  AppendField               Appends field to end of paragraph.  
  AppendFootnote            Appends footnote to end of paragraph.
  AppendPicture             Appends picture to end of paragraph.
  AppendSymbol              Appends special symbol to end of paragraph.  
  AppendTable               Append Table.  
  AppendText                Appends text to end of document.  
  AppendTextBox             Append Text box to the end of the paragraph.  
  AppendTextFormField       Appends text form field to end of paragraph. 
  AppendTOC                 Appends the TOC.  
  ApplyStyle                Applies style to the paragraph.
  Find                      Finds text inside the paragraph.
  GetStyle                  Gets related style.
  Replace                   Replaced text inside the paragraph.
  InsertSectionBreak        Inserts a section break.
  ------------------------- -------------------------------------------------------------------


 

The following example illustrates how to add various formats to paragraphs.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
|                                                                                                                                                   |
|                                                                                                                                                   |
| [// Add paragraph and apply formatting.]                                                        |
|                                                                                                                                                   |
| [paragraph = section.AddParagraph();]                                                                         |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.Borders.Bottom.BorderType = [BorderStyle].ThinThickSmallGap;] |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.HorizontalAlignment = [HorizontalAlignment].Center;]          |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.BeforeSpacing = 18;]                                                               |
|                                                                                                                                                   |
| [textRange = paragraph.AppendText([\"Windows Forms. \"]);]                             |
|                                                                                                                                                   |
| []                                                                                                            |
|                                                                                                                                                   |
| [paragraph = section.AddParagraph();]                                                                         |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.PageBreakBefore = [true];]                                    |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.BackColor = [Color].FromArgb(102, 102, 153);]                 |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.BeforeSpacing = 18;]                                                               |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.AfterSpacing = 6;]                                                                 |
|                                                                                                                                                   |
| [paragraph.ParagraphFormat.FirstLineIndent = 45;]                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\' Add paragraph and apply formatting.]                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [paragraph = section.AddParagraph()]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.Borders.Bottom.BorderType = BorderStyle.ThinThickSmallGap]                                                                                        |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Center]                                                                                                 |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.BeforeSpacing = 18]                                                                                                                               |
|                                                                                                                                                                                                                                |
| [textRange = paragraph.AppendText(\"Windows Forms. \")]                                                                                                                      |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [paragraph = section.AddParagraph()]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.PageBreakBefore = ][True]                                                                        |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.BackColor = ][Color][.FromArgb(102, 102, 153)] |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.BeforeSpacing = 18]                                                                                                                               |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.AfterSpacing = 6]                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [paragraph.ParagraphFormat.FirstLineIndent = 45]                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**For More Information Refer:**

 

, 

More:







