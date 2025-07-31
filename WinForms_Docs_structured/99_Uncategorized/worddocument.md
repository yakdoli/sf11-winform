---
title: worddocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\worddocument.md
created_at: 2025-07-03
---








  









## Word Document {#word-document style="tab-stops: 0pt"}

 

You can open, modify and create Microsoft Word documents by using the **WordDocument** class. WordDocument class models the structure of a Microsoft Word document.

 

Creating a Word Document

 

To create a new document, use the **EnsureMinimal** method. This method creates a document with an empty section, and adds empty paragraphs to the newly created section.

 

Opening a Word Document

 

DocIO also gives you an opportunity to open existing documents, or read data from streams saved in the following FormatType variants.

 

[·      ]**Doc**: Microsoft Word File Format

[·      ]**Txt**: Text File Format

[·      ]**Docx**: Word 2007 File Format

[·      ]**Dot**: Word Template Format

[·      ]**HTML**: HTML Format

[·      ]**RTF**: Rich Text Format

[·      ]**Docm** -- Word Macro-enabled Document Format

[·      ]**Dotm** -- Word Macro-enabled Template Format

[·      ]**Dotx** -- Word Open xml Template Format

 

To open a document, use the **Open** method. There are several overloads for this method.

 

[·      ]**Open(string fileName)**: opens Word document

[·      ]**Open(string fileName, FormatType formatType)**: opens the document with specified format type (.doc, .xml or .txt file)

[·      ]**Open(Stream stream, FormatType formatType)**: opens the document from the stream which has the specified format type

 

To save a document back to the Word document format use the **Save** method. There are several overloads for this method.

 

[·      ]**Save(string fileName)**: saves to file in Microsoft Word format

[·      ]**Save(string fileName, FormatType formatType)**: saves the document to file in .xml or Microsoft Word format

[·      ]**Save(Stream stream, FormatType formatType)**: saves the document into stream in .xml or Microsoft Word format

[·      ]**Save(string fileName, FormatType formatType, HttpResponse response, HttpContentDisposition contentDisposition)**: saves the document into the client browser

 

To open the document which is already opened in Word, use the **OpenReadOnly** method to open the document in the read-only mode.

 

[·      ]OpenReadOnly(string fileName, FormatType formatType): opens the document in the read-only mode

 

Public Properties

 


+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                              | Description                                                                                                                                                                   |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Background                            | Gets document\'s background.                                                                                                                                                  |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bookmarks                             | Gets document bookmarks.                                                                                                                                                      |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Built-inDocumentProperties            | Gets document built-in properties object.                                                                                                                                     |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChildEntities                         | Gets the child entities.                                                                                                                                                      |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CustomDocumentProperties              | Gets document custom properties object.                                                                                                                                       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EndnoteNumberFormat                   | Gets or sets endnote numbering format.                                                                                                                                        |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EndnotePosition                       | Gets or sets endnote position in the document.                                                                                                                                |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EntityType                            | Gets the type of the entity.                                                                                                                                                  |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FootnoteNumberFormat                  | Gets or sets footnote numbering format.                                                                                                                                       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FootnotePosition                      | Gets or sets footnote position in the document.                                                                                                                               |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| InitialEndnoteNumber                  | Gets or sets the initial endnote number.                                                                                                                                      |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| InitialFootnoteNumber                 | Gets or sets the initial footnote number.                                                                                                                                     |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LastParagraph                         | Gets last section object.                                                                                                                                                     |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LastSection                           | Gets last section of the document.                                                                                                                                            |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ListStyles                            | Gets document list styles.                                                                                                                                                    |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MailMerge                             | Gets mail merge engine.                                                                                                                                                       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ProtectionType                        | Gets or sets the type of protection of the document.                                                                                                                          |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RestartIndexForEndnote                | Gets or sets the restart index for endnote.                                                                                                                                   |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RestartIndexForFootnotes              | Gets or sets the restart index for footnotes.                                                                                                                                 |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sections                              | Gets document sections.                                                                                                                                                       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Styles                                | Gets document styles.                                                                                                                                                         |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TextBoxes                             | Gets or sets textbox items of main document.                                                                                                                                  |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ThrowExceptionsForUnsupportedElements | Gets or sets whether to throw exceptions for unsupported elements.                                                                                                            |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ViewSetup                             | Gets view setup options in MSWord.                                                                                                                                            |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Watermark                             | Gets or sets document\'s watermark.                                                                                                                                           |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FontSubtitutionTable                  | Gets or sets a dictionary object which represents the font substitution table. The key should be the font name and the value should be its corresponding alternate font name. |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HasMacros                             | Determines whether the document has Macros.                                                                                                                                   |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AttachedTemplate                      | Gets the attached template.                                                                                                                                                   |
|                                       |                                                                                                                                                                               |
|                                       |                                                                                                                                                                               |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UpdateStylesOnOpen                    | Gets or sets a value indicating whether to automatically update the styles of a document from the attached template each time the document is opened.                         |
|                                       |                                                                                                                                                                               |
|                                       |                                                                                                                                                                               |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Public Constructors

 


+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Name                                                   | Description                                                                                                             |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument ()                           | Initializes a new instance of the WordDocument class.                                                                   |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (Stream)                     | Initializes a new instance of the WordDocument class from the stream.                                                   |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (Stream, FormatType, string) | Initializes a new instance of the WordDocument class from the stream of specified type, protected with password.        |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (Stream, string)             | Initializes a new instance of the WordDocument class from the Word document's stream, which is protected with password. |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (string)                     | Initializes a new instance of the WordDocument class from Word document.                                                |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (string, FormatType, string) | Initializes a new instance of the WordDocument class from existing file of specified type protected with password.      |
|                                                        |                                                                                                                         |
|                                                        |                                                                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WordDocument.WordDocument (string, string)             | Initializes a new instance of the WordDocument class from existing Word document, which is protected with password.     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+


 

Public Methods

 


  ------------------------ --------------------------------------------------------------------------------------
  Name                     Description
  AddListStyle             Adds new list style to document.  
  AddParagraphStyle        Adds new paragraph style to the document.  
  AddSection               Adds new section to document.  
  Clone                    Clones itself.  
  CreateParagraph          Creates the paragraph.  
  CreateParagraphItem      Creates new paragraph item instance.  
  EnsureMinimal            Adds one empty section to the document and one empty paragraph to created section.  
  Find                     Finds the first entry of specified string.
  FindAll                  Finds all entries of specified string.
  GetText                  Gets the document\'s text.  
  ImportContent            Imports all content into document.  
  ImportSection            Imports section into document.  
  Open                     Opens doc file.
  OpenTxt                  Opens the document in text format.  
  OpenXml                  Opens the document in xml format.
  Replace                  Replaces all entries of given string.
  Save                     Saves WordDocument instance to the specified file format.
  OpenReadOnly             Open the document in ReadOnly mode.
  UpdateDocumentFields()   Updates the fields present in the document.
  RemoveMacros             Removes the macros in the document
  ------------------------ --------------------------------------------------------------------------------------


 

The following example illustrates how to use the Open and Save methods.

 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [//Open the Word document]                                             |
|                                                                                                                          |
| [WordDocument sourceDoc = [new] WordDocument();]                |
|                                                                                                                          |
| [sourceDoc.Open([\"SourceDocument.doc\"], FormatType.Doc);]   |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [//Create a new word document with one section and one paragraph]      |
|                                                                                                                          |
| [WordDocument doc = [new] WordDocument();]                      |
|                                                                                                                          |
| [doc.EnsureMinimal();]                                                               |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [//Clone the content of source document to the newly created document] |
|                                                                                                                          |
| [doc = sourceDoc.Clone();]                                                           |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [//Save the document as xml]                                           |
|                                                                                                                          |
| [doc.Save([\"Document.doc\"], FormatType.Doc);]               |
+--------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                       |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [\'Open the Word document]                                             |
|                                                                                                                          |
| [Dim sourceDoc As WordDocument = New WordDocument()]                   |
|                                                                                                                          |
| [sourceDoc.Open(\"SourceDocument.doc\", FormatType.Doc)]               |
|                                                                                                                          |
| []                                                                     |
|                                                                                                                          |
| [\'Create a new word document with one section and one paragraph]      |
|                                                                                                                          |
| [Dim doc As WordDocument = New WordDocument()]                         |
|                                                                                                                          |
| [doc.EnsureMinimal()]                                                  |
|                                                                                                                          |
| []                                                                     |
|                                                                                                                          |
| [\'Clone the content of source document to the newly created document] |
|                                                                                                                          |
| [doc = sourceDoc.Clone()]                                              |
|                                                                                                                          |
| []                                                                     |
|                                                                                                                          |
| [\'Save the document as xml]                                           |
|                                                                                                                          |
| [doc.Save(\"Document.doc\", FormatType.Doc)]                           |
|                                                                                                                          |
| []                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+

 

For More Information Refer:

 

, , []{.UGHyperlink}

[[]]{.UGHyperlink} 

[[]]{.UGHyperlink} 

 

More:

















