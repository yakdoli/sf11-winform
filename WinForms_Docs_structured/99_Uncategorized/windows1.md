---
title: windows1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\windows1.md
created_at: 2025-07-03
---








  









### Windows {#windows style="tab-stops: 0pt"}

 

Now, you have created a Windows application (refer ). This section covers information on the following:

 

[·      ]Deploying Essential DocIO in a Windows Application

[·      ]Creating a Word Document

 

Deploying Essential DocIO in a Windows Application

 

In order to deploy an application that uses the Syncfusion assemblies, the referenced Syncfusion assemblies should reside in the application folder where the exe file exists, in the target machine.

 

In order to do that, go to the Solution Explorer; Under References, select all the Syncfusion assemblies and then change the Copy Local property of the Syncfusion assemblies to true and compile the project.

[] 

Now, the Syncfusion assemblies referenced in the project will be copied to the output directory along with the application executable (bin/debug/).

 

Deploy the exe file along with the Syncfusion assemblies found, to the target machine. Be sure that these Syncfusion assemblies reside in the same location as the application exe file, in the target machine.

[] 

{border="0"}[]

Figure 16: DLLs to be referenced in the Application

 


{border="0"}Note: Application with Essential DocIO needs the following dependent assemblies for deployment.


[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.dll

[·      ]Syncfusion.DocIO.Base.dll

 


{border="0"}Note: For detailed documentation on Windows Application deployment, see [[http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf]{.UGHyperlink}](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf).


 

Essential DocIO is deployed in the Windows application.

 

Creating a Word Document

 

In this section, you will learn how to create a simple Word document with \"Hello World\" written on the first paragraph of the first section.

 

1.   Include the following namespaces in your application.

 

[·      ]**Syncfusion.DocIO.DLS** (using Syncfusion.DocIO.DLS)

[·      ]**Syncfusion.DocIO** (using Syncfusion.DocIO)

 

2.   Instantiate the **WordDocument** class.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [// Create a new Word document. ]                                                                                                      |
|                                                                                                                                                                                          |
| [// This document has no section and no paragraph by default.]                                                                         |
|                                                                                                                                                                                          |
| [WordDocument][ document = [new] [WordDocument]();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                               |
|                                                                                                                  |
| **[]**                                                         |
|                                                                                                                  |
| [\' Create a new Word document. ]                              |
|                                                                                                                  |
| [\' This document has no section and no paragraph by default.] |
|                                                                                                                  |
| [Dim document As WordDocument = New WordDocument()]                          |
+------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: The WordDocument class represents the Word documents created in memory. This is the memory representation of the Word document written to disk.


 

3.   Add a section to the newly created Word document by using the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                                        |
| []                                                                                   |
|                                                                                                                                        |
| [// Add a new section to the document.]                                              |
|                                                                                                                                        |
| [IWSection][ section = document.AddSection();] |
+----------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                        |
|                                                                                           |
| **[]**                                  |
|                                                                                           |
| [\' Add a new section to the document.] |
|                                                                                           |
| [Dim section As IWSection = document.AddSection()]    |
+-------------------------------------------------------------------------------------------+

 

4.   Add a paragraph to the newly created section in the Word document by using the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| **[]**                                                                                    |
|                                                                                                                                             |
| [// Add a new paragraph to the section.]                                                  |
|                                                                                                                                             |
| [IWParagraph][ paragraph = section.AddParagraph();] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                          |
|                                                                                             |
| **[]**                                    |
|                                                                                             |
| [\' Add a new paragraph to the section.]  |
|                                                                                             |
| [Dim paragraph As IWParagraph = section.AddParagraph()] |
+---------------------------------------------------------------------------------------------+

 

5.   Add a paragraph to the newly created section in the Word document by using the following code.

 

+---------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                          |
|                                                                                                         |
| **[]**                                                |
|                                                                                                         |
| [// Insert text into the paragraph.]                  |
|                                                                                                         |
| [paragraph.AppendText([\"Hello World!\"]);] |
+---------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                     |
|                                                                                        |
| []                                   |
|                                                                                        |
| [\' Insert text into the paragraph.] |
|                                                                                        |
| [paragraph.AppendText(\"Hello World!\")]           |
+----------------------------------------------------------------------------------------+

 

6.   Finally, save the Word document. The following code example illustrates how to do this.

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                                          |
| **[]**                                                                                 |
|                                                                                                                                          |
| [// Saving the document to disk.]                                                      |
|                                                                                                                                          |
| [document.Save([\"Sample.doc\"], [FormatType].Doc);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                  |
|                                                                                     |
| **[]**                            |
|                                                                                     |
| [\' Saving the document to disk.] |
|                                                                                     |
| [document.Save(\"Sample.doc\", FormatType.Doc)] |
+-------------------------------------------------------------------------------------+

 

7.   The sample Word document created through the above procedure is shown below.

 

{border="0"}

Figure 17: Word Document

 

A Word document is created in the Windows application.

[]{#related-topics}

