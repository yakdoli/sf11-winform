---
title: thedroplists1.md
original_path: WinForms_Docs/99_Uncategorized/thedroplists1.md
created_at: 2025-08-05
---






#### The DropLists {#the-droplists style="tab-stops: 0pt"}

[] 

Two of the five data interfaces work directly with the **DropList** data. Here are the two interfaces.

[] 

[·      ]**ILookUpObject Interface**

**ILookUpObject** is part of the data support to provide the DropList data. This interface defines the object that may appear in a droplist.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [///][ Defines items that can be included in a ILookUpObjectList.]                    |
|                                                                                                                                                                                          |
| [///][ Choice lists within the ScheduleControl are used to provide possible ]         |
|                                                                                                                                                                                          |
| [///][ schedule item information like location or a reminder. ILookUpObject ]         |
|                                                                                                                                                                                          |
| [///][ allows such list items to have a ValueMember / DisplayMember associated with ] |
|                                                                                                                                                                                          |
| [///][ the choices as well as a color that will be used in drop-downs showing these]  |
|                                                                                                                                                                                          |
| [///][ lists. Value members are normally the values serialized to data stores.]       |
|                                                                                                                                                                                          |
| [public][ [interface] [ILookUpObject] ]                   |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [///][ The value member associated with this item.]                                   |
|                                                                                                                                                                                          |
| [int][ ValueMember {[get]; [set];}]                       |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [///][ The display member associated with this item.]                                 |
|                                                                                                                                                                                          |
| [string][ DisplayMember {[get]; [set];}]                  |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [///][ A color associated with this item.]                                            |
|                                                                                                                                                                                          |
| [Color][ ColorMember {[get]; [set];}]                     |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ILookUpObjectList** **Interface**

**ILookUpObjectList** is the wrapper for this list of objects that may appear in a droplist.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| [\                                                                                                                                                                                                                                                                                                                        |
| ][///][ Collection of ][\<see cref=\"ILookUpObject\"/\>][ items.] |
|                                                                                                                                                                                                                                                                                                                           |
| [public][ [interface] [ILookUpObjectList]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [///][ Indexer that returns a ILookUpObject object.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [ILookUpObject][ [this]\[[int] i\] {[get]; [set];}]                                                                                              |
|                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

