---
title: thedroplists.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\thedroplists.md
created_at: 2025-07-03
---






#### The DropLists {#the-droplists style="tab-stops: 0pt"}

[] 

The second type of data required of the ScheduleControl is the **DropList** data. You have seen a concrete implementation of providing this DropList data in the [The Appointments Data] discussion. Two classes that can provide such data are listed below.

[] 

[·      ]**ListObjectClass**

The **ListObject** is a wrapper class for list choices that can have a ValueMember, DisplayMember and ColorMember associated with them. The class is an implementation of the **IListObject** that exposes the IListObject functionality as virtual members. This allows you to implement the IListObject by deriving the ListObject and overriding virtual properties. Here are the properties exposed by this class.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [///][ An integer that is stored in the data objects to represent this object.] |
|                                                                                                                                                                                    |
| [public][ [virtual] [int] ValueMember]              |
|                                                                                                                                                                                    |
| [                ]                                                                                                                             |
|                                                                                                                                                                                    |
| [///][ A string that is used when this object is displayed.]                    |
|                                                                                                                                                                                    |
| [public][ [virtual] [string] DisplayMember]         |
|                                                                                                                                                                                    |
| [                ]                                                                                                                             |
|                                                                                                                                                                                    |
| [///][ A color associated with this object.]                                    |
|                                                                                                                                                                                    |
| [public][ [virtual] [Color] ColorMember]            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ListObjectList**

The **ListObjectList** is a strongly-typed ArrayList that holds a collection of ListObjects. The class is derived from ArrayList and implements both **ITypedList** and **IlistListObjectList**. Here are the properties and methods exposed in this class.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [///][ Returns the property descriptors for each property in ListObject.][\</returns\>] |
|                                                                                                                                                                                                                                             |
| [public][ [PropertyDescriptorCollection] GetItemProperties(PropertyDescriptor\[\] listAccessors)]                                 |
|                                                                                                                                                                                                                                             |
| [               ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [///][ Returns a list name][\</returns\>]                                               |
|                                                                                                                                                                                                                                             |
| [public][ [string] GetListName(PropertyDescriptor\[\] listAccessors)]                                                             |
|                                                                                                                                                                                                                                             |
| [                ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the i-th item in the list.]                                                                                          |
|                                                                                                                                                                                                                                             |
| [public][ [new] [ILookUpObject] [this]\[[int] i\]]                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p18}[] 

[]{#related-topics}

