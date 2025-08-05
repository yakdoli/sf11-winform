---
title: filterexpression1.md
original_path: WinForms_Docs/99_Uncategorized/filterexpression1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Filter Expression {#filter-expression style="tab-stops: 0pt"}

This class encapsulates the information needed to define a filter. It contains the following properties.

+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 |                             |                |
| Property Name | Description                                                                         | Type            | Value it Accepts            | Reference link |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 |                             |                |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
| CaseSensitive | Gets or sets whether the expression should be treated in a case sensitive manner.   | bool            | True or False               | \-             |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
| Error         | Gets the last error that was logged during the compilation and calculation phases.  | ExpressionError | CannotCompareDifferentTypes | \-             |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | ExceptionRaised             |                |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | MismatchedParentheses       |                |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | MissingRightQuote           |                |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | None                        |                |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | NotAValidFormula            |                |
|               |                                                                                     |                 |                             |                |
|               |                                                                                     |                 | UnknownOperator             |                |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
| ErrorString   | Gets a descriptive string for the last error raised.                                | string          | \-                          | \-             |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
| Expression    | Gets or sets the well-formed logical expression that defines this FilterExpression. | string          | \-                          | \-             |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+
| Name          | Gets or sets the name of this FilterExpression.                                     | string          | \-                          | \-             |
+---------------+-------------------------------------------------------------------------------------+-----------------+-----------------------------+----------------+

[]{#related-topics}

