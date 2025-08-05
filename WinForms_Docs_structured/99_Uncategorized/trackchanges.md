---
title: trackchanges.md
original_path: WinForms_Docs/99_Uncategorized/trackchanges.md
created_at: 2025-08-05
---








  









### Track Changes {#track-changes style="tab-stops: 0pt"}

 

Track Changes feature enables you to keep track of the changes made to a document in Microsoft Word. Using this feature, you can maintain a record of every insertion, deletion and modification in the document, including who made the change and when it was made. The objects that carry such information are called \"Tracking Changes\" or \"Revisions\".

 

Revision Tracking is normally meant for use in a shared environment, so you can track how other people may have changed a document for which you are responsible. However, it can also be a valuable tool even if you are the only one using a document, as you can view your own changes in the document.\
\
**Accessing Revisions**

 

You can choose to accept or reject the changes made to a document in Microsoft Word. ParagraphItem and TextBodyItem (WParagraph and WTable are TextBodyItems) objects have the **WordDocument.AcceptChanges** and **WordDocument.RejectChanges** properties, to detect whether an object was inserted or deleted in Microsoft Word (revision tracking being enabled).

 

**WordDocument.HasChanges** specifies whether the document has any revisions (changes). It returns **True**, if the document has atleast one revision.

 

**WordDocument.TrackChanges** property is used to enable revision tracking in Microsoft Word. Note that this setting does not affect the changes made to the document by using DocIO. Also, the changes made to the document by using DocIO, are never tracked as revisions.

*[]* 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [Syncfusion.DocIO.DLS.[WordDocument] doc = [new] [WordDocument]([@\"../../Essential DocIO.doc\"], [FormatType].Doc);] |
|                                                                                                                                                                                                                                                                                |
| [foreach][ ([WSection] section [in] doc.Sections)]                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [    [for] ([int] i = 0; i \<= section.Paragraphs.Count - 1; i++)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        para = section.Paragraphs\[i\];]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [        [// Check each paragraph items revisions.]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [        [foreach] ([ParagraphItem] item [in] para.Items)]                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [            [Console].WriteLine(item.EntityType.ToString() + [\" Inserted: \"] + item.IsInsertRevision.ToString());]                                                                      |
|                                                                                                                                                                                                                                                                                |
| [            [Console].WriteLine(item.EntityType.ToString() + [\"Deleted:\"] + item.IsDeleteRevision.ToString());]                                                                         |
|                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Accept tracking changes of the document.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [doc.AcceptChanges();]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [doc.Save([\"sample.doc\"]);]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ doc [As] Syncfusion.DocIO.DLS.WordDocument = [New] WordDocument([\"../../Essential DocIO.doc\"], FormatType.Doc)] |
|                                                                                                                                                                                                                                                                                 |
| [For][ [Each] section [As] WSection [In] doc.Sections]                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [For][ i [As] [Integer] = 0 [To] section.Paragraphs.Count - 1]                                                              |
|                                                                                                                                                                                                                                                                                 |
| [para = section.Paragraphs(i)]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [\' Check each paragraph items revisions.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [For][ [Each] item [As] ParagraphItem [In] para.Items]                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine((item.EntityType.ToString() & [\" Inserted: \"]) + item.IsInsertRevision.ToString())]                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine((item.EntityType.ToString() & [\"Deleted:\"]) + item.IsDeleteRevision.ToString())]                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [Next]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [Next]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [Next]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [\' Accept tracking changes of the document.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [doc.AcceptChanges()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [doc.Save([\"sample.doc\"])]                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

