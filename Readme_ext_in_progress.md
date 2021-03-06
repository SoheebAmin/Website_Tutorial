# How to Add/Remove HTML, CSS, and Javascript from Webpages

The most I had to learn in building this sample website had to deal with how to dynamically alter the HTML, CSS, and Javascript within a webpage. Let's look at the techniques used here for each one.

## HTML

HTML was loaded and unlaoded using a simple Javascript function that used JQuery. So first, be sure to include JQuery in the header, such as via this source:

```html

<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>

```

The function ias as follows. It can be included in a script tage in the head, or factored out into another .js file.

```javascript

$(function()
{
    $("#your_id").load("html_source.html");
});

```

and the body would include the following:

```html

<div id="your_id"><div>

```

The "#id" in the function ("id" replaced with your own tag name) will identify where to place the HTML in the body.

## CSS

CSS was the most sraightforward of the bunch. Stylesheets were swapped out with a simple Javascript function that finds an element by ID and updates the reference link for the CSS. I used another simple Javascript counting function to append a number to the name of the CSS stylesheet to correspond to a list of sheets which differed in name by a single number.

```javascript

let style_counter = 0;
let stylesheets_max = 4;

function changeStyleCSS()
{
  // cycling the stylesheet number to append from 0 to the max number of stylesheets.
  if (style_counter != stylesheets_max)
  {
    style_counter++;
  }
  else
  {
    style_counter = 0;
  }

  //The actual update of the stylesheet location to be "stylesheet" + 1
  document.getElementById('stylesheet').href = "for_bg_page_cycles/css_bgs/stylesheet" + style_counter +".css";
}

```

## Javascript

The first thing to go over is what NOT TO DO to swap style sheets. Attempting the same method for CSS, changing href to src, didn't actually work, even though it did swap out the code in the HTML itself. The following code actually updates the source reference, but the page itself does not actually reload the Javascript to be from said source:

```javascript

  document.getElementById('script').src= "anoter_source.js";

```

Instead, creating a new script tag and added the source did actually include this new source to the page:

```javascript

function add_script()
{
  var myScript = document.createElement('script');
  myScript.setAttribute('src', 'new_script.js');
  document.head.appendChild(myScript);
}

```

TBC.
