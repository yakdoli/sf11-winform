---
title: introductiontoessentialgrouping.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\introductiontoessentialgrouping.md
created_at: 2025-07-03
---








  









## Introduction to Essential Grouping {#introduction-to-essential-grouping style="tab-stops: 0pt"}

[] 

Essential Grouping is a 100% Native .NET library that provides you with support for managing and manipulating tabular information without dependencies on any particular UI component. Our grouping framework can be used in any .NET environment, including C#, VB.NET, and managed C++.

 

Syncfusion Essential Grouping is a data technology that allows you to easily access, manipulate, and display your data in a variety of configurations. Your data source can be any IList object whose items have public properties. You can easily sort the items on one or several of these public properties. You can display and retrieve items based on the grouping that is produced through these sorts, you can include caption information and / or summary information on these groups; you can impose filters on the items, retrieving only items that specify your filter conditions and you can also add expression properties to display calculated values depending upon other properties in the item.

[] 



Figure 1: Grouping in Data Grid

[] 

Key Features

[] 

Some of the key features of Essential Grouping are listed below:

[] 

[·      ]Grouping supports data presentation techniques like sorting, grouping, adding caption and summary information for the groups.

[·      ]Grouping also supports nested tables and hierarchies in the form of related tables.

[·      ]The grouping technology uses balanced binary trees as the core data structure instead of arrays. Binary trees have this advantage whereby parent branches can cache information about their children. This allows position information and summary information to be cached in parent branches facilitating quick inserts of new records honoring any sort of criteria that is applied. Inserting, removing, and moving of records takes \\ only Log2(n) operations. With linear lookup structures such as an ArrayList, each of these operations would take O(n) operations.

[·      ]Expressions can be any well-formed algebraic combination of property (column) names enclosed with brackets (\[\]), numerical constants and literals, and the algebraic and logical operators.

[·      ]Grouping is a recursive process whereby a data source may be grouped several times. This leads to the recursive situation of groups having sub-groups and so on.

[] 

User Guide Organization

[] 

The product comes with numerous samples as well as an extensive documentation to guide you. This User Guide provides detailed information on the features and functionalities of Essential Grouping. It is organized into the following sections:

[] 

[·      ]**Overview**-This section gives a brief introduction to our product and its key features.

[·      ]**Installation and Deployment**-This section elaborates on the install location of the samples, license etc.

[·      ]**Getting Started**-This section guides you on getting started with various platform application, controls etc.

[·      ]**Concepts and Features**-The features of Essential Grouping is illustrated with use case scenarios, code examples and screen shots under this section.

[·      ]**Frequently Asked Questions**-This section illustrates the solutions for various task-based queries about Grouping.

**[]** 

Document Conventions

**[]** 

The conventions listed below will help you to quickly identify the important sections of information, while using the content:

[] 

Table 1: Document Conventions


  ------------------------ ----------------------------------------- ---------------------------------------------------------------------------
  Convention               Icon                                      Description
  Note                     ***Note:***   Represents important information
  Example                  **Example**                               Represents an example
  Tip                                    Represents useful hints that will help you in using the controls/features
  Additional Information                 Represents additional information on the topic
  ------------------------ ----------------------------------------- ---------------------------------------------------------------------------


 

 

 

[]{#related-topics}

