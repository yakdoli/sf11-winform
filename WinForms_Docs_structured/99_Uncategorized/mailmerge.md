---
title: mailmerge.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\mailmerge.md
created_at: 2025-07-03
---








  









## [][]{#p80}Mail Merge {#mail-merge style="tab-stops: 0pt"}

 

The mail merge function allows you to fill a template document with data from the data source. It is represented by the **MailMerge** class. The following data source types are used in mail merge: String Arrays, DataTable, DataReader or DataView class objects. The template of the document is created by using the MergeFields of MS Word.

 

To perform Mail Merge

**[]** 

1.   Open the **Insert** menu, point to **Fields**, and then click **MergeField**.

 

{border="0"}

Figure 78: Field Dialog Box

 

2.   Provide the merge field name, and the text to be inserted before and after the field. Note that the merge field name should match the field name of the data source.

 

[]{#p81}{border="0"}

Figure 79[: Merge field name Provided]

 

 

Mail merge operations are performed by the **Execute** or **ExecuteGroup** methods. There are several overloads of these methods for different data sources.

 

**Execute**

 

[·      ]**void Execute(string\[ \] fieldNames, string\[ \] fieldValues)**: performs replacements of every merge field in the document, in which field name matches one of the values from fieldNames string array, with the corresponding value from fieldValues string array.

[·      ]**void Execute(DataTable table**): performs replacements of merge fields, in which field names match the table column names, with the corresponding values of table cell. These replacements are performed for every row contained in the table.

 

For example, consider you have a document containing a single page, with a MergeField on it, whose field name is \"Country\", with the words: \"is a beautiful country\". Also, you have a DataTable, \"Geography\", containing the following data.

 


  -------- --------------- -----------
  Column   Continent       Country
  1        Australia       Australia
  2        North America   USA
  3        Eurasia         France
  -------- --------------- -----------


 

After performing mail merge operations, you will have a document containing three pages with the following text.

 

**1 page**: Australia is a beautiful country.

**2 page**: USA is a beautiful country.

**3 page**: France is a beautiful country.

 

You can also use the **Next** field, if you want to display the values of some rows at the same place.

 

For example, if you want to enumerate all the countries contained in the table, you have to insert the Next field before every MergeField, with field name \"Country\" beginning with the second MergeField.

 

[·      ]**void Execute(DataRow row)**: works similarly to that with DataTable parameter for the only row

[·      ]**void Execute(DataView dataView)**: works similarly to that with DataTable parameter

[·      ]**void Execute(IDataReader dataReader)**: works similarly to that with DataTable parameter

 

ExecuteGroup

 

[·      ]**void ExecuteGroup(DataTable table)**: performs replacements of merge fields, in which field names match the table column names, with the corresponding values of table cell

 

These replacements are performed for every row contained in the table in the specified region. The region where the mail merge operations are to be performed must be marked by two MergeFields with the following names:

 

[·      ]**TableStart:TableName** -- for the entry point of the region

[·      ]**TableEnd:TableName** -- for the end point of the region

 

For example, consider you have a DataTable containing the same data as in previous example, and you want to get the document with following content:

 

Australia

USA

France

 

are beautiful countries.

 

You have to insert three MergeFields in the document with the following field names:

 

[·      ]**TableStart:Geography** -- marks the beginning of mail merge region

[·      ]**Country** -- will be replaced by values from table, \"Geography\"

[·      ]**TableEnd:Geography** -- marks the end of mail merge region

 

[·      ]**void ExecuteGroup(DataView dataView)**: works similarly to that with DataTable parameter

[·      ]**void ExecuteGroup(IDataReader dataReader)**: works similarly to that with DataTable parameter

 

Public Methods

 


  -------------------- -----------------------------------------------------------------
  Name                 Description
  Execute              Executes mail merge.
  ExecuteGroup         Executes mail merge for a group (region). 
  GetMergeFieldNames   Returns a collection of mergefield names found in the document.
  ExecuteNestedGroup   Executes nested mail merge for a group(Region or tables)
  -------------------- -----------------------------------------------------------------


 

The following example illustrates how to use the MailMerge class for different data sources.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [IWordDocument][ document = [new] [WordDocument]( [\"MailMergeDocument.doc\"] );]                                                             |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Mail merge operations with string arrays data sources]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [string][\[\] fieldNames = [new] [string]\[\]{ [\"Continent\"], [\"Country\"], [\"Region\"] };] |
|                                                                                                                                                                                                                                                                                                     |
| [string][\[\] fieldValues = [new] [string]\[\]{ [\"Eurasia\"], [\"Germany\"], [\"Bavaria\"] };] |
|                                                                                                                                                                                                                                                                                                     |
| [document.MailMerge.Execute( fieldNames, fieldValues );]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [// Mail merge operations with DataTable data source containing data from database.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [DataTable][ table = GetDataTable( [\"select \* from Geography\"] );]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [document.MailMerge.Execute( table );]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [// Mail merge operations with DataView data source, created basing on the DataTable]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [DataView][ dataView = [new] [DataView]( GetDataTable( [\"select \* from Geography \"] ) );]                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [dataView.Sort = [\"CountryName ASC\"];]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [document.MailMerge.Execute( dataView );]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [// Mail merge operations with DataReader data source]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [IDataReader][ dataReader = GetDataReader( [\"select \* from Geography \"] );]                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [document.MailMerge.Execute( dataReader );]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [dataReader.Close();]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [// Mail merge operations for the specified region]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [DataTable][ table = GetDataTable( [\"select \* from Employees\"] );]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [table.TableName = [\"Geography\"];]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [document.MailMerge.ExecuteGroup( table );]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [document.Save( [\"AfterMailMerge.doc\"] );]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [//or]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [document.Save([\"AfterMailMerge.docx\",FormatType.Docx]);]                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ document [As] IWordDocument = [New] WordDocument([\"MailMergeDocument.doc\"])]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\' Mail merge operations with string arrays data sources]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ fieldNames [As] [String]() = [New] [String]() {[\"Continent\"], [\"Country\"], [\"Region\"]}] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ fieldValues [As] [String]() = [New] [String]() {[\"Eurasia\"], [\"Germany\"], [\"Bavaria\"]}] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.MailMerge.Execute(fieldNames, fieldValues)]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\' Mail merge operations with DataTable data source containing data from database.]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ table [As] DataTable = GetDataTable([\"select \* from Geography\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.MailMerge.Execute(table)]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\' Mail merge operations with DataView data source, created basing on the DataTable]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ dataView [As] DataView = [New] DataView(GetDataTable([\"select \* from Geography \"]))]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [dataView.Sort = [\"CountryName ASC\"]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.MailMerge.Execute(dataView)]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\' Mail merge operations with DataReader data source]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ dataReader [As] IDataReader = GetDataReader([\"select \* from Geography \"])]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.MailMerge.Execute(dataReader)]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    |
| [dataReader.Close()]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\' Mail merge operations for the specified region]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ table [As] DataTable = GetDataTable([\"select \* from Employees\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    |
| [table.TableName = [\"Geography\"]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.MailMerge.ExecuteGroup(table)]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.Save([\"AfterMailMerge.doc\"])]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\'or]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [document.Save([\"AfterMailMerge.docx\",FormatType.Docx])]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

It is also possible to conditionally format the merge fields dynamically by using the **MergeField** events.

 

**See Also**

 

, ]{.UGHyperlink}

[]{#_Nested_Mail_Merge} 

 

More:









