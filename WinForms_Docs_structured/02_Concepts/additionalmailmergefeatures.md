---
title: additionalmailmergefeatures.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\additionalmailmergefeatures.md
created_at: 2025-07-03
---








  









### Additional Mail Merge Features {#additional-mail-merge-features style="tab-stops: 0pt"}

 

Using Mapped Fields

 

The MailMerge class allows to automatically map between names of fields in your data source and names of mail merge fields in the document. To perform this, use the **MailMerge.MappedDataFields** property that returns a MappedDataFields object. MappedDataFields is a collection of string keys into string values. The keys are the names of mail merge fields in the document and the values are the names of fields in your data source. The class provides all properties and methods typical for a regular .NET collection such as Add, Clear, Remove, and so on.

 

The following example illustrates how to add a mapping when a merge field in a document and a data field in a data source have different names.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                     |
|                                                                                                                                                                                     |
| **[]**                                                                                                                            |
|                                                                                                                                                                                     |
| [doc.MailMerge.MappedDataFields.Add([\"FieldName_InDocument\"], [\"FieldName_InDataSource\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                  |
|                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                  |
| [doc.MailMerge.MappedDataFields.Add([\"FieldName_InDocument\"], [\"FieldName_InDataSource\"])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Obtaining Merge Field Names**

 

You can get the collection of the merge field names available in the document by using the **MailMerge.GetFieldNames** method. This returns an array of string that contains the names.

 

The following example illustrates how to get the names of all the merge fields in a document.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                      |
|                                                                                                                                                      |
|                                                                                                                                                      |
|                                                                                                                                                      |
| [string][\[\] fieldNames = doc.MailMerge.GetMergeFieldNames();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [Dim][ fieldNames [As] [String]() = doc.MailMerge.GetMergeFieldNames()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Obtaining Merge Field Group Names**

 

You can get the collection of the Merge Field Group names available in the document by using the **MailMerge.GetMergeGroupNames** method. This returns an array of string that contains the names.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                       |
|                                                                                                                                                       |
| **[]**                                                                                              |
|                                                                                                                                                       |
| [string][\[\] groupNames =  doc.MailMerge.GetMergeGroupNames() ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [Dim][ filednames [As] [String]() = doc.MailMerge.GetMergeFieldNames(groupName)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Obtaining Merge Fields for a Specific Group**

 

You can get the collection of the Merge Fields for a specific group in the document by using the **doc.MailMerge.GetMergeFieldNames(String groupName)** method. This returns an array of string that contains the field names.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                               |
|                                                                                                                                                               |
|                                                                                                                                                               |
|                                                                                                                                                               |
| [string][\[\] filednames = doc.MailMerge.GetMergeFieldNames(groupName);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [Dim][ filednames [As] [String]() = doc.MailMerge.GetMergeFieldNames(groupName)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Removing Empty Paragraphs

 

To remove paragraphs that contain empty mail merge fields from the document, set the **doc.MailMerge.RemoveEmptyParagraphs** to **True**.

 

The following example illustrates how to remove paragraphs that contain empty mail merge fields.

 

+----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                           |
|                                                                                                          |
|                                                                                                          |
|                                                                                                          |
| [doc.MailMerge.RemoveEmptyParagraphs = [true];] |
+----------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                          |
|                                                                                                         |
|                                                                                                         |
|                                                                                                         |
| [doc.MailMerge.RemoveEmptyParagraphs = [True]] |
+---------------------------------------------------------------------------------------------------------+

 

Removing Empty Groups

 

To remove empty groups from the document during mail merge, set the **document.MailMerge.RemoveEmptyGroup** to **True**. The default value of RemoveEmptyGroup is false.

 

The following example illustrates how to remove empty groups from the document.

[] 

+----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                           |
|                                                                                                          |
|                                                                                                          |
|                                                                                                          |
| [document.MailMerge.RemoveEmptyGroup = [true];] |
+----------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                          |
|                                                                                                         |
|                                                                                                         |
|                                                                                                         |
| [document.MailMerge.RemoveEmptyGroup = [True]] |
+---------------------------------------------------------------------------------------------------------+

 

Clear Fields

 

To remove empty mail merge fields from the document, set **MailMerge.ClearField** property to **True**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [WordDocument][ doc = [new] [WordDocument]([\"Sample.doc\"]);] |
|                                                                                                                                                                                                                      |
| [string][\[\] fieldname ={ [\"FirstName\"], [\"LastName\"] };]                    |
|                                                                                                                                                                                                                      |
| [string][\[\] fieldvalues ={ [\"John\"], [\"David\"] ,};]                         |
|                                                                                                                                                                                                                      |
| [doc.MailMerge.ClearFields = [false];]                                                                                                                      |
|                                                                                                                                                                                                                      |
| [doc.MailMerge.Execute(fieldname, fieldvalues);]                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [Dim][ doc [As] WordDocument = [New] WordDocument([\"Sample.doc\"])] |
|                                                                                                                                                                                                                            |
| [Dim fieldname As String() = {\"FirstName\", \"LastName\"}]                                                                                                                            |
|                                                                                                                                                                                                                            |
| [Dim fieldvalues As String() = {\"John\", \"David\"}]                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [doc.MailMerge.ClearFields = [false]]                                                                                                                             |
|                                                                                                                                                                                                                            |
| [doc.MailMerge.Execute(fieldname, fieldvalues)]                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p84}[]{#_Security} 

[]{#related-topics}

