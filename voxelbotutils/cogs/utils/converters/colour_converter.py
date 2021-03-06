import discord
from discord.ext import commands


"""
Shamlessly stolen from Wikipedia's list of colours articles which they have apparently,
as well as a random page on Github that seems to be a list of CSS colours as hex:
https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F
https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M
https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z
https://github.com/bahamas10/css-color-names/blob/master/css-color-names.json
"""


COLOURS_BY_NAME = {
    "kae blue": 0x5dadec,
    "ollie yellow": 0xf5e59d,
    "poop brown": 0x7a5901,
    "stegosans": 0xf1e6a9,
    "teddy purple": 0xb19cd9,
    "medusa green": 0x173b0b,

    # Below this point is directly copied from the Github link,
    # minus a bunch that were repeated colours later
    "alice blue": 0xf0f8ff,
    "antique white": 0xfaebd7,
    "aquamarine": 0x7fffd4,
    "beige": 0xf5f5dc,
    "bisque": 0xffe4c4,
    "black": 0x000001,
    "blanched almond": 0xffebcd,
    "blue": 0x0000ff,
    "blue violet": 0x8a2be2,
    "cadet blue": 0x5f9ea0,
    "chartreuse": 0x7fff00,
    "chocolate": 0xd2691e,
    "coral": 0xff7f50,
    "cornflower blue": 0x6495ed,
    "cornsilk": 0xfff8dc,
    "crimson": 0xdc143c,
    "cyan": 0x00ffff,
    "dark blue": 0x00008b,
    "dark cyan": 0x008b8b,
    "dark goldenrod": 0xb8860b,
    "dark grey": 0xa9a9a9,
    "dark khaki": 0xbdb76b,
    "dark magenta": 0x8b008b,
    "dark orange": 0xff8c00,
    "dark orchid": 0x9932cc,
    "dark red": 0x8b0000,
    "dark salmon": 0xe9967a,
    "dark sea green": 0x8fbc8f,
    "dark slate blue": 0x483d8b,
    "dark slate grey": 0x2f4f4f,
    "dark turquoise": 0x00ced1,
    "dark violet": 0x9400d3,
    "deep pink": 0xff1493,
    "deep sky blue": 0x00bfff,
    "dim grey": 0x696969,
    "dodger blue": 0x1e90ff,
    "floral white": 0xfffaf0,
    "forest green": 0x228b22,
    "frank green": 0x9acd32,
    "gainsboro": 0xdcdcdc,
    "ghost white": 0xf8f8ff,
    "goldenrod": 0xdaa520,
    "green yellow": 0xadff2f,
    "grey": 0x808080,
    "honeydew": 0xf0fff0,
    "hot pink": 0xff69b4,
    "indian red": 0xcd5c5c,
    "indigo": 0x4b0082,
    "ivory": 0xfffff0,
    "khaki": 0xf0e68c,
    "lavender": 0xe6e6fa,
    "lavender blush": 0xfff0f5,
    "lawn green": 0x7cfc00,
    "lemon chiffon": 0xfffacd,
    "light blue": 0xadd8e6,
    "light coral": 0xf08080,
    "light cyan": 0xe0ffff,
    "light goldenrod yellow": 0xfafad2,
    "light green": 0x90ee90,
    "light grey": 0xd3d3d3,
    "light pink": 0xffb6c1,
    "light salmon": 0xffa07a,
    "light sea green": 0x20b2aa,
    "light sky blue": 0x87cefa,
    "light slate grey": 0x778899,
    "light steel blue": 0xb0c4de,
    "light yellow": 0xffffe0,
    "lime green": 0x32cd32,
    "linen": 0xfaf0e6,
    "magenta": 0xff00ff,
    "malachite": 0x0bda51,
    "maroon": 0x800000,
    "medium blue": 0x0000cd,
    "medium orchid": 0xba55d3,
    "medium purple": 0x9370db,
    "medium sea green": 0x3cb371,
    "medium slate blue": 0x7b68ee,
    "medium spring green": 0x00fa9a,
    "medium turquoise": 0x48d1cc,
    "medium violet red": 0xc71585,
    "midnight blue": 0x191970,
    "mint cream": 0xf5fffa,
    "misty rose": 0xffe4e1,
    "moccasin": 0xffe4b5,
    "navajo white": 0xffdead,
    "old lace": 0xfdf5e6,
    "olive": 0x808000,
    "olive drab": 0x6b8e23,
    "ollie yellow": 0xf5e59d,
    "orange red": 0xff4500,
    "orchid": 0xda70d6,
    "pale goldenrod": 0xeee8aa,
    "pale green": 0x98fb98,
    "pale turquoise": 0xafeeee,
    "pale violet red": 0xdb7093,
    "papaya whip": 0xffefd5,
    "peach puff": 0xffdab9,
    "peru": 0xcd853f,
    "pink": 0xffc0cb,
    "poop brown": 0x7a5901,
    "powder blue": 0xb0e0e6,
    "rebecca purple": 0x663399,
    "red": 0xff0000,
    "rosy brown": 0xbc8f8f,
    "royal blue": 0x4169e1,
    "saddle brown": 0x8b4513,
    "salmon": 0xfa8072,
    "sandy brown": 0xf4a460,
    "sea green": 0x2e8b57,
    "seashell": 0xfff5ee,
    "silver": 0xc0c0c0,
    "sky blue": 0x87ceeb,
    "slate blue": 0x6a5acd,
    "slate grey": 0x708090,
    "snow": 0xfffafa,
    "spring green": 0x00ff7f,
    "steel blue": 0x4682b4,
    "stegosans": 0xf1e6a9,
    "tan": 0xd2b48c,
    "teal": 0x008080,
    "thistle": 0xd8bfd8,
    "tomato": 0xff6347,
    "turquoise": 0x40e0d0,
    "wheat": 0xf5deb3,
    "white": 0xffffff,
    "white smoke": 0xf5f5f5,
    "yellow": 0xffff00,
    "paynes grey": 0x536878,

    # Below this point is directly copied from the Wikipedia list of colours
    # APART FROM black, which has been changed from 0 to 1 because
    # of how Discord works out its colours
    "absolute zero": 18618,
    "acid green": 11583258,
    "aero": 8174056,
    "aero blue": 12642517,
    "african violet": 11699390,
    "air superiority blue": 7512257,
    "alabaster": 15592160,
    "alice blue": 15792383,
    "alloy orange": 12870160,
    "almond": 15720141,
    "amaranth": 15018832,
    "amaranth pink": 15834299,
    "amaranth purple": 11216719,
    "amaranth red": 13836589,
    "amazon": 3897943,
    "amber": 16760576,
    "amethyst": 10053324,
    "android green": 10798649,
    "antique brass": 13473141,
    "antique bronze": 6708510,
    "antique fuchsia": 9526403,
    "antique ruby": 8657709,
    "antique white": 16444375,
    "apple green": 9287168,
    "apricot": 16502449,
    "aquamarine": 8388564,
    "arctic lime": 13696788,
    "army green": 4936480,
    "artichoke": 9410425,
    "arylide yellow": 15324779,
    "ash gray": 11714229,
    "asparagus": 8890731,
    "atomic tangerine": 16750950,
    "auburn": 10824234,
    "aureolin": 16641536,
    "avocado": 5669379,
    "azure": 32767,
    "baby blue": 9031664,
    "baby blue eyes": 10603249,
    "baby pink": 16040642,
    "baby powder": 16711418,
    "banana mania": 16443317,
    "barbie pink": 14293124,
    "barn red": 8129026,
    "beau blue": 12375270,
    "beaver": 10453360,
    "beige": 16119260,
    "b'dazzled blue": 3037332,
    "big dip o\u00e2\u20ac\u2122ruby": 10233154,
    "bisque": 16770244,
    "bistre": 4008735,
    "bitter lemon": 13295629,
    "bitter lime": 12582656,
    "bittersweet": 16674654,
    "bittersweet shimmer": 12537681,
    "black": 1,
    "black bean": 4000770,
    "black chocolate": 1775633,
    "black coffee": 3878703,
    "black coral": 5530223,
    "black olive": 3882038,
    "black shadows": 12562354,
    "blanched almond": 16772045,
    "blast-off bronze": 10842468,
    "bleu de france": 3247335,
    "blizzard blue": 11331054,
    "blond": 16445630,
    "blood red": 6684672,
    "blue": 255,
    "blue bell": 10658512,
    "blue-green": 891066,
    "blue sapphire": 1204608,
    "blue yonder": 5272231,
    "bluetiful": 3959271,
    "blush": 14572931,
    "bole": 7947323,
    "bone": 14932681,
    "bottle green": 27214,
    "brandy": 8864063,
    "brick red": 13320532,
    "bright green": 6749952,
    "bright lilac": 14193135,
    "bright maroon": 12788040,
    "bright navy blue": 1668306,
    "brilliant rose": 16733603,
    "brink pink": 16474239,
    "british racing green": 16933,
    "bronze": 13467442,
    "brown": 8934411,
    "brown sugar": 11497037,
    "bud green": 8107617,
    "buff": 15785090,
    "burgundy": 8388640,
    "burlywood": 14596231,
    "burnished brown": 10582644,
    "burnt orange": 13391104,
    "burnt sienna": 15299665,
    "burnt umber": 9057060,
    "byzantine": 12399524,
    "byzantium": 7350627,
    "cadet": 5466226,
    "cadet blue": 6266528,
    "cadet grey": 9544624,
    "cadmium green": 27452,
    "cadmium orange": 15566637,
    "cadmium red": 14876706,
    "cadmium yellow": 16774656,
    "caf\u00e3\u00a9 noir": 4929057,
    "cambridge blue": 10731949,
    "camel": 12687979,
    "cameo pink": 15711180,
    "canary": 16777113,
    "canary yellow": 16772864,
    "candy apple red": 16713728,
    "candy pink": 14971258,
    "caput mortuum": 5842720,
    "cardinal": 12852794,
    "caribbean green": 52377,
    "carmine": 9830424,
    "carnation pink": 16754377,
    "carnelian": 11737883,
    "carolina blue": 5677267,
    "carrot orange": 15569185,
    "castleton green": 22079,
    "catawba": 7353922,
    "cedar chest": 13195849,
    "celadon": 11329967,
    "celadon blue": 31655,
    "celadon green": 3114108,
    "celeste": 11730943,
    "celtic blue": 2386894,
    "cerise": 14561635,
    "cerulean blue": 2773694,
    "cerulean frost": 7183299,
    "cg blue": 31397,
    "cg red": 14695473,
    "champagne": 16246734,
    "champagne pink": 15850959,
    "charcoal": 3556687,
    "charleston green": 2304811,
    "charm pink": 15110060,
    "cherry blossom pink": 16758725,
    "chestnut": 9782581,
    "china rose": 11030894,
    "chinese red": 11155486,
    "chinese violet": 8741000,
    "chinese yellow": 16757248,
    "chrome yellow": 16754432,
    "cinereous": 9994619,
    "cinnabar": 14893620,
    "cinnamon satin": 13459582,
    "citrine": 14995466,
    "citron": 10463519,
    "claret": 8329012,
    "cobalt blue": 18347,
    "coffee": 7294519,
    "columbia blue": 12179947,
    "cool grey": 9212588,
    "copper": 12088115,
    "copper penny": 11366249,
    "copper red": 13331793,
    "copper rose": 10053222,
    "coquelicot": 16726016,
    "coral": 16744272,
    "coral pink": 16286585,
    "cordovan": 8994629,
    "cornflower blue": 6591981,
    "cornsilk": 16775388,
    "cosmic cobalt": 3026312,
    "cosmic latte": 16775399,
    "coyote brown": 8479036,
    "cotton candy": 16760025,
    "cream": 16776656,
    "crimson": 14423100,
    "cyan": 65535,
    "cyber grape": 5784188,
    "cyber yellow": 16765696,
    "cyclamen": 16084897,
    "dark blue-gray": 6710937,
    "dark brown": 6636321,
    "dark byzantium": 6109524,
    "dark cornflower blue": 2507403,
    "dark cyan": 35723,
    "dark goldenrod": 12092939,
    "dark green": 78368,
    "dark jungle green": 1713185,
    "dark khaki": 12433259,
    "dark liver": 5458767,
    "dark magenta": 9109643,
    "dark moss green": 4873507,
    "dark olive green": 5597999,
    "dark orange": 16747520,
    "dark orchid": 10040012,
    "dark pastel green": 245820,
    "dark purple": 3152180,
    "dark red": 9109504,
    "dark salmon": 15308410,
    "dark sea green": 9419919,
    "dark sienna": 3937300,
    "dark sky blue": 9223894,
    "dark slate blue": 4734347,
    "dark spring green": 1536581,
    "dark turquoise": 52945,
    "dark violet": 9699539,
    "dartmouth green": 28732,
    "davy's grey": 5592405,
    "deep cerise": 14299783,
    "deep chestnut": 12144200,
    "deep jungle green": 19273,
    "deep pink": 16716947,
    "deep saffron": 16750899,
    "deep sky blue": 49151,
    "deep space sparkle": 4875372,
    "deep taupe": 8281696,
    "denim": 1401021,
    "denim blue": 2245558,
    "desert sand": 15583663,
    "dodger blue": 2003199,
    "dogwood rose": 14096488,
    "drab": 9859351,
    "duke blue": 156,
    "dutch white": 15720379,
    "earth yellow": 14788959,
    "ebony": 5594448,
    "eerie black": 1776411,
    "eggplant": 6373457,
    "eggshell": 15788758,
    "egyptian blue": 1062054,
    "electric blue": 8255999,
    "electric indigo": 7274751,
    "electric lime": 13434624,
    "electric purple": 12517631,
    "emerald": 5294200,
    "eminence": 7090306,
    "english green": 1789246,
    "english lavender": 11830165,
    "english red": 11225938,
    "english vermillion": 13387595,
    "english violet": 5651548,
    "erin": 65344,
    "eton blue": 9881762,
    "falu red": 8394776,
    "fandango": 11875209,
    "fandango pink": 14570117,
    "fashion fuchsia": 15990945,
    "fawn": 15051376,
    "feldgrau": 5070163,
    "fern green": 5208386,
    "field drab": 7099422,
    "fiery rose": 16733296,
    "firebrick": 11674146,
    "fire engine red": 13508649,
    "fire opal": 15293515,
    "flame": 14833698,
    "flax": 15654018,
    "flirt": 10616941,
    "floral white": 16775920,
    "fluorescent blue": 1438958,
    "french beige": 10910555,
    "french bistre": 8744269,
    "french blue": 29371,
    "french fuchsia": 16596882,
    "french lilac": 8806542,
    "french lime": 10419512,
    "french mauve": 13923284,
    "french pink": 16608414,
    "french raspberry": 13053000,
    "french rose": 16140938,
    "french sky blue": 7845374,
    "french violet": 8914638,
    "frostbite": 15283879,
    "fuchsia purple": 13384059,
    "fuchsia rose": 13058933,
    "fulvous": 14976000,
    "fuzzy wuzzy": 8864287,
    "gainsboro": 14474460,
    "gamboge": 14981903,
    "generic viridian": 32614,
    "ghost white": 16316671,
    "glaucous": 6324918,
    "glossy grape": 11244211,
    "go green": 43878,
    "gold": 10845184,
    "gold fusion": 8746318,
    "golden brown": 10052885,
    "golden poppy": 16564736,
    "golden yellow": 16768768,
    "goldenrod": 14329120,
    "granite gray": 6776679,
    "granny smith apple": 11068576,
    "green": 65280,
    "green-blue": 1139892,
    "green-cyan": 39270,
    "green lizard": 11007026,
    "green sheen": 7253665,
    "grullo": 11115142,
    "gunmetal": 2765881,
    "han blue": 4484303,
    "han purple": 5380346,
    "harlequin": 4194048,
    "harvest gold": 14323968,
    "heat wave": 16742912,
    "heliotrope": 14644223,
    "honeydew": 15794160,
    "honolulu blue": 28080,
    "hooker's green": 4815211,
    "hot magenta": 16719310,
    "hot pink": 16738740,
    "hunter green": 3497531,
    "iceberg": 7448274,
    "icterine": 16578398,
    "illuminating emerald": 3248503,
    "imperial red": 15542585,
    "inchworm": 11725917,
    "independence": 5001581,
    "india green": 1280008,
    "indian red": 13458524,
    "indian yellow": 14919767,
    "indigo": 4915330,
    "indigo dye": 16746,
    "iris": 5918671,
    "irresistible": 11748460,
    "isabelline": 16052460,
    "ivory": 16777200,
    "jade": 43115,
    "japanese carmine": 10299699,
    "japanese violet": 5976662,
    "jasmine": 16309886,
    "jazzberry jam": 10816350,
    "jet": 3421236,
    "jonquil": 16042518,
    "june bud": 12442199,
    "jungle green": 2730887,
    "kelly green": 5028631,
    "keppel": 3846302,
    "key lime": 15266956,
    "kobi": 15179716,
    "kobicha": 7029795,
    "kombu green": 3490352,
    "ksu purple": 5318792,
    "languid lavender": 14076637,
    "lapis lazuli": 2515356,
    "laurel green": 11123357,
    "lava": 13570080,
    "lavender blush": 16773365,
    "lavender gray": 12895184,
    "lawn green": 8190976,
    "lemon": 16774912,
    "lemon chiffon": 16775885,
    "lemon curry": 13410333,
    "lemon glacier": 16645888,
    "lemon meringue": 16181950,
    "lemon yellow": 16774223,
    "liberty": 5528231,
    "light blue": 11393254,
    "light coral": 15761536,
    "light cornflower blue": 9686250,
    "light cyan": 14745599,
    "light french beige": 13151615,
    "light goldenrod yellow": 16448210,
    "light green": 9498256,
    "light orange": 16701617,
    "light periwinkle": 12962785,
    "light pink": 16758465,
    "light salmon": 16752762,
    "light sea green": 2142890,
    "light sky blue": 8900346,
    "light steel blue": 11584734,
    "light yellow": 16777184,
    "lilac": 13148872,
    "lilac luster": 11442346,
    "lime green": 3329330,
    "lincoln green": 1661189,
    "linen": 16445670,
    "liseran purple": 14577569,
    "little boy blue": 7119068,
    "liver": 6769735,
    "liver chestnut": 9991254,
    "macaroni and cheese": 16760200,
    "madder lake": 13382454,
    "magenta": 16711935,
    "magenta haze": 10438006,
    "magic mint": 11202769,
    "magnolia": 15919319,
    "mahogany": 12599296,
    "maize": 16510045,
    "majorelle blue": 6312156,
    "malachite": 776785,
    "manatee": 9935530,
    "mandarin": 15956552,
    "mango": 16629250,
    "mango tango": 16745027,
    "mantis": 7652197,
    "mardi gras": 8913029,
    "marigold": 15376929,
    "mauve": 14725375,
    "mauve taupe": 9527149,
    "mauvelous": 15702186,
    "maximum blue": 4697036,
    "maximum blue green": 3194815,
    "maximum blue purple": 11316454,
    "maximum green": 6196273,
    "maximum green yellow": 14280272,
    "maximum purple": 7549824,
    "maximum red": 14229793,
    "maximum red purple": 10893945,
    "maximum yellow": 16448055,
    "maximum yellow red": 15907401,
    "may green": 5017921,
    "maya blue": 7586555,
    "medium aquamarine": 6741418,
    "medium blue": 205,
    "medium candy apple red": 14812716,
    "medium carmine": 11485237,
    "medium orchid": 12211667,
    "medium purple": 9662683,
    "medium sea green": 3978097,
    "medium slate blue": 8087790,
    "medium spring green": 64154,
    "medium turquoise": 4772300,
    "mellow apricot": 16300152,
    "melon": 16693933,
    "metallic gold": 13872951,
    "metallic seaweed": 687756,
    "metallic sunburst": 10255416,
    "mexican pink": 14942332,
    "middle blue": 8312038,
    "middle blue green": 9296332,
    "middle blue purple": 9138878,
    "middle grey": 9143936,
    "middle green": 5082199,
    "middle green yellow": 11321184,
    "middle purple": 14254773,
    "middle red": 15044211,
    "middle red purple": 10834771,
    "middle yellow": 16771840,
    "middle yellow red": 15511926,
    "midnight": 7349872,
    "midnight blue": 1644912,
    "mikado yellow": 16761868,
    "mimi pink": 16767721,
    "mindaro": 14940552,
    "ming": 3568765,
    "minion yellow": 16113744,
    "mint": 4109449,
    "mint cream": 16121850,
    "mint green": 10026904,
    "misty moss": 12301431,
    "misty rose": 16770273,
    "morning blue": 9282457,
    "moss green": 9083483,
    "mountain meadow": 3193487,
    "mountbatten pink": 10058381,
    "msu green": 1590587,
    "mulberry": 12929932,
    "mustard": 16767832,
    "myrtle green": 3242099,
    "mystic": 14045826,
    "mystic maroon": 11355001,
    "nadeshiko pink": 16166342,
    "naples yellow": 16439902,
    "navajo white": 16768685,
    "navy blue": 128,
    "neon blue": 4613887,
    "neon carrot": 16753475,
    "neon green": 3800852,
    "neon fuchsia": 16662884,
    "new york pink": 14123903,
    "nickel": 7500914,
    "non-photo blue": 10804717,
    "nyanza": 15335387,
    "ocean blue": 5194421,
    "ocean green": 4767633,
    "ochre": 13399842,
    "old burgundy": 4403246,
    "old gold": 13612347,
    "old lace": 16643558,
    "old lavender": 7956600,
    "old rose": 12615809,
    "old silver": 8684674,
    "olive": 8421376,
    "olive drab #7": 3945503,
    "olive green": 11907932,
    "olivine": 10140019,
    "onyx": 3487801,
    "opal": 11060156,
    "opera mauve": 12027047,
    "orange": 16744192,
    "orange peel": 16752384,
    "orange-red": 16738335,
    "orange soda": 16407357,
    "orange-yellow": 16104735,
    "orchid": 14315734,
    "orchid pink": 15908301,
    "outrageous orange": 16739914,
    "oxford blue": 8519,
    "ou crimson red": 8656407,
    "pacific blue": 1878473,
    "pakistan green": 26112,
    "palatinate purple": 6826080,
    "pale cerulean": 10208482,
    "pale pink": 16440029,
    "pale silver": 13222075,
    "pale spring bud": 15526845,
    "pansy purple": 7870538,
    "paolo veronese green": 39805,
    "papaya whip": 16773077,
    "paradise pink": 15089250,
    "pastel pink": 14591396,
    "patriarch": 8388736,
    "peach": 16770484,
    "peach puff": 16767673,
    "pear": 13754929,
    "pearly purple": 12019874,
    "periwinkle": 13421823,
    "permanent geranium lake": 14756908,
    "persian blue": 1849787,
    "persian green": 42643,
    "persian indigo": 3281530,
    "persian orange": 14258264,
    "persian pink": 16220094,
    "persian red": 13382451,
    "persian rose": 16656546,
    "persimmon": 15489024,
    "pewter blue": 9152695,
    "phlox": 14614783,
    "phthalo blue": 3977,
    "phthalo green": 1193252,
    "picotee blue": 3024775,
    "pictorial carmine": 12782414,
    "piggy pink": 16637414,
    "pine green": 96623,
    "pine tree": 2764579,
    "pink": 16761035,
    "pink flamingo": 16545021,
    "pink lace": 16768500,
    "pink lavender": 14201553,
    "pink sherbet": 16224167,
    "pistachio": 9684338,
    "platinum": 15066338,
    "plum": 9323909,
    "plump purple": 5850802,
    "polished pine": 6136979,
    "popstar": 12472162,
    "portland orange": 16734774,
    "powder blue": 11591910,
    "princeton orange": 16089125,
    "prune": 7347228,
    "prussian blue": 12627,
    "puce": 13404313,
    "pumpkin": 16741656,
    "purple": 6950317,
    "purple mountain majesty": 9861302,
    "purple navy": 5132672,
    "purple pizzazz": 16666330,
    "purple plum": 10244534,
    "purpureus": 10112686,
    "queen blue": 4418453,
    "queen pink": 15256791,
    "quick silver": 10921638,
    "quinacridone magenta": 9321049,
    "radical red": 16725342,
    "raisin black": 2367780,
    "rajah": 16493408,
    "raspberry": 14879581,
    "raw sienna": 14060121,
    "raw umber": 8545860,
    "razzle dazzle rose": 16724940,
    "razzmatazz": 14886251,
    "razzmic berry": 9260677,
    "rebecca purple": 6697881,
    "red": 16711680,
    "red-orange": 16733001,
    "red-purple": 14942328,
    "red salsa": 16595530,
    "redwood": 10771026,
    "resolution blue": 9095,
    "rhythm": 7829142,
    "rich black": 16448,
    "rifle green": 4475960,
    "robin egg blue": 52428,
    "rocket metallic": 9076608,
    "roman silver": 8620438,
    "rose": 16711807,
    "rose bonbon": 16335518,
    "rose dust": 10378863,
    "rose ebony": 6768710,
    "rose madder": 14886454,
    "rose pink": 16737996,
    "rose quartz": 11180201,
    "rose red": 12721750,
    "rose taupe": 9461085,
    "rose vale": 11226706,
    "rosewood": 6619147,
    "rosso corsa": 13893632,
    "rosy brown": 12357519,
    "royal purple": 7885225,
    "ruber": 13518454,
    "rubine red": 13697110,
    "ruby": 14684511,
    "ruby red": 10162462,
    "rufous": 11017223,
    "russet": 8406555,
    "russian green": 6787687,
    "russian violet": 3282765,
    "rust": 12009742,
    "rusty red": 14298179,
    "sacramento state green": 276775,
    "saddle brown": 9127187,
    "safety orange": 16742400,
    "safety yellow": 15651330,
    "saffron": 16041008,
    "sage": 12368010,
    "st. patrick's blue": 2304378,
    "salmon": 16416882,
    "salmon pink": 16748964,
    "sand": 12759680,
    "sandy brown": 16032864,
    "sap green": 5274922,
    "sapphire": 1004218,
    "sapphire blue": 26533,
    "satin sheen gold": 13345077,
    "scarlet": 16720896,
    "schauss pink": 16748975,
    "school bus yellow": 16766976,
    "screamin' green": 6750054,
    "sea green": 3050327,
    "seal brown": 5842443,
    "seashell": 16774638,
    "selective yellow": 16759296,
    "sepia": 7356948,
    "shadow": 9075037,
    "shadow blue": 7834533,
    "shamrock green": 40544,
    "sheen green": 9425920,
    "shimmering blush": 14255765,
    "shiny shamrock": 6268792,
    "shocking pink": 16519104,
    "sienna": 8924439,
    "silver": 12632256,
    "silver chalice": 11316396,
    "silver pink": 12889773,
    "silver sand": 12566978,
    "sinopia": 13320459,
    "sizzling red": 16726101,
    "sizzling sunrise": 16767744,
    "skobeloff": 29812,
    "sky blue": 8900331,
    "sky magenta": 13595055,
    "slate blue": 6970061,
    "slimy green": 2725399,
    "smitten": 13123974,
    "smoky black": 1051656,
    "snow": 16775930,
    "solid pink": 8992835,
    "sonic silver": 7697781,
    "space cadet": 1911121,
    "spanish bistre": 8418610,
    "spanish blue": 28856,
    "spanish carmine": 13697095,
    "spanish gray": 10000536,
    "spanish green": 37200,
    "spanish orange": 15229184,
    "spanish pink": 16236478,
    "spanish red": 15073318,
    "spanish violet": 4991106,
    "spanish viridian": 32604,
    "spring bud": 11009024,
    "spring frost": 8912682,
    "spring green": 65407,
    "star command blue": 31672,
    "steel blue": 4620980,
    "steel pink": 13382604,
    "steel teal": 6261387,
    "straw": 14997871,
    "sugar plum": 9522805,
    "sunglow": 16763955,
    "sunray": 14920535,
    "sunset": 16438949,
    "super pink": 13593513,
    "sweet brown": 11024177,
    "tan": 13808780,
    "tangerine": 15893760,
    "tart orange": 16469318,
    "taupe": 4734002,
    "taupe gray": 9143689,
    "tea green": 13693120,
    "teal": 32896,
    "teal blue": 3569032,
    "telemagenta": 13579382,
    "terra cotta": 14840411,
    "thistle": 14204888,
    "tickle me pink": 16550316,
    "tiffany blue": 703157,
    "timberwolf": 14407634,
    "titanium yellow": 15656448,
    "tomato": 16737095,
    "tropical rainforest": 30046,
    "true blue": 2975940,
    "trypan blue": 1836467,
    "tufts blue": 4099806,
    "tumbleweed": 14592648,
    "turquoise": 4251856,
    "turquoise blue": 65519,
    "turquoise green": 10540724,
    "tuscan red": 8144968,
    "tuscany": 12622233,
    "twilight lavender": 9062763,
    "tyrian purple": 6685244,
    "ua blue": 13226,
    "ua red": 14221388,
    "ultramarine": 4129023,
    "ultramarine blue": 4286197,
    "ultra pink": 16740351,
    "umber": 6508871,
    "unbleached silk": 16768458,
    "united nations blue": 6001381,
    "unmellow yellow": 16777062,
    "up forest green": 82977,
    "up maroon": 8065299,
    "upsdell red": 11411497,
    "uranian blue": 11525109,
    "usafa blue": 20376,
    "van dyke brown": 6701608,
    "vanilla": 15984043,
    "vanilla ice": 15962025,
    "vegas gold": 12956504,
    "venetian red": 13109269,
    "verdigris": 4436910,
    "vermilion": 14235678,
    "veronica": 10494192,
    "violet": 9371903,
    "violet-blue": 3295922,
    "violet-red": 16208788,
    "viridian": 4227693,
    "viridian green": 38552,
    "vivid burgundy": 10427701,
    "vivid sky blue": 52479,
    "vivid tangerine": 16752777,
    "vivid violet": 10420479,
    "volt": 13565696,
    "warm black": 16962,
    "wheat": 16113331,
    "white": 16777215,
    "wild blue yonder": 10661328,
    "wild orchid": 13922466,
    "wild strawberry": 16728996,
    "wild watermelon": 16542853,
    "windsor tan": 10966274,
    "wine": 7483191,
    "wine dregs": 6762823,
    "winter sky": 16711804,
    "wintergreen dream": 5671037,
    "wisteria": 13213916,
    "xanthic": 15658249,
    "xanadu": 7571064,
    "yale blue": 1002898,
    "yellow": 16776960,
    "yellow orange": 16756290,
    "yinmn blue": 3035280,
    "zaffre": 5288,
    "zomp": 3778446
}
COLOURS_BY_VALUE = {o:i for i, o in COLOURS_BY_NAME.items()}


class ColourConverter(commands.ColourConverter):

    COLOURS_BY_NAME = COLOURS_BY_NAME
    COLOURS_BY_VALUE = COLOURS_BY_VALUE

    def __init__(self, *, allow_custom_colour_names:bool=True, allow_default_colours:bool=True):
        self.allow_custom_colour_names = allow_custom_colour_names
        self.allow_default_colours = allow_default_colours

    async def convert(self, ctx, argument):
        if self.allow_custom_colour_names:
            v = COLOURS_BY_NAME.get(argument.lower().strip())
            if v:
                x = discord.Colour(value=v)
                # x.colour_name = v
                return x
        if self.allow_default_colours:
            return await super().convert(ctx, argument)
        raise commands.BadArgument()
