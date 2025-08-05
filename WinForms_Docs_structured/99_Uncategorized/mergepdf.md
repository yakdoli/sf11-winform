---
title: mergepdf.md
original_path: WinForms_Docs/99_Uncategorized/mergepdf.md
created_at: 2025-08-05
---








  









### Merge PDF {#merge-pdf style="tab-stops: 0pt"}

 

Merging feature in the Essential PDF enables appending all documents to the target document. While merging, all bookmarks and attachments will be copied, additionally to **ImportPageRange** behavior.

 

There are various overloads of the **Merge** method that allow specifying different parameters. Some important parameters are: 

 

[·      ]Array of strings

[·      ]Array of PdfDocumentBase instances

 

If the target document is null (in overload that accepts PdfDocumentBase class as a target), a new instance will be created.

 

You can also merge the documents in the following ways:

 

[·      ]Append all the documents one after the another by using the **Append** method.

[·      ]Import the pages from different documents by using the **ImportPageRange** or **ImportPage** method.

[·      ]Use **Insert** method to insert the pages one by one.

 

For more details, see [[Merge PDF]{.UGHyperlink}]().

 

[]{#related-topics}

