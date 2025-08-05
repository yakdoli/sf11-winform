---
title: differencebetweenattributehierarchyanduserdefinedhierarchy.md
original_path: WinForms_Docs/99_Uncategorized/differencebetweenattributehierarchyanduserdefinedhierarchy.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Difference between Attribute Hierarchy and User-Defined Hierarchy {#difference-between-attribute-hierarchy-and-user-defined-hierarchy style="tab-stops: 0pt"}

 

Attribute Hierarchy:

[·      ]An attribute hierarchy is a hierarchy  of attribute members that contains the following levels:

[·      ]A leaf level that contains each distinct attribute member, with each member of the leaf level also known as a leaf member.

[·      ]Intermediate levels if the attribute hierarchy is a parent-child hierarchy.

[·      ]An optional (All) level (IsAggreagatable = True) containing the aggregated value of the attribute hierarchy's members, with the member of the (All) level also known as the (All) member.

***[]***  

User-Defined Hierarchy:

 

User-Defined hierarchy organizes the members of a dimension into hierarchical structures and provides navigation paths in a cube. For example, take a dimension table that supports three attributes, named Year, Quarter and Months. The Year, Quarter and Month attributes are used to construct a User-Defined hierarchy, named Calendar in the time dimension.

[]{#related-topics}

