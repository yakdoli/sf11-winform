---
title: characters.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\characters.md
created_at: 2025-07-03
---






#### Characters {#characters style="tab-stops: 0pt"}

 

Digital Gauge can display either numbers or characters,or both by using the **Value** property. The default value is **String.Empty**. The number of characters that the Digital Gauge should display is set by using **CharacterCount** property.

Digital gauge provides two character type segments:

[·      ]Seven-Segment Display-A seven segment display is composed of seven elements which can be combined to produce simplified representations to aid readability for numerals and certain letters.

[·      ]Fourteen-Segment Display-A fourteen-segment display is a type of display based on 14 segments that can be turned on or off to produce letters and numerals.

 

The character type can be set using the Digital Gauge's **CharacterType** property. It accepts values: SegementSeven and SegmentFourteen. The default value is SegmentFourteen.

 

+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| Property         | Description                                                                            | Type of Property              | Value It Accepts                                                          | Any other dependencies/Sub properties associated |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| CharacterCount   | Sets the count of characters.                                                          | [double] | [double]                                             | NA                                               |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| CharacterHeight  | Sets the height of characters.                                                         | [double] | [double]                                             | NA                                               |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| CharacterSpacing | Sets the distance between characters.                                                  | [double] | [double]                                             | NA                                               |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| CharacterType    | Sets the value indicating whether character should contain seven or fourteen segments. | [enum]   | [CharacterType].SegmentFourteen                   | NA                                               |
|                  |                                                                                        |                               |                                                                           |                                                  |
|                  |                                                                                        |                               |                                                                           |                                                  |
|                  |                                                                                        |                               |                                                                           |                                                  |
|                  |                                                                                        |                               | [CharacterType].SegmentSeven                      |                                                  |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| SkewAngleX       | Sets the angle to skew the characters along the X-axis.                                | [double] | [double]                                             | NA                                               |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+
| SkewAngleY       | Sets the angle to skew the characters along the Y-axis.                                | [double] | [double][] | NA                                               |
+------------------+----------------------------------------------------------------------------------------+-------------------------------+---------------------------------------------------------------------------+--------------------------------------------------+

[] 

More:







