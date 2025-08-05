---
title: mergefield.md
original_path: WinForms_Docs/99_Uncategorized/mergefield.md
created_at: 2025-08-05
---






##### Merge Field {#merge-field style="tab-stops: 0pt"}

 

**WMergeField** class represents a merge field in the Word document. To add a merge field in Microsoft Word, open the **Insert** menu, click **Field**, and then click **MergeField**. Merge field is suitable for mail merge because it is easy to set the user\'s data inside it.

 

[·      ]**FieldName**: defines the name of the field

[·      ]**TextBefore** and **TextAfter**: define the text that is displayed before and after the merge field

[·      ]**NumberFormat** and **DateFormat**: define the number and date format respectively

 

These properties are used during mail merge. NumberFormat and DateFormat properties do not have an equivalent in Word MergeField.

 

**Class Hierarchy**

 

WTextRange

             \|

       WField

              \|   

             WMergeField

 

**Public Constructor**

 


  ----------------------------------------- ------------------------------------------------------
  Name                                      Description
  WMergeField.WMergeField (IWordDocument)   Initializes a new instance of the WMergeField class.
  ----------------------------------------- ------------------------------------------------------


 

Public Properties

 


  -------------- ---------------------------------------------
  Name           Description
  DateFormat     Gets the date format.  
  EntityType     Gets the type of the entity.  
  FieldName      Gets or sets field name.
  NumberFormat   Gets the number format.  
  Prefix         Gets the prefix of merge field.
  TextAfter      Gets or sets the text after merge field.  
  TextBefore     Gets or sets the text before merge field.  
  -------------- ---------------------------------------------


 

The following example illustrates how to add the a merge field to the header and footer of the document.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [IWSection][ section = doc.AddSection();]                              |
|                                                                                                                                                                |
| [IWParagraph][ paragraph = section.AddParagraph();]                    |
|                                                                                                                                                                |
| [paragraph.AppendText([\"Testing writing Merge Fields into Header\"]);]                            |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [section.PageSetup.DifferentFirstPage = [true];]                                                      |
|                                                                                                                                                                |
| [section.PageSetup.DifferentOddAndEvenPages = [true];]                                                |
|                                                                                                                                                                |
| [paragraph = [new] [WParagraph](doc);]                                        |
|                                                                                                                                                                |
| [paragraph.AppendText([\"\[ FIRST PAGE Header \]\"]);]                                             |
|                                                                                                                                                                |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);]                                                        |
|                                                                                                                                                                |
| [paragraph = [new] [WParagraph](doc);]                                        |
|                                                                                                                                                                |
| [paragraph.AppendField([\"Field\'s Name\"], [FieldType].FieldMergeField);] |
|                                                                                                                                                                |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);]                                                        |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [paragraph = [new] [WParagraph](doc);]                                        |
|                                                                                                                                                                |
| [paragraph.AppendText([\"\[ FIRST PAGE Footer \]\\r\"]);]                                          |
|                                                                                                                                                                |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);]                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [Dim][ section [As] IWSection = doc.AddSection()]           |
|                                                                                                                                                                       |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()] |
|                                                                                                                                                                       |
| [paragraph.AppendText([\"Testing writing Merge Fields into Header\"])]                                    |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [section.PageSetup.DifferentFirstPage = [True]]                                                              |
|                                                                                                                                                                       |
| [section.PageSetup.DifferentOddAndEvenPages = [True]]                                                        |
|                                                                                                                                                                       |
| [paragraph = [New] WParagraph(doc)]                                                                          |
|                                                                                                                                                                       |
| [paragraph.AppendText([\"\[ FIRST PAGE Header \]\"])]                                                     |
|                                                                                                                                                                       |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)]                                                                |
|                                                                                                                                                                       |
| [paragraph = [New] WParagraph(doc)]                                                                          |
|                                                                                                                                                                       |
| [paragraph.AppendField([\"Field\'s Name\"], FieldType.FieldMergeField)]                                   |
|                                                                                                                                                                       |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)]                                                                |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [paragraph = [New] WParagraph(doc)]                                                                          |
|                                                                                                                                                                       |
| [paragraph.AppendText([\"\[ FIRST PAGE Footer \]\"] & Constants.vbCr)]                                    |
|                                                                                                                                                                       |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph) ]                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

