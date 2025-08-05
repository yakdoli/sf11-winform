---
title: bindingtoxmldata.md
original_path: WinForms_Docs/03_Data_Binding/bindingtoxmldata.md
created_at: 2025-08-05
---






##### Binding to XML Data {#binding-to-xml-data style="tab-stops: 0pt"}

[] 

Grid Grouping Control can be bound to data from XML files. To do this, a **DataSet** object is required which provides the necessary methods that will let you read the Xml data into the dataset. After loading the data, you can bind the grouping grid to this dataset by setting the data binding properties, the **DataSource** and the **DataMember** to the dataset and the table name respectively. It is also possible to save the changes back to the Xml file.

 

The following table lists some important methods provided by the dataset that allows you to manipulate Xml data. In this, the XmlSchema represents the type of the data stored in the Xml file.

[] 


  ---------------- --------------------------------------------------------------------------------------------------
  Method Name      Description
  ReadXml          Reads the Xml Schema and the data into the dataset using the specified Xml file.
  ReadXmlSchema    Reads the Xml Schema from the specified file into the dataset.
  WriteXml         Writes the current data, and optionally the schema, for the dataset into the specified Xml file.
  WriteXmlSchema   Writes the dataset structure as an Xml schema into the specified file.
  ---------------- --------------------------------------------------------------------------------------------------


[] 

The following code example illustrates the binding process.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                                               |
| [// Create a Data Set.]                                                                                                     |
|                                                                                                                                                                               |
| [DataSet][ XmlData = [new] [DataSet]();] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Populate it with data from an XML file.]                                                                                |
|                                                                                                                                                                               |
| [XmlData.ReadXml([\"C:\\\\Data\\\\Customers_Orders.xml\"]);]                                                      |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Bind the grid to the Data Set.]                                                                                         |
|                                                                                                                                                                               |
| [gridGroupingControl1.DataSource = XmlData;]                                                                                              |
|                                                                                                                                                                               |
| [gridGroupingControl1.DataMember = XmlData.Tables\[0\];]                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [\' Create a Data Set.]                                                                                           |
|                                                                                                                                                                     |
| [Dim][ XmlData [As] [New] DataSet()] |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Populate it with data from an XML file]                                                                       |
|                                                                                                                                                                     |
| [XmlData.ReadXml([\"C:\\\\Data\\\\Customers_Orders.xml\"])]                                             |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Bind the grid to the Data Set.]                                                                               |
|                                                                                                                                                                     |
| [gridGroupingControl1.DataSource = XmlData]                                                                                     |
|                                                                                                                                                                     |
| [gridGroupingControl1.DataMember = XmlData.Tables(0)]                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p406} 

 

[]{#related-topics}

