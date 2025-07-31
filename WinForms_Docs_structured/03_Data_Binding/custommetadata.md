---
title: custommetadata.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\custommetadata.md
created_at: 2025-07-03
---






#### Custom Metadata {#custom-metadata style="tab-stops: 0pt"}

[] 

Essential PDF allows you to add required metadata (custom metadata) to a PDF document. Custom metadata can be information about the document which cannot be fit in the predefined metadata fields. For example: If a metadata field "Link" is available, you can only provide a link there.  But, Essential PDF allows you to add additional information like Author, date of creation etc. about the link.

This feature allows you to add as many metadata fields as you want. Only new metadata fields can be added. You cannot add metadata fields under the predefined metadata fields.

[] 

How to add a Custom Metadata Field

 

To add a custom metadata field,

 

[·      ]Add namespace in the project

[·      ]Create an XML document container

[·      ]Create a custom schema

[] 

Adding Namespace in the Project

 

[The user needs to add the namespace Syncfusion.Pdf.Xmp in the project to enable addition of custom metadata fields in the PDF document.  ]

[Add the namespace using the following code.]

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                    |
| []                                                               |
|                                                                                                                    |
| [using][ Syncfusion.Pdf.Xmp;] |
+--------------------------------------------------------------------------------------------------------------------+

[] 

Creating an XML Document Container

The custom metadata to be created has to be stored and linked to the PDF document in use. Here an XML document is used as a container to save the custom metadata fields for the PDF document.

Add the following code to create an XML document to store custom metadata fields.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [XmpMetadata][ xmp = [new] [XmpMetadata](pdfDoc.DocumentInformation.XmpMetadata.XmlData);] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following table provides more information on the code.

 


  ---------- ------------ ------------------
  Property   Type         Value It Accepts
  XmlData    XmlElement   XmlElement
  ---------- ------------ ------------------


 

Creating a Custom Schema

 

A custom schema defines the structure of the customized information records. You can use the customschema class to:

[·      ]Define custom metadata files; and,

[·      ]Add them to the PDF document

 

Add the following code to define a custom schema.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [//create a custom schema]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                               |
| [CustomSchema][ cs = [new] [CustomSchema](xmp,[\"custom\"],[\"http://www.syncfusion.com\"]);           ] |
|                                                                                                                                                                                                                                                                                               |
| [cs\[[\"Author\"]\] = [\"Syncfusion\"];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                               |
| [cs\[[\"creationDate\"]\] = [DateTime].Now.ToString();]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                               |
| [cs\[[\"DOCID\"]\] = [\"SYNCSAM001\"];]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The code snippet above, illustrates creation of custom schema or first-level metadata field *www.syncfusion.com*, which is a link. The second-level metadata fields under the link are Author, creation date and DocID.

On running the code, the values assigned to these fields are reflected as data on expanding the first-level metadata field as shown in the following screenshot.

 

{border="0"}

Figure 33: Custom Metadata Field

 

You have successfully created a custom metadata field in the PDF document.[]{#p65}

 

[]{#related-topics}

