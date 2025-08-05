---
title: cloningandmerging.md
original_path: WinForms_Docs/99_Uncategorized/cloningandmerging.md
created_at: 2025-08-05
---








  









### Cloning and Merging {#cloning-and-merging style="tab-stops: 0pt"}

 

DocIO has an ability to clone the whole Word document or a part of it.

*[]* 

Use the **Clone** method for \"deep\" document cloning. This method returns the new object of the WordDocument class along with the content of the cloned document which invoked the Clone method. You can use the Clone method to clone any document entity.

 


{border="0"}Note: If source and destination documents have styles with the same names, then the styles of the imported document will be renamed after importing.


 

The following example illustrates how to merge two documents by using the Clone method.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                                                     |
|                                                                                                                                                                                              |
| [// Create the first document.]                                                                                                            |
|                                                                                                                                                                                              |
| [IWordDocument][ doc = [new] [WordDocument]();]               |
|                                                                                                                                                                                              |
| [IWSection][ section = doc.AddSection();]                                                               |
|                                                                                                                                                                                              |
| [IWTextRange][ text1 = section.AddParagraph().AppendText( [\"First document ]]   |
|                                                                                                                                                                                              |
| [section\...[\" );]]                                                                                                              |
|                                                                                                                                                                                              |
| [text1.CharacterFormat.TextColor = [Color].Red;]                                                                                    |
|                                                                                                                                                                                              |
| [section.AddParagraph().AppendText( [\"Some Text\...\"] );]                                                                       |
|                                                                                                                                                                                              |
| [section.AddParagraph().AppendText( [\"New Paragraph\"] );]                                                                       |
|                                                                                                                                                                                              |
| [section.AddParagraph().AppendText( [\"Third Paragraph\"] );]                                                                     |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [// Create the second document.]                                                                                                           |
|                                                                                                                                                                                              |
| [IWordDocument][ doc2 = [new] [WordDocument]();]              |
|                                                                                                                                                                                              |
| [IWSection][ section2 = doc2.AddSection();]                                                             |
|                                                                                                                                                                                              |
| [IWTextRange][ text2 = section2.AddParagraph().AppendText( [\"Second document ]] |
|                                                                                                                                                                                              |
| [section\...[\" );]]                                                                                                              |
|                                                                                                                                                                                              |
| [text2.CharacterFormat.TextColor = [Color].Blue;]                                                                                   |
|                                                                                                                                                                                              |
| [section2.AddParagraph().AppendText( [\"Some Text\...\"] );]                                                                      |
|                                                                                                                                                                                              |
| [section2.AddParagraph().AppendText( [\"New Paragraph More Text\"] );]                                                            |
|                                                                                                                                                                                              |
| [section2.AddParagraph().AppendText( [\"Third Paragraph More Text\"] );]                                                          |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [// Merge the second document with the first.]                                                                                             |
|                                                                                                                                                                                              |
| [doc.Sections.Add( section2.Clone() );]                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [\' Create the first document.]                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()]                                                    |
|                                                                                                                                                                                                                                         |
| [Dim][ section [As] IWSection = doc.AddSection()]                                                                             |
|                                                                                                                                                                                                                                         |
| [Dim][ text1 [As] IWTextRange = section.AddParagraph().AppendText([\"First document section\...\"])]   |
|                                                                                                                                                                                                                                         |
| [text1.CharacterFormat.TextColor = Color.Red]                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [section.AddParagraph().AppendText([\"Some Text\...\"])]                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [section.AddParagraph().AppendText([\"New Paragraph\"])]                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [section.AddParagraph().AppendText([\"Third Paragraph\"])]                                                                                                                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\' Create the second document.]                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [Dim][ doc2 [As] IWordDocument = [New] WordDocument()]                                                   |
|                                                                                                                                                                                                                                         |
| [Dim][ section2 [As] IWSection = doc2.AddSection()]                                                                           |
|                                                                                                                                                                                                                                         |
| [Dim][ text2 [As] IWTextRange = section2.AddParagraph().AppendText([\"Second document section\...\"])] |
|                                                                                                                                                                                                                                         |
| [text2.CharacterFormat.TextColor = Color.Blue]                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [section2.AddParagraph().AppendText([\"Some Text\...\"])]                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [section2.AddParagraph().AppendText([\"New Paragraph More Text\"])]                                                                                                          |
|                                                                                                                                                                                                                                         |
| [section2.AddParagraph().AppendText([\"Third Paragraph More Text\"])]                                                                                                        |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\' Merge the second document with the first.]                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [doc.Sections.Add(section2.Clone())]                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_Headers_and_Footers} 

**Import Contents**

Import content functionality is used to copy/merge the contents from one document to another. Compatibility options of the source document will not be imported to the destination document.

Use the **ImportContent(WordDocument doc)** method to import contents and styles from the source document to the destination document.

Use the **ImportContent(WordDocument doc, bool importStyles)** method to import contents from the source document to the destination document by specifying whether to import styles which have the same name between the source and destination document.

[·      ][If **importStyles** is true, all the contents and styles of the source document will be imported to the destination document. In cases where a style in the source document has the same name as a style in the destination document, "Guid" is added as a suffix to the name of the imported style in order to preserve unique style name.]

[·      ][If **importStyles** is false, all the contents will be imported, but only the styles that are not present in the destination document will be preserved. In cases where a style with the same name exists in the destination document, the destination style is applied to the imported contents.]

{border="0"}Note: If source and destination documents have styles with the same names, then Guid is added as a suffix to the name of the imported styles in the destination document.

 

Use the **ImportContent(WordDocument doc, ImportOptions importOptions)** method to import contents from the source document to the destination document with various import options similar to MS Word copy and paste options. Below are the import options supported by Essential DocIO.

[·      ]**[KeepSourceFormatting]**[---Imports all the contents of the source document to the destination document and preserves the entire source document formatting of the content as direct formatting. Header and footer contents will be imported similar to the **UseDestinationStyles** option.]

[·      ]**[MergeFormatting---]**[Imports all the contents of the source document to the destination document and applies the formatting of surrounding content in destination document. Merges the formatting of the contents surrounding it by preserving some of the source formatting (such as bold, italic, underline, etc.). Header and footer contents will be imported similar to the **UseDestinationStyles** option.]

[·      ]**[KeepTextOnly]**[---Imports only the text from the source document to the destination document (tables, textboxes, pictures, headers, footers, etc., will be removed), similar to content copied from a text file (.txt).]

[·      ]**[UseDestinationStyles]**[---Imports all the content of the source document to the destination document and applies the styles present in the destination document, or imports the source style to the destination document if no style with same name in destination document.]

 

The following example illustrates how to import contents from one document to another with various import options.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                 |
|                                                                                                                                                |
| [// Open the destination word document.][] |
|                                                                                                                                                |
| [WordDocument destination = new WordDocument(\"Destination.doc\");]                                        |
|                                                                                                                                                |
| [// Open the source word document.]                                                          |
|                                                                                                                                                |
| [WordDocument source = new WordDocument(\"Source.doc\");]                                                  |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| [// Imports the contents with import option keep source formatting.]                         |
|                                                                                                                                                |
| [destination.ImportContent(source, [ImportOptions].KeepSourceFormatting);]         |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| [// Save the document.]                                                                      |
|                                                                                                                                                |
| [destination.Save(\"Sample.doc\", FormatType.Doc);][]                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[ ]                                                                                                                 |
|                                                                                                                                                                                                                           |
| [\' Open the destination word document.]                                                                                                                                |
|                                                                                                                                                                                                                           |
| [Dim][ destination [As] [New] WordDocument([\"Destination.doc\"])] |
|                                                                                                                                                                                                                           |
| [\' Open the source word document.]                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [Dim][ source [As] [New] WordDocument([\"Source.doc\"])]           |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\' Imports the contents with import option keep source formatting.]                                                                                                    |
|                                                                                                                                                                                                                           |
| [destination.ImportContent(source, ImportOptions.KeepSourceFormatting)]                                                                                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\' Save the document.]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [destination.Save([\"Sample.doc\"], FormatType.Doc)]**[]**                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

