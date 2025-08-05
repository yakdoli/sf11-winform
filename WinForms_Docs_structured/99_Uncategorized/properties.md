---
title: properties.md
original_path: WinForms_Docs/99_Uncategorized/properties.md
created_at: 2025-08-05
---






#### Properties {#properties style="tab-stops: 0pt"}

 

+-------------------------+----------------------------------------------------------+------------------+---------------------------------------------+------------------------------------------------------------------------------------------+
| Property                | Description                                              | Type of Property | Value it accepts                            | Dependencies                                                                             |
+-------------------------+----------------------------------------------------------+------------------+---------------------------------------------+------------------------------------------------------------------------------------------+
| AllowExpressionFilter   | Specifies if the Expression filter feature is enabled    | bool             | [·      ]True  | Depends on ShowFilterBar and                                                             |
|                         |                                                          |                  |                                             |                                                                                          |
|                         |                                                          |                  | [·      ]False | ShowFilterBarTextCell---                                                                 |
|                         |                                                          |                  |                                             |                                                                                          |
|                         |                                                          |                  |                                             | only if both these properties are enabled, the AllowExpressionFilter property is enabled |
+-------------------------+----------------------------------------------------------+------------------+---------------------------------------------+------------------------------------------------------------------------------------------+
| ShowFilterStatusMessage | Specifies if the Filter status message is enabled or not | bool             | [·      ]True  | Depends on                                                                               |
|                         |                                                          |                  |                                             |                                                                                          |
|                         |                                                          |                  | [·      ]False | ShowFilterStatusMessage---                                                               |
|                         |                                                          |                  |                                             |                                                                                          |
|                         |                                                          |                  |                                             | only if this property is enabled, ShowFilterStatusMessage is enabled.                    |
+-------------------------+----------------------------------------------------------+------------------+---------------------------------------------+------------------------------------------------------------------------------------------+
| FilterStatusBarWidth    | Specifies the width of the filter status bar             | int              | Any integer value                           | Depends on ShowFilterStatusMessage---                                                    |
|                         |                                                          |                  |                                             |                                                                                          |
|                         |                                                          |                  |                                             | Only if ShowFilterStatusMessage is enabled, FilterStatusBarWidth is enabled              |
+-------------------------+----------------------------------------------------------+------------------+---------------------------------------------+------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

