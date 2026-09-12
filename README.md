# Zodiac Copy Collection

An original, ready-to-use writing bank for zodiac-themed products aimed at ages 16–22.

The collection contains 252 creative pieces across all 12 Western tropical zodiac signs:

- 120 punchy one-liners
- 96 affirmations and forward-looking predictions
- 36 four-line micro-poems

## Sign index

| Sign | Matter |
|---|---|
| Aries | [aries/matter.json](aries/matter.json) |
| Taurus | [taurus/matter.json](taurus/matter.json) |
| Gemini | [gemini/matter.json](gemini/matter.json) |
| Cancer | [cancer/matter.json](cancer/matter.json) |
| Leo | [leo/matter.json](leo/matter.json) |
| Virgo | [virgo/matter.json](virgo/matter.json) |
| Libra | [libra/matter.json](libra/matter.json) |
| Scorpio | [scorpio/matter.json](scorpio/matter.json) |
| Sagittarius | [sagittarius/matter.json](sagittarius/matter.json) |
| Capricorn | [capricorn/matter.json](capricorn/matter.json) |
| Aquarius | [aquarius/matter.json](aquarius/matter.json) |
| Pisces | [pisces/matter.json](pisces/matter.json) |

## Folder structure

```text
zodiac-copy-collection/
├── README.md
├── aries/matter.json
├── taurus/matter.json
├── gemini/matter.json
├── cancer/matter.json
├── leo/matter.json
├── virgo/matter.json
├── libra/matter.json
├── scorpio/matter.json
├── sagittarius/matter.json
├── capricorn/matter.json
├── aquarius/matter.json
└── pisces/matter.json
```

## JSON shape

Each `matter.json` file follows the same structure:

```json
{
  "sign": "Aries",
  "audience": "16-22",
  "language": "English",
  "tradition": "Western tropical zodiac archetypes",
  "editorial_note": "...",
  "matter": {
    "one_liners": ["..."],
    "affirmations_predictions": ["..."],
    "micro_poems": [
      ["line 1", "line 2", "line 3", "line 4"]
    ]
  }
}
```

## Editorial direction

The copy is concise, contemporary, warm, and slightly self-aware. It uses recognisable sign archetypes while avoiding the most tired one-note caricatures. For example, Aries is not reduced to anger, Cancer is not reduced to crying, Leo is not reduced to attention-seeking, and Aquarius is not reduced to emotional coldness.

Every line in the repository is original. Online astrology communities were used only to study the jokes people recognise, the stereotypes they dislike, and the language patterns that feel current. No community post was copied into the collection.

The astrological framing follows the Western tropical sign archetypes documented by the open-source [Astro engine](https://github.com/aryaminus/astro). This is creative sign-level content, not an individual birth-chart reading or a factual prediction about a specific person.

## Suggested uses

- Sticker captions and packaging copy
- Social posts, carousels, and short-form video overlays
- Bios, wallpapers, postcards, and apparel
- Zodiac apps, quizzes, and editorial calendars

## Status

Written matter is complete. Visual sticker assets are intentionally excluded from this release and can be added later without changing the JSON schema.
