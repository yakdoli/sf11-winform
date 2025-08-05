---
title: howcanwemakeie9torendermetafile.md
original_path: WinForms_Docs/99_Uncategorized/howcanwemakeie9torendermetafile.md
created_at: 2025-08-05
---








  









### How can we make IE9 to render metafile? {#how-can-we-make-ie9-to-render-metafile style="tab-stops: 0pt"}

Webpages can be converted to searchable metafile format using IE9 if the following registry value is set to (DWORD) 00000001.

 

HKEY_LOCAL_MACHINE (or HKEY_CURRENT_USER)\\SOFTWARE\\Microsoft\\Internet Explorer\\MAIN\\FeatureControl\\FEATURE_IVIEWOBJECTDRAW_DMLT9_WITH_GDI

 


{border="0"}Note: This registry setting will not be effective for webpages displayed in IE9 Standards mode.


 

[]{#related-topics}

