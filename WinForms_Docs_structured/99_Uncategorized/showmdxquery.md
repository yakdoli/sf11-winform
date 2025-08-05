---
title: showmdxquery.md
original_path: WinForms_Docs/99_Uncategorized/showmdxquery.md
created_at: 2025-08-05
---








  









## Show MDX query {#show-mdx-query style="tab-stops: 0pt"}

 

The MDX query of a report, which is used by the UI for displaying data in Grid/Chart control, can be retrieved by the user through MDX button located in the OlapClient Toolbar.

This feature performs the following:

[·      ]When the MDX (Analysis Service MDX Query) Query button that is available in the OlapClient Toolbar (as shown in the below image) is clicked, it will display the MDX (Multi-dimensional expression) query for the current report generated in the OlapGrid/OlapChart through a separate dialog box.

 

The following image shows the MDX Query button located in the OlapClient Toolbar:

{border="0"}

Figure 38OlapClient Toolbar with MDX Query button

The following screen shot shows the dialog box which displays the MDX Query:

{border="0"}

Figure 39MDX Query Dialog with Sample MDX Query

 

 

Use Case Scenarios

This feature is mainly used to view the current state of a report using the MDX query.

 

Tables for Properties, Methods, and Events

 

Methods

  Method    Description                                                        Parameters   Type    Return Type   Reference links
  --------- ------------------------------------------------------------------ ------------ ------- ------------- -----------------
  ShowMdx   Shows the MDX query based on the current report of an OlapClient   \-           **-**   Void          \-

 

More:





