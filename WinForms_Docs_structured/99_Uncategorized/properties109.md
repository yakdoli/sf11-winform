---
title: properties109.md
original_path: WinForms_Docs/99_Uncategorized/properties109.md
created_at: 2025-08-05
---






#### Properties {#properties style="tab-stops: 0pt"}

+-------------+-----------------------------------------------+--------------------+------------------------------------------------------------+------------------------------------------------------------------------------+
| Property    | Description                                   | Type of property   | Value it accepts                                           | Dependencies                                                                 |
+-------------+-----------------------------------------------+--------------------+------------------------------------------------------------+------------------------------------------------------------------------------+
| EditMode    | Specifies the Edit Mode                       | GridEditMode(Enum) | [·      ]ExternalForm         | Depends on AllowEditing---\                                                  |
|             |                                               |                    |                                                            | \                                                                            |
|             |                                               |                    | [·      ]ExternalFormTemplate |                                                                              |
|             |                                               |                    |                                                            | If AllowEditing is set to **True**, the EditMode property is enabled.        |
+-------------+-----------------------------------------------+--------------------+------------------------------------------------------------+------------------------------------------------------------------------------+
| Position    | Specifies position of the external form       | Enum               | [·      ]Position.TopRight,   | Depends on **ExternalForm**---                                               |
|             |                                               |                    |                                                            |                                                                              |
|             |                                               |                    | [·      ]Position.BottomLeft, |                                                                              |
|             |                                               |                    |                                                            |                                                                              |
|             |                                               |                    | [·      ]Position.Custom      | If GridEditMode is External Form, position of the external form is posibile. |
+-------------+-----------------------------------------------+--------------------+------------------------------------------------------------+------------------------------------------------------------------------------+
| TargetID    | Specifies the target ID of External Edit Form | String             | Any String                                                 | ExternalForm                                                                 |
+-------------+-----------------------------------------------+--------------------+------------------------------------------------------------+------------------------------------------------------------------------------+

 

 

[]{#related-topics}

