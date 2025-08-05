---
title: settingupforeignkeyrelations.md
original_path: WinForms_Docs/99_Uncategorized/settingupforeignkeyrelations.md
created_at: 2025-08-05
---








  









### Setting up Foreign Key Relations {#setting-up-foreign-key-relations style="tab-stops: 0pt"}

[] 

**GridForeignKeyHelper** class is used to set up foreign key relations to perform foreign key look ups. With this class, you can easily set up a foreign table with a single method call instead of implementing numerous steps.

 

The following code example illustrates how to use this class.

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [GridForeignKeyHelper][.SetupForeignTableLookUp(gridGroupingControl1, [\"Country\"], countries, [\"CountryCode\"], [\"CountryName\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [GridForeignKeyHelper.SetupForeignTableLookUp(gridGroupingControl1, [\"Country\"], countries, [\"CountryCode\"], [\"CountryName\"])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 


{border="0"}Note:

The first argument in this method is an instance of the Grid Grouping control.

The second argument is the column name of the Parent table\'s Value Member.

The third argument is the name of the Foreign table.

The fourth argument is the column name of the Child table\'s Value Member.

The fifth argument is the column name of the Child tables\'s Display Member.


 

The following screen shot illustrates Foreign Key Relations in the Grid Grouping control.

[] 

{border="0"}

***[]*** 

*[Figure ][447][: Grid Grouping control with Foreign Key Relations]*

 

[]{#p534} 

 

[]{#related-topics}

