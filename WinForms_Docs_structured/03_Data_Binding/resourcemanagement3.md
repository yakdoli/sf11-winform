---
title: resourcemanagement3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\resourcemanagement3.md
created_at: 2025-07-03
---








  









## Resource Management {#resource-management style="tab-stops: 0pt"}

Many web developers will most probably be aware of various website optimization techniques described in Yahoo Developer Network article(Please refer [[http://developer.yahoo.com/performance/rules.html]](http://developer.yahoo.com/performance/rules.html)).

Here are some important rules to improve the website optimization.

 

Minimize HTTP Requests:

Browsers spend approximately 80% of the time fetching external components such as scripts, style sheets and images. Each unique HTTP request requires a round trip to a server, introducing indeterminate delays.Browsers must load and parse external CSS files referenced within the head of your HTML before they parse the body content. By minimizing the HTTP request load, you can maximize the initial display speed of your content.

Number of HTTP requests may be reduced by combining all the scripts into a single script and similarly combining all external stylesheets into a single stylesheet. For more information Refer to Yahoo\'s performance rules #1.

 

Minify JavaScript and CSS:

Minification is the practice of removing unnecessary characters from code to reduce its size, removing unnecessary spacing, newlines, tabs  and optimizing the CSS/javascript code; thus improving load times. Additionally, code can be further formatted onto a single line instead of multiple lines.For more information Refer to Yahoo\'s performance rules #10.

 

Put Stylesheets at the Top:

Loadingstylesheets in the document HEAD makes the page to start rendering sooner. Because this allows three pages to render progressively. For more information Refer to Yahoo\'s performance rules #5.

 

Put Scripts at the Bottom:

Scripts block parallel downloads. While a script is downloading, the browser won\'t start any other downloads. You can get your site to load faster by moving your scripts to the bottom.. For more information Refer to Yahoo\'s performance rules #6.

 

 

More:







