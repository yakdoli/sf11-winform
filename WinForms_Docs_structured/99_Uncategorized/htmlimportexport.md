---
title: htmlimportexport.md
original_path: WinForms_Docs/99_Uncategorized/htmlimportexport.md
created_at: 2025-08-05
---






#####  HTML Import/Export {#html-importexport style="tab-stops: 0pt"}

The HTML import feature allows the user to import an .html file into the RichTextBoxAdv. It renders the HTML tags like a browser and displays the text in the format of RichTextBoxAdv's content model. The HTML export feature actually exposes the RichTextBoxAdv's document as an .html file. The following methods clearly show this use case.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                        |
| [      [DocumentAdv] doucment = [HTMLImporting].ConvertToDocumentAdv(stream);]     |
|                                                                                                                                                                        |
| [      [DocumentAdv] document = [HTMLImporting].ConvertToDocumentAdv(htmlstring);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                    |
| [       string][ html = [HTMLExporting].ConvertToHtml(RichTextBox.Document, stream);] |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Methods

+------------------------+---------------------------------------------+---------------------+-------------+-------------+
| Method                 | Description                                 | Parameters          | Type        | Return Type |
+------------------------+---------------------------------------------+---------------------+-------------+-------------+
| ConvertToDocumentAdv() | Converts htmlstream into DocumentAdv.       | (Stream stream)     | NA          | DocumentAdv |
|                        |                                             |                     |             |             |
|                        |                                             | (string htmlstring) |             |             |
+------------------------+---------------------------------------------+---------------------+-------------+-------------+
| ConvertToHtml()        | Converts the DocumentAdv to an HTML string. | NA                  | NA          | String      |
+------------------------+---------------------------------------------+---------------------+-------------+-------------+

###### 3.32.3.8.1.1         Limitations {#limitations style="tab-stops: 0pt"}

The HTML import/export feature has the following limitations:

1.   Script support has not been provided.

2.   It does not provide support for tables.

[]{#related-topics}

