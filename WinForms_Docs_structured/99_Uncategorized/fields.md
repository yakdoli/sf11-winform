---
title: fields.md
original_path: WinForms_Docs/99_Uncategorized/fields.md
created_at: 2025-08-05
---






#### Fields {#fields style="tab-stops: 0pt"}

 

[]{#p45}Fields are special elements of the Word document. To insert a field, open the Insert menu and click Field option in Microsoft Word.

 

{border="0"}

Figure 44: Field Dialog Box

 

 

Fields are widely used for Mail Merge. In Word document, almost every field consists of the field start marker text, which defines the type of the field, field separator marker, field value, and field end marker.

 

**WField** class represents a field in the Word document. There are many types of fields.

 

{border="0"}

Figure 45: WField Class Hierarchy

 

You can get or set the type of field by using the **FieldType** property. WField class also has the **TextFormat** property, which defines the text format for the field. There are four different types of text formats for fields.

 

[·      ]None -- no text formatting

[·      ]Uppercase -- uppercase text formatting

[·      ]Lowercase -- lowercase text formatting

[·      ]FirstCapital -- first capital text formatting

[·      ]Titlecase -- title case text formatting

 

Adding Field to Paragraph

 

You can use the **AppendField** function of the **WParagraph** class to add new fields to a paragraph. When you add a field to a paragraph, all the field markers are automatically added to the paragraph. For details, refer WFieldMark class description.

 

There are special fields like Form Field, Merge Field, Embed Field and Seq Field. For details, refer the WFormField, WMergeField, WEmbedField and WSeqField documentation.

 

**Class Hierarchy**

 

WTextRange

               \|

            WField

 

**Public Constructor**

 


  ------------------------------- ---------------------------------------------------
  Name                            Description
  WField.WField (IWordDocument)   Initializes a new instance of the WField class.  
  ------------------------------- ---------------------------------------------------


 

Public Properties

 


  -------------- -------------------------------------------
  Name           Description
  EntityType     Gets the type of the entity.  
  FieldPattern   Gets / sets field pattern.  
  FieldType      Gets / sets field type                   
  FieldValue     Gets the field value.  
  TextFormat     Gets/ sets regular text format.  
  -------------- -------------------------------------------


 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                                                   |
|                                                                                                                                                            |
| [IWSection][ section = doc.AddSection();]                             |
|                                                                                                                                                            |
| [IWParagraph][ paragraph = section.AddParagraph();]                   |
|                                                                                                                                                            |
| [paragraph.AppendText([\"Testing writing Merge Fields into Header\"]);]                         |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [section.PageSetup.DifferentFirstPage = [true];]                                                  |
|                                                                                                                                                            |
| [section.PageSetup.DifferentOddAndEvenPages = [true];]                                            |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [paragraph = [new] [WParagraph](doc);]                                       |
|                                                                                                                                                            |
| [paragraph.AppendText([\"\[ FIRST PAGE Header \]\"]);]                                          |
|                                                                                                                                                            |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);]                                                    |
|                                                                                                                                                            |
| [paragraph = [new] [WParagraph](doc);]                                       |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [//Appends field]                                                                                        |
|                                                                                                                                                            |
| [paragraph.AppendField([\"Field\'s Name\"], [FieldType].FieldMergeField);] |
|                                                                                                                                                            |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);]                                                    |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [paragraph = [new] [WParagraph](doc);]                                       |
|                                                                                                                                                            |
| [paragraph.AppendText([\"\[ FIRST PAGE Footer \]\\r\"]);]                                       |
|                                                                                                                                                            |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);]                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [Dim ][section As ][IWSection][ = doc.AddSection()]           |
|                                                                                                                                                                                                                                                                     |
| [Dim][ paragraph As ][IWParagraph][ = section.AddParagraph()] |
|                                                                                                                                                                                                                                                                     |
| [paragraph.AppendText(\"Testing writing Merge Fields into Header\")]                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [section.PageSetup.DifferentFirstPage = True]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [section.PageSetup.DifferentOddAndEvenPages = True]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [paragraph = ][New][ WParagraph(doc)]                                                                          |
|                                                                                                                                                                                                                                                                     |
| [paragraph.AppendText(\"\[ FIRST PAGE Header \]\")]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)]                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [paragraph = ][New][ WParagraph(doc)]                                                                          |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [\'Appends field]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [paragraph.AppendField(\"Field\'s Name\", FieldType.FieldMergeField)]                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)]                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [paragraph = ][New][ WParagraph(doc)]                                                                          |
|                                                                                                                                                                                                                                                                     |
| [paragraph.AppendText(\"\[ FIRST PAGE Footer \]\" & Constants.vbCr)]                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)]                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

More:

















