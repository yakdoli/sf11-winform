---
title: importpages.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\importpages.md
created_at: 2025-07-03
---








  









### Import Pages {#import-pages style="tab-stops: 0pt"}

 

Pages from other document can be imported to the existing document using the **ImportPage** method. The following code example illustrates this method.

 

+--------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                   |
|                                                                                                  |
| []                                             |
|                                                                                                  |
| [doc.ImportPage(ldDoc, page);]                               |
|                                                                                                  |
| [doc.ImportPage(ldDoc, pageIndex);]                          |
|                                                                                                  |
| [doc.ImportPageRange(ldDoc, startPageIndex, endPageIndex); ] |
+--------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]** |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [doc.ImportPage(ldDoc, page)]                                                                |
|                                                                                                                                  |
| [doc.ImportPage(ldDoc, pageIndex)]                                                           |
|                                                                                                                                  |
| [doc.ImportPageRange(ldDoc, startPageIndex, endPageIndex)]                                   |
+----------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: The first two methods in the above code are just shortcuts to the last one, which is a powerful tool appending not just pages, but annotations and forms as well.


 

The parameters included are as follows.

[] 

[·      ]**ldDoc**: Loaded PDF document

[·      ]**Page**: Page that should be appended (not a page itself, but its valid representation)

[·      ]**PageIndex**: Index of the page

[·      ]**StartPageIndex, endPageIndex**: Indices specifying the page range

 

The following code snippets illustrate how to import a page to the existing document.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument]( filename ); ] |
|                                                                                                                                                                                                      |
| [int][ startIndex = 0; ]                                                                                        |
|                                                                                                                                                                                                      |
| [int][ endIndex = ldDoc.Pages.Count - 1; ]                                                                      |
|                                                                                                                                                                                                      |
| [newDoc.ImportPageRange( ldDoc, startIndex, endIndex ); ]                                                                                                        |
|                                                                                                                                                                                                      |
| [newDoc.Save( newFilename ); ]                                                                                                                                   |
|                                                                                                                                                                                                      |
| [newDoc.Close(); ]                                                                                                                                               |
|                                                                                                                                                                                                      |
| [ldDoc.Close();]                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                                         |
| [Dim][ startIndex [As] [Integer] = 0]                                    |
|                                                                                                                                                                                                         |
| [Dim][ endIndex [As] [Integer] = ldDoc.Pages.Count - 1]                  |
|                                                                                                                                                                                                         |
| [NewDoc.ImportPageRange(ldDoc, startIndex, endIndex) ]                                                                                                              |
|                                                                                                                                                                                                         |
| [NewDoc.Save(NewFilename) ]                                                                                                                                         |
|                                                                                                                                                                                                         |
| [NewDoc.Close() ]                                                                                                                                                   |
|                                                                                                                                                                                                         |
| [ldDoc.Close()]                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Implementation Note

 

The importing is done by converting the page content to the PdfTemplate object, which means that the new page will not inherit the possibly complex layer structure, so you will see just one default layer. Obviously, you will be able to place something beneath that layer. However you will not be able to manipulate the \"old\" layers, because they won\'t exist.

 

This conversion is performed in order to avoid an incomplete page, harming further user output.

 

Restrictions

[] 

[·      ]All pages are appended to the host document to make easier bookmarks (outlines) merging. Bookmarks are organized as a complex tree, as it is hard to calculate where the new items should be placed.

[·      ]Outlines (Bookmarks) will be copied to the target document along with the pages. The library will try to rebuild the bookmark tree with those bookmarks that have the destination pointing to any of the imported pages.

[·      ]The outline tree might look a bit weird if just part of it was copied, as it is hard to recreate the tree with part of the bookmarks.

[·      ]Some of the contents are usually imported from the original document to the final document during saving process. Hence, the original document has to be closed only after the final document is saved.

 

 

 

[]{#related-topics}

