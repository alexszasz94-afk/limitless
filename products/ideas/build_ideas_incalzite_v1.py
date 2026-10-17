"""100 invented product ideas for LIMITLESS (17 oct 2026). Scored 0-100 on our criteria (docs/09-reguli-produs.md + what sells for us:
identity/character + warmth + gift + instant demo + one size). Output: ideas.json (for the board collection `ideas`)."""
import json, re
W = dict(E=2.5, D=2.0, G=1.5, M=1.5, P=1.0, N=1.0, R=0.5)  # emotion, demo in 1-3 s, gift/season, price & margin, easy to film with AI, few competitors, low return risk
I = []
def add(name, cat, price, emo, hook, demo, why, risk, E, D, G, M, P, N, R):
    I.append(dict(name=name, category=cat, price=price, emotions=emo, hook=hook, demo=demo, why=why, risk=risk,
                  scores=dict(E=E, D=D, G=G, M=M, P=P, N=N, R=R)))

C1 = "Heated character robes"
add("Heated Mermaid Tail Blanket", C1, 69, ["nostalgia", "identity", "mom & daughter"], "POV: you finally became the mermaid you always wanted to be 🧜‍♀️",
    "Slides legs in, scales shimmer, presses the button, sighs warm", "Mermaid-tail blankets already went viral; a HEATED one barely exists. Same identity + warmth formula as our princess robe, one size, perfect Christmas gift for women 25-45 and their daughters.", "Sequins drift in AI video - use printed velvet scales", 10, 9, 9, 8, 8, 9, 9)
add("Heated Gingerbread Robe", C1, 79, ["cute", "Christmas", "humor"], "Me after eating the whole gingerbread house 🍪",
    "Turns around: icing trim, gumdrop buttons, cookie-brown plush", "Same proven robe body as HeatGrump with a no-IP Christmas character. Instantly readable, kids + adults, very shareable.", "Must not look like a costume - keep it cozy", 9, 9, 10, 8, 9, 8, 8)
add("Heated Reindeer Robe with Light-up Nose", C1, 79, ["humor", "Christmas", "family"], "Dad said he's not wearing it. Dad is wearing it. 🦌",
    "Presses nose, it glows red, antler hood goes up", "A 2-second gag (nose lights up) that stops the scroll, plus the robe we already know how to sell. Great for 'dad' humor angle.", "Light-up nose battery adds a part", 9, 10, 10, 8, 8, 8, 8)
add("Heated Snow Queen Robe (ice blue)", C1, 89, ["identity", "royalty", "nostalgia"], "Every girl who wanted to be the ice queen is now 30 and cold 👑❄️",
    "Ice-blue sherpa cape robe sparkles, she twirls, then cuddles in", "Princess robe formula, new palette that pairs with Heat Majesty as a 2nd variant; strong nostalgia without naming any movie.", "Stay far from any movie design (no snowflake cape copy)", 9, 8, 9, 9, 8, 7, 8)
add("Heated Dragon Robe (spiky hood, wings)", C1, 85, ["identity", "fantasy", "humor"], "Unlocked: dragon mode. Heat level 3 🐉",
    "Hood with spikes, wing sleeves open like wings", "Fantasy fans and gamers; wings opening is a natural hook. Men 20-35 are an untapped robe audience.", "Wings need clean pattern", 8, 9, 8, 8, 7, 8, 8)
add("Heated Unicorn Robe", C1, 75, ["cute", "kids", "mom & daughter"], "My daughter wanted a unicorn. I wanted a heated robe. We both won 🦄",
    "Pastel rainbow mane hood, horn, glitter cuffs", "Evergreen girl theme, matching mom/kid sizes, easy demo.", "Crowded in kids' onesies - win on 'heated'", 8, 8, 9, 8, 9, 6, 8)
add("Heated Bear Hug Robe", C1, 79, ["comfort", "couples", "cozy"], "When he's at work but you still want a bear hug 🐻",
    "Teddy-bear ears hood, arms of the robe 'hug' back", "Warm 'hug' feeling = strongest comfort emotion; works for women gifting themselves.", "Generic look - needs a signature detail", 8, 7, 9, 8, 9, 6, 8)
add("Heated Yeti Robe (extra fluffy white)", C1, 85, ["humor", "winter", "identity"], "Dressed as the abominable snowman because I am abominably cold ❄️",
    "Huge fluffy white robe, face peeks out of the hood", "Funny winter character, visually loud, a natural pair with 'monster feet' slippers.", "Long fur sheds - specify short faux fur", 8, 9, 8, 8, 8, 8, 7)
add("Heated Polar Bear Robe", C1, 79, ["cute", "winter", "family"], "Polar bear mode: activated 🐻‍❄️",
    "White bear ears hood, black nose, sits by the fire", "Cute Christmas animal, unisex, family matching packs.", "Close to generic onesies", 7, 7, 9, 8, 9, 6, 8)
add("Heated Nutcracker Soldier Robe", C1, 85, ["Christmas", "nostalgia", "humor"], "Guarding the couch all winter 🎖️",
    "Red jacket robe with gold buttons, tall black hat hood", "Classic Christmas icon with no IP, very photogenic, stands out from fluffy robes.", "Hat shape must be soft, not stiff", 8, 8, 10, 8, 8, 9, 7)
add("Heated Elf Robe with Pointy Ears Hood", C1, 75, ["Christmas", "humor", "family"], "Santa's least productive elf reporting for nap duty 🧝",
    "Green robe, striped cuffs, ears flop on the hood", "Family matching Christmas pyjama culture + heat; funny for office parties.", "Seasonal only", 8, 8, 10, 8, 9, 7, 8)
add("Heated Wizard Robe with Star Hood", C1, 85, ["fantasy", "nostalgia", "identity"], "Studying for my exams like a real wizard ✨",
    "Long midnight-blue robe with stars, tall pointed hood", "Wizard-school nostalgia without names; students + adults; dark, elegant colours.", "Avoid house crests and school colours", 8, 7, 8, 8, 8, 7, 8)
add("Heated Fairy Robe with Wing Cape", C1, 85, ["identity", "cute", "girls"], "Fairy godmother era begins tonight 🧚",
    "Pastel robe, sheer wing-shaped cape opens", "Princess-adjacent identity for women, 'cottage core' trend.", "Sheer fabric must stay cozy", 8, 8, 8, 8, 7, 7, 8)
add("Heated Mrs. Claus Robe", C1, 85, ["Christmas", "mom", "nostalgia"], "Mrs. Claus does NOT do cold mornings ❤️",
    "Red velvet robe, white fur trim, little apron bow", "Christmas identity for moms and grandmas; elegant, gift-able, no IP.", "Seasonal; could look like costume", 8, 8, 10, 8, 9, 8, 8)
add("Heated Santa Robe for Dads", C1, 85, ["humor", "dad", "Christmas"], "Dad finally found a Santa suit he'll actually wear 🎅",
    "Big red robe, white trim, black belt, hat hood", "Dad gift angle (hard to shop for), pairs with Mrs. Claus as couples set.", "Sizing for men - offer XL", 8, 8, 10, 8, 9, 7, 7)
add("Heated Cat Robe with Ears & Tail", C1, 75, ["cute", "pets", "identity"], "When your cat judges you, so you become the cat 🐱",
    "Ears hood, little tail swings when she walks", "Cat lovers are a huge emotional audience; tail swing = demo.", "Tail must be short (tripping)", 8, 8, 8, 8, 9, 7, 8)
add("Heated Bunny Robe (floppy ears)", C1, 75, ["cute", "Easter", "kids"], "Bunny ears up = heat level up 🐰",
    "Floppy ears hood that perk up with a pull-string", "Works past Christmas (Easter), cute for mom & daughter sets.", "Pull-string ears add cost", 7, 8, 7, 8, 8, 7, 8)
add("Heated Penguin Robe", C1, 75, ["cute", "winter", "humor"], "Waddling to the kitchen at 2 am like 🐧",
    "Black and white robe, orange beak hood, waddle walk", "Cute winter animal + funny waddle demo, unisex.", "Similar to onesies", 7, 9, 9, 8, 9, 6, 8)
add("Heated Monster Robe (furry, big eyes)", C1, 79, ["humor", "kids", "family"], "Feed me cookies or nobody gets warm 👹",
    "Bright furry robe, big googly eyes on the hood", "Funny 'monster' character that kids love, no IP.", "Avoid looking like known puppets", 7, 9, 8, 8, 8, 7, 8)
add("Heated Sloth Robe (slow, lazy, warm)", C1, 75, ["humor", "self-care", "identity"], "Productivity level: sloth. Warmth level: maximum 🦥",
    "Brown fluffy robe, sloth face hood, slow-motion walk", "Lazy-day humor resonates with tired moms and students.", "Niche look", 7, 8, 8, 8, 9, 8, 8)

C2 = "Couples & family"
add("Heated Couple Hoodie Blanket (two hoods)", C2, 89, ["couples", "humor", "togetherness"], "Stop stealing the blanket. Now we share ONE 🫶",
    "Two heads pop out of one giant heated hoodie", "Couples gift, funny in 1 second, high price, one size fits two.", "Large item, higher shipping", 9, 10, 9, 9, 7, 8, 8)
add("Matching Mom & Me Heated Robe Set", C2, 119, ["mom & daughter", "family", "gift"], "Twinning with my mini, both toasty 💕",
    "Mom and kid in identical robes, both press the button", "Bundle raises AOV; mom/kid content gets huge emotional reach.", "Kids' heated items need extra safety specs", 9, 8, 10, 9, 7, 7, 7)
add("Heated Family Movie Night Mega Blanket", C2, 129, ["family", "togetherness", "Christmas"], "Family of 5. One blanket. Zero complaints 🍿",
    "Whole family under one huge heated blanket on the sofa", "Christmas-morning family moment, big ticket.", "Bulky, lower novelty", 8, 8, 9, 9, 8, 6, 8)
add("His & Hers Heated Robes (grumpy + royal)", C2, 159, ["couples", "humor", "gift"], "He's the grump. I'm the princess. We're both warm.",
    "Couple side by side in HeatGrump + Heat Majesty", "Cross-sell our two robes as a couples bundle - no new product needed.", "Shipping two units", 8, 8, 10, 9, 10, 9, 8)
add("Heated Matching Christmas Pajama Robe for Dogs & Owners", C2, 99, ["pets", "family", "cute"], "Me and my dog, matching and toasty 🐶",
    "Owner and dog in matching plaid robes", "Pet-owner matching is a huge Christmas trend; adds a pet SKU.", "Pet sizes add complexity", 9, 8, 9, 8, 7, 7, 7)
add("Heated Long-Distance Hug Pillow (two pillows, touch to warm)", C2, 99, ["love", "distance", "emotion"], "He touches his pillow in Texas. Mine warms up in Ohio 🥹",
    "She hugs pillow, it glows and warms; cut to him across the country", "Very strong emotion; tech gift for couples. Needs an app - harder to source.", "Electronics + app = supplier risk", 10, 8, 9, 9, 5, 9, 5)
add("Heated Grandma Shawl with Embroidered Names", C2, 69, ["grandma", "personalized", "gift"], "Grandma cried when she saw all our names on it 🥹",
    "Grandma opens box, names of grandkids embroidered, she wraps it on", "Personalisation + grandma tears = viral emotion; high perceived value.", "Personalisation slows production", 10, 8, 10, 8, 7, 8, 8)
add("Matching Sibling Heated Ponchos", C2, 99, ["kids", "family", "cute"], "The only time my kids agreed on something 😂",
    "Two kids in matching hooded ponchos high-five", "Funny parent angle, bundle.", "Kids' safety specs", 7, 8, 8, 8, 8, 7, 7)

C3 = "Feet & hands"
add("Heated Monster Feet Slipper Boots", C3, 49, ["humor", "cold feet", "gift"], "My wife's feet were ice cold. Were. 👹",
    "Huge fluffy monster paws stomp, she plugs in and wiggles toes", "Cold-feet complaint is universal; funny visual; cheap gift.", "Sizing returns - one-size boot", 9, 10, 9, 7, 8, 8, 7)
add("Heated Bear Paw Slippers", C3, 45, ["cute", "cold feet", "cozy"], "Bear paws > cold floors 🐾",
    "Fluffy paw slippers with claws, warm glow", "Cute, cheap, impulse gift.", "Many similar slippers", 7, 9, 9, 6, 9, 5, 7)
add("Heated Foot Pocket Blanket (sofa footwarmer bag)", C3, 59, ["cold feet", "self-care", "cozy"], "Put your feet in the warm pocket. Thank me later.",
    "Feet slide into a fluffy heated pocket at the end of the sofa", "Clear problem-solution demo, women 30+.", "Lower emotion", 7, 9, 8, 7, 9, 7, 8)
add("Heated Mitten for Two (couples hand-holding mitten)", C3, 39, ["couples", "romance", "winter"], "Holding hands in -10°C. One mitten. Heated. 🫶",
    "Couple walks, hands joined inside one heated mitten", "Romantic winter walk gift, funny + sweet in 1 second.", "Low price - needs bundle", 9, 10, 9, 6, 8, 8, 9)
add("Heated Hand-Warmer Muff (Victorian style)", C3, 49, ["elegance", "winter", "nostalgia"], "Main character energy, warm hands edition ❄️",
    "She slides hands into a fluffy round muff, steam breath", "Elegant 'old money' winter look, royal line add-on.", "Small niche", 7, 8, 8, 7, 8, 9, 9)
add("Heated Pom-Pom Socks with Remote", C3, 39, ["cozy", "cold feet", "gift"], "Cold feet club is officially closed 🧦",
    "Socks glow warm on thermal camera", "Thermal camera shot = instant proof.", "Heated socks are crowded", 6, 9, 9, 6, 9, 4, 7)
add("Heated Bunny Slipper with Ears that Flop", C3, 45, ["cute", "kids", "gift"], "Every step = ears flop 😂",
    "Ears flop on every step", "Motion demo + cute.", "Cheap category", 7, 9, 8, 6, 9, 6, 7)

C4 = "Pets"
add("Heated Pet Robe Matching Our Robes", C4, 49, ["pets", "cute", "family"], "My dog in a tiny heated robe. I can't. 🐶",
    "Small dog trots in a mini green/royal robe", "Extends HeatGrump/Heat Majesty; pet content gets massive reach.", "Pet heating must be low-temp", 9, 9, 9, 7, 8, 7, 7)
add("Heated Cat Tent Igloo", C4, 59, ["pets", "cute", "comfort"], "My cat moved out of my bed and into her igloo 🐱",
    "Cat walks in, curls up, thermal glow", "Cat videos = top engagement; owners love gifting pets.", "Pet products have competitors", 8, 8, 8, 7, 8, 6, 8)
add("Heated Dog Bed Shaped Like a Sofa", C4, 89, ["pets", "home", "cozy"], "He has a better sofa than me now 😂",
    "Dog climbs on a mini heated sofa", "Funny, high price.", "Bulky shipping", 7, 8, 8, 8, 8, 6, 7)
add("Heated Pet Hoodie for Walks", C4, 39, ["pets", "winter", "cute"], "Winter walks without the shivers 🐕",
    "Dog in hoodie in snow, owner zooms in", "Cheap add-on; winter need.", "Low price", 6, 8, 8, 5, 8, 5, 7)
add("Cat Ear Heated Hoodie for Cat Moms", C4, 69, ["pets", "identity", "cute"], "Cat mom uniform: activated 🐾",
    "Woman with cat, both 'wearing' ears", "Identity for cat moms.", "Simple product, easy to copy", 7, 7, 8, 7, 9, 6, 8)

C5 = "Home cozy & self-care"
add("Heated Weighted Hug Plush (giant)", C5, 69, ["comfort", "anxiety relief", "self-care"], "When you need a hug but everyone's busy 🤍",
    "She hugs a giant plush, it warms her", "Comfort + anxiety niche, strong emotion, women & teens.", "Weighted + heat = heavier shipping", 9, 8, 8, 8, 8, 7, 8)
add("Heated Reading Nook Cape with Book Pocket", C5, 79, ["self-care", "book lovers", "identity"], "BookTok, but make it warm 📚",
    "Cape wraps, book slides into a front pocket", "BookTok community is huge and gifts a lot.", "Pocket design detail", 8, 8, 8, 8, 8, 9, 8)
add("Heated Lavender Neck Wrap with Steam Eye Mask", C5, 49, ["self-care", "relief", "gift"], "My neck after 9 hours at the desk vs after this 😮‍💨",
    "Wrap on neck, she melts", "Self-care gift; pain relief angle.", "Health claims - keep to 'comfort'", 7, 8, 8, 7, 9, 5, 8)
add("Heated Desk Footrest Cave", C5, 59, ["work from home", "cold feet", "comfort"], "WFH hack nobody told you about 🦶",
    "Feet slide into a warm cave under the desk", "WFH audience, simple demo.", "Low emotion", 6, 9, 7, 7, 9, 7, 8)
add("Heated Sofa Throw That Looks Like a Giant Cookie", C5, 69, ["humor", "Christmas", "cozy"], "I'm wrapped in a giant cookie. Life is good 🍪",
    "Round cookie blanket, she rolls up in it", "Funny visual, gift; round blankets went viral before.", "Heating in round shape", 8, 9, 9, 8, 9, 7, 8)
add("Heated Pizza Blanket (round, slices pattern)", C5, 69, ["humor", "food", "teens"], "Me as a pizza burrito at 2 am 🍕",
    "Rolls into a pizza burrito", "Food-humor is a proven viral blanket theme; heated is new.", "Food designs feel kid-ish", 8, 9, 8, 8, 9, 7, 8)
add("Heated Wearable Sleeping Bag Onesie for Adults", C5, 99, ["comfort", "winter", "camping"], "My heating bill vs me in this 😎",
    "Zips into a full sleeping-bag suit, walks around", "Heating-bill savings angle is very strong in US winter.", "Bulky, sizing", 7, 8, 8, 9, 8, 7, 7)
add("Heated Hot-Cocoa Mug Warmer Plush", C5, 39, ["cozy", "gift", "cute"], "My cocoa stays hot AND my hands stay warm ☕",
    "Plush with a mug-shaped warmer pocket", "Cute stocking stuffer, upsell.", "Low price", 6, 8, 9, 5, 9, 7, 9)
add("Heated Window-Seat Cushion with Fireplace Print", C5, 79, ["cozy", "home", "self-care"], "Fake fireplace, real warmth 🔥",
    "Cushion glows, cat jumps on", "Cozy home aesthetic.", "Home niche, medium emotion", 6, 7, 7, 7, 8, 8, 8)
add("Heated Bath Robe Warmer Hook", C5, 59, ["self-care", "luxury", "gift"], "Hotel-level warm robe after every shower 🛁",
    "Robe hangs on a heated hook, she wraps in warm robe", "Luxury self-care for women 30+.", "Electric near water - safety specs", 7, 8, 8, 7, 7, 7, 6)
add("Heated Throw with Built-in Speaker Hood", C5, 89, ["tech", "teens", "cozy"], "Music + heat in one hood 🎧",
    "Hood with speakers, she nods to music", "Teens/gamers.", "Electronics complexity", 7, 7, 8, 8, 6, 8, 6)

C6 = "Kids (parents buy)"
add("Heated Bedtime Story Dragon Plush (glows + warms)", C6, 49, ["kids", "bedtime", "comfort"], "The only plush that keeps my toddler in bed 🐉",
    "Plush glows soft, kid hugs and falls asleep", "Parents pay for better sleep; gift.", "Kids' heated items - USB low heat + certification", 8, 8, 9, 7, 8, 7, 6)
add("Kids Princess Cape with Light-up Crown Hood", C6, 49, ["kids", "identity", "princess"], "She hasn't taken it off in 3 days 👑",
    "Girl twirls, crown lights up", "Little-princess identity; pairs with Heat Majesty.", "Kids sizing", 8, 9, 9, 7, 8, 7, 7)
add("Kids Dinosaur Heated Hoodie Blanket", C6, 49, ["kids", "dinosaurs", "cozy"], "Rawr means 'I'm warm' in dinosaur 🦖",
    "Dino spikes hood, kid stomps", "Dino-loving boys = huge market.", "Crowded kids market", 7, 9, 8, 6, 9, 5, 7)
add("Kids Astronaut Heated Sleeping Suit", C6, 59, ["kids", "dreams", "identity"], "Ready for launch... to bed 🚀",
    "White suit, helmet hood, kid 'floats' onto bed", "Identity play for boys and girls.", "Kids heated specs", 7, 8, 8, 7, 8, 8, 7)
add("Kids Superhero Cape Blanket (plain, no logos)", C6, 45, ["kids", "identity", "fun"], "Captain Cozy has entered the room 🦸",
    "Kid jumps off sofa with cape", "Identity + play.", "Must stay far from known heroes", 7, 8, 8, 6, 9, 6, 8)
add("Kids Snowman Heated Robe", C6, 55, ["kids", "Christmas", "cute"], "Do you want to build a... never mind, I'm the snowman ☃️",
    "Little snowman robe, carrot nose hood", "Christmas cute; avoid movie references in copy.", "Seasonal", 7, 8, 9, 6, 9, 7, 7)

C7 = "Novelty & funny gifts"
add("Heated 'Do Not Disturb' Hood (closes over face)", C7, 59, ["humor", "introvert", "self-care"], "Introvert mode: ON 🙈",
    "Hood zips down into a mask with 'Do not disturb'", "Introvert humor has massive reach.", "Text on product - ok if ours", 8, 9, 8, 7, 9, 9, 8)
add("Heated Burrito Blanket (tortilla print) for Adults", C7, 69, ["humor", "food", "gift"], "Wrapped like a burrito and heated like one 🌯",
    "She rolls into a tortilla burrito", "Proven viral print, heated twist.", "Already sold non-heated", 7, 9, 8, 7, 9, 6, 8)
add("Heated Shark Sleeping Bag Blanket", C7, 69, ["humor", "identity", "teens"], "Being eaten by a shark never felt this warm 🦈",
    "Sits inside shark mouth blanket", "Shark blankets are proven virals; heated version new.", "Copycats", 8, 9, 8, 7, 9, 6, 8)
add("Heated Hot-Dog Sleeping Bag", C7, 79, ["humor", "food", "family"], "I'm the hot dog now 🌭",
    "Lies in a bun-shaped bag, mustard pillow", "Absurd humor = shares.", "Big & silly", 8, 9, 7, 7, 8, 8, 7)
add("Heated Chicken-Nugget Pillow Blanket", C7, 59, ["humor", "food", "teens"], "Nuggets keep me warm 🍗",
    "Pulls out a heated nugget blanket from a nugget pillow", "Food humor for teens/college gifts.", "Low price ceiling", 7, 9, 7, 6, 9, 8, 8)
add("Heated Toast Blanket with Butter Pillow", C7, 59, ["humor", "cute", "food"], "Me: toast. Heat level: golden 🍞",
    "She lies under a toast blanket, butter pillow on top", "Cute food humour.", "Novelty fades fast", 7, 8, 7, 6, 9, 8, 8)
add("Heated Grumpy Old Man Cardigan Robe", C7, 79, ["humor", "dad", "grandpa"], "Grandpa approved: 'finally something useful' 👴",
    "Grandpa in plaid cardigan robe, pipe-shaped controller", "Hard-to-shop-for men; funny.", "Older audience buys less online", 7, 7, 9, 8, 9, 8, 8)
add("Heated 'Crying in the Car' Seat Blanket", C7, 49, ["humor", "relatable", "car"], "For the 5-minute car cry before work 🚗",
    "Plugs into car, wraps legs", "Relatable humour + car heat.", "Car 12V version needed", 7, 8, 7, 6, 8, 9, 8)

C8 = "Elegant & luxe"
add("Heated Faux-Fur Winter Cape (old money)", C8, 129, ["elegance", "identity", "luxury"], "Old money winter, but heated 🤍",
    "She walks in a creamy faux-fur cape, cut to warm glow", "Aspirational, high price, women 30-55.", "Higher quality expectations", 8, 8, 8, 10, 8, 8, 7)
add("Heated Velvet Lounge Robe with Gold Initial", C8, 99, ["luxury", "personalized", "gift"], "Personalized + heated = best gift I ever gave 💛",
    "Gold initial embroidery close-up, she wraps on", "Personalization raises value and gift appeal.", "Personalization logistics", 8, 8, 10, 9, 8, 7, 8)
add("Heated Bridal 'Getting Ready' Robe", C8, 89, ["wedding", "identity", "gift"], "Winter bride, zero goosebumps 👰",
    "Bride in white heated robe, bridesmaids too", "Wedding market buys in groups (bridesmaids).", "Seasonal winter weddings", 8, 7, 8, 9, 8, 9, 8)
add("Heated Cashmere-Feel Travel Wrap", C8, 89, ["travel", "elegance", "comfort"], "Freezing planes are no longer my problem ✈️",
    "Wrap on plane with power bank", "Travel pain point + elegance.", "Battery rules on planes", 7, 8, 8, 9, 8, 7, 7)
add("Heated Royal Cape for Little & Big Princess (set)", C8, 129, ["royalty", "mom & daughter", "gift"], "Queen and princess of the house 👑👑",
    "Mom and daughter capes, crowns", "Extends Heat Majesty; bundle.", "Kids specs", 9, 8, 10, 9, 8, 8, 7)

C9 = "Outdoor & practical"
add("Heated Stadium Poncho (game day)", C9, 79, ["sports", "dad", "winter"], "Football in December, warm in December 🏈",
    "Fan in stands, poncho glows on thermal", "Huge US sports culture; dads/moms at kids' games.", "Team logos = IP, keep colors only", 8, 8, 9, 8, 8, 7, 8)
add("Heated Car-Seat Blanket for Kids' Pickup", C9, 59, ["mom", "practical", "winter"], "School pickup at 7 am in January? Not cold anymore.",
    "Mom in car, blanket plugs into 12V", "Mom winter pain point.", "Car plug", 6, 8, 7, 7, 8, 7, 8)
add("Heated Hunting / Fishing Seat Cushion", C9, 49, ["outdoors", "men", "practical"], "Ice fishing just got comfortable 🎣",
    "Sits on icy bucket, warm", "Men's gift.", "Niche", 5, 8, 7, 6, 8, 7, 8)
add("Heated Dog-Walk Hooded Cape for Owners", C9, 79, ["pets", "winter", "practical"], "6 am dog walks in January, solved 🐕",
    "Owner and dog walking at dawn in snow", "Daily pain point for dog owners.", "Mid emotion", 7, 8, 8, 8, 8, 8, 8)
add("Heated Kneeling Pad for Christmas Lights Decorating", C9, 39, ["humor", "practical"], "Dad decorating the roof, heated 🎄",
    "Dad on roof with lights", "Funny seasonal.", "Low value", 5, 7, 7, 5, 8, 9, 8)

C10 = "Variations of our winners"
add("HeatGrump Kids Size", C10, 69, ["kids", "family", "humor"], "Little grump, big attitude 💚",
    "Kid in mini grumpy robe frowning", "Direct variation of a product that already sells; family bundles.", "Kids heated specs", 9, 9, 10, 8, 10, 8, 7)
add("Heat Majesty Second Design (ice / rose / mermaid)", C10, 99, ["royalty", "identity", "choice"], "Which princess are you? Pick your robe 👑",
    "Grid of designs, she picks one", "Choice of designs increases conversion and repeat orders.", "More SKUs", 9, 8, 10, 9, 9, 8, 8)
add("HeatGrump Couples Set (Mr. & Mrs. Grump)", C10, 149, ["couples", "humor", "gift"], "Mr. & Mrs. Grump do Christmas together 💚❤️",
    "Couple in two grumpy robes on sofa", "Bundle on a proven product.", "Shipping", 8, 8, 10, 9, 10, 8, 8)
add("HeatGrump Slippers Add-on", C10, 39, ["humor", "matching", "gift"], "The full grumpy set 💚",
    "Green furry slippers match the robe", "AOV booster on checkout.", "Low price", 7, 8, 9, 6, 9, 8, 8)
add("Heat Majesty Tiara Hair Clip (free gift)", C10, 0, ["royalty", "gift"], "Free tiara with every royal robe 👑",
    "Tiara clip in box", "Free gift raises conversion and video content.", "Cost only", 6, 7, 8, 5, 9, 7, 9)
add("Royal Gift Box Upgrade with Name Card", C10, 15, ["gift", "personalized"], "Her name on a royal gift card 💌",
    "Box opens, name card", "Cheap upsell with big perceived value.", "Manual work", 7, 7, 10, 7, 8, 8, 9)
add("Heated Robe + Power Bank Cordless Bundle", C10, 129, ["freedom", "practical"], "No cable. Warm anywhere.",
    "Walks around house, no cord", "Cordless use is a top request in heated wearables.", "Battery shipping", 7, 8, 9, 9, 9, 6, 7)

C11 = "Seasonal beyond Christmas"
add("Heated Valentine Heart Robe (red, heart pockets)", C11, 79, ["love", "couples", "gift"], "My Valentine is a heated robe ❤️",
    "Red robe with heart pockets, couple", "Continues robe sales in February.", "Short window", 7, 8, 8, 8, 9, 8, 8)
add("Heated Pumpkin-Spice Robe (fall)", C11, 79, ["fall", "identity", "cozy"], "Pumpkin-spice girlie, now heated 🎃",
    "Orange knit robe, latte", "Fall basic-girl identity for Sept-Nov.", "Seasonal", 7, 8, 8, 8, 9, 8, 8)
add("Heated Spooky Ghost Robe (Halloween)", C11, 69, ["Halloween", "humor", "cute"], "Ghosting everyone but staying warm 👻",
    "White ghost robe with eyes", "Halloween + warmth; cute ghost trend.", "Short window", 7, 8, 7, 7, 9, 8, 8)
add("Heated Snow-Day Hooded Scarf", C11, 45, ["winter", "cozy", "gift"], "Snow day essential ❄️",
    "Hooded scarf in snowfall", "Cheap gift.", "Crowded", 6, 7, 8, 6, 9, 5, 9)
add("Heated Lunar New Year Dragon Robe (red & gold)", C11, 89, ["culture", "celebration", "family"], "Year of comfort 🧧",
    "Red & gold dragon robe", "Asian-American audience; Jan-Feb window.", "Cultural sensitivity", 6, 7, 7, 8, 8, 9, 8)

C12 = "Big bold concepts"
add("Heated Hooded Throne Blanket (crown-shaped back)", C12, 99, ["royalty", "humor", "identity"], "Sitting on my throne like the queen I am 👑",
    "Blanket stands up like a throne back on the sofa", "Royal identity on the sofa; unique silhouette.", "Structure inside blanket", 8, 8, 8, 9, 7, 9, 7)
add("Heated Igloo Pod Chair Cover", C12, 149, ["cozy", "winter", "home"], "My own igloo in the living room ❄️",
    "Dome cover over chair, she peeks out", "Big ticket, cozy home.", "Bulky", 7, 8, 7, 9, 7, 9, 6)
add("Heated Wearable Christmas Tree Cape (with lights)", C12, 99, ["Christmas", "humor", "party"], "I AM the Christmas tree this year 🎄",
    "Cape with LED lights turns on", "Ugly-sweater-party winner; light-up demo.", "LEDs + heat = more parts", 9, 10, 10, 8, 7, 9, 6)
add("Heated Fireplace-Print Blanket with Crackling Sound", C12, 79, ["cozy", "home", "sound"], "Fake fire, real warmth, real crackle 🔥",
    "Blanket with fire print crackles", "Multi-sense demo.", "Speaker part", 7, 8, 8, 8, 7, 9, 7)
add("Heated 'Hug Me' Robe with Arms That Wrap (long sleeves hug)", C12, 89, ["comfort", "lonely", "emotion"], "Self-hug, but heated 🤍",
    "Extra-long sleeves wrap around her", "Strong comfort emotion for singles/ lonely winter.", "Design must be cute not sad", 9, 8, 8, 8, 8, 9, 8)
add("Heated Sherpa Hood Cocoon for Gamers", C12, 79, ["gaming", "identity", "comfort"], "8 hours of gaming. Warm the whole time 🎮",
    "Gamer in cocoon hood, RGB light", "Gamer audience spends; few heated products.", "Mostly male teens", 7, 7, 8, 8, 8, 8, 8)
add("Heated Pregnancy Belly Wrap Robe", C12, 89, ["moms-to-be", "comfort", "gift"], "Baby shower gift that actually gets used 🤰",
    "Pregnant woman in robe, gentle warmth", "Baby shower gifting; strong emotion.", "Medical/safety sensitivity - keep low heat, careful claims", 8, 7, 8, 8, 8, 8, 5)
add("Heated Graduation Cap Hoodie (college)", C12, 69, ["students", "identity", "gift"], "Finals week survival kit 🎓",
    "Student studying in hoodie", "Students + parents gifting.", "Seasonal May/Dec", 6, 7, 7, 7, 9, 8, 8)
add("Heated Firefighter-Style Turnout Robe", C12, 89, ["hero", "identity", "gift"], "For the hero who comes home cold 🚒",
    "Tan robe with reflective stripes", "Gift for first responders' families.", "Respect uniforms", 7, 7, 8, 8, 8, 9, 8)
add("Heated Nurse Night-Shift Wrap", C12, 69, ["nurses", "gratitude", "gift"], "For the nurse who works Christmas night 🩺",
    "Nurse after shift wraps in robe", "Huge, loyal audience; gratitude gifts.", "Careful with claims", 8, 7, 8, 7, 9, 9, 8)

add("Heated Teacher Cardigan Robe (classroom cold)", C12, 69, ["teachers", "gratitude", "gift"], "Every teacher's classroom is freezing. Fixed 🍎",
    "Teacher grading papers in a cozy cardigan robe", "Teacher-gift season (Christmas, end of year) - parents buy in groups.", "Plain design needs a hook", 7, 7, 9, 7, 9, 8, 8)
add("Heated Bigfoot Robe (hairy, huge)", C1, 85, ["humor", "identity", "men"], "Bigfoot sightings at my house went up this winter 👣",
    "Huge hairy brown robe walking in the snow at dusk", "Absurd humour + men audience, links to 'monster feet'.", "Long fur shedding", 8, 9, 8, 8, 8, 9, 7)
add("Heated Swan Princess Robe (white & feather trim)", C1, 89, ["royalty", "elegance", "identity"], "Ballet girl at heart, cold girl in reality 🦢",
    "White robe with feather-like trim, ballet twirl", "Ballet/swan identity for women; elegant royal line variant.", "Feathers must be faux fur", 8, 8, 8, 9, 8, 9, 8)

assert len(I) == 100, len(I)
for x in I:
    s = x["scores"]; x["score"] = round(sum(s[k] * w for k, w in W.items()))
I.sort(key=lambda x: -x["score"])
for r, x in enumerate(I, 1):
    x["rank"] = r; x["status"] = "idea"; x["id"] = re.sub(r"[^a-z0-9]+", "-", x["name"].lower()).strip("-")[:60]
json.dump(I, open(__file__.replace("build_ideas.py", "ideas.json"), "w"), indent=1, ensure_ascii=False)
print(len(I), [(x["rank"], x["name"], x["score"]) for x in I[:12]])
