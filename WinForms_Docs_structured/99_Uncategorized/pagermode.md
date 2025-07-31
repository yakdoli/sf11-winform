---
title: pagermode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pagermode.md
created_at: 2025-07-03
---






#### [Pager Mode]{#PagerMode} {#pager-mode style="tab-stops: 0pt"}

This defines the type paging we are going to do with OlapPager control. The PagerMode contains the three different options:

[·      ]Both

[·      ]Categorical (Column)

[·      ]Series (Row)

 

**Both**

This mode displays two pagers in the control. One is for Categorical (Column) paging and another one is for Series (Row) paging. The code snippet to set this is as follows:

 

  ----------------------------------------------------------------------------------------------------------------------------------
  **[\[C#\]]**
  [this][.pager1.PagerMode = PagerMode.Both;]
  ----------------------------------------------------------------------------------------------------------------------------------

 

  -------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]]**
  [Me][.pager1.PagerMode = PagerMode.Both]
  -------------------------------------------------------------------------------------------------------------------------------

 

**Categorical** **(Column)**

This mode allows only categorical paging. It displays only one pager within the control for categorical paging. The code snippet to set this is as follows:

 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                                         |
| [this][.pager1.PagerMode = PagerMode.Categorical;] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

 

  --------------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]]**
  [Me][.pager1.PagerMode = PagerMode.Categorical]
  --------------------------------------------------------------------------------------------------------------------------------------

 

**Series (Row)**

This mode allows only Series paging. It displays only one pager within the control for series paging. The code snippet to set this is as follows:

 

  ------------------------------------------------------------------------------------------------------------------------------------
  **[\[C#\]]**
  [this][.pager1.PagerMode = PagerMode.Series;]
  ------------------------------------------------------------------------------------------------------------------------------------

 

  ---------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]]**[]
  [Me][.pager1.PagerMode = PagerMode.Series]
  ---------------------------------------------------------------------------------------------------------------------------------

[]{#_Appearance} 

[]{#related-topics}

