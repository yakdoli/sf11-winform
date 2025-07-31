---
title: customobjectinthecodebehind.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customobjectinthecodebehind.md
created_at: 2025-07-03
---






##### Custom object in the Code Behind {#custom-object-in-the-code-behind style="tab-stops: 0pt"}

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [        [///][ ][\<summary\>]]                                                                                   |
|                                                                                                                                                                                                                                         |
| [        [///][ Interaction logic for the class person]]                                                                               |
|                                                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                                  |
|                                                                                                                                                                                                                                         |
| [        [public] [class] [Person]]                                                                             |
|                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<summary\>]]                                                                               |
|                                                                                                                                                                                                                                         |
| [            [///][ Initializes a new instance of the ][\<see cref=\"Person\"/\>][ class.]] |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\</summary\>]]                                                                              |
|                                                                                                                                                                                                                                         |
| [            [public] Person()]                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                [this].Name = [\"Tres\"];]                                                                                          |
|                                                                                                                                                                                                                                         |
| [                [this].Age = 45;]                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [                [this].BackgroundBrush = [Brushes].Red;]                                                                            |
|                                                                                                                                                                                                                                         |
| [            }]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<summary\>]]                                                                               |
|                                                                                                                                                                                                                                         |
| [            [///][ Gets or sets the name.]]                                                                                           |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\</summary\>]]                                                                              |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<value\>][The name.][\</value\>]]               |
|                                                                                                                                                                                                                                         |
| [            [public] [string] Name]                                                                                                    |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                [get];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                [set];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [            }]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<summary\>]]                                                                               |
|                                                                                                                                                                                                                                         |
| [            [///][ Gets or sets the age.]]                                                                                            |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\</summary\>]]                                                                              |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<value\>][The age.][\</value\>]]                |
|                                                                                                                                                                                                                                         |
| [            [public] [int] Age]                                                                                                        |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                [get];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                [set];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [            }]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<summary\>]]                                                                               |
|                                                                                                                                                                                                                                         |
| [            [///][ Gets or sets the background brush.]]                                                                               |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\</summary\>]]                                                                              |
|                                                                                                                                                                                                                                         |
| [            [///][ ][\<value\>][The background brush.][\</value\>]]   |
|                                                                                                                                                                                                                                         |
| [            [public] [Brush] BackgroundBrush]                                                                                       |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                [get];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                [set];]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [            }]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 363:DataBinding Demo[]

[                                              ]

[]{#related-topics}

