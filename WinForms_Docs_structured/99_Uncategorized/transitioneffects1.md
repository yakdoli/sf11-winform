---
title: transitioneffects1.md
original_path: WinForms_Docs/99_Uncategorized/transitioneffects1.md
created_at: 2025-08-05
---






##### Transition Effects {#transition-effects style="tab-stops: 0pt"}

[] 

Transition and slide effects can be applied to enhance and provide a rich interface for the groupbar item on expand and collapse.

The transition effects can be set for expand and collapse action of a parent item. These effects can be applied just by setting the **ExpandTransition** and **CollapseTransition** to one of the effects.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| ExpandTransition                  | Specifies the transition effect for expand animation. The options included are as follows: |
|                                   |                                                                                            |
|                                   | [·      ]None                                                 |
|                                   |                                                                                            |
|                                   | [·      ]Fade                                                 |
|                                   |                                                                                            |
|                                   | [·      ]Dissolve                                             |
|                                   |                                                                                            |
|                                   | [·      ]Pixelate                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeDown                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeLeft                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeRight                                            |
|                                   |                                                                                            |
|                                   | [·      ]WipeUp                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| CollapseTransition                | Specifies the visual effect during item collapse. The options included are as follows:     |
|                                   |                                                                                            |
|                                   | [·      ]None                                                 |
|                                   |                                                                                            |
|                                   | [·      ]Fade                                                 |
|                                   |                                                                                            |
|                                   | [·      ]Dissolve                                             |
|                                   |                                                                                            |
|                                   | [·      ]Pixelate                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeDown                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeLeft                                             |
|                                   |                                                                                            |
|                                   | [·      ]WipeRight                                            |
|                                   |                                                                                            |
|                                   | [·      ]WipeUp                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------+


*[]* 

The visual effect can be enhanced for expand and collapse animation by setting the **ExpandType** and **CollapseType** properties respectively.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ExpandSlideType                   | Specifies the type of slide effect used on expanding an item. The options included are as follows:         |
|                                   |                                                                                                            |
|                                   | [·      ]None                                                                 |
|                                   |                                                                                                            |
|                                   | [·      ]Exponentialaccelerate                                                |
|                                   |                                                                                                            |
|                                   | [·      ]Exponentialdecelerate                                                |
|                                   |                                                                                                            |
|                                   | [·      ]Quadraticaccelerate                                                  |
|                                   |                                                                                                            |
|                                   | [·      ]Quadraticdecelerate                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| CollapseSlideType                 | Specifies to use the type of slide effect used on collapsing an item. The options included are as follows: |
|                                   |                                                                                                            |
|                                   | [·      ]None                                                                 |
|                                   |                                                                                                            |
|                                   | [·      ]Exponentialaccelerate                                                |
|                                   |                                                                                                            |
|                                   | [·      ]Exponentialdecelerate                                                |
|                                   |                                                                                                            |
|                                   | [·      ]Quadraticaccelerate                                                  |
|                                   |                                                                                                            |
|                                   | [·      ]Quadraticdecelerate                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+


*[]* 

Duration can be set for the expand and collapse action using the **ExpandDuration** and **CollapseDuration** properties.

[] 


  ------------------ --------------------------------------------------------------------------------------
  Property           Description
  CollapseDuration   Specifies the duration of collapse animation, in milliseconds. Default value is 100.
  ExpandDuration     Specifies the duration of expand animation, in milliseconds. Default value is 100.
  ------------------ --------------------------------------------------------------------------------------


 

[]{#related-topics}

