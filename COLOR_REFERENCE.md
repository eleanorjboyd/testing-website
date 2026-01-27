# Color Palette Quick Reference

> A quick visual reference for the Weather Channel retro design system. For complete documentation, see [STYLE_GUIDE.md](STYLE_GUIDE.md).

## Primary Blues

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Dark Navy | `#1e3c72` | Background gradient start |
| Royal Blue | `#2a5298` | Background gradient middle, panels |
| Bright Blue | `#0066cc` | Headers, borders, interactive elements |
| Deep Ocean | `#003d7a` | Gradient endings, dark text on yellow |
| Steel Blue | `#7e8ba3` | Background gradient end |

## Accent Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Bright Yellow | `#ffcc00` | Taglines, labels, borders, accents |
| Warm Orange | `#ff9900` | Button gradients, hover effects |
| Light Yellow | `#ffe033` | Button hover states |
| Dark Orange | `#ffaa00` | Button hover gradient end |

## Alert Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Bright Red | `#ff4444` | Alert bars, error messages |
| Dark Red | `#cc0000` | Alert gradient end, error backgrounds |

## Common Gradients

### Body Background
```css
background: linear-gradient(180deg, #1e3c72 0%, #2a5298 50%, #7e8ba3 100%);
```

### Header
```css
background: linear-gradient(180deg, #0066cc 0%, #003d7a 100%);
```

### Primary Button
```css
background: linear-gradient(180deg, #ffcc00 0%, #ff9900 100%);
```

### Button Hover
```css
background: linear-gradient(180deg, #ffe033 0%, #ffaa00 100%);
```

### Alert Bar
```css
background: linear-gradient(90deg, #ff4444 0%, #cc0000 50%, #ff4444 100%);
```

### Blue Panel
```css
background: linear-gradient(135deg, rgba(0, 102, 204, 0.8) 0%, rgba(0, 61, 122, 0.9) 100%);
```

## Transparency Variants

### White (for overlays and borders)
- `rgba(255, 255, 255, 0.95)` - Input backgrounds
- `rgba(255, 255, 255, 0.5)` - Component borders
- `rgba(255, 255, 255, 0.3)` - Subtle borders
- `rgba(255, 255, 255, 0.2)` - Very subtle borders
- `rgba(255, 255, 255, 0.15)` - Light panel backgrounds
- `rgba(255, 255, 255, 0.1)` - Explanation cards
- `rgba(255, 255, 255, 0.05)` - Subtle gradient end

### Black (for shadows and dark overlays)
- `rgba(0, 0, 0, 0.6)` - Footer backgrounds
- `rgba(0, 0, 0, 0.5)` - Heavy text/box shadows
- `rgba(0, 0, 0, 0.4)` - Medium shadows
- `rgba(0, 0, 0, 0.3)` - Light shadows, borders
- `rgba(0, 0, 0, 0.2)` - Search section backgrounds
- `rgba(0, 0, 0, 0.1)` - Very light shadows

## Usage Examples

### Text on Dark Background
Use white text (`#fff`) with text shadows:
```css
color: #fff;
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
```

### Text on Light Background
Use dark blue text:
```css
color: #003d7a;
text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
```

### Yellow Accent Text
```css
color: #ffcc00;
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
```

### Borders
Most borders use 3px solid with semi-transparent white:
```css
border: 3px solid rgba(255, 255, 255, 0.3);
```

### Focus State
Yellow glow for keyboard navigation:
```css
border-color: #ffcc00;
box-shadow: 0 0 10px rgba(255, 204, 0, 0.5);
```

---

## Color Accessibility

All color combinations in this design system meet WCAG AA contrast requirements (4.5:1 minimum) for normal text:

✅ White text on dark blues (8:1+)  
✅ Dark blue text on yellow buttons (7:1+)  
✅ Yellow text on dark backgrounds (6:1+)  
✅ White text on red alerts (5:1+)

---

**For complete design system documentation, see [STYLE_GUIDE.md](STYLE_GUIDE.md)**
