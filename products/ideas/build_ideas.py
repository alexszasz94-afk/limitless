"""100 invented products of ANY kind (v2, 17 oct 2026) - not only heated items. Same scoring as v1:
emotion 25% · demo in 1-3 s 20% · gift/season 15% · price & margin 15% · easy to film with AI 10% · few competitors 10% · low return risk 5%.
Hypotheses until tested (docs/09-reguli-produs.md). Output: ideas.json -> board doc ideas/all."""
import json, re
W = dict(E=2.5, D=2.0, G=1.5, M=1.5, P=1.0, N=1.0, R=0.5)
I = []
def add(name, cat, price, emo, hook, demo, why, risk, *s):
    I.append(dict(name=name, category=cat, price=price, emotions=emo, hook=hook, demo=demo, why=why, risk=risk,
                  scores=dict(zip("EDGMPNR", s))))

K = "Home & cozy"
add("Fireplace Projector Lantern", K, 49, ["cozy", "Christmas", "home"], "My apartment has no fireplace. Now it does 🔥", "Turns it on, a crackling fire appears on the wall", "Renters can't have fireplaces; instant cozy transformation, Christmas gift.", "Projector quality must look real", 9, 10, 9, 7, 8, 7, 8)
add("Snow Globe Night Light with Your Photo Inside", K, 59, ["nostalgia", "personalized", "gift"], "Our family photo, inside a snow globe that snows 🥹", "Shake it - snow falls around the family photo, light glows", "Personalized Christmas keepsake, tears on unboxing.", "Personalisation logistics", 10, 10, 10, 8, 8, 8, 8)
add("Floating Moon Lamp (magnetic levitation)", K, 69, ["wonder", "decor", "gift"], "It floats. It glows. It spins. 🌕", "Moon levitates and slowly rotates above the base", "Magic effect stops the scroll; teens and couples.", "Exists already - win with design", 8, 10, 8, 8, 8, 5, 8)
add("Book Nook Shelf Insert (tiny lit alley)", K, 59, ["book lovers", "wonder", "decor"], "There's a tiny magical street hidden in my bookshelf ✨", "Slides between books, lights reveal a miniature alley", "BookTok community, cozy aesthetic, DIY kit or finished.", "Must be pre-assembled for easy gifting", 9, 9, 9, 8, 8, 7, 8)
add("Sunset Lamp with Rotating Golden Hour", K, 39, ["mood", "selfies", "cozy"], "Golden hour every night at 9 pm 🌅", "Room turns sunset orange, she takes a selfie", "Proven TikTok category; add timer + colours.", "Crowded", 7, 10, 7, 6, 9, 4, 9)
add("Rain-Cloud Humidifier that Drips on a Plant", K, 49, ["calm", "wonder", "decor"], "A tiny rain cloud waters my plant 🌧️", "Cloud drips water drops slowly onto a plant pot", "Mesmerising loop video, calming sound.", "Water mess if badly made", 8, 10, 8, 7, 8, 7, 7)
add("Smart Cozy Corner Kit (lights + throw + candles)", K, 79, ["cozy", "self-care", "gift"], "From sad corner to cozy corner in 60 seconds", "Before/after time-lapse of a corner", "Bundle with high perceived value, transformation demo.", "Many parts", 8, 9, 8, 8, 8, 8, 8)
add("Glow-in-the-Dark Star Ceiling Projector for Adults", K, 45, ["calm", "sleep", "wonder"], "Falling asleep under the galaxy every night 🌌", "Lights off, ceiling becomes the Milky Way", "Sleep/relax angle.", "Common category", 7, 10, 7, 6, 9, 4, 8)
add("Self-Stirring Cocoa Mug with Marshmallow Lid", K, 39, ["cozy", "fun", "gift"], "My cocoa stirs itself now ☕", "Press button, whirlpool in mug", "Fun stocking gift.", "Low price", 6, 10, 8, 5, 9, 6, 8)
add("Personalised Family Christmas Doormat that Lights Up", K, 59, ["family", "Christmas", "personalized"], "Our family name lights up when guests arrive 🎄", "Step on mat, LED border glows", "Personalised + light-up demo.", "Outdoor electronics", 7, 9, 9, 7, 8, 9, 7)

K = "Gifts that make people cry"
add("Audio Photo Frame (press to hear their voice)", K, 59, ["love", "memory", "gift"], "I can still hear my grandpa say goodnight 🥹", "Presses frame, a recorded voice plays", "Grief/memory gifts are the most emotional category; huge shares.", "Sensitive topic - handle respectfully", 10, 9, 10, 8, 8, 8, 8)
add("Heartbeat Recording Teddy Bear", K, 49, ["love", "pregnancy", "memory"], "My baby's heartbeat inside a teddy 🤍", "Squeezes bear, a heartbeat plays", "Pregnancy & memorial gifts, extreme emotion.", "Kids toy safety", 10, 9, 9, 7, 8, 7, 8)
add("Star Map of the Night You Met (lit frame)", K, 69, ["love", "couples", "personalized"], "The exact sky on the night we met ✨", "Frame lights up showing the stars on that date", "Couples gift with story.", "Personalisation", 9, 8, 10, 8, 8, 6, 9)
add("Letters-to-Open-When Box", K, 45, ["love", "distance", "gift"], "Open when you miss me 💌", "Opens wooden box full of labelled envelopes", "Long-distance couples, graduation gifts.", "Low tech, easy to copy", 8, 8, 9, 7, 9, 7, 9)
add("Hand-Holding Sculpture from Your Couple Photo", K, 89, ["love", "couples", "luxury"], "They turned our hands into a sculpture 😭", "Reveals a resin/clay sculpture of two hands", "High price emotional keepsake.", "Production complexity", 9, 8, 9, 9, 6, 9, 8)
add("Grandparent Story Journal with QR Voice Notes", K, 49, ["family", "memory", "grandparents"], "Grandma's stories, saved forever 📖", "Scans QR in journal, hears grandma's voice", "Memory keeping for families.", "Needs app/host", 9, 7, 9, 7, 7, 8, 8)
add("Pet Portrait Ornament from Photo", K, 39, ["pets", "Christmas", "personalized"], "My dog is on the Christmas tree now 🐶🎄", "Hangs ornament with dog's face", "Pet owners + Christmas; cheap to make.", "Crowded on Etsy", 8, 8, 10, 6, 9, 5, 9)
add("Custom 'Our Song' Vinyl Plaque (spinning)", K, 59, ["love", "music", "couples"], "Our wedding song, framed and spinning 💿", "Vinyl spins, QR plays the song", "Couples & anniversaries.", "Music licensing - QR to Spotify only", 8, 8, 9, 7, 8, 7, 9)

K = "Kids (parents buy)"
add("Talking Plush that Reads the Kid's Name", K, 49, ["kids", "personalized", "wonder"], "His face when the bear said his name 😭", "Kid hugs plush, it says the kid's name", "Personalised toy reactions go viral.", "Electronics + kids safety", 9, 9, 9, 7, 8, 8, 7)
add("Kids' Magic Drawing Board with Projector", K, 45, ["kids", "creativity", "screen-free"], "Screen-free and he's been drawing for an hour", "Projects animal, kid traces it", "Screen-free parent angle.", "Common", 7, 9, 8, 6, 9, 5, 8)
add("Tooth-Fairy Door with Tiny Glowing Footprints", K, 39, ["kids", "magic", "parents"], "The tooth fairy left footprints 😱✨", "Morning: tiny glowing footprints lead to the door", "Magic moments parents film.", "Low price", 9, 9, 7, 5, 9, 9, 9)
add("Santa Key + Magic Snow Footprint Stencil Kit", K, 39, ["Christmas", "kids", "magic"], "Santa's boots left snow in our living room 🎅", "Morning reveal of snowy boot prints by the tree", "Christmas morning magic content.", "Seasonal", 9, 9, 10, 5, 9, 8, 9)
add("Bedtime Story Projector Torch", K, 39, ["kids", "bedtime", "cozy"], "Bedtime stories on the ceiling", "Torch projects story slides on wall", "Parents bedtime pain point.", "Cheap category", 7, 9, 8, 5, 9, 5, 8)
add("Kids' Ride-On Suitcase Shaped like an Animal", K, 79, ["kids", "travel", "fun"], "Airport meltdowns: solved 🧳", "Kid rides suitcase through airport", "Travel parents; strong demo.", "Bulky shipping", 7, 9, 7, 8, 8, 6, 7)
add("Growth-Chart Wall Sticker that Lights at Night", K, 45, ["kids", "memory", "decor"], "Watching her grow, one glowing line at a time", "Night: glowing growth chart", "Memory + decor.", "Niche", 7, 7, 7, 6, 9, 9, 9)

K = "Pets"
add("Cat Window Hammock with Bird Feeder View", K, 49, ["pets", "cute", "entertainment"], "Cat TV is now on 24/7 📺🐱", "Cat lies in window hammock watching birds", "Cat videos = huge engagement.", "Suction quality", 8, 9, 7, 7, 8, 6, 7)
add("Dog Birthday Cake Mix + Party Kit", K, 39, ["pets", "celebration", "cute"], "His 5th birthday was better than mine 🎂🐶", "Dog wearing party hat eats cake", "Pet parents celebrate; content goldmine.", "Food regs", 8, 8, 8, 5, 8, 7, 8)
add("Interactive Laser Feather Toy that Hides", K, 39, ["pets", "fun"], "My cat hasn't been this active in years 😂", "Feather pops out of holes randomly, cat pounces", "Proven pet toy demand.", "Crowded", 7, 10, 7, 5, 9, 4, 8)
add("Pet Memorial Paw-Print Glow Stone", K, 49, ["pets", "grief", "memory"], "Her paw print glows every night 🐾", "Stone glows with paw print", "Very emotional niche.", "Sensitive", 9, 8, 7, 7, 8, 8, 9)
add("Dog Car Seat Booster with Window View", K, 69, ["pets", "travel", "safety"], "He finally sees out the window 🐕", "Dog sits in booster, head out", "Small dog owners.", "Safety claims", 7, 9, 7, 7, 8, 6, 8)
add("Automatic Ball Launcher for Dogs", K, 89, ["pets", "fun", "practical"], "He plays fetch with himself now 🎾", "Dog drops ball, machine launches it", "Busy owners; viral demo.", "Existing brands", 8, 10, 7, 8, 8, 5, 7)

K = "Beauty & self-care"
add("LED Mirror with Hollywood Bulbs (foldable)", K, 69, ["glam", "identity", "self-care"], "Main character makeup lighting ✨", "Unfolds, bulbs light up", "Women 18-35; aesthetic transformation.", "Fragile shipping", 7, 9, 8, 8, 8, 5, 7)
add("Ice Roller Face Mask Set in Gift Box", K, 39, ["self-care", "glow", "gift"], "Puffy face to fresh in 2 minutes", "Rolls ice roller, before/after", "Self-care gift.", "Claims must be cosmetic only", 6, 9, 8, 5, 9, 4, 9)
add("Scalp Massager Head Spa Kit", K, 49, ["relax", "ASMR", "self-care"], "Head spa at home - the ASMR is unreal 😮‍💨", "Massager on scalp with ASMR sound", "Head-spa trend is huge.", "Many sellers", 7, 9, 7, 7, 8, 5, 9)
add("Personalised Silk Pillowcase with Initials", K, 49, ["luxury", "self-care", "personalized"], "Silk pillowcase, my initials, my hair thanks me", "Embroidery close-up, hair flip", "Gift with personal touch.", "Silk quality", 7, 7, 9, 7, 9, 6, 9)
add("Nail-Polish Organizer Wheel (rotating, lit)", K, 49, ["organisation", "beauty", "satisfying"], "My 120 polishes finally have a home 💅", "Spins rotating wheel with lights", "Satisfying organisation content.", "Niche", 6, 9, 7, 7, 8, 8, 8)
add("At-Home Gel Nail Printer Kit", K, 129, ["beauty", "tech", "wow"], "It PRINTED a design on my nail 😱", "Finger in, design appears", "Wow demo, high price.", "Tech sourcing quality", 8, 10, 8, 9, 6, 7, 6)

K = "Kitchen & food fun"
add("Mini Waffle Maker Shaped Like a Snowflake", K, 39, ["Christmas", "family", "fun"], "Christmas morning snowflake waffles ❄️🧇", "Opens maker, snowflake waffle", "Seasonal family breakfast content.", "Low price", 7, 9, 9, 5, 9, 7, 8)
add("Hot Chocolate Bomb Mould + Kit", K, 39, ["Christmas", "family", "satisfying"], "Watch it explode in the milk 🍫", "Bomb drops in milk, marshmallows burst", "Satisfying reveal.", "Food safety", 7, 10, 9, 5, 9, 4, 8)
add("Personalised Cutting Board with Grandma's Recipe", K, 69, ["family", "memory", "personalized"], "Grandma's handwriting, engraved forever 🥹", "Engraved handwritten recipe close-up", "Memory + kitchen; tears.", "Personalisation", 10, 8, 10, 8, 8, 8, 9)
add("Pancake Art Bottle Kit with Stencils", K, 39, ["family", "fun", "kids"], "Dad made a dinosaur pancake 🦕", "Squeezes batter into dino shape", "Dad + kids content.", "Cheap", 7, 9, 7, 5, 9, 7, 9)
add("Cotton-Candy Machine (retro cart)", K, 59, ["nostalgia", "kids", "party"], "Carnival vibes at home 🎪", "Pink cloud spins onto stick", "Party nostalgia.", "Exists", 8, 10, 8, 7, 8, 5, 7)
add("Smart Spice Rack that Lights the Spice You Need", K, 89, ["organisation", "tech", "satisfying"], "It tells me which spice to grab 🌶️", "Recipe on app, jar lights up", "Satisfying tech.", "App needed", 6, 9, 6, 8, 6, 9, 7)

K = "Fitness & wellness"
add("Under-Desk Walking Pad (foldable)", K, 199, ["productivity", "health", "identity"], "10,000 steps while answering emails", "Walking at desk, folds away", "WFH health; high ticket.", "Shipping heavy", 7, 9, 6, 9, 8, 4, 6)
add("Smart Jump Rope with Step Counter Handle", K, 39, ["fitness", "fun"], "Counted 500 jumps for me", "Handle display counting", "Cheap fitness gift.", "Crowded", 5, 9, 6, 5, 9, 4, 9)
add("Posture Corrector that Vibrates", K, 49, ["health", "confidence"], "My posture after 2 weeks", "Vibrates when slouching", "Problem-solution.", "Health claims risk", 6, 9, 5, 7, 8, 4, 7)
add("Weighted Hula Hoop with Counter", K, 45, ["fitness", "fun", "women"], "Lost my excuses, not my hula hoop", "Smart hoop spinning around waist", "Women fitness trend.", "Crowded", 6, 10, 6, 6, 9, 4, 8)
add("Mini Sauna Blanket", K, 149, ["self-care", "luxury", "wellness"], "Spa day in my living room", "Lies in blanket, sweats, glows", "Wellness trend; high price.", "Health claims", 7, 8, 7, 9, 8, 5, 6)
add("Massage Gun Shaped like a Cute Animal", K, 59, ["self-care", "cute", "gift"], "The cutest massage gun ever 🐻", "Bear-shaped gun massaging shoulders", "Cute twist on proven product.", "Design needed", 7, 9, 8, 7, 8, 8, 8)

K = "Car & travel"
add("Car Seat Gap Organizer with Light", K, 39, ["practical", "satisfying"], "No more phone in the abyss 🚗", "Phone drops - caught by organizer", "Universal pain point.", "Low price", 6, 10, 6, 5, 9, 5, 9)
add("Galaxy Car Roof Star Projector", K, 49, ["vibes", "couples", "car"], "My car at night now 🌌", "Car ceiling becomes starry sky", "Car aesthetic trend.", "Common", 7, 10, 7, 6, 9, 5, 8)
add("Travel Neck Pillow that Turns into a Hood Cocoon", K, 59, ["travel", "comfort", "funny"], "Sleeping on a plane in my own cocoon ✈️", "Pillow unfolds into hood", "Travel discomfort.", "Bulky", 6, 9, 7, 7, 8, 7, 8)
add("Kids' Car Tray with Tablet Holder", K, 39, ["parents", "travel", "practical"], "Road trip without 'are we there yet' 🚙", "Snaps tray onto seat, kid plays", "Parents road trip.", "Common", 6, 9, 6, 5, 9, 5, 9)
add("Personalised Luggage Cover with Pet Face", K, 49, ["travel", "pets", "funny"], "Spotted my suitcase in 0.2 seconds 🐶", "Baggage claim: suitcase with giant dog face", "Funny + practical + personalised.", "Sizing", 8, 9, 8, 6, 9, 8, 8)

K = "Tech & gadgets"
add("Phone Case with Built-in Mirror & Ring Light", K, 39, ["selfie", "beauty"], "Perfect selfie lighting anywhere", "Case flips open, ring lights up", "Selfie culture.", "Fit per phone model", 6, 9, 6, 5, 8, 6, 6)
add("Retro Game Console Shaped like a TV (400 games)", K, 79, ["nostalgia", "family", "gift"], "My dad played for 3 hours straight 😂", "Plugs into TV, retro games light up", "Nostalgia for 30-50 y/o + family.", "IP on games - only original/licensed", 9, 9, 9, 8, 7, 5, 6)
add("Instant Print Camera for Kids", K, 59, ["kids", "creativity", "memory"], "She prints her own memories now 📸", "Takes photo, thermal print slides out", "Creative kids gift.", "Common", 8, 10, 9, 7, 8, 5, 8)
add("Smart Plant Pot with Emotions (shows face)", K, 69, ["cute", "plants", "tech"], "My plant tells me when it's thirsty 🥺", "Screen face goes sad, waters, face smiles", "Cute + useful; plant lovers.", "Electronics quality", 9, 10, 8, 8, 7, 8, 7)
add("Bluetooth Beanie with Built-in Headphones", K, 39, ["winter", "music", "practical"], "Music without freezing ears 🎧", "Pulls beanie on, music plays", "Winter gift.", "Crowded", 5, 8, 8, 5, 9, 4, 9)
add("Desk Pet Robot that Reacts to Your Mood", K, 99, ["cute", "companion", "tech"], "My desk buddy gets sad when I leave 🥺", "Robot reacts with eyes and sounds", "Companion tech trend.", "Tech sourcing", 9, 9, 8, 9, 6, 8, 6)

K = "Fashion & accessories"
add("Necklace with Hidden Photo Projection", K, 49, ["love", "memory", "jewellery"], "Look inside the stone 🥹", "Light through stone shows a photo", "Hidden-photo jewellery is emotional.", "Common on ads", 9, 9, 10, 7, 9, 5, 9)
add("Birth-Flower Personalized Jewellery Box", K, 59, ["personalized", "mom", "gift"], "Every kid's birth flower on mom's box 💐", "Opens box: engraved flowers + names", "Mom gift.", "Personalisation", 8, 8, 10, 7, 8, 7, 9)
add("Matching Mom & Daughter Bracelets that Glow", K, 45, ["mom & daughter", "love"], "When one glows, the other glows 💗", "Taps bracelet, both light", "Emotional pair.", "Tech", 9, 9, 9, 6, 8, 8, 8)
add("Convertible Backpack-Purse with Charging", K, 69, ["practical", "style"], "One bag, three looks", "Bag converts in 3 moves", "Transformation demo.", "Crowded", 6, 9, 7, 7, 8, 5, 8)
add("Light-Up Ugly Christmas Sweater (custom face)", K, 59, ["Christmas", "humor", "party"], "My face on a light-up ugly sweater 😂", "Sweater lights up showing your face", "Ugly-sweater parties are huge.", "Sizing", 9, 10, 10, 7, 8, 8, 6)

K = "Organization & satisfying"
add("Rotating Makeup Tower with Lights", K, 69, ["organisation", "satisfying"], "From chaos to this ✨", "Before/after vanity", "Satisfying transformation.", "Common", 6, 9, 7, 7, 8, 5, 8)
add("Fridge Organizer Set that Looks Like a Store", K, 59, ["satisfying", "home"], "My fridge looks like a store now", "Restock video ASMR", "Restock trend.", "Crowded", 7, 9, 6, 7, 8, 5, 9)
add("Christmas Ornament Storage Box with Lights", K, 49, ["Christmas", "organisation"], "Ornaments stored, zero broken", "Box with compartments glows", "Seasonal practical.", "Low emotion", 5, 8, 8, 6, 9, 7, 9)
add("Gift-Wrap Station Wall Organizer", K, 59, ["Christmas", "satisfying"], "Wrapping 40 presents was fun this year 🎁", "Rolls on wall, cuts paper", "Seasonal satisfying.", "Niche", 6, 9, 8, 7, 8, 8, 8)
add("Sock & Underwear Drawer Cube Organizers", K, 39, ["satisfying"], "Folded like a store", "Satisfying folding", "Cheap.", "Low price", 4, 8, 5, 5, 9, 4, 9)

K = "Funny & viral gifts"
add("Screaming Goat Desk Toy (stress button)", K, 39, ["humor", "office"], "Press when your boss emails 🐐", "Presses goat, it screams", "Office humour shares.", "Low price", 8, 10, 8, 5, 9, 6, 9)
add("Toilet Golf / Bathroom Mini Games Set", K, 39, ["humor", "dad"], "Dad's new favourite game 😂", "Dad putting on toilet mini green", "Gag gift for dads.", "Low price", 7, 9, 8, 5, 9, 6, 9)
add("Personalised Face Socks (your face on them)", K, 39, ["humor", "personalized"], "I gave everyone socks with my face 😂", "Opens gift: socks with giver's face", "Gag gift viral loop.", "Low price", 8, 9, 9, 5, 9, 4, 9)
add("Fake Snow Machine for the Window", K, 79, ["Christmas", "wonder", "kids"], "It's snowing... inside 😳❄️", "Machine blows snow outside window", "Christmas wonder.", "Mess", 9, 10, 9, 7, 8, 8, 7)
add("Santa Hidden Camera Ornament (fake) + Certificate", K, 39, ["Christmas", "kids", "humor"], "Santa is watching... literally 🎅📷", "Ornament with red light; kid behaves", "Parent hack content.", "Ethics: decor only", 8, 9, 9, 5, 9, 8, 9)
add("Wine Glass that Holds a Whole Bottle", K, 39, ["humor", "women", "gift"], "Me after the kids go to bed 🍷", "Pours whole bottle into glass", "Mom humour.", "Alcohol content limits on ads", 7, 10, 8, 5, 9, 5, 9)

K = "Outdoor & garden"
add("Solar Fairy-Light Garden Mushrooms", K, 39, ["magic", "garden", "cozy"], "My garden turned into a fairytale 🍄✨", "Dusk: mushrooms glow", "Cottage-core aesthetic.", "Common", 7, 9, 6, 5, 9, 5, 9)
add("Bird Feeder with Camera (AI identifies birds)", K, 149, ["wonder", "nature", "gift"], "It tells me which bird is visiting 🐦", "App notification + bird close-up", "Huge trend with retirees & parents.", "Tech sourcing", 9, 9, 9, 9, 6, 6, 7)
add("Giant Inflatable Snowman with Projector Face", K, 99, ["Christmas", "kids", "fun"], "Our snowman talks to the neighbours 😂", "Projector face sings on inflatable", "Christmas yard competition.", "Bulky", 8, 10, 9, 8, 7, 8, 7)
add("Smart Fire Pit with Color Flames", K, 129, ["cozy", "friends", "wow"], "Rainbow flames for movie night 🔥", "Flames change colour", "Wow demo; high price.", "Safety", 8, 10, 7, 9, 7, 7, 6)
add("Hammock Chair Pod for the Bedroom", K, 79, ["cozy", "teens", "aesthetic"], "My reading spot is a cloud ☁️", "Swings in pod with fairy lights", "Teen room aesthetic.", "Installation", 7, 9, 7, 8, 8, 6, 7)

K = "Seasonal & celebrations"
add("Advent Calendar of Mini Self-Care Gifts", K, 59, ["Christmas", "self-care", "anticipation"], "24 days of tiny treats for me 🎁", "Opens a door each day", "Daily-reveal content series.", "Must ship before December", 8, 9, 10, 7, 8, 5, 8)
add("Advent Calendar for Dogs", K, 45, ["pets", "Christmas", "cute"], "His face opening door #1 🐶", "Dog noses a door open", "Pet + advent.", "Pet food regs", 8, 9, 10, 6, 8, 6, 8)
add("Elf-on-a-Shelf Style Mischief Kit (our own character)", K, 39, ["Christmas", "kids", "magic"], "Our elf made snow angels in flour 😂", "Morning reveal scenes", "Daily content for parents; our own character, no IP.", "Must be our character", 9, 9, 10, 5, 8, 6, 9)
add("Personalised Christmas Eve Box", K, 45, ["Christmas", "family", "tradition"], "Christmas Eve box with her name 🎄", "Opens box: pyjamas, cocoa, book", "Tradition gift.", "Assembly", 8, 8, 10, 7, 8, 6, 8)
add("Light-Up Birthday Sash & Crown Set (40+)", K, 39, ["celebration", "humor"], "Turning 40 like royalty 👑", "Crown lights up at party", "Milestone birthdays.", "Low price", 6, 9, 7, 5, 9, 7, 9)

K = "Big swings (higher risk, higher reward)"
add("Mini Indoor Snow Machine Globe (walk-in photo booth)", K, 299, ["wonder", "events", "Christmas"], "We built a snow globe in our living room 😳", "Family inside a giant inflatable globe with falling snow", "Ultra-shareable; parties.", "Bulky, high price", 9, 10, 8, 9, 6, 9, 5)
add("Smart Mirror that Shows Weather & Compliments You", K, 149, ["confidence", "tech", "fun"], "My mirror hypes me up every morning 🥹", "Mirror text: 'You look great today'", "Feel-good tech.", "Tech", 8, 9, 7, 9, 6, 9, 6)
add("Personalised Storybook Starring Your Kid & Pet", K, 49, ["kids", "personalized", "pets"], "My son and our dog are the heroes 📚", "Flips book: kid & dog illustrated", "Personalised book market proven; add pet.", "Illustration pipeline", 9, 8, 10, 7, 8, 6, 9)
add("Memory Snow Globe with Ashes/ Fur (pet)", K, 79, ["grief", "pets", "memory"], "She's always with us now 🤍", "Globe with tiny fur keepsake", "Deep emotion; careful tone.", "Very sensitive", 9, 7, 6, 8, 7, 9, 8)
add("AI Bedtime Plush that Tells New Stories", K, 99, ["kids", "tech", "bedtime"], "A new story every night, in mom's voice", "Plush talks in mom's cloned voice", "Strong emotion + tech.", "Privacy & tech complexity", 9, 8, 9, 9, 5, 9, 5)
add("Couples Bracelets that Vibrate When the Other Taps", K, 79, ["love", "distance", "tech"], "He tapped his bracelet in Texas. I felt it in Ohio 🥹", "Tap -> partner's bracelet glows & buzzes", "Long-distance emotion.", "Tech + app", 10, 9, 9, 8, 6, 7, 6)
add("Life-Size Cardboard Cutout from Your Photo", K, 69, ["humor", "personalized"], "Sent my husband to his own party 😂", "Reveal of life-size cutout", "Gag gift, parties.", "Shipping size", 8, 9, 8, 7, 9, 6, 8)

K = "Christmas magic"
add("Santa's Magic Key + Light-Up Front Door Lock", K, 45, ["Christmas", "kids", "magic"], "No chimney? Santa uses the magic key 🗝️🎅", "Key glows when hung on the door on Christmas Eve", "Answers the #1 kid question (no chimney); morning reveal content.", "Low price - bundle with letter", 9, 9, 10, 6, 9, 8, 9)
add("Personalised Video Message Ornament (plays a video)", K, 79, ["Christmas", "family", "memory"], "Grandma's message plays every time we open it 🥹🎄", "Opens ornament: tiny screen plays a family video", "Christmas + memory + tech wow; very emotional.", "Electronics quality", 10, 9, 10, 8, 7, 9, 7)
add("Snowing Christmas Tree Topper (blows real-looking snow)", K, 69, ["Christmas", "wonder", "family"], "Our tree is SNOWING ❄️🎄", "Topper starts, soft snow falls around the tree", "Wow moment for families; nobody owns it yet.", "Mess / snow material safety", 9, 10, 10, 8, 8, 9, 7)
add("Santa Footprint & Sleigh-Track Christmas Morning Kit", K, 39, ["Christmas", "kids", "magic"], "Santa's sleigh landed in our yard 😱", "Morning: sleigh tracks in snow + glitter", "Christmas morning proof videos are huge.", "Low price", 9, 9, 10, 5, 9, 8, 9)
add("Personalised 'Letter from Santa' Kit with Wax Seal & North Pole Stamp", K, 39, ["Christmas", "kids", "personalized"], "She got a real letter from the North Pole ✉️", "Kid opens wax-sealed letter with her name", "Classic tradition, premium version.", "Low price", 9, 8, 10, 5, 9, 6, 9)
add("Gingerbread House Kit that Lights Up from Inside", K, 49, ["Christmas", "family", "cozy"], "Our gingerbread house glows at night 🏠✨", "Lights switch on inside the finished house", "Family activity + cozy decor.", "Food + electronics", 8, 9, 10, 6, 9, 8, 8)
add("Musical Rotating Christmas Village with Snow", K, 89, ["Christmas", "nostalgia", "decor"], "Grandma's Christmas village, but it snows now ❄️", "Train circles the village, snow falls, music plays", "Nostalgia for 35-65; high price.", "Fragile", 9, 10, 10, 8, 8, 7, 7)
add("Family Matching Christmas Pyjamas with Names", K, 99, ["Christmas", "family", "personalized"], "The whole family, matching, names on the back 🎄", "Family walks down the stairs in matching PJs", "Christmas photo tradition; group purchase = high AOV.", "Sizing returns", 9, 9, 10, 8, 9, 5, 6)
add("Christmas Eve 'Reindeer Food' Glitter Kit (eco)", K, 39, ["Christmas", "kids", "tradition"], "Sprinkle it on the lawn so the reindeer find us 🦌", "Kid sprinkles glittery oats on snow", "Tradition content; eco glitter.", "Low price", 8, 9, 10, 5, 9, 7, 9)
add("Santa Cam Doorbell Overlay (catch Santa on camera)", K, 45, ["Christmas", "kids", "magic"], "We caught Santa on our camera 🎅📹", "Kid watches video of Santa in their living room", "Proven 'catch Santa' videos go viral every year.", "Digital product - deliver well", 10, 9, 10, 6, 9, 6, 9)
add("Christmas Tree Collar that Plays Music & Lights Up", K, 79, ["Christmas", "decor", "wow"], "Our tree has a light show now 🎶", "Lights pulse to music at the tree base", "Decor upgrade.", "Electronics", 7, 9, 10, 8, 8, 8, 7)
add("Countdown-to-Christmas Wooden Advent House (refillable)", K, 69, ["Christmas", "family", "tradition"], "24 tiny doors, filled with love 🎁", "Kid opens a lit door each morning", "Reusable heirloom; daily content.", "Bulky", 8, 9, 10, 8, 8, 6, 8)
add("Ugly Christmas Sweater for Dog & Owner Matching Set", K, 59, ["Christmas", "pets", "humor"], "Matching ugly sweaters with my dog 🐶🎄", "Owner and dog strike a pose", "Pets + Christmas humour.", "Sizing", 9, 9, 10, 7, 9, 6, 7)
add("Christmas Window Projector (Santa flying past)", K, 59, ["Christmas", "kids", "wonder"], "Santa just flew past our window 😱", "Projector shows Santa silhouette crossing the window", "Neighbourhood wow.", "Projector quality", 9, 10, 10, 7, 8, 7, 8)
add("Hot-Cocoa Station Kit (bar sign, toppings jars, mugs)", K, 69, ["Christmas", "cozy", "family"], "We set up a cocoa bar for Christmas Eve ☕", "Reveal of a styled cocoa station", "Hosting trend.", "Many parts", 8, 8, 10, 8, 8, 7, 8)
add("Personalised Christmas Stocking with Light-Up Name", K, 45, ["Christmas", "family", "personalized"], "Our names glow on the fireplace 🎄", "Lights off: names glow on stockings", "Family personalised decor.", "Personalisation", 8, 9, 10, 6, 9, 7, 8)
add("Christmas Memory Jar (write one memory each day)", K, 39, ["Christmas", "family", "memory"], "We read all our memories on Christmas morning 🥹", "Family reads notes from a glowing jar", "Emotional tradition.", "Low price", 8, 7, 10, 5, 9, 8, 9)
add("Snowball Fight Indoor Kit (soft snowballs + fort)", K, 45, ["Christmas", "family", "fun"], "Snowball fight in the living room ⛄", "Family throws soft snowballs, laughing", "Fun family content.", "Low novelty", 8, 9, 9, 6, 9, 7, 9)
add("Santa's Nice List Certificate + Gold Medal Box", K, 39, ["Christmas", "kids", "pride"], "He made the NICE list 🏅", "Kid opens box with medal & certificate", "Pride moment for kids.", "Low price", 9, 8, 10, 5, 9, 8, 9)
add("Christmas Tree Skirt with Kids' Handprints (DIY kit)", K, 49, ["Christmas", "family", "memory"], "Every year, a new handprint 🎄🖐️", "Kids press painted hands on tree skirt", "Heirloom tradition.", "Mess", 8, 8, 10, 6, 9, 8, 9)
add("Nativity-Free Winter Wonderland Light Tunnel (garden)", K, 129, ["Christmas", "wonder", "family"], "We walked through a tunnel of light 😍", "Family walks through a glowing arch tunnel", "Big-ticket outdoor wow.", "Outdoor install", 8, 10, 10, 9, 7, 8, 6)

K = "Christmas magic"
add("Talking Santa Phone Call Ornament (kid presses, Santa answers)", K, 49, ["Christmas", "kids", "magic"], "She called Santa and he ANSWERED 😭", "Kid presses ornament, Santa's voice says her name", "Personalised voice + Christmas = tears.", "Voice recording workflow", 10, 9, 10, 7, 8, 8, 8)
add("Christmas Countdown Clock (days until Christmas, snow display)", K, 49, ["Christmas", "anticipation", "decor"], "Only 12 more sleeps ❄️", "Clock flips to the new number, snow animation", "Daily anticipation, decor gift.", "Seasonal", 7, 9, 10, 6, 9, 8, 9)
add("Santa Sack Personalised with Velvet & Name", K, 45, ["Christmas", "kids", "personalized"], "Santa left a sack with her name on it 🎅", "Christmas morning: huge velvet sack by the tree", "Gift-wrapping alternative, tradition.", "Low price", 8, 8, 10, 6, 9, 6, 9)
add("Christmas Tree Ornament Advent (24 ornaments, one per day)", K, 59, ["Christmas", "family", "tradition"], "A new ornament every day until Christmas 🎄", "Kid hangs one ornament per day", "Daily ritual + keepsakes.", "Fragile", 8, 8, 10, 7, 8, 7, 8)
add("Light-Up Reindeer Antler Headband Family Pack", K, 39, ["Christmas", "family", "humor"], "The whole family turned into reindeer 🦌", "Family turns on glowing antlers in the dark", "Party fun, cheap.", "Low price", 7, 9, 10, 5, 9, 6, 9)
add("Christmas Morning Photo Backdrop Kit (balloon arch + sign)", K, 69, ["Christmas", "family", "memories"], "Our Christmas photos look professional now 📸", "Time-lapse building backdrop, family photo", "Photo culture.", "Many parts", 7, 9, 10, 7, 8, 7, 8)
add("Cozy Christmas Movie Night Box (pjs, cocoa, popcorn, socks)", K, 79, ["Christmas", "cozy", "gift"], "The best Christmas Eve box ever 🍿🎄", "Opens box layer by layer", "Unboxing + cozy; high AOV.", "Assembly", 8, 8, 10, 8, 8, 6, 8)
add("Elf Door with Light-Up Window & Tiny Mailbox", K, 39, ["Christmas", "kids", "magic"], "An elf moved into our wall 😱", "Tiny door glows, mailbox has a note", "Magic for kids.", "Low price", 9, 9, 10, 5, 9, 7, 9)
add("Christmas Tree Angel that Moves Its Wings", K, 59, ["Christmas", "decor", "wonder"], "Our angel waves her wings at midnight 👼", "Topper wings slowly flap, lights glow", "Decor with motion.", "Mechanics", 7, 10, 10, 7, 8, 9, 7)
add("Personalised Baby's First Christmas Ornament with Footprint", K, 39, ["Christmas", "baby", "memory"], "Her first Christmas, her tiny footprint 🥹", "Ornament with clay footprint and name", "New parents are a huge gift market.", "Low price", 9, 8, 10, 5, 9, 6, 9)
add("Christmas Lights Hat / Beanie that Glows", K, 39, ["Christmas", "humor", "party"], "Lit up like a Christmas tree (literally) 🎄", "Beanie lights in colours", "Party gag.", "Low price", 7, 9, 9, 5, 9, 7, 9)
add("Santa's Workshop Desk Kit for Kids (stamp, letters, list)", K, 49, ["Christmas", "kids", "creativity"], "My son runs Santa's workshop now 🎅", "Kid stamps 'APPROVED' on nice list", "Role-play gift.", "Medium novelty", 8, 8, 10, 6, 9, 8, 9)
add("Christmas Train that Runs Around the Tree with Smoke", K, 89, ["Christmas", "nostalgia", "family"], "Dad's childhood train, back under our tree 🚂", "Train circles the tree, puffs smoke", "Nostalgia for dads; high price.", "Existing category", 9, 10, 10, 8, 8, 5, 7)
add("Personalised Christmas Cookie Cutter of Your Pet", K, 39, ["Christmas", "pets", "personalized"], "Cookies shaped like our dog 🐶🍪", "Cuts dough, dog-shaped cookie", "Pets + baking + Christmas.", "Low price", 8, 9, 10, 5, 9, 9, 9)
add("Christmas Wreath with Hidden Speaker that Says Welcome", K, 69, ["Christmas", "humor", "home"], "Our wreath greets every guest 😂", "Guest arrives, wreath says hello", "Funny + decor.", "Electronics outdoor", 7, 9, 9, 7, 8, 9, 7)
add("Ugly Christmas Sweater Kit (DIY with patches & lights)", K, 45, ["Christmas", "creativity", "party"], "Made the ugliest sweater at the party 🏆", "Time-lapse decorating a sweater", "Party content + DIY.", "Sizing", 7, 8, 10, 6, 9, 7, 8)
add("Christmas Tree Fresh-Scent Diffuser for Fake Trees", K, 39, ["Christmas", "cozy", "sensory"], "Fake tree, real pine smell 🌲", "Clips diffuser on branch, mist", "Fake-tree owners problem.", "Low emotion", 6, 7, 9, 5, 9, 8, 9)
add("Personalised North Pole Passport for Kids", K, 39, ["Christmas", "kids", "magic"], "She's officially allowed into the North Pole 🛂", "Kid gets passport stamped by 'elf'", "Magic role-play.", "Low price", 8, 8, 10, 5, 9, 9, 9)
add("Giant Christmas Present Box Seat (sit-in photo prop)", K, 59, ["Christmas", "kids", "funny"], "We wrapped our toddler 🎁", "Toddler pops out of a giant present", "Funny photo content.", "Bulky", 8, 9, 10, 6, 8, 8, 8)
add("Christmas Card Holder Tree (wall, lights)", K, 45, ["Christmas", "decor", "family"], "All our Christmas cards in one glowing tree", "Cards clipped on lit wall tree", "Decor + family.", "Low emotion", 6, 8, 9, 6, 9, 8, 9)
add("Snow Globe Water Bottle for Kids", K, 39, ["Christmas", "kids", "cute"], "Her water bottle has a snow globe inside ❄️", "Shake: glitter snow swirls", "Cute daily use.", "Leaks", 7, 9, 9, 5, 9, 8, 8)
add("Personalised Christmas Plate Set for Santa's Cookies", K, 45, ["Christmas", "kids", "tradition"], "Cookies for Santa, on his own plate 🍪🥛", "Kid leaves cookies; morning crumbs + note", "Tradition + keepsake.", "Ceramic shipping", 8, 8, 10, 6, 9, 6, 8)
add("Light-Up Christmas Pyjama Onesie for Adults", K, 59, ["Christmas", "humor", "cozy"], "Mom's new Christmas morning uniform 😂", "Onesie trim lights up", "Funny + cozy.", "Sizing", 7, 9, 10, 7, 9, 7, 7)
add("Christmas Bucket-List Scratch Poster for Families", K, 39, ["Christmas", "family", "anticipation"], "24 Christmas things to do together", "Kid scratches gold foil to reveal activity", "Family activity content.", "Low price", 7, 8, 10, 5, 9, 7, 9)
add("Personalised Christmas Tree Ornament with Couple's Names & Year", K, 39, ["Christmas", "couples", "personalized"], "Our first Christmas in our first home 🏡", "Hangs ornament with names and year", "Couples milestone.", "Crowded on Etsy", 8, 8, 10, 5, 9, 4, 9)
add("Gingerbread Man Plush with Heated Belly", K, 45, ["Christmas", "kids", "cozy"], "The cutest bedtime buddy this Christmas 🍪", "Kid hugs warm gingerbread plush", "Cute + cozy.", "Kids heating safety", 8, 8, 10, 6, 8, 8, 7)
add("Christmas Ornament Photo Projector Ball", K, 49, ["Christmas", "memory", "family"], "Our family photos glow on the wall from the tree 🎄", "Ornament projects photos on the wall", "Memory + decor.", "Tech", 9, 9, 10, 7, 8, 9, 8)
add("Santa's Magic Snow Dust (instant snow powder kit)", K, 39, ["Christmas", "kids", "wonder"], "Add water and it turns into snow 😱", "Powder + water = fluffy snow", "Wow science demo.", "Low price", 8, 10, 9, 5, 9, 6, 9)

xmas = lambda x: any(w in " ".join(x["emotions"]) + x["name"] for w in ("Christmas", "Santa", "Advent", "ornament", "Ornament", "Snow", "snow"))
for x in I:
    x["score"] = round(sum(x["scores"][k] * w for k, w in W.items())); x["christmas"] = bool(xmas(x))
keep = sorted(I, key=lambda x: (-x["christmas"], -x["score"]))
nonx = sorted([x for x in I if not x["christmas"]], key=lambda x: -x["score"])
I = [x for x in I if x["christmas"]] + nonx[:max(0, 100 - sum(x["christmas"] for x in I))]
I = I[:100]
assert len(I) == 100, len(I)
I.sort(key=lambda x: -x["score"])
for r, x in enumerate(I, 1):
    x.update(rank=r, status="idea", id=re.sub(r"[^a-z0-9]+", "-", x["name"].lower()).strip("-")[:60])
json.dump(I, open(__file__.replace("build_ideas.py", "ideas.json"), "w"), indent=1, ensure_ascii=False)
