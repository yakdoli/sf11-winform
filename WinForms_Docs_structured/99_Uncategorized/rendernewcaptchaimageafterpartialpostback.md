---
title: rendernewcaptchaimageafterpartialpostback.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rendernewcaptchaimageafterpartialpostback.md
created_at: 2025-07-03
---






##### Render New Captcha [i]mage [a]fter [p]artial [P]ost back {#render-new-captcha-image-after-partial-post-back style="tab-stops: 0pt"}

After partial post back, the encrypted code for generating the captcha control image will be null. You can regenerate the image using the *RenderNewChallenge* method.

 

Table 1: Method Table


+-------------------------------------------------------------------+----------------------------+------------+-------------+-------------+-----------------+
| Method                                                            | Description                | Parameters | Type        | Return Type | Reference links |
+-------------------------------------------------------------------+----------------------------+------------+-------------+-------------+-----------------+
| [`RenderNewChallenge`] | Renders new captcha image. | NA         | Server side | void        | NA              |
|                                                                   |                            |            |             |             |                 |
|                                                                   |                            |            |             |             |                 |
+===================================================================+============================+============+=============+=============+=================+


**[]** 

The following code illustrates how to render captcha image using the *RenderNewChallenge* method:

**[]** 

+-----------------------------------------------------------------------+
| [\[C#\]]                          |
|                                                                       |
| []                                |
|                                                                       |
| [Captcha2.RenderNewChallenge()]   |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

[] 

**[]** 

 

 

[]{#related-topics}

