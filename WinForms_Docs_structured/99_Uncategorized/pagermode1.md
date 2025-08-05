---
title: pagermode1.md
original_path: WinForms_Docs/99_Uncategorized/pagermode1.md
created_at: 2025-08-05
---






##### [Pager Mode]{#PagerMode} {#pager-mode style="tab-stops: 0pt"}

This defines the type paging we are going to do with the OlapPager control. The PagerMode contains three different options. They are:

[·      ]Categorical (Column)

[·      ]Series (Row)

[·      ]Both

 

Categorical (Column)

This mode allows only categorical paging. That is, it displays only one pager within the control for categorical paging. The code snippet to set this is as follows:

 

  -----------------------------------------------------------------------------------------------------------------------------------------
  **[\[C#\]]**
  [this][.pager1.PagerMode = PagerMode.Categorical;]
  -----------------------------------------------------------------------------------------------------------------------------------------

 

  --------------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]]**
  [Me][.pager1.PagerMode = PagerMode.Categorical]
  --------------------------------------------------------------------------------------------------------------------------------------

 

Series (Row)

This mode allows only series paging. That is, it displays only one pager within the control for series paging. The code snippet to set this is as follows:

 

  ------------------------------------------------------------------------------------------------------------------------------------
  **[\[C#\]]**
  [this][.pager1.PagerMode = PagerMode.Series;]
  ------------------------------------------------------------------------------------------------------------------------------------

 

  ---------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]][]**
  [Me][.pager1.PagerMode = PagerMode.Series]
  ---------------------------------------------------------------------------------------------------------------------------------

[]{#_Appearance} 

Both

This mode displays two pagers in the control. One is for categorical (column) paging and another one is for series (row) paging. The code snippet to set this is as follows:

 

  ----------------------------------------------------------------------------------------------------------------------------------
  **[\[C#\]]**
  [this][.pager1.PagerMode = PagerMode.Both;]
  ----------------------------------------------------------------------------------------------------------------------------------

 

  -------------------------------------------------------------------------------------------------------------------------------
  **[\[VB\]]**
  [Me][.pager1.PagerMode = PagerMode.Both]
  -------------------------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

