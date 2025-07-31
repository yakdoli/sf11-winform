---
title: loaddocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loaddocument.md
created_at: 2025-07-03
---








  









### Load Document {#load-document style="tab-stops: 0pt"}

[]{#p81} 

An existing PDF document can be loaded and customized. To open an existing PDF document for further manipulations, use the **PdfLoadedDocument** class. Its constructor allows you to specify the file name, stream or byte array as the source of the document data and the password for the encrypted documents.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename);]              |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](memoryStream);]          |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](byte);]                  |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename,password);]     |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](memoryStream,password);] |
|                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](byte,password);]         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)]              |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(memoryStream)]          |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(byte)]                  |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename,password)]     |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(memoryStream,password)] |
|                                                                                                                                                                                                                      |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(byte,password)]         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


Note: You must add the Syncfusion.Pdf.Parsing namespace to work with the loaded documents.


 

In the loaded document, you can do the following:

 

[·      ]Access the bookmarks

[·    ]Add a new page[]

[·    ]Add an Attachment[]

[·    ]Load dynamic fields[]

 

 Go the above individual links for detailed information.

 

Public Members

 

[The following table lists the public members of the PdfLoadedDocument class.]

[] 

Methods

[] 


  -------------------- --------------------------------------------------------------------------------------------------------------------------------
  Name                 Description
  AddFields            Adds the fields connected to the page.
  Append               Appends the specified loaded document to this one.
  Clone                Creates a shallow copy of the current document.
  Close                Releases the document stream.
  CreateBookmarkRoot   Creates the bookmark root.
  CreateForm           Creates a new form.
  Dispose              Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
  DisposeOnClose       Adds an object to a collection of the objects that will be disposed during document closing. (Inherited from PdfDocumentBase.)
  ImportPage           Overloaded.
  ImportPageRange      Imports a page range from a loaded document. (Inherited from PdfDocumentBase.)
  OnDocumentSaved      Raises DocumentSaved event. (Inherited from PdfDocumentBase.)
  Save                 Saves the document.
  Split                Splits a PDF file to many PDF files; each of them consists of one page from the source file.
  -------------------- --------------------------------------------------------------------------------------------------------------------------------


 

Properties

 


  --------------------- ---------------------------------------------------------------------------------------------------------------------------
  Name                  Description
  Bookmarks             Gets the bookmarks.
  Compression           Gets or sets the desired level of stream compression.
  Conformance           Gets the conformance level applied in the PDF.
  DocumentInformation   Gets or sets document\'s information and properties.
  FileStructure         Gets or sets the internal structure of the PDF file.
  Form                  Gets the loaded form.
  Pages                 Gets the pages.
  Security              Gets the security parameters of the document.
  ViewerPreferences     Gets or sets a viewer preferences object, controlling the way the document is to be presented on the screen, or in print.
  --------------------- ---------------------------------------------------------------------------------------------------------------------------


[] 

Cloning a document

 

You can clone a PDF document in order to copy the document without saving it. This can be done by using the **PdfLoadedDocument.Clone** method.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [PdfLoadedDocument][ ldoc = [new] [PdfLoadedDocument]([\"sample.pdf\"]);] |
|                                                                                                                                                                                                                                 |
| [PdfLoadedDocument][ doc = lDoc.Clone() [as] [PdfLoadedDocument];]                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                                               |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ ldoc [As] [New] PdfLoadedDocument(sample.pdf)]                           |
|                                                                                                                                                                                                                |
| [Dim][ doc [As] PdfLoadedDocument = [TryCast](lDoc.Clone(), PdfLoadedDocument)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:











