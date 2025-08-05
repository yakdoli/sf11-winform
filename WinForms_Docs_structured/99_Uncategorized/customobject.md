---
title: customobject.md
original_path: WinForms_Docs/99_Uncategorized/customobject.md
created_at: 2025-08-05
---






#### Custom Object {#custom-object style="tab-stops: 0pt"}

You can edit the custom object properties using the PropertyGrid. The following example illustrates how to edit the custom object properties.

1.  [Create a class called **Person** and define the properties. ]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                       |
| [\[[TypeConverter]([typeof]([ExpandableObjects]))\]]            |
|                                                                                                                                                                                       |
| [    [public] [class] [Person]]                                    |
|                                                                                                                                                                                       |
| [    {]                                                                                                                              |
|                                                                                                                                                                                       |
| [        [public] Person()]                                                                                     |
|                                                                                                                                                                                       |
| [        {            ]                                                                                                              |
|                                                                                                                                                                                       |
| [            Name = [\"Johnson\"];]                                                                          |
|                                                                                                                                                                                       |
| [            Age = 30;]                                                                                                              |
|                                                                                                                                                                                       |
| [            Mobile = 91983467382;]                                                                                                  |
|                                                                                                                                                                                       |
| [            Email = [\"carljohnson@gta.com\"];]                                                             |
|                                                                                                                                                                                       |
| [            ID = [\"0005A\"];]                                                                              |
|                                                                                                                                                                                       |
| [            DOB = [new] [DateTime](1987, 10, 16);           ]                          |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Identity\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Name\"])\]]                                     |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Name of the actual person.\"])\]]               |
|                                                                                                                                                                                       |
| [        [public] [string] Name]                                                           |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [       ]                                                                                                                            |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Identity\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"ID\"])\]]                                       |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"ID of the actual person.\"])\]]                 |
|                                                                                                                                                                                       |
| [        [public] [string] ID]                                                             |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Identity\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Date of Birth\"])\]]                            |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Birth date of the actual person.\"])\]]         |
|                                                                                                                                                                                       |
| [        [public] [DateTime] DOB]                                                       |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Contact Details\"])\]]                             |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Email ID\"])\]]                                 |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Email address of the actual person.\"])\]]      |
|                                                                                                                                                                                       |
| [        [public] [string] Email]                                                          |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Contact Details\"])\]]                             |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Mobile Number\"])\]]                            |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Contact number of the actual person.\"])\]]     |
|                                                                                                                                                                                       |
| [        [public] [long] Mobile]                                                           |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Identity\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Age\"])\]]                                      |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Age of the actual person.\"])\]]                |
|                                                                                                                                                                                       |
| [        [public] [int] Age]                                                               |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [      ]                                                                                                                             |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Identity\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Gender\"])\]]                                   |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Gender information of the actual person.\"])\]] |
|                                                                                                                                                                                       |
| [        [public] [Gender] Gender]                                                      |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }]                                                                                                                          |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [        \[[CategoryAttribute]([\"Location\"])\]]                                    |
|                                                                                                                                                                                       |
| [        \[[DisplayNameAttribute]([\"Country\"])\]]                                  |
|                                                                                                                                                                                       |
| [        \[[DescriptionAttribute]([\"Country where the person is located.\"])\]]     |
|                                                                                                                                                                                       |
| [        [public] [Country] Country]                                                    |
|                                                                                                                                                                                       |
| [        {]                                                                                                                          |
|                                                                                                                                                                                       |
| [            [get];]                                                                                            |
|                                                                                                                                                                                       |
| [            [set];]                                                                                            |
|                                                                                                                                                                                       |
| [        }       ]                                                                                                                   |
|                                                                                                                                                                                       |
| [    }]                                                                                                                              |
|                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                       |
| [  ]                                                                                                                                              |
|                                                                                                                                                                                       |
| [  [public] [enum] [Country]]                                                   |
|                                                                                                                                                                                       |
| [    {]                                                                                                                                           |
|                                                                                                                                                                                       |
| [        UnitedStates,]                                                                                                                           |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [        Germany,]                                                                                                                                |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [        Canada,]                                                                                                                                 |
|                                                                                                                                                                                       |
| [     ]                                                                                                                                           |
|                                                                                                                                                                                       |
| [    }]                                                                                                                                           |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.  [Set the ]**[SelectedObject]**[ of the property to the instance of the class **Person**.]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                       |
| [PropertyGrid][ pGrid = [new] [PropertyGrid]();] |
|                                                                                                                                                                                       |
| [            pGrid.SelectedObject = [new] [Person]();]                                               |
|                                                                                                                                                                                       |
|                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  [The PropertyGrid will be generated as shown in the following screenshot.]

 

{border="0"}

Figure 812: PropertyGrid with Custom Object

[]{#related-topics}

