# Weather Channel Retro Style Guide

## Table of Contents
1. [Brand Identity & Design Philosophy](#brand-identity--design-philosophy)
2. [Color Palette](#color-palette)
3. [Typography](#typography)
4. [Component Library](#component-library)
5. [Spacing & Layout](#spacing--layout)
6. [Animations & Interactions](#animations--interactions)
7. [Responsive Design](#responsive-design)
8. [Code Examples](#code-examples)

---

## Brand Identity & Design Philosophy

### Overall Aesthetic
This design system recreates the nostalgic, iconic look of The Weather Channel from the 2000s and early 2010s era. It embraces a **bold, vibrant, and playful** visual language that combines professional weather broadcasting aesthetics with fun, retro charm.

### Core Design Principles

1. **Vibrant & Bold**: Use saturated blues, bright yellows, and attention-grabbing reds to create visual impact
2. **Layered Depth**: Leverage gradients, shadows, and borders to create dimension and hierarchy
3. **Playful Professionalism**: Balance serious weather data with fun animations and bubbly styling
4. **Clear Readability**: Ensure all text is highly legible with proper contrast and text shadows
5. **Nostalgic Motion**: Use smooth animations that evoke 2000s-era broadcast graphics
6. **Accessibility First**: Respect user preferences for reduced motion and maintain proper contrast ratios

### When to Use This Style

✅ **Perfect for:**
- Weather forecast applications
- Retro-themed web experiences
- Dashboard interfaces requiring visual hierarchy
- Projects celebrating 2000s/2010s design aesthetics
- Applications where bold colors enhance user engagement

❌ **Not suitable for:**
- Minimal/flat design projects
- Corporate/professional business applications
- Content-heavy reading experiences
- Subtle, understated interfaces

---

## Color Palette

### Primary Colors

#### Deep Blues (Background & Structure)
- **Dark Navy**: `#1e3c72`
  - Usage: Primary background gradient (top)
  - Context: Creates depth and professionalism

- **Royal Blue**: `#2a5298`
  - Usage: Background gradient (middle), component backgrounds
  - Context: Primary brand color

- **Bright Blue**: `#0066cc`
  - Usage: Headers, borders, interactive elements
  - Context: High-contrast accent color

- **Deep Ocean**: `#003d7a`
  - Usage: Gradient endings, header backgrounds
  - Context: Creates depth in gradients

- **Steel Blue**: `#7e8ba3`
  - Usage: Background gradient (bottom)
  - Context: Softer transition for body backgrounds

### Accent Colors

#### Yellow/Gold (Highlights & CTAs)
- **Bright Yellow**: `#ffcc00`
  - Usage: Taglines, labels, borders, call-to-action buttons
  - Context: Primary accent color, draws attention

- **Warm Orange**: `#ff9900`
  - Usage: Button gradients, hover effects
  - Context: Creates warmth and energy

- **Light Yellow**: `#ffe033`
  - Usage: Hover states for buttons
  - Context: Brightens on interaction

- **Dark Orange**: `#ffaa00`
  - Usage: Button hover gradient endings
  - Context: Maintains visibility in hover states

#### Red (Alerts & Warnings)
- **Bright Red**: `#ff4444`
  - Usage: Alert bars, error messages
  - Context: Immediate attention required

- **Dark Red**: `#cc0000`
  - Usage: Alert gradient endings, error backgrounds
  - Context: Creates urgency and depth

### Neutral Colors

#### White
- **Pure White**: `#fff`
  - Usage: Text, borders, highlights
  - Context: Maximum contrast on dark backgrounds

- **Transparent White Variants**:
  - `rgba(255, 255, 255, 0.95)` - Input backgrounds
  - `rgba(255, 255, 255, 0.5)` - Component borders
  - `rgba(255, 255, 255, 0.3)` - Subtle borders
  - `rgba(255, 255, 255, 0.2)` - Very subtle borders
  - `rgba(255, 255, 255, 0.15)` - Light panel backgrounds
  - `rgba(255, 255, 255, 0.1)` - Explanation card backgrounds
  - `rgba(255, 255, 255, 0.05)` - Subtle gradient endings

#### Black
- **Dark Gray**: `#333`
  - Usage: Input text color
  - Context: Readable on light backgrounds

- **Transparent Black Variants**:
  - `rgba(0, 0, 0, 0.6)` - Footer backgrounds
  - `rgba(0, 0, 0, 0.5)` - Text shadows, alert shadows
  - `rgba(0, 0, 0, 0.4)` - Header shadows, footer gradient start
  - `rgba(0, 0, 0, 0.3)` - Box shadows, borders, explanations background
  - `rgba(0, 0, 0, 0.2)` - Search section backgrounds
  - `rgba(0, 0, 0, 0.1)` - Search section gradient end, input shadows

### Gradient Patterns

#### Primary Body Gradient
```css
background: linear-gradient(180deg, #1e3c72 0%, #2a5298 50%, #7e8ba3 100%);
```
**Usage**: Main body background, creates sky-like depth

#### Alert Bar Gradient
```css
background: linear-gradient(90deg, #ff4444 0%, #cc0000 50%, #ff4444 100%);
```
**Usage**: Scrolling alert bars, error messages (horizontal gradient)

#### Header Gradient
```css
background: linear-gradient(180deg, #0066cc 0%, #003d7a 100%);
```
**Usage**: Main header sections

#### Button Gradient
```css
background: linear-gradient(180deg, #ffcc00 0%, #ff9900 100%);
```
**Usage**: Primary action buttons

#### Button Hover Gradient
```css
background: linear-gradient(180deg, #ffe033 0%, #ffaa00 100%);
```
**Usage**: Button hover states

#### Panel Gradient (Blue)
```css
background: linear-gradient(135deg, rgba(0, 102, 204, 0.8) 0%, rgba(0, 61, 122, 0.9) 100%);
```
**Usage**: Current conditions panels (diagonal gradient)

#### Panel Gradient (Alternative)
```css
background: linear-gradient(135deg, rgba(0, 102, 204, 0.7) 0%, rgba(0, 61, 122, 0.8) 100%);
```
**Usage**: Welcome content panels

#### Detail Box Gradient
```css
background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
```
**Usage**: Weather detail boxes

#### Search Section Gradient
```css
background: linear-gradient(180deg, rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0.1) 100%);
```
**Usage**: Search input section backgrounds

#### Footer Gradient
```css
background: linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.6) 100%);
```
**Usage**: Bottom info bars

---

## Typography

### Font Families

#### Primary Font Stack
```css
font-family: 'Arial', 'Helvetica', sans-serif;
```
**Usage**: All text throughout the application  
**Rationale**: Clean, highly readable sans-serif that was ubiquitous in 2000s broadcast graphics

### Font Sizes

#### Heading Sizes
- **Logo/Main Title**: `3em` (desktop) → `2em` (tablet) → `1.5em` (mobile)
  - Usage: `.channel-logo`
  - Context: Primary branding element

- **Location Headers**: `2.5em` (desktop) → `2em` (mobile)
  - Usage: `.location-header h2`
  - Context: City/location display

- **Section Titles**: `2em` (desktop) → `1.5em` (mobile)
  - Usage: `.section-title`
  - Context: Major section headings

- **Condition Text**: `2em` (desktop) → `1.5em` (mobile)
  - Usage: `.condition-text`
  - Context: Weather description

- **Explanation Card Headings**: `1.4em`
  - Usage: `.explanation-card h4`
  - Context: Subheadings within sections

- **Tagline**: `1.2em` (desktop) → `1em` (mobile)
  - Usage: `.tagline`
  - Context: Subtitle text

#### Body Text Sizes
- **Large Body**: `1.3em`
  - Usage: `.welcome-text`, `.feels-like`
  - Context: Prominent body text

- **Standard Body**: `1.1em` to `1.2em`
  - Usage: `.search-input`, `.search-button`, `.explanation-card p`, `.time-display`
  - Context: Regular content text

- **Standard**: `1em`
  - Usage: `.bottom-content`
  - Context: Footer and supplementary text

- **Small Text**: `0.9em`
  - Usage: `.update-time`, `.detail-label`
  - Context: Labels and metadata

- **Alert Text**: `14px` (desktop) → `12px` (mobile)
  - Usage: `.alert-text`
  - Context: Scrolling alert ticker

#### Display Sizes
- **Temperature (Extra Large)**: `6em` (desktop) → `4em` (tablet) → `3em` (mobile)
  - Usage: `.temperature`
  - Context: Primary temperature display

- **Temperature Unit**: `3em` (desktop) → `2em` (tablet) → `1.5em` (mobile)
  - Usage: `.temp-unit`
  - Context: Temperature unit symbol (°C/°F)

- **Detail Values**: `1.8em` (desktop) → `1.4em` (mobile)
  - Usage: `.detail-value`
  - Context: Weather metric values

- **Conditions Value**: `1.2em`
  - Usage: `.conditions-value`
  - Context: Weather condition descriptions in detail boxes

- **Icons**: `3em` (large) → `2em` (mobile)
  - Usage: `.detail-icon`, `.welcome-icons`
  - Context: Weather and decorative icons

### Font Weights
- **Bold**: `font-weight: bold`
  - Usage: Headers, buttons, labels, data values, emphasis
  - Context: Most text in the design uses bold for high impact

- **Normal**: Default weight
  - Usage: Paragraph text in explanations (minimal use)
  - Context: Only used where readability of longer text is paramount

### Text Effects

#### Text Shadows (Depth & Readability)
- **Heavy Shadow**: `3px 3px 6px rgba(0, 0, 0, 0.5)`
  - Usage: `.channel-logo`, `.location-header h2`, `.welcome-content h2`
  - Context: Large headings requiring maximum depth

- **Medium Shadow**: `2px 2px 4px rgba(0, 0, 0, 0.5)`
  - Usage: `.tagline`, `.alert-text`, `.condition-text`, `.detail-value`, `.section-title`
  - Context: Standard text shadow for most text elements

- **Large Shadow**: `4px 4px 8px rgba(0, 0, 0, 0.5)`
  - Usage: `.temperature`
  - Context: Extra large display text

- **Light Shadow**: `1px 1px 2px rgba(255, 255, 255, 0.5)`
  - Usage: `.search-button`
  - Context: Creates embossed effect on light buttons

#### Text Transforms
- **Uppercase**: `text-transform: uppercase`
  - Usage: `.condition-text`
  - Context: Weather conditions for emphasis

- **Capitalize**: `text-transform: capitalize`
  - Usage: `.conditions-value`
  - Context: Proper casing for multi-word conditions

#### Letter Spacing
- **Wide**: `letter-spacing: 3px`
  - Usage: `.channel-logo`
  - Context: Logo branding

- **Medium**: `letter-spacing: 2px`
  - Usage: `.bottom-content`
  - Context: Footer text

- **Tight**: `letter-spacing: 1px`
  - Usage: `.alert-text`, `.detail-label`
  - Context: Compact uppercase text

#### Line Height
- **Tight Leading**: `line-height: 1`
  - Usage: `.temperature`
  - Context: Display numerals with no extra spacing

- **Comfortable**: `line-height: 1.6`
  - Usage: `.explanation-card p`
  - Context: Paragraph text for readability

### Typography Usage Guidelines

1. **Always apply text shadows** to white text on semi-transparent backgrounds for readability
2. **Use bold weights liberally** to maintain the broadcast aesthetic
3. **Uppercase sparingly** - only for short, impactful text
4. **Scale fonts responsively** - reduce sizes significantly on mobile to prevent overflow
5. **Maintain hierarchy** - each level should be distinctly different from adjacent levels

---

## Component Library

### 1. Alert Bar (`.alerts-bar`)

**Purpose**: Scrolling ticker for important weather alerts and updates

**HTML Structure**:
```html
<div class="alerts-bar">
  <div class="alerts-container">
    <div class="alerts-ticker">
      <span class="alert-text">⚠️ WEATHER ALERTS</span>
      <span class="alert-text">• UPDATE TEXT •</span>
    </div>
  </div>
</div>
```

**CSS Classes**:
- `.alerts-bar` - Container with red gradient background
- `.alerts-container` - Overflow handler
- `.alerts-ticker` - Animated scrolling content
- `.alert-text` - Individual alert message spans

**Styling**:
- Background: Red gradient (`#ff4444` to `#cc0000`)
- Border: 3px white top and bottom
- Height: 35px
- Animation: Continuous scroll-left (30s duration)
- Text: Bold, 14px, uppercase, white with shadow

**States**:
- Default: Continuous scrolling animation
- Reduced Motion: Animation disabled via `@media (prefers-reduced-motion: reduce)`

**Usage Guidelines**:
- Duplicate content to ensure seamless infinite scroll
- Keep messages short and impactful
- Use emoji icons for visual interest
- Separate messages with bullet points (•)

---

### 2. Main Header (`.main-header`)

**Purpose**: Primary branding and navigation area

**HTML Structure**:
```html
<header class="main-header">
  <div class="header-content">
    <h1 class="channel-logo">THE WEATHER CHANNEL</h1>
    <p class="tagline">Local on the 8s</p>
  </div>
</header>
```

**CSS Classes**:
- `.main-header` - Header container with blue gradient
- `.header-content` - Centered content wrapper (max-width: 1200px)
- `.channel-logo` - Main title/logo text
- `.tagline` - Subtitle/slogan text

**Styling**:
- Background: Deep blue gradient (`#0066cc` to `#003d7a`)
- Border Bottom: 5px solid yellow (`#ffcc00`)
- Padding: 25px 20px
- Text: Centered, white, bold with shadows

**States**:
- Static (no hover states)

**Usage Guidelines**:
- Keep logo text short and bold
- Tagline should be italicized and yellow
- Maintain the yellow border as a signature element
- Center all content

---

### 3. Time Display (`.time-display`)

**Purpose**: Shows current date/time

**HTML Structure**:
```html
<div class="time-display">
  <div id="currentTime"></div>
</div>
```

**CSS Classes**:
- `.time-display` - Container for time information

**Styling**:
- Background: `rgba(0, 0, 0, 0.3)`
- Border Bottom: 2px solid `rgba(255, 255, 255, 0.3)`
- Padding: 10px
- Text: Centered, bold, 1.1em

**States**:
- Dynamic content (updates via JavaScript)

---

### 4. Search Section (`.search-section`)

**Purpose**: City search input and submission

**HTML Structure**:
```html
<section class="search-section">
  <div class="search-container">
    <form class="search-form">
      <input type="text" class="search-input" placeholder="Enter your city...">
      <button type="submit" class="search-button">GET WEATHER</button>
    </form>
  </div>
</section>
```

**CSS Classes**:
- `.search-section` - Outer section wrapper
- `.search-container` - Centered container (max-width: 600px)
- `.search-form` - Flex container for input and button
- `.search-input` - Text input field
- `.search-button` - Submit button

**Styling**:

**Input (`.search-input`)**:
- Background: `rgba(255, 255, 255, 0.95)`
- Border: 3px solid `#0066cc`
- Border Radius: 5px
- Padding: 15px 20px
- Font: Bold, 1.1em
- Color: `#333`
- Shadow: Inset `0 2px 5px rgba(0, 0, 0, 0.1)`

**Button (`.search-button`)**:
- Background: Yellow-to-orange gradient
- Border: 3px solid white
- Border Radius: 5px
- Padding: 15px 30px
- Font: Bold, 1.1em
- Color: `#003d7a` (dark blue text)
- Shadow: `0 4px 8px rgba(0, 0, 0, 0.3)`

**States**:
- **Input Focus**:
  - Border: Yellow (`#ffcc00`)
  - Box Shadow: `0 0 10px rgba(255, 204, 0, 0.5)`

- **Button Hover**:
  - Background: Brighter yellow gradient
  - Transform: `translateY(-2px)` (lifts up)
  - Box Shadow: `0 6px 12px rgba(0, 0, 0, 0.4)` (deeper shadow)

- **Button Active** (clicked):
  - Transform: `translateY(0)` (returns to position)
  - Box Shadow: `0 2px 4px rgba(0, 0, 0, 0.3)` (compressed shadow)

**Usage Guidelines**:
- Always use bold fonts
- Maintain 3px borders for consistency
- Input should have blue focus state
- Button should have yellow/orange gradient
- Add smooth transitions (0.3s ease) for interactions

---

### 5. Error Message (`.error-message`)

**Purpose**: Display error states and invalid input feedback

**HTML Structure**:
```html
<div class="error-message">
  <p>⚠️ Error message text here</p>
</div>
```

**CSS Classes**:
- `.error-message` - Error container

**Styling**:
- Background: Red gradient (`#ff4444` to `#cc0000`)
- Border: 3px solid white
- Border Radius: 8px
- Padding: 20px
- Max Width: 800px
- Margin: 20px auto
- Text: Centered, bold, 1.2em, white

**States**:
- Static (no interactions)

**Usage Guidelines**:
- Always include warning emoji (⚠️) or similar icon
- Keep messages clear and actionable
- Center on page
- Use bold text for emphasis

---

### 6. Current Conditions Panel (`.current-conditions`)

**Purpose**: Main weather information display

**HTML Structure**:
```html
<div class="current-conditions">
  <div class="location-header">
    <h2>City, Country</h2>
    <p class="update-time">AS OF <span id="updateTime"></span></p>
  </div>
  
  <div class="current-temp-display">
    <div class="temp-large">
      <span class="temperature">72°</span>
      <span class="temp-unit">C</span>
    </div>
    <div class="condition-info">
      <p class="condition-text">PARTLY CLOUDY</p>
      <p class="feels-like">FEELS LIKE 68°C</p>
    </div>
  </div>
</div>
```

**CSS Classes**:
- `.current-conditions` - Main panel container
- `.location-header` - Location and time info
- `.update-time` - Timestamp display
- `.current-temp-display` - Flex container for temp and conditions
- `.temp-large` - Temperature wrapper
- `.temperature` - Large numeric temperature
- `.temp-unit` - Degree symbol and unit
- `.condition-info` - Weather description wrapper
- `.condition-text` - Main condition description
- `.feels-like` - "Feels like" temperature

**Styling**:
- Background: Diagonal blue gradient with transparency
- Border: 4px solid `rgba(255, 255, 255, 0.5)`
- Border Radius: 10px
- Padding: 30px
- Box Shadow: `0 8px 20px rgba(0, 0, 0, 0.5)`

**States**:
- Static (no hover states)

**Usage Guidelines**:
- Temperature should be the dominant visual element
- Use yellow color for `.update-time` and `.feels-like`
- Uppercase condition text for emphasis
- Maintain large size difference between temp and unit

---

### 7. Detail Box (`.detail-box`)

**Purpose**: Individual weather metric display (humidity, wind, etc.)

**HTML Structure**:
```html
<div class="detail-box">
  <div class="detail-icon">💧</div>
  <div class="detail-content">
    <span class="detail-label">HUMIDITY</span>
    <span class="detail-value">65%</span>
  </div>
</div>
```

**CSS Classes**:
- `.detail-box` - Container for individual metric
- `.detail-icon` - Emoji/icon display
- `.detail-content` - Text content wrapper
- `.detail-label` - Metric name
- `.detail-value` - Metric value (or `.conditions-value` for text descriptions)

**Styling**:
- Background: Diagonal white gradient with low opacity
- Border: 3px solid `rgba(255, 255, 255, 0.3)`
- Border Radius: 8px
- Padding: 25px
- Gap: 20px (flex)
- Box Shadow: `0 4px 10px rgba(0, 0, 0, 0.3)`
- Transition: `transform 0.3s ease`

**States**:
- **Default**: 
  - Opacity: 0, Transform: `translateY(20px)` (for animation-in)
  
- **Animated In** (`.animate-in`):
  - Opacity: 1, Transform: `translateY(0)`
  - Transition: 0.6s ease

- **Hover**:
  - Transform: `translateY(-5px)` (lifts up)
  - Border Color: Yellow (`#ffcc00`)

**Usage Guidelines**:
- Always use emoji icons (3em size)
- Label should be uppercase and yellow
- Value should be bold and large (1.8em)
- Use `.conditions-value` class for text values (capitalizes, smaller size)
- Add `.animate-in` class via JavaScript for entrance animation

---

### 8. Weather Details Grid (`.weather-details-grid`)

**Purpose**: Container for multiple detail boxes

**HTML Structure**:
```html
<div class="weather-details-grid">
  <!-- Multiple .detail-box elements -->
</div>
```

**CSS Classes**:
- `.weather-details-grid` - Grid container

**Styling**:
- Display: CSS Grid
- Grid Template: `repeat(auto-fit, minmax(250px, 1fr))`
- Gap: 20px
- Responsive: Collapses to single column on mobile

**Usage Guidelines**:
- Use for grouping 4+ related metrics
- Each child should be a `.detail-box`
- Grid automatically wraps on narrow screens

---

### 9. Explanations Section (`.explanations-section`)

**Purpose**: Educational content about weather metrics

**HTML Structure**:
```html
<div class="explanations-section">
  <h3 class="section-title">UNDERSTANDING YOUR WEATHER</h3>
  
  <div class="explanation-card">
    <h4>🌡️ Temperature</h4>
    <p>Explanation text here...</p>
  </div>
</div>
```

**CSS Classes**:
- `.explanations-section` - Section container
- `.section-title` - Section heading
- `.explanation-card` - Individual explanation item

**Styling**:

**Section**:
- Background: `rgba(0, 0, 0, 0.3)`
- Border: 3px solid `rgba(255, 255, 255, 0.3)`
- Border Radius: 10px
- Padding: 30px

**Section Title**:
- Font Size: 2em
- Color: Yellow (`#ffcc00`)
- Text Align: Center
- Border Bottom: 3px solid yellow
- Padding Bottom: 10px

**Explanation Card**:
- Background: `rgba(255, 255, 255, 0.1)`
- Border: 2px solid `rgba(255, 255, 255, 0.2)`
- Border Radius: 8px
- Padding: 20px
- Margin Bottom: 15px
- Transition: `all 0.3s ease`

**States**:
- **Card Hover**:
  - Background: `rgba(255, 255, 255, 0.15)` (brighter)
  - Border Color: Yellow (`#ffcc00`)

**Usage Guidelines**:
- Use section titles sparingly for major content divisions
- Each explanation card should have an emoji heading
- Card headings (h4) should be yellow and 1.4em
- Paragraph text should be comfortable to read (1.1em, line-height 1.6)
- Add hover effects for interactivity

---

### 10. Welcome Section (`.welcome-section`, `.welcome-content`)

**Purpose**: Empty state / landing screen before search

**HTML Structure**:
```html
<div class="welcome-section">
  <div class="welcome-content">
    <h2>WELCOME TO THE WEATHER CHANNEL</h2>
    <p class="welcome-text">Enter your city above to get your local forecast</p>
    <div class="welcome-icons">
      <span class="weather-icon">☀️</span>
      <span class="weather-icon">⛅</span>
      <span class="weather-icon">🌧️</span>
      <span class="weather-icon">⛈️</span>
      <span class="weather-icon">❄️</span>
    </div>
  </div>
</div>
```

**CSS Classes**:
- `.welcome-section` - Outer wrapper
- `.welcome-content` - Inner panel
- `.welcome-text` - Description paragraph
- `.welcome-icons` - Icon container
- `.weather-icon` - Individual animated icons

**Styling**:

**Section**:
- Max Width: 800px
- Margin: 50px auto
- Padding: 0 20px

**Content**:
- Background: Diagonal blue gradient with transparency
- Border: 4px solid `rgba(255, 255, 255, 0.5)`
- Border Radius: 10px
- Padding: 50px
- Text Align: Center
- Box Shadow: `0 8px 20px rgba(0, 0, 0, 0.5)`

**Icons**:
- Display: Flex
- Gap: 30px (desktop) → 15px (mobile)
- Font Size: 3em (desktop) → 2em (mobile)
- Justify: Center

**States**:
- **Icon Animation**: Each icon has a staggered bounce animation
  - Duration: 2s, easing: ease-in-out, infinite
  - Delay: 0s, 0.2s, 0.4s, 0.6s, 0.8s
  - Movement: `translateY(-10px)` at 50% keyframe

**Usage Guidelines**:
- Display only when no weather data is present
- Use variety of weather emoji
- Stagger animation delays for playful effect
- Keep welcome message concise and actionable

---

### 11. Bottom Bar (`.bottom-bar`)

**Purpose**: Footer information and branding

**HTML Structure**:
```html
<footer class="bottom-bar">
  <div class="bottom-content">
    <span>LOCAL FORECAST</span>
    <span>•</span>
    <span>UPDATED CONTINUOUSLY</span>
    <span>•</span>
    <span>WEATHER.COM</span>
  </div>
</footer>
```

**CSS Classes**:
- `.bottom-bar` - Footer container
- `.bottom-content` - Centered content

**Styling**:
- Background: Dark gradient (`rgba(0, 0, 0, 0.4)` to `rgba(0, 0, 0, 0.6)`)
- Border Top: 3px solid `rgba(255, 255, 255, 0.3)`
- Padding: 15px 20px
- Margin Top: 40px
- Text: Centered, bold, 1em, wide letter-spacing (2px)

**Usage Guidelines**:
- Keep text short and separated by bullets (•)
- Maintain uppercase styling
- Add 10px margin around each span for spacing

---

## Spacing & Layout

### Container Widths

#### Max-Width Standards
- **Extra Large**: `1200px`
  - Usage: `.header-content`, `.weather-main`, `.bottom-content`
  - Context: Primary content containers on large screens

- **Large**: `800px`
  - Usage: `.welcome-section`, `.error-message`
  - Context: Focused content panels

- **Medium**: `600px`
  - Usage: `.search-container`
  - Context: Form inputs and narrow content

### Padding Standards

#### Component Padding
- **Extra Large**: `50px`
  - Usage: `.welcome-content`
  - Context: Hero sections with lots of breathing room

- **Large**: `30px`
  - Usage: `.current-conditions`, `.explanations-section`, `.search-section`
  - Context: Major content panels

- **Medium**: `25px`
  - Usage: `.detail-box`, `.main-header`
  - Context: Standard component padding

- **Standard**: `20px`
  - Usage: `.error-message`, `.explanation-card`, body side padding
  - Context: Most common padding value

- **Small**: `15px`
  - Usage: `.search-input`, `.search-button`, `.bottom-bar`
  - Context: Compact components

- **Minimal**: `10px`
  - Usage: `.time-display`, `.section-title` (bottom), span margins
  - Context: Tight spacing

### Margin Standards

#### Vertical Spacing
- **Section Separation**: `30px`
  - Usage: Between major sections (`.current-conditions`, `.weather-details-grid`, `.explanations-section`)
  - Context: Clear visual separation

- **Large**: `40px`
  - Usage: `.bottom-bar` margin-top
  - Context: Pushes footer down

- **Welcome Section**: `50px`
  - Usage: `.welcome-section` top/bottom margin
  - Context: Centers empty state vertically

- **Medium**: `25px`
  - Usage: `.section-title` margin-bottom
  - Context: Space below headings

- **Standard**: `20px`
  - Usage: `.current-temp-display` margin-top, `.error-message` vertical margin
  - Context: Standard spacing

- **Small**: `15px`
  - Usage: `.explanation-card` margin-bottom
  - Context: Stacking similar components

- **Minimal**: `5px` to `10px`
  - Usage: Small gaps within components (`.channel-logo`, `.detail-label`, `.condition-text`)

#### Horizontal Spacing (Gap)
- **Large**: `40px`
  - Usage: `.current-temp-display` gap
  - Context: Major component separation

- **Medium**: `30px`
  - Usage: `.welcome-icons` gap (desktop)
  - Context: Icon spacing

- **Standard**: `20px`
  - Usage: `.weather-details-grid` gap, `.detail-box` gap
  - Context: Grid spacing

- **Small**: `10px`
  - Usage: `.search-form` gap
  - Context: Related form elements

### Border Standards

#### Border Widths
- **Extra Thick**: `5px`
  - Usage: `.main-header` bottom border
  - Context: Major visual separation, branding

- **Thick**: `4px`
  - Usage: `.current-conditions`, `.welcome-content` borders
  - Context: Primary content panels

- **Standard**: `3px`
  - Usage: Most borders (`.alerts-bar`, `.search-input`, `.search-button`, `.error-message`, `.detail-box`, etc.)
  - Context: Default border width for consistency

- **Thin**: `2px`
  - Usage: `.time-display`, `.explanation-card`
  - Context: Subtle borders for nested content

#### Border Radius
- **Large**: `10px`
  - Usage: `.current-conditions`, `.welcome-content`, `.explanations-section`
  - Context: Major panels

- **Standard**: `8px`
  - Usage: `.error-message`, `.detail-box`, `.explanation-card`
  - Context: Most rounded corners

- **Small**: `5px`
  - Usage: `.search-input`, `.search-button`
  - Context: Form elements and buttons

### Grid Systems

#### CSS Grid (Auto-fit Pattern)
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
```
**Usage**: `.weather-details-grid`  
**Behavior**: Automatically creates responsive columns that wrap  
**Min Column Width**: 250px  
**Max Columns**: As many as fit

#### Flexbox Patterns

**Horizontal Layout with Gap**:
```css
display: flex;
gap: 10px;
```
**Usage**: `.search-form`, `.current-temp-display`, `.detail-box`

**Centered Content**:
```css
display: flex;
justify-content: center;
gap: 30px;
```
**Usage**: `.welcome-icons`

**Vertical Flexbox**:
```css
display: flex;
flex-direction: column;
```
**Usage**: `.detail-content`

### Box Shadows

#### Heavy Shadow (Panels)
```css
box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
```
**Usage**: `.current-conditions`, `.welcome-content`  
**Context**: Creates strong depth for major panels

#### Medium Shadow (Cards)
```css
box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
```
**Usage**: `.detail-box`  
**Context**: Standard card depth

#### Standard Shadow (Buttons)
```css
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
```
**Usage**: `.search-button`, `.alerts-bar`, `.error-message`  
**Context**: Raised button effect

#### Hover Shadow (Enhanced)
```css
box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
```
**Usage**: `.search-button:hover`  
**Context**: Increased depth on hover

#### Active Shadow (Compressed)
```css
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
```
**Usage**: `.search-button:active`  
**Context**: Button pressed state

#### Header Shadow
```css
box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
```
**Usage**: `.main-header`  
**Context**: Separates header from body

#### Inset Shadow
```css
box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
```
**Usage**: `.search-input`  
**Context**: Creates recessed input appearance

### Spacing Guidelines

1. **Use consistent increments**: 5px, 10px, 15px, 20px, 25px, 30px, 40px, 50px
2. **Maintain rhythm**: Related elements should have similar spacing
3. **Breathe**: Don't be afraid of generous padding - it enhances the retro feel
4. **Stack spacing**: Use bottom margins for vertical stacking, not top margins
5. **Responsive reduction**: Reduce padding/margins by 30-50% on mobile

---

## Animations & Interactions

### Animation Principles

1. **Smooth Transitions**: Use `0.3s ease` as the default timing
2. **Playful Motion**: Bounces and lifts create personality
3. **Staggered Entrance**: Offset animation delays for sequential items
4. **Respect Accessibility**: Disable animations for users with `prefers-reduced-motion`

### Keyframe Animations

#### Scroll Animation
```css
@keyframes scroll-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
```
**Usage**: `.alerts-ticker`  
**Duration**: 30s  
**Timing**: `linear`  
**Iterations**: `infinite`  
**Purpose**: Creates infinite horizontal scrolling ticker

#### Bounce Animation
```css
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
```
**Usage**: `.weather-icon`  
**Duration**: 2s  
**Timing**: `ease-in-out`  
**Iterations**: `infinite`  
**Stagger**: 0.2s delay per icon (0s, 0.2s, 0.4s, 0.6s, 0.8s)  
**Purpose**: Playful bouncing weather icons

### Transition Effects

#### Standard Transition
```css
transition: all 0.3s ease;
```
**Usage**: `.search-button`, `.explanation-card`  
**Purpose**: Smooth hover effects on multiple properties

#### Transform Transition
```css
transition: transform 0.3s ease;
```
**Usage**: `.detail-box`  
**Purpose**: Isolated hover lift effect

#### Fade-In Animation
```css
opacity: 0;
transform: translateY(20px);

.animate-in {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
```
**Usage**: `.detail-box`  
**Purpose**: Entrance animation for content that loads dynamically

### Hover States

#### Button Hover (`.search-button:hover`)
- **Background**: Brighter gradient
- **Transform**: `translateY(-2px)` (lifts up)
- **Box Shadow**: Deeper shadow
- **Transition**: 0.3s ease

#### Card Hover (`.detail-box:hover`)
- **Transform**: `translateY(-5px)` (more dramatic lift)
- **Border Color**: Changes to yellow
- **Transition**: 0.3s ease

#### Explanation Card Hover (`.explanation-card:hover`)
- **Background**: Slightly brighter transparency
- **Border Color**: Changes to yellow
- **Transition**: 0.3s ease

### Active States

#### Button Active (`.search-button:active`)
- **Transform**: `translateY(0)` (returns to original position)
- **Box Shadow**: Compressed shadow (less elevation)
- **Purpose**: Tactile "pressed" feedback

### Focus States

#### Input Focus (`.search-input:focus`)
- **Outline**: None (custom border instead)
- **Border Color**: Yellow (`#ffcc00`)
- **Box Shadow**: Yellow glow `0 0 10px rgba(255, 204, 0, 0.5)`
- **Purpose**: Clear visual feedback for keyboard navigation

### Accessibility Considerations

#### Reduced Motion Media Query
```css
@media (prefers-reduced-motion: reduce) {
  .alerts-ticker {
    animation: none;
  }
  
  .weather-icon {
    animation: none;
  }
}
```

**Purpose**: Respects user preferences for reduced motion  
**Implementation**: Disables all looping animations  
**Scope**: Should be applied to:
- Infinite scrolling animations
- Bouncing/repeating icon animations
- Any animation longer than 0.5s

#### Focus Indicators
- Always provide visible focus states for keyboard navigation
- Use yellow glow effect to match brand colors
- Never remove outlines without providing alternative focus indicators

### Animation Timing Reference

| Duration | Use Case |
|----------|----------|
| `0.3s` | Standard hover transitions |
| `0.6s` | Fade-in entrance animations |
| `2s` | Icon bounce animations |
| `30s` | Infinite scrolling ticker |

### Easing Functions

| Function | Usage |
|----------|-------|
| `ease` | Default for most transitions (buttons, cards) |
| `ease-in-out` | Bounce animations (smoother acceleration/deceleration) |
| `linear` | Scrolling ticker (constant speed) |

### Implementation Guidelines

1. **Always add transitions to base state**, not hover state
2. **Use `transform` over positional properties** for better performance
3. **Combine multiple transforms** in a single property: `transform: translateY(-2px) scale(1.05);`
4. **Test reduced motion** media query with all animations
5. **Stagger delays** by 0.2s increments for sequential items
6. **Keep hover lifts subtle** (2-5px) to avoid jarring motion
7. **Compress shadows on active states** to simulate depth change

---

## Responsive Design

### Mobile-First Approach

This design system uses a **hybrid approach**: desktop-first CSS with mobile breakpoints for adjustments. Consider adopting true mobile-first in future iterations.

### Breakpoints

#### Tablet/Small Desktop: `768px`
```css
@media (max-width: 768px) { ... }
```

**Changes**:
- Logo: 3em → 2em
- Tagline: 1.2em → 1em
- Search form: Flex-direction changes to column
- Current temp display: Changes to vertical layout
- Temperature: 6em → 4em
- Temperature unit: 3em → 2em
- Condition text: 2em → 1.5em
- Location header: 2.5em → 2em
- Weather grid: Switches to single column
- Welcome icons: 3em → 2em, gap 30px → 15px
- Alert text: 14px → 12px, padding 40px → 20px

#### Mobile: `480px`
```css
@media (max-width: 480px) { ... }
```

**Changes**:
- Logo: 2em → 1.5em, letter-spacing 3px → 1px
- Temperature: 4em → 3em
- Temperature unit: 2em → 1.5em
- Detail value: 1.8em → 1.4em
- Section title: 2em → 1.5em

### Responsive Patterns

#### Grid to Single Column
```css
.weather-details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

@media (max-width: 768px) {
  .weather-details-grid {
    grid-template-columns: 1fr;
  }
}
```

#### Flex Direction Change
```css
.search-form {
  display: flex;
  gap: 10px;
}

@media (max-width: 768px) {
  .search-form {
    flex-direction: column;
  }
}
```

#### Stacked Layout
```css
.current-temp-display {
  display: flex;
  gap: 40px;
}

@media (max-width: 768px) {
  .current-temp-display {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
}
```

### Responsive Typography Scale

| Element | Desktop | Tablet (768px) | Mobile (480px) |
|---------|---------|----------------|----------------|
| Logo | 3em | 2em | 1.5em |
| Location Header | 2.5em | 2em | 2em |
| Section Title | 2em | 2em | 1.5em |
| Temperature | 6em | 4em | 3em |
| Temp Unit | 3em | 2em | 1.5em |
| Condition Text | 2em | 1.5em | 1.5em |
| Detail Value | 1.8em | 1.8em | 1.4em |
| Welcome Icons | 3em | 2em | 2em |

### Responsive Spacing Scale

- **Padding reduction**: 30-50% on mobile
- **Gap reduction**: 25-50% on mobile
- **Margin reduction**: Stay consistent or reduce by 20%

### Mobile Optimization Guidelines

1. **Single column layouts** on mobile (< 768px)
2. **Larger touch targets**: Minimum 44x44px for buttons
3. **Readable font sizes**: Never below 14px on mobile
4. **Generous padding**: Maintain at least 20px side padding
5. **Vertical stacking**: Convert horizontal layouts to vertical
6. **Simplified navigation**: Reduce complexity on small screens
7. **Test on real devices**: Emulators don't capture touch UX accurately

### Viewport Meta Tag

Always include in HTML:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Responsive Images

If adding images in the future:
```css
img {
  max-width: 100%;
  height: auto;
}
```

### Testing Checklist

- [ ] Test at 320px (smallest mobile)
- [ ] Test at 375px (iPhone SE)
- [ ] Test at 768px (tablet)
- [ ] Test at 1024px (small laptop)
- [ ] Test at 1440px+ (desktop)
- [ ] Test with browser zoom at 150% and 200%
- [ ] Test in portrait and landscape orientations

---

## Code Examples

### Example 1: Creating a New Weather Metric Card

```html
<div class="detail-box">
  <div class="detail-icon">🌙</div>
  <div class="detail-content">
    <span class="detail-label">MOON PHASE</span>
    <span class="detail-value conditions-value">Waxing Crescent</span>
  </div>
</div>
```

**Notes**:
- Use emoji for icons (3em size)
- Labels should be uppercase
- Use `.conditions-value` class for text values (applies capitalize and smaller size)
- Use `.detail-value` for numeric values

### Example 2: Creating a New Section with Cards

```html
<div class="explanations-section">
  <h3 class="section-title">FORECAST DETAILS</h3>
  
  <div class="explanation-card">
    <h4>🌅 Sunrise & Sunset</h4>
    <p>The sun rises at <strong>6:45 AM</strong> and sets at <strong>7:30 PM</strong> today.</p>
  </div>
  
  <div class="explanation-card">
    <h4>🌙 Moon Phase</h4>
    <p>Tonight's moon is a <strong>waxing crescent</strong>, visible in the western sky after sunset.</p>
  </div>
</div>
```

**CSS** (already included in system):
```css
.explanations-section { /* Dark panel with border */ }
.section-title { /* Yellow, centered, bordered heading */ }
.explanation-card { /* Light panel with hover effect */ }
```

### Example 3: Creating a Custom Button

```html
<button class="search-button" type="submit">
  GET FORECAST
</button>
```

**CSS** (follows existing pattern):
```css
.custom-button {
  padding: 15px 30px;
  font-size: 1.1em;
  font-weight: bold;
  background: linear-gradient(180deg, #ffcc00 0%, #ff9900 100%);
  color: #003d7a;
  border: 3px solid #fff;
  border-radius: 5px;
  cursor: pointer;
  text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.custom-button:hover {
  background: linear-gradient(180deg, #ffe033 0%, #ffaa00 100%);
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
}

.custom-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}
```

### Example 4: Adding Animation to New Elements

```html
<div class="detail-box" data-animate>
  <!-- Content -->
</div>
```

**JavaScript** (add to existing animation script):
```javascript
// Animate in detail boxes on page load
document.addEventListener('DOMContentLoaded', function() {
  const detailBoxes = document.querySelectorAll('.detail-box[data-animate]');
  
  detailBoxes.forEach((box, index) => {
    setTimeout(() => {
      box.classList.add('animate-in');
    }, index * 100); // Stagger by 100ms
  });
});
```

### Example 5: Creating a Custom Alert Banner

```html
<div class="custom-alert-bar">
  <div class="alerts-container">
    <div class="alerts-ticker">
      <span class="alert-text">🎉 SPECIAL ANNOUNCEMENT</span>
      <span class="alert-text">• YOUR MESSAGE HERE •</span>
      <span class="alert-text">🎉 SPECIAL ANNOUNCEMENT</span>
      <span class="alert-text">• YOUR MESSAGE HERE •</span>
    </div>
  </div>
</div>
```

**CSS** (create variant):
```css
.custom-alert-bar {
  background: linear-gradient(90deg, #0066cc 0%, #003d7a 50%, #0066cc 100%);
  border-bottom: 3px solid #fff;
  border-top: 3px solid #fff;
  overflow: hidden;
  position: relative;
  height: 35px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.custom-alert-bar .alerts-ticker {
  animation: scroll-left 30s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .custom-alert-bar .alerts-ticker {
    animation: none;
  }
}
```

### Example 6: Responsive Image Component

```html
<div class="weather-image-panel">
  <img src="radar.png" alt="Weather radar" class="responsive-image">
  <p class="image-caption">Local Radar - Last Updated 5:30 PM</p>
</div>
```

**CSS**:
```css
.weather-image-panel {
  background: linear-gradient(135deg, rgba(0, 102, 204, 0.7) 0%, rgba(0, 61, 122, 0.8) 100%);
  border: 4px solid rgba(255, 255, 255, 0.5);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
}

.responsive-image {
  width: 100%;
  height: auto;
  border-radius: 5px;
  border: 3px solid rgba(255, 255, 255, 0.3);
}

.image-caption {
  margin-top: 15px;
  font-size: 1.1em;
  font-weight: bold;
  text-align: center;
  color: #ffcc00;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
```

### Example 7: Common Class Combinations

**Large Temperature Display**:
```html
<div class="temp-large">
  <span class="temperature">72°</span>
  <span class="temp-unit">C</span>
</div>
```

**Detail Box with Text Value**:
```html
<div class="detail-box">
  <div class="detail-icon">🌤️</div>
  <div class="detail-content">
    <span class="detail-label">CONDITIONS</span>
    <span class="detail-value conditions-value">Partly Cloudy</span>
  </div>
</div>
```

**Detail Box with Numeric Value**:
```html
<div class="detail-box">
  <div class="detail-icon">💨</div>
  <div class="detail-content">
    <span class="detail-label">WIND SPEED</span>
    <span class="detail-value">15 km/h</span>
  </div>
</div>
```

**Section with Cards**:
```html
<div class="explanations-section">
  <h3 class="section-title">SECTION TITLE</h3>
  <div class="explanation-card">
    <h4>Card Title</h4>
    <p>Card content...</p>
  </div>
</div>
```

---

## Maintenance Guidelines

### Adding New Components

1. **Follow existing patterns**: Use similar structure to existing components
2. **Use the color palette**: Don't introduce new colors without updating this guide
3. **Maintain spacing standards**: Use the documented padding/margin values
4. **Add hover states**: Interactive elements should have feedback
5. **Test responsively**: Ensure component works on all breakpoints
6. **Document changes**: Update this guide when adding new patterns

### Updating Colors

1. **Global search and replace**: Colors are used in multiple places
2. **Test contrast**: Ensure WCAG AA compliance (4.5:1 for normal text)
3. **Update gradients**: Many gradients use multiple shades of the same color
4. **Check shadows**: Shadows may need adjustment with different backgrounds

### Modifying Typography

1. **Maintain hierarchy**: Font sizes should have clear relationships
2. **Scale responsively**: Update all breakpoints when changing sizes
3. **Test readability**: Ensure text remains legible at all sizes
4. **Update line heights**: May need adjustment for different fonts

### Refactoring Considerations

1. **CSS Custom Properties**: Consider converting hard-coded values to CSS variables for easier theming
2. **Component Library**: Extract reusable components into separate CSS files
3. **Utility Classes**: Create utility classes for common patterns (`.text-yellow`, `.gradient-blue`, etc.)
4. **CSS Preprocessor**: Consider Sass/SCSS for better organization and maintainability

---

## Browser Support

### Target Browsers
- **Chrome/Edge**: Last 2 versions
- **Firefox**: Last 2 versions
- **Safari**: Last 2 versions (iOS and macOS)
- **Mobile Browsers**: iOS Safari, Chrome Mobile

### CSS Features Used
- CSS Grid (with auto-fit)
- Flexbox
- CSS Gradients (linear)
- CSS Transitions
- CSS Animations (keyframes)
- Transform properties
- RGBA colors
- Media queries
- Box shadows
- Text shadows

### Fallbacks
- All browsers in scope support these features natively
- No polyfills required for modern browsers
- For older browsers (IE11), consider:
  - Flexbox fallbacks
  - Solid color backgrounds instead of gradients
  - Simplified shadows

---

## Accessibility Checklist

- [x] Color contrast meets WCAG AA standards (4.5:1 minimum)
- [x] Focus indicators visible for keyboard navigation
- [x] Reduced motion preferences respected
- [x] Semantic HTML structure (header, main, section, footer)
- [x] Form inputs have labels (via placeholder and context)
- [ ] **TODO**: Add ARIA labels where needed
- [ ] **TODO**: Ensure all interactive elements are keyboard accessible
- [ ] **TODO**: Test with screen readers
- [ ] **TODO**: Add skip navigation links

---

## Quick Reference

### Most Common Colors
- Primary Blue: `#0066cc`
- Primary Yellow: `#ffcc00`
- Alert Red: `#ff4444`
- White: `#fff`

### Most Common Spacing
- Standard Padding: `20px` to `30px`
- Standard Gap: `20px`
- Standard Border: `3px`
- Standard Border Radius: `8px`

### Most Common Transitions
```css
transition: all 0.3s ease;
transition: transform 0.3s ease;
```

### Most Common Hover Effects
```css
:hover {
  transform: translateY(-5px);
  border-color: #ffcc00;
}
```

### Most Common Gradients
```css
/* Blue panel */
background: linear-gradient(135deg, rgba(0, 102, 204, 0.8) 0%, rgba(0, 61, 122, 0.9) 100%);

/* Yellow button */
background: linear-gradient(180deg, #ffcc00 0%, #ff9900 100%);
```

---

## Version History

### Version 1.0 (Current)
- Initial style guide creation
- Documented all existing components
- Established color palette
- Defined typography system
- Documented animations and interactions
- Created responsive design guidelines
- Added code examples

---

## Contributing

When contributing to this design system:

1. **Read this guide thoroughly** before making changes
2. **Discuss major changes** with the team before implementing
3. **Update this guide** when adding new patterns or components
4. **Test responsively** on multiple devices and browsers
5. **Maintain consistency** with existing patterns
6. **Consider accessibility** in all design decisions
7. **Document your reasoning** for design choices

---

## Credits

**Design Inspiration**: The Weather Channel (2000s-2010s era)  
**Style Guide Created**: 2024  
**CSS Framework**: Custom (no external dependencies)  
**Design Philosophy**: Retro, bold, and playful with a professional edge

---

*This style guide is a living document. Keep it updated as the design system evolves.*
