---
title: documentproperties.md
original_path: WinForms_Docs/99_Uncategorized/documentproperties.md
created_at: 2025-08-05
---








  









### Document Properties {#document-properties style="tab-stops: 0pt"}

 

Document Properties contain general information about the document like author of the document, subject, character count, word count, page count, creation date and so on.

 

To view or edit the document properties, go to the **File** menu and click **Properties**. The Document Properties dialog box will appear as follows.

 

{border="0"}

Figure 25: Document Properties Dialog Box

 

 

The Document Properties dialog box contains the following tabs.

 

[·      ]**General** (not editable): contains general document information such as file name, type, size, location, creation, modification and access date

[·      ]**Summary** (editable): set or modify the document properties such as author name, title, company, subject, keywords, and so on

[·      ]**Statistics** (not editable): displays the statistics of the document such as creation, modification, access and print dates, revision number, characters, words, pages number, and so on

[·      ]**Contents** (not editable): displays the content of the document

[·      ]**Custom** (editable): enables you to create your own properties combining their name, type and value. For example, you may want to mark some document as \"Checked\". You can do it by creating a custom property with the Name as \"Checked\", Type as \"Text\", and Value as \"your name\".

 

Built-in Properties

 

BuiltinDocumentProperties class represents all document properties, excluding custom properties.

 

Class Hierarchy

 

SummaryDocumentProperties

            \|

            BuiltinDocumentProperties

 

**Public Properties**

 


  ---------------- ----------------------------------------------------------
  Name             Description
  BytesCount       Represents the number of bytes in the document.  
  Category         Gets or sets the category of the document.  
  Company          Gets or sets Company property.  
  HiddenCount      Gets or sets hidden count.  
  LinesCount       Gets or sets the number of lines in the document.  
  Manager          Gets or sets Manager property.  
  NoteCount        Gets or sets Note count.
  ParagraphCount   Gets or sets the number of paragraphs in the document.  
  SlideCount       Gets or sets slide count.  
  ---------------- ----------------------------------------------------------


 

Public Methods

 


  ------- -----------------
  Name    Description
  Clone    Clones itself.
  ------- -----------------


 

The following example illustrates how to get, set and modify the document properties.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                                                      |
|                                                                                                                                                                               |
| [WordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                               |
| [doc.Open( [\"DocumentProperties.doc\"] );]                                                                        |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [string][ author = doc.BuiltinDocumentProperties.Author;]                                |
|                                                                                                                                                                               |
| [int][ bytesCount = doc.BuiltinDocumentProperties.BytesCount;]                           |
|                                                                                                                                                                               |
| [doc.BuiltinDocumentProperties.Keywords += [\"document properties\"];]                                             |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [doc.BuiltinDocumentProperties.Author = [\"Author\'s name\"];]                                                     |
|                                                                                                                                                                               |
| [doc.BuiltinDocumentProperties.Comments = [\"Document comments\"];]                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [Dim][ doc [As] WordDocument = [New] WordDocument()]                         |
|                                                                                                                                                                                                             |
| [doc.Open([\"DocumentProperties.doc\"])]                                                                                                         |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [Dim][ author [As] [String] = doc.BuiltinDocumentProperties.Author]          |
|                                                                                                                                                                                                             |
| [Dim][ bytesCount [As] [Integer] = doc.BuiltinDocumentProperties.BytesCount] |
|                                                                                                                                                                                                             |
| [doc.BuiltinDocumentProperties.Keywords &= [\"document properties\"]]                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                       |
|                                                                                                                                                                                                             |
| [doc.BuiltinDocumentProperties.Author = [\"Author\'s name\"]]                                                                                    |
|                                                                                                                                                                                                             |
| [doc.BuiltinDocumentProperties.Comments = [\"Document comments\"]]                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Custom Properties**

 

**CustomDocumentProperties** class enables you to create and save custom properties. It contains a collection of DocumentProperty class instances. You can access a document property by indexing, i.e., by specifying the property name or index.

 

{border="0"}

Figure 26: Custom Tab in Document Properties Dialog Box

 

 

Public Properties

 


  ------- -------------------------------
  Name    Description
  Count   Gets count of the properties.
  ------- -------------------------------


 

Public Methods

 


  -------- --------------------------------------
  Name     Description
  Add      Adds a new custom property.
  Clone    Clones itself.
  Remove   Remove property specified by name.  
  -------- --------------------------------------


 

DocumentProperty

 

**DocumentProperty** class represents each custom document property.

 

**Public Methods**

 


  ------------- -------------------------------
  Name          Description
  Clone         Clones itself.
  ToBool        Converts value to Boolean.
  ToByteArray   Converts value to byte array.
  ToDateTime    Converts value to DateTime.
  ToFloat       Converts value to float.
  ToInt         Converts value to integer.
  ToString      Converts value to string.
  ------------- -------------------------------


 

The following example illustrates how to get or set the existing custom document properties, and also how to add new custom document properties.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                    |
| [WordDocument][ doc = [new] [WordDocument]();]                      |
|                                                                                                                                                                                                    |
| [doc.Open( [\"DocumentProperties.doc\"] );]                                                                                             |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [// Getting custom property value]                                                                                                               |
|                                                                                                                                                                                                    |
| [int][ phoneNumber = doc.CustomDocumentProperties\[[\"Telephone number \"]\].ToInt();] |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [// Setting existent custom property value]                                                                                                      |
|                                                                                                                                                                                                    |
| [doc.CustomDocumentProperties\[[\"Check by\"]\].Value = [\"user name\"];]                                        |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [// Adding new custom property]                                                                                                                  |
|                                                                                                                                                                                                    |
| [DateTime][ completedDate = [DateTime].Now;]                                             |
|                                                                                                                                                                                                    |
| [doc.CustomDocumentProperties.Add( [\"Date completed\"], completedDate );]                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [Dim][ doc [As] WordDocument = [New] WordDocument()]                                                                      |
|                                                                                                                                                                                                                                                          |
| [doc.Open([\"DocumentProperties.doc\"])]                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\' Getting custom property value]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [Dim][ phoneNumber [As] [Integer] = doc.CustomDocumentProperties([\"Telephone number \"]).ToInt()] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\' Setting existent custom property value]                                                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [doc.CustomDocumentProperties([\"Check by\"]).Value = [\"user name\"]]                                                                                                 |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| [\' Adding new custom property]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [Dim][ completedDate [As] DateTime = DateTime.Now]                                                                                             |
|                                                                                                                                                                                                                                                          |
| [doc.CustomDocumentProperties.Add([\"Date completed\"], completedDate)]                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

