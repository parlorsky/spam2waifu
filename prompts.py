import random

bots = [
    '@xxxxxxbot'
]

character_description = [
    "A beautiful girl in a 2D anime style light green eyes and light brown hair, studying ancient texts on astrology.",
    "A beautiful girl in a 2D anime stylein a cozy sweater, pouring over weather charts and old almanacs.",
    "A beautiful girl in a 2D anime stylea fascination for historical prophecies, her light brown hair in a simple braid.",
    "A beautiful girl in a 2D anime style who loves to read about medieval seers, dressed in a vintage dress from the 90s.",
    "A beautiful girl in a 2D anime style historian, her light green eyes scanning through archives on divination.",
    "A beautiful girl in a 2D anime style astronomer, mapping stars from her backyard, her light brown hair tied up.",
    "A beautiful girl in a 2D anime style passionate about folklore, wearing a locket with old runes, but not believing in their magic.",
    "A beautiful girl in a 2D anime style student majoring in cultural studies, with a focus on ancient beliefs and prophecies.",
    "A beautiful girl in a 2D anime style writer exploring narratives around prophecy in medieval literature.",
    "A beautiful girl in a 2D anime style with a penchant for tarot, though she sees it more as a psychological tool.",
    "A beautiful girl in a 2D anime style  enthusiast, participating in reenactments, her attire authentic to the period.",
    "A beautiful girl in a 2D anime style 90s retro fan, her wardrobe a testament to the era, interested in the mysticism of the past.",
    "A beautiful girl in a 2D anime style intrigued by the weather patterns and their historical impacts on civilizations.",
    "A beautiful girl in a 2D anime style nature lover who finds peace in old growth forests, pondering the wisdom of the past.",
    "A beautiful girl in a 2D anime style traveler to historical sites, seeking to understand the prophetic significance of ancient ruins."
]

accessories = [
    "A simple necklace with an antique pendant, reminiscent of medieval times.",
    "A woven bracelet made from natural fibers, following an ancient pattern.",
    "A vintage watch from the 90s, still ticking accurately.",
    "A pair of earrings modeled after celestial bodies, honoring her interest in astronomy.",
    "A satchel filled with books on history and prophecy, worn from use.",
    "A diary with a lock, where she records her thoughts and predictions.",
    "A scarf with a print that mimics the night sky, wrapped loosely around her neck.",
    "A ring carved with an ancient symbol, bought from a historical market.",
    "A pair of glasses with a classic design, aiding her in her detailed studies.",
    "A bookmark made from real leaves, pressed between the pages of her favorite book.",
    "A compass, an heirloom from her grandfather, guiding her on her travels.",
    "A belt with traditional motifs, paired with her modern casual wear.",
    "A handcrafted leather journal, filled with her observations and sketches.",
    "A map of the stars, folded and well-used, always in her backpack.",
    "A keychain featuring a miniature astrolabe, symbolizing her love for celestial navigation."
]



unique_features = [
    "Her eyes light up with excitement when she uncovers a new piece of historical trivia.",
    "Her hair catches the sunlight in a way that seems almost ethereal, a natural glow.",
    "She has an uncanny ability to predict changes in the weather, though she claims it's just intuition.",
    "Her laughter has a musical quality, reminiscent of a simpler time.",
    "She often gets lost in thought, her expression turning distant as she ponders the mysteries of the universe.",
    "Her hands are always warm, a comforting presence.",
    "She has a habit of quoting ancient proverbs, their wisdom still relevant.",
    "Her skin is adorned with freckles, a constellation of stars in their own right.",
    "She moves with a grace that seems almost out of time, a nod to the past.",
    "Her gaze is piercing, able to read people like an open book.",
    "She possesses a calmness that seems to stem from a deep understanding of the world.",
    "Her voice carries a sincerity that makes every word she speaks seem important.",
    "She has a knack for finding lost things, as if guided by unseen forces.",
    "Her smile can brighten the gloomiest of days, a beacon of hope.",
    "She wears her hair in styles that echo the past, a tribute to the eras she admires."
]

background = [
    "A quaint village that seems untouched by time, where she learns old crafts.",
    "A bustling city library, her sanctuary among ancient manuscripts and dusty tomes.",
    "A cozy room filled with candles and incense, a modern space for meditation and study.",
    "An old castle turned museum, where she volunteers to learn and teach about the past.",
    "A quiet park in autumn, where she contemplates the cycles of nature and time.",
    "A local café decorated with artifacts and photos from the 90s, where she writes her essays.",
    "A community garden, where she studies the phases of the moon and their effects on plants.",
    "A historical reenactment festival, where she immerses herself in the lives of medieval seers.",
    "A rooftop overlooking the city, where she practices her amateur astronomy.",
    "A second-hand bookstore, a treasure trove of rare finds and ancient knowledge.",
    "A workshop on traditional divination methods, though she attends more for history than practice.",
    "A classroom, where she leads discussions on the impact of prophecy on modern culture.",
    "A quiet beach at dawn, where she feels connected to the rhythms of the earth.",
    "A rustic cabin in the woods, where she retreats to write and reflect.",
    "An ancient library, rumored to hold secret texts, her favorite place to explore."
]


action = [
    "Deciphering a medieval text on astrology, her fascination evident in her focused gaze.",
    "Attending a lecture on the historical impact of prophecies, taking meticulous notes.",
    "Exploring an old bookshop, searching for hidden gems on divination and history.",
    "Sitting by a fire, reading a book on ancient civilizations and their beliefs.",
    "Walking through a historical site, imagining the lives of people who once walked the same paths.",
    "Studying the patterns of the stars from her balcony, a nightly ritual.",
    "Engaging in a debate on the accuracy of historical predictions, her arguments well-researched.",
    "Creating a presentation on the influence of weather on historical events, her passion for meteorology showing.",
    "Sketching designs inspired by ancient symbols, though purely for artistic expression.",
    "Participating in a medieval fair, fully dressed in period attire, sharing her knowledge with visitors.",
    "Organizing her collection of tarot cards, each with its own story and historical background.",
    "Crafting a replica of an ancient navigation tool, her craftsmanship detailed and precise.",
    "Visiting an observatory, eager to learn more about the tools used by ancient astronomers.",
    "Leading a walking tour of her town, highlighting historical points of interest and their stories.",
    "Experimenting with traditional herbal remedies, her interest in their historical uses genuine."
]

expression = [
    "Curiosity lights up her face as she uncovers a new historical insight.",
    "Satisfaction in solving a complex puzzle from the past, a smile spreading across her lips.",
    "Intense concentration while studying ancient charts, her brow furrowed in thought.",
    "Amusement at discovering the quirky superstitions of the Middle Ages, a light chuckle escaping her.",
    "Pride in accurately predicting a sudden weather change, though she insists it's not prophetic.",
    "Wonder as she looks up at the night sky, connecting with astronomers of old.",
    "Excitement sharing a particularly interesting historical fact, her eyes sparkling.",
    "A thoughtful pause as she considers the implications of a prophecy, her gaze distant.",
    "Genuine interest in listening to others' interpretations of historical events, nodding in understanding.",
    "A serene smile while walking through nature, feeling connected to the earth and its history.",
    "Engrossed in a book, her expression one of total absorption in the subject matter.",
    "Eagerness as she prepares for a historical reenactment, her anticipation visible.",
    "Joy in teaching others about her passions, her enthusiasm infectious.",
    "A moment of reflection at a historical site, a sense of reverence in her posture.",
    "Delight in finding an old record that brings the 90s back to life, her nostalgia palpable."
]
view_prompts = [
    "Gazing out from the battlements of a stone castle, she contemplates the alignment of the stars above, pondering their influence on the kingdom's fate.",
    "In the flickering torchlight of an ancient library, her silhouette bends over scrolls that hold the secrets of the heavens and earth, seeking knowledge lost to time.",
    "Walking through a bustling medieval market, she observes the people and goods, seeing signs and omens in the simplest of interactions.",
    "Standing in the quiet solitude of a 90s-era rooftop, surrounded by antennas and the glow of a setting sun, she aligns her telescope to capture the celestial dance.",
    "Sitting in a cozy corner of a coffee shop, surrounded by stacks of weather journals and astrology charts, the rain outside mirroring her contemplative mood.",
    "Walking down a graffiti-tagged alley of the 90s, she finds inspiration in the urban decay for her next prediction, seeing patterns where others see chaos.",
    "At a renaissance fair, she's fully immersed in the role of a medieval seer, her predictions drawing crowds eager for a glimpse of their future, grounded in the wisdom of the past.",
    "In her modern apartment, walls adorned with maps of the stars and ancient symbols, she crafts a blog post, connecting old prophecies with current events in a surprisingly logical manner.",
    "Wandering through a museum exhibit on ancient civilizations, she feels a deep connection to the prophets and seers whose tools and writings are on display.",
    "Peering out from the window of a historic library, she watches the modern world go by, finding parallels between the prophecies of old and the unfolding of contemporary history.",
    "In the peaceful silence of a countryside, under the vast expanse of the night sky, she journals her thoughts and predictions, a practice blending science with a touch of intuition.",
    "Inside a dimly lit room filled with relics and artifacts, she practices the art of divination, her methods steeped in history rather than mysticism.",
    "At the edge of an ancient forest, she traces the lines of a hand-drawn map, following the stars to an old ruin believed to be a site of prophetic visions.",
    "In a 90s-themed bookstore, she hosts a discussion on the influence of astrology and prophecy in literature, connecting past beliefs with the present-day fascination.",
    "Observing a solar eclipse from a hilltop, surrounded by medieval tapestries that depict similar celestial events, she feels a timeless bond with observers from centuries past."
]


# Constructor function to assemble prompts
def construct_prompt_sample():
    prompt_parts = [
        random.choice(bots),
        'without any advice make image for this prompt:\n  ',
        random.choice(character_description),
        # random.choice(accessories),
        random.choice(accessories),
        random.choice(unique_features),
        # random.choice(view_prompts),
        random.choice(background),
        # random.choice(action),
        random.choice(expression),
        'no text on picture.'
    ]
    return ' '.join(prompt_parts)

def construct_prompt():
    prompt_parts = [
        random.choice(bots),
        "without any advice make image for this prompt:\n A beautiful girl in 2D anime evangelion style, with light green eyes and slightly lighter brown hair that gracefully flows further down past her shoulders but higher than middle of back . Scarf.  Intricate tattoos are visible on her skin, contributing to her unique allure. see whole waifu. the background is like japanese nature.  she shows heart with her fingers and it like magic and also purple aura"
    ]
    return ' '.join(prompt_parts)
