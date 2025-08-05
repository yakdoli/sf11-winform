---
title: oleobjects.md
original_path: WinForms_Docs/99_Uncategorized/oleobjects.md
created_at: 2025-08-05
---








  









### OLE Objects {#ole-objects style="tab-stops: 0pt"}

**[]** 

Object Linking and Embedding (OLE) is one of the best known ways of inserting data into Microsoft Office documents. Though embedding or linking objects increase the size of the original document, they help improve the document readability by providing offline reading of documents (where the existing online links can be replaced). In order to read the content of the object, you may need the associated software to be installed in the machine. For example, a PDF file linked or embedded to an Excel file needs Adobe Reader in order to launch and read the PDF file.

[] 

Essential XlsIO supports read and write of OLE Objects in XLSX file format. Objects can either be linked or embedded in the Excel documents using **IOleObject** interface.

[] 


{border="0"}Note: Currently read and write functions for OLE Objects are supported in Windows, ASP.NET and WPF platforms only[.]


 

This section lists the following topics:

 

List of Properties

 

The following table lists the properties available.

 


  Name of the Property   Type     Value Accepted        Description
  ---------------------- -------- --------------------- -----------------------------------------------------------------------------------------------------------------
  DisplayAsIcon          Normal   Boolean               Gets or sets value indicating whether to display the OLE object as icon.
  Location               Normal   IRange                Gets or sets the location of the OLE object in the sheet.
  Picture                Normal   Image                 Gets or sets the picture to display to represent the OLE object.
  Shape                  Normal   IPictureShape         Gets or sets picture shape object that defines look and position of the OLE Object inside the parent worksheet.
  Size                   Normal   System.Drawing.Size   Gets of sets the size of the OLE object.
  OleObjectType          Normal   OleObjectType         Gets or sets the value indicating the type of OLE object.


 

Displaying an Object as Icon

 

The following set of code snippet illustrates the condition when the property is set to True.

[] 

+---------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                                               |
| **[]**                                                    |
|                                                                                                               |
| [oleObject1.DisplayAsIcon = [true];] |
+---------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                         |
|                                                                                                              |
| **[]**                                                   |
|                                                                                                              |
| [oleObject1.DisplayAsIcon = [True]] |
+--------------------------------------------------------------------------------------------------------------+

 

Run the code. The following output is generated.

 

{border="0"}

Figure 100: Displayed as Icon[]

***[]*** 

Setting the Location of an Object

***[]*** 

The following set of code snippet illustrates the condition when the location is set to K column, 8th cell.

[] 

+--------------------------------------------------------------------------------------------+
| **[\[C#\]]**                           |
|                                                                                            |
| **[]**                                 |
|                                                                                            |
| [oleObject1.Location = sheet\["K8"\];] |
+--------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                    |
|                                                                                         |
| **[]**                              |
|                                                                                         |
| [oleObject1.Location = sheet("K8")] |
+-----------------------------------------------------------------------------------------+

[] 

Run the code. The following output is generated.

[] 

{border="0"}

Figure 101: Location[]

 

Setting an Image an Object

[] 

The following set of code snippet illustrates the condition when the property is set to any .png file image.

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                     |
| **[]**                                                                          |
|                                                                                                                                     |
| [oleObject1.Picture = [Image].FromFile(@"image.png\");] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [oleObject1.Picture = [Image].FromFile("image.png\")][.Picture = Image.FromFile("image.png\")] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the code. The following output is generated.

 

{border="0"}

Figure 102: Word Icon Image[]

***[]*** 

Setting Required Shape as an Object

***[]*** 

 

The following set of code snippet illustrates the condition when the property is set to any .png file image.

 

+-----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                              |
|                                                                                               |
| **[]**                                    |
|                                                                                               |
| [oleObject1.Shape = sheet.Pictures\[0\];] |
+-----------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                       |
|                                                                                            |
| **[]**                                 |
|                                                                                            |
| [oleObject1.Shape = sheet.Pictures(0)] |
+--------------------------------------------------------------------------------------------+

 

Run the code. The following output is generated.

 

{border="0"}

Figure 103: Word Icon Shape

 

Setting the Size of the Object

 

The following set of code snippet illustrates the condition when the property is set to (30,30).

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                                            |
| **[]**                                                                                 |
|                                                                                                                                            |
| [oleObject1.Size = [new][ Size](30, 30);] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                      |
|                                                                                                                                           |
| **[]**                                                                                |
|                                                                                                                                           |
| [oleObject1.Size = [New][ Size](30, 30)] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the code. The following output is generated.

 

{border="0"}

Figure 104: Size-Displayed Icon[]

***[]*** 

OLE Objects and Linking Types

 

XlsIO supports two types of association of objects:

[·      ]Objects can be linked to the program

[·      ]Objects can be embedded in the program

[] 

1\. Linked Objects

**[]** 

Linked objects remain as separate files. The linked object would expect the object to be in the same location as created, when the file is opened in another machine.

[] 

Linking an OLE Object to an Excel document

**[]** 

The following sample code illustrates how to linking an OLE Object to an Excel document.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| [Image][ image = [Image].FromFile([@\"..\\..\\image.png\"]);]                                        |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [// Select the object to insert, image for the display icon and the type of the OLEObject field.]                                                                                          |
|                                                                                                                                                                                                                                              |
| [IOleObject][ ole2 = sheet.OleObjects.Add([@\"..\\..\\Document.docx\"], image, [OleLinkType].Link);] |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Set the location]                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [ole2.Location = sheet\[5, 12\];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Set the size]                                                                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [ole2.Size = [new] [Size](30, 30);]                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [Dim][ image [As] Image = [Image].FromFile([\"..\\..\\image.png\"])]                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [\' Select the object to insert, image for the display icon and the type of the OLEObject field.]                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [Dim][ ole2 [As] IOleObject = sheet.OleObjects.Add([\"..\\..\\Document.docx\"], image, [OleLinkType].Link)] |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [\' Set the location]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [ole2.Location = sheet(5, 12)]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [\' Set the size]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [ole2.Size = [New] Size(30, 30)]                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the code. The following output is generated.

[] 

{border="0"}

Figure 105: Linked Object[]

[] 

1\. Embedded Objects 

**[]** 

Embedded objects are stored in the document. When the file is opened in another machine, the embedded object can be viewed without having access to the original data.

 

Embedding an OLE Object in an Excel document

 

The following sample code illustrates how to embed an OLE Object to an Excel document.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [Image][ image = [Image].FromFile([@\"..\\..\\image.png\"]);]                                     |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Select the object to insert, image for the display icon and the type of the OLEObject field.]                                                                                       |
|                                                                                                                                                                                                                                           |
| [IOleObject][ ole1 = sheet.OleObjects.Add([@\"..\\..\\Test.pptx\"], image, [OleLinkType].Embed);] |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the location]                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [ole1.Location = sheet\[5, 2\];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the size]                                                                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [ole1.Size = [new] [Size](30, 30);]                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [Dim][ image [As] Image = [Image].FromFile([\"..\\..\\image.png\"])]                                     |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [\' Select the object to insert, image for the display icon and the type of the OLEObject field.]                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Dim][ ole1 [As] IOleObject = sheet.OleObjects.Add([\"..\\..\\Test.pptx\"], image, [OleLinkType].Embed)] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [\' Set the location]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [ole1.Location = sheet(5, 2)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [\' Set the size]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [ole1.Size = [New] Size(30, 30)]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the code. The following output is generated.

 

{border="0"}

Figure 106: Embedded Object[]

[] 

Setting the Type of the OLE Object

The following code snippets illustrate the condition when the property is set to AdobeAcrobatDocument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [ole][Object1.][OleObjectType = [OleObjectType].AdobeAcrobatDocument;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [ole][Object1.][ OleObjectType = [OleObjectType].AdobeAcrobatDocument] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

