---
title: installationsteps.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\installationsteps.md
created_at: 2025-07-03
---






##### Installation Steps {#installation-steps style="tab-stops: 0pt"}

 

To facilitate conversion, our HTML Converter depends on our Active-X Wrapper control which talks to GECKO APIs during conversion.  While installing the Essential Studio, the assembly manager will register the Syncfusion.GeckoWrapper.dll in the machine. To register our Active-X wrapper control manually:

1.   Copy the Syncfusion.GeckoWrapper.dll to the Bin folder of Gecko SDK (a.k.a, XulRunner-SDK 2.0.) which can download from this [[location]{.UGHyperlink}](https://developer.mozilla.org/en/Gecko_SDK).

2.   Register the Syncfusion.GeckoWrapper.dll using the following command in the command prompt:

*regsvr32 Syncfusion.GeckoWrapper.dll*

[]{#related-topics}

