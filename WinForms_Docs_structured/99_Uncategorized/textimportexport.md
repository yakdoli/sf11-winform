---
title: textimportexport.md
original_path: WinForms_Docs/99_Uncategorized/textimportexport.md
created_at: 2025-08-05
---






#####  Text Import/Export {#text-importexport style="tab-stops: 0pt"}

The text import feature allows the user to import a .txt file into the RichTextBoxAdv. It renders the text in Notepad format and displays the text in the format of RichTextBoxAdv's content model. The text export feature actually exposes the RichTextBoxAdv's document as a .txt file. The following methods clearly show this usage.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| **[      ]**[RichTextBox.Document = [TextImporting].ConvertToDocumentAdv(textstream);]                                                              |
|                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| **[      ]**[string][ txtstring= [TextExporting].ConvertToText(RichTextBox.Document, textStream);] |
|                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Methods

+------------------------+-----------------------------------------------+-------------+-------------+-------------+
| Method                 | Description                                   | Parameters  | Type        | Return Type |
+------------------------+-----------------------------------------------+-------------+-------------+-------------+
| ConvertToDocumentAdv() | Converts text stream into DocumentAdv.        | NA          | NA          | DocumentAdv |
+------------------------+-----------------------------------------------+-------------+-------------+-------------+
| ConvertText()          | Returns the rich-text content as a text file. | NA          | NA          | String      |
|                        |                                               |             |             |             |
|                        |                                               |             |             |             |
+------------------------+-----------------------------------------------+-------------+-------------+-------------+

[]{#related-topics}

