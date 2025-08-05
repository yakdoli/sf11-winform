---
title: macroenableddocumentsupport.md
original_path: WinForms_Docs/99_Uncategorized/macroenableddocumentsupport.md
created_at: 2025-08-05
---








  









### Macro-enabled Document Support {#macro-enabled-document-support style="tab-stops: 0pt"}

 

A macro is a piece of Visual Basic (VB) programming code that is embedded in a word file to automate repetitive tasks. Essential DocIO provides support for manipulating Microsoft Word macro-enabled documents (\*.docm) and Microsoft Word macro-enabled templates (\*.dotm) of Word 2007 and Word 2010 formats.

 

Microsoft Word macro-enabled format files can be created with the following format type enumerations while saving the WordDocument object:

 

[·      ]Word2007Docm - Microsoft Word 2007 macro enabled document format.

[·      ]Word2007Dotm - Microsoft Word 2007 macro enabled template format.

[·      ]Word2010Docm - Microsoft Word 2010 macro enabled document format.

[·      ]Word2010Dotm - Microsoft Word 2010 macro enabled template format.

 


{border="0"}Note: The macros present in the input macro-enabled document will be preserved as it is in the output macro-enabled document. However, Essential DocIO does not have support to create or edit macro commands in the macro-enabled documents.


 

Use Case Scenario

 

Using this feature you can preserve the macros present in the input macro-enabled document during conversion to another macro-enabled document (\*.docm to \*.docm, \*.dotm to \*.dotm, \*.docm to \*.dotm, and vice versa). ****

 

The following code illustrates how to open and save a Word macro-enabled document.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| [WordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                                     |
| [//Opens the Word macro-enabled document.]                                                                                        |
|                                                                                                                                                                                     |
| [doc.Open([\"SourceDocument.docm\"], [FormatType].Automatic);]                                  |
|                                                                                                                                                                                     |
| [//Saves as the Word macro-enabled document.]                                                                                     |
|                                                                                                                                                                                     |
| [doc.Save([\"OutDocument.docm\"], [FormatType].Word2007Docm);]                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| [Dim][ doc [As] [New] WordDocument()] |
|                                                                                                                                                                      |
| ['Opens the Word macro-enabled document.]                                                                          |
|                                                                                                                                                                      |
| [doc.Open([\"SourceDocument.docm\"], [FormatType].Automatic)]                     |
|                                                                                                                                                                      |
| ['Saves as the Word macro-enabled document.]                                                                       |
|                                                                                                                                                                      |
| [doc.Save([\"OutDocument.docm\"], [FormatType].Word2007Docm)]                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code illustrates how to open a Word macro-enabled document and save it as macro free document.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| [WordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                                     |
| [//Opens the Word macro-enabled document.]                                                                                        |
|                                                                                                                                                                                     |
| [doc.Open([\"SourceDocument.docm\"], [FormatType].Automatic);]                                  |
|                                                                                                                                                                                     |
| [//Determines whether the document has Macros.][ ]                                            |
|                                                                                                                                                                                     |
| [if][ (doc.HasMacros)]                                                                         |
|                                                                                                                                                                                     |
| [{]                                                                                                                                             |
|                                                                                                                                                                                     |
| [    [//Removes the macro commands present in the macro-enabled document.]]                                               |
|                                                                                                                                                                                     |
| [    doc.RemoveMacros();]                                                                                                                       |
|                                                                                                                                                                                     |
| [}]                                                                                                                                             |
|                                                                                                                                                                                     |
| [//Saves as the macro free Word document.]                                                                                        |
|                                                                                                                                                                                     |
| [doc.Save([\"OutDocument.docx\"], [FormatType].Word2007);]                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| [Dim][ doc [As] [New] [WordDocument]()] |
|                                                                                                                                                                                                |
| ['Opens the Word macro-enabled document.]                                                                                                    |
|                                                                                                                                                                                                |
| [doc.Open([\"SourceDocument.docm\"], [FormatType].Automatic)]                                               |
|                                                                                                                                                                                                |
| ['Determines whether the document has Macros.]                                                                                               |
|                                                                                                                                                                                                |
| [If][ doc.HasMacros[ Then]]                                                          |
|                                                                                                                                                                                                |
| [    ]['Removes the macro commands present in the macro-enabled document.]                               |
|                                                                                                                                                                                                |
| [    ][doc.RemoveMacros()]                                                                                             |
|                                                                                                                                                                                                |
| [End][ [If]]                                                                         |
|                                                                                                                                                                                                |
| ['Saves as the macro free Word document.]                                                                                                    |
|                                                                                                                                                                                                |
| [doc.Save([\"OutDocument.docx\"], [FormatType].Word2007)]                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: Now macros will not be cloned/imported to the destination macro-enabled document while cloning/importing a macro-enabled document. If the macros are present in the destination macro-enabled document, then it will be preserved as it is in the macro-enabled document.


 

Samples Link

 

To view samples:

 

1.   Open the Syncfusion's Dashboard.

2.   Select **Reporting** Edition, and then click **ASP.NET.**


{border="0"}Note: You can select required platform under Reporting Edition.


3.   Click **Run Samples,** and then click **DocIo** at the bottom.

4.   Navigate to **View** \> **Macro Preservation**.

 

[]{#related-topics}

