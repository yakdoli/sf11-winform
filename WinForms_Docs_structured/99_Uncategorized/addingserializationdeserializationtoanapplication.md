---
title: addingserializationdeserializationtoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingserializationdeserializationtoanapplication.md
created_at: 2025-08-05
---






#### Adding Serialization/Deserialization[ ]to an Application {#adding-serializationdeserialization-to-an-application style="tab-stops: 0pt"}

**Serializing**

There are three methods of serialization/deserialization available in the GridTree control.

[·      ]XML string

[·      ]XML file

[·      ]XML stream

 

 **API Usage**

 

**Serializing as an XML String**

The following code illustrates how to serialize the GridTree control as an XML string.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [string][ result=][this][.treeGrid.InternalGrid.SerializeAsString();] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Serializing as an XML File**

The following code illustrates how to serialize the GridTree control as an XML file.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [this][.treeGrid.InternalGrid.Serialize(][\"newChanges.xml\"][);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Serializing as an XML Stream**

The following code illustrates how to serialize the GridTree control as an XML stream.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [TextWriter][ sw=][new][ ][StreamWriter][(][\"newChanges.xml\"][);]**[]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.treeGrid.InternalGrid.SerializeToStream(sw);]                                                                                                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Deserializing**

There are three methods to deserializing forms:

[·      ]XML string

[·      ]XML file

[·      ]XML stream

 

**API Usage**

 

**Deserialize from XML String**

The following code illustrates how to deserialize from an XML string*.*

+-------------------------------------------------------------------------------+
| **[\[C#\]]**                              |
|                                                                               |
| ```                                              |
|  //the result should be an XML string saved during the serialization process. |
| ```                                                                           |
|                                                                               |
| ```                                              |
| this.treeGrid.InternalGrid.DeserializeFromString(result);                     |
| ```                                                                           |
+-------------------------------------------------------------------------------+

 

**Deserialize from XML File**

The following code illustrates how to deserialize an XML file.

+------------------------------------------------------------------------------+
| **[\[C#\]]**                             |
|                                                                              |
| ```                                             |
| //newChanges.xml file should be the XML file saved during the serialization  |
| ```                                                                          |
|                                                                              |
| ```                                             |
| process.                                                                     |
| ```                                                                          |
|                                                                              |
| ```                                             |
| this.treeGrid.InternalGrid.Deserialize("newChanges.xml");                    |
| ```                                                                          |
+------------------------------------------------------------------------------+

 

**Deserialize from XML Stream**

The following code illustrates how to deserialize an XML stream.

+------------------------------------------------------------------------------+
| **[\[C#\]]**                             |
|                                                                              |
| ```                                             |
| //newChanges.txt file should be the text file saved during the serialization |
| ```                                                                          |
|                                                                              |
| ```                                             |
| process.                                                                     |
| ```                                                                          |
|                                                                              |
| ```                                             |
| TextReader sr = new StreamReader("newChanges.txt");                          |
| ```                                                                          |
|                                                                              |
| ```                                             |
| this.treeGrid.InternalGrid.DeserializeFromStream(sr);                        |
| ```                                                                          |
+------------------------------------------------------------------------------+

[]{#related-topics}

