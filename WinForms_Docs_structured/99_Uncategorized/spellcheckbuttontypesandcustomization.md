---
title: spellcheckbuttontypesandcustomization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\spellcheckbuttontypesandcustomization.md
created_at: 2025-07-03
---






##### Spell Check button types and customization {#spell-check-button-types-and-customization style="MARGIN-LEFT: 1.8pt; tab-stops: 1.8pt"}

[] 

Button Types

[] 

The SpellCheckControl can be rendered as one of the pre-defined button types. The **ShowSpellCheckButton** property can be handled to control the visibility of the spell control button.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ShowSpellCheckButton              | Can be set to show or hide the spell button. When set to false, SpellCheck button will be hidden. Default value is True. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| SpellCheckButtonType              | Specifies to set any one of the following button types. Default value is Button. The options included are as follows:    |
|                                   |                                                                                                                          |
|                                   | [·      ]Button                                                                             |
|                                   |                                                                                                                          |
|                                   | [·      ]ImageButton                                                                        |
|                                   |                                                                                                                          |
|                                   | [·      ]LinkButton                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the button types can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                                       |
| [SpellCheck1.SpellCheckButtonType = [SpellCheckControl].[SpellButtonType].ImageButton;] |
|                                                                                                                                                                                       |
| [SpellCheck1.ShowSpellCheckButton = [true];]                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [Private][ SpellCheck1.SpellCheckButtonType = SpellCheckControl.SpellButtonType.ImageButton] |
|                                                                                                                                                                                                                   |
| [Private][ SpellCheck1.ShowSpellCheckButton = [True]]                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing ImageButton

[] 

When the button type is set to **Image**, custom image can be set by specifying the path to the **ImageUrl** property and it can be aligned using the **ImageOrientation** property.

[] 


  ------------------ ------------------------------------------------------------------------------------------
  Property           Description
  ImageOrientation   Specifies the image alignment when the image button type is used. Default value is Left.
  ImageUrl           Specifies the url of the image to be used for the image button.
  ------------------ ------------------------------------------------------------------------------------------


[] 

Programmatically the image can be set and customized as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                                 |
| **[]**                                                                      |
|                                                                                                                                 |
| [SpellCheck.ImageUrl = [\"eyeglasses.png\"];]        |
|                                                                                                                                 |
| [SpellCheck.ImageOrientation = [ImageAlign].Baseline;] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                    |
| [Private][ SpellCheck.ImageUrl = [\"eyeglasses.png\"]] |
|                                                                                                                                                                                                    |
| [Private][ SpellCheck.ImageOrientation = ImageAlign.Baseline]                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p150} 

[]{#related-topics}

