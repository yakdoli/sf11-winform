---
title: stylemanagerandscriptmanager1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\stylemanagerandscriptmanager1.md
created_at: 2025-07-03
---








  









### StyleManager and ScriptManager {#stylemanager-and-scriptmanager style="tab-stops: 0pt"}

 

StyleManager

 

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables minification, compression, and combination of CSS resources for ASP.NET MVC Web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before being sent to the browser. All are done using a single HTTP request per resource set.

 

ScriptManager

 

**ScriptManager** is a new script resource manager that helps in registering JavaScript files. The ScriptManager registers only the Syncfusion.Mvc component script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before being sent to the browser.

 

Use Case Scenarios

StyleManager and ScriptManager enable minification, compression, and combination of CSS resources and JavaScript resources respectively. These resource managers improve the performance of the Web site.

 

[] 

[]{#related-topics}

