# Need of performance
- phone: way more strict: stick with fingers -> simpler the better
- web: less strict

# Resource
- def'n: things embedded into the app
- res/ dir
- severral categories

## Layout
- way to organize view inside ui
- xml files in res/layout
- can be nested
- wysiwyg/ manual editor

### Layout xml
- containers(vg) contains views
- require: layout_width, layout_height
- optional: id (for finding later)
- load:
  - activity: onCreate(), setContentView()
  - fragment: onCreateView()

### Adaptive layout
- tablet: layout-large, layout-xlarge
- phone: layout-normal
- small phone: layout-small
- orientation: layout-land, layout-port

### FrameLayout
- contain multiple views
- multiple layers, z-based
- supports child margins
- supports gravity

### LinearLayout
one direction: vertical: top -> bot; horizontal: L -> R
#### stretching:
- use layout_weight
- horizontal: stretch width
- vertical: stretch height

### RelativeLayout
- multiple layers, Z-order based
- relativity of child's pos and size to parent/ ea other
- make relative layout has streching like linear layout:
  - make a 0 height view(anchor) at center
  - make top panel above anchor
  - make bot panel below anchor
- scrolling: scroll view

# ViewPager
- tab-like container
  - widely used
  - hor swipe gesture
  - page-by-page scrolling
- each tab is a fragment
  - UI inflated by fragment
  - controlled by fragment
  - can be nested (but pls dont much)
  - off-screen limit: fragments outside limit are destroyed and recreated when necessary
- "adapter" class in java to specify which fragment in which page

# Raw data
- embedded in your apps
- places: 
  - res/raw: R.raw.<name>, access with Context.getResources().openRawResoure(R.raw.resid)
  - assets: getAssets().open("<filename>");

