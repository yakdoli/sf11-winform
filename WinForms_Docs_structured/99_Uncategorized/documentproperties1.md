---
title: documentproperties1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\documentproperties1.md
created_at: 2025-07-03
---








  









### Document Properties {#document-properties style="tab-stops: 0pt"}

**[]** 

Document Properties are named values that provide information about the document, such as the date and time at which the document was last saved, the last user to modify the document, and so on. Document Properties are either built into the document, or are custom user-defined properties.

[] 

You can read, and manually add or modify some Built-In properties, and all Custom properties, by selecting the properties from the **File** menu. Built-in properties can be automatically updated properties such as **LastSaveDate**, or preset properties such as **Keywords**.

[] 

XlsIO allows to read and write Built-In and Custom properties through the **IBuiltinDocumentProperties** and **ICustomDocumentProperties**.

[] 

The following code example illustrates how to set the spreadsheet\'s Built-In and Custom properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [// Setting Built-in Document Properties.     ]                                                                                 |
|                                                                                                                                                                                   |
| [IBuiltInDocumentProperties][ builtInProperites = book.BuiltInDocumentProperties;]           |
|                                                                                                                                                                                   |
| [builtInProperites.Author  =  [\"Essential XlsIO\"];]                                                                  |
|                                                                                                                                                                                   |
| [builtInProperites.Comments = [\"This document was generated using Essential XlsIO\"];]                                |
|                                                                                                                                                                                   |
| [builtInProperites.ByteCount = 120;]                                                                                                          |
|                                                                                                                                                                                   |
| [builtInProperites.LastSaveDate = [new] [DateTime]( 1950, 1, 2, 3, 4, 5, 6 );]                      |
|                                                                                                                                                                                   |
| [builtInProperites.Manager = [\"Manager\"];]                                                                           |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [// Setting Custom Properties.]                                                                                                 |
|                                                                                                                                                                                   |
| [ICustomDocumentProperties][ customProperites = workbook.CustomDocumentProperties;]          |
|                                                                                                                                                                                   |
| [customProperites\[ [\"Author\"] \].Text = [\"\"]Essential XlsIO[\"\"];] |
|                                                                                                                                                                                   |
| [customProperites\[ [\"Comments\"] \].Text = [\"XlsIO support Custom document properties\"];]   |
|                                                                                                                                                                                   |
| [customProperites\[ [\"Double\"] \].Double = 120.2;  ]                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' Setting Built-in Document Properties.     ]                                                                                                     |
|                                                                                                                                                                                                       |
| [Dim][ builtInProperites [As] IBuiltInDocumentProperties = book.BuiltInDocumentProperties]  |
|                                                                                                                                                                                                       |
| [builtInProperites.Author = [\"Essential XlsIO\"]]                                                                                         |
|                                                                                                                                                                                                       |
| [builtInProperites.Comments  = [\"This document was generated using Essential XlsIO\"]]                                                    |
|                                                                                                                                                                                                       |
| [builtInProperites.ByteCount = 120]                                                                                                                               |
|                                                                                                                                                                                                       |
| [builtInProperites.LastSaveDate  = [New] DateTime(1950, 1, 2, 3, 4, 5, 6)]                                                                   |
|                                                                                                                                                                                                       |
| [builtInProperites.Manager = [\"Manager\"]]                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                 |
|                                                                                                                                                                                                       |
| [\' Setting Custom Properties.]                                                                                                                     |
|                                                                                                                                                                                                       |
| [Dim][ customProperites [As] ICustomDocumentProperties = workbook.CustomDocumentProperties] |
|                                                                                                                                                                                                       |
| [customProperites( [\"Author\"] ).Text = [\"Essential XlsIO\"]]                                                     |
|                                                                                                                                                                                                       |
| [customProperites( [\"Comments\"] ).Text = [\"XlsIO support Custom document properties\"]]                          |
|                                                                                                                                                                                                       |
| [customProperites( [\"Double\"] ).Double = 120.2]                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 153: XlsIO with Document Properties[]

[] 

 

[]{#related-topics}

