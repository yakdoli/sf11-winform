---
title: serializationingriddatacontrol.md
original_path: WinForms_Docs/04_Controls/Grid/serializationingriddatacontrol.md
created_at: 2025-08-05
---






#### Serialization in GridDataControl {#serialization-in-griddatacontrol style="tab-stops: 0pt"}

[] 

GridDataControl state can be serialized in XML format.

All the properties that are exposed in GridDataTableProperties can be serilized.

Serializing

There are two methods to serialize forms:

[] 

[·      ]XML string

[·      ]XML file

 

API Usage

Serializing as an XML String

The following code illustrates how to serialize as an XML string.

*[]* 

+------------------------------------------------------------------------------------------------+
| [\[**C#\]**]                                 |
|                                                                                                |
| []                                                         |
|                                                                                                |
| [string result = this.dataGrid.Model.SerializeAsString();] |
+------------------------------------------------------------------------------------------------+

**[]** 

Serializing as an XML File

The following code illustrates how to serialize as an XML file.

*[]* 

+--------------------------------------------------------------------------------------+
| [\[**C#\]**]         |
|                                                                                      |
| []                                   |
|                                                                                      |
| [this.dataGrid.Model.Serialize(\"sample.xml\");] |
+--------------------------------------------------------------------------------------+

***[]*** 

De-serializing

There are two methods to serialize forms:

[·      ]XML string

[·      ]XML file

 

API Usage

De-serialize from XML String

The following code illustrates how to de-serialize from XML string.

*[]* 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [this.dataGrid.Model.DeserializeFromString (content); // the content should be an XML string saved during the serialization process.] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

 De-serialize from XML File

The following code illustrates how to de-serialize from an XML file.

*[]* 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [this.dataGrid.Model.Deserialize (\"sample.xml\"); // sample.xml file should be the XML file saved during the serialization process.] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p262} 

 

[]{#related-topics}

