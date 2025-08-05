---
title: documentexplorer1.md
original_path: WinForms_Docs/99_Uncategorized/documentexplorer1.md
created_at: 2025-08-05
---








  









## Document Explorer {#document-explorer style="tab-stops: 0pt"}

We have also provided a command line tool called **NETDepends.exe** that can take any assembly and dump a list of its dependencies. It comes with a help file, netdepends.htm and is included for download along with this article. You can use this tool to verify that all your non-system file dependencies are accounted for.

 

Document Explorer Utility helps to view and modify existing Word documents that are generated using Essential DocIO and MS Word. The documents generated using the following MS Word versions are viewable:

[·      ]Word 97

[·      ]Word 2000

[·      ]Word 2002

[·      ]Word 2003

 

It also helps users to update the content of the Word document and save it using Essential DocIO.

***[]*** 

Requirements

This utility requires Essential DocIO windows version installed in the machine to run.

Dependent Assemblies (not earlier to v6.2.x.x) are:

[·      ]Syncfusion.Compression.Base

[·      ]Syncfusion.DocIO.Base

***[]*** 

Usage

[·      ]Document Viewer

To view a file, go to **File**-\>**Open** menu. The entire document is now open and available for reading in the **Document Viewer** Tab.

 

[·      ]Document Tree

The various elements of the document can be navigated using the Document tree. Each and every element available in the document can be viewed with the help of this tree and new elements such as sections, paragraphs and text could be added using the context menu of the corresponding parent element that appears on right-clicking.

 

[·      ]Document Log

Each and every change in the document content is recorded in the Document Log tab.

 

[·      ]Document Entities

The Document Entities show the content of the selected element in the document tree.

***[]*** 

How to update a document?

 

To update a document:

1.   Open the file using **File**-\>**Open** menu.

2.   Navigate to the document element to which the content is to be updated.

3.   Select the appropriate option from the context menu of the parent element. In case of appending a text, a small dialog box appears, which takes the text to be appended as the input.

 

Utility source is available in the following location:

***{Installed Drive}:\\Program Files\\Syncfusion\\Essential Studio\\versionnumber\\Utilities\\DocIO\\Document Explorer\\***

 

 

[]{#related-topics}

