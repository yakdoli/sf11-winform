---
title: howtoserializethecustompropertyofanode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoserializethecustompropertyofanode.md
created_at: 2025-07-03
---








  









## How To Serialize the Custom Property Of a Node {#how-to-serialize-the-custom-property-of-a-node style="tab-stops: 0pt"}

[] 

Essential Diagram supports custom serialization. To serialize the custom property, you should derive the **Group** class and create a custom node. After creating a custom node, you should override the **GetObjectData()** method and add the custom property in the SerializationInfo. This is illustrated in the below code snippet.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [\[[Serializable]()\]]                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [public][ [class] [CustomNode] : [Group]]                                  |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [protected][ CustomNode(SerializationInfo info, StreamingContext context) : [base](info, context)]                   |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [this][.m_nodeInformation = info.GetString([\"strDescription\"]);]                                                 |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [protected][ [override] [void] GetObjectData(SerializationInfo info, StreamingContext context)] |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [base][.GetObjectData(info, context);]                                                                                                    |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Additional member variables are serialized here.]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [info.AddValue([\"strDescription\"], [this].NodeInformation);]                                                                                 |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                              |
| [\<Serializable()\>]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Class] CustomNode]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [Inherits][ Group]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Sub] [New]()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] [New]([ByVal] info [As] SerializationInfo, [ByVal] context [As] StreamingContext)]                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [MyBase][.New(info, context)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| [Me][.m_nodeInformation = info.GetString([\"strDescription\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Overrides] [Sub] GetObjectData([ByVal] info [As] SerializationInfo, [ByVal] context [As] StreamingContext)] |
|                                                                                                                                                                                                                                                                                                                                              |
| [MyBase][.GetObjectData(info, context)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                              |
| [\' Additional member variables are serialized here.]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [info.AddValue([\"strDescription\"], [Me].NodeInformation)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Class]]                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p95} 

 

[]{#related-topics}

