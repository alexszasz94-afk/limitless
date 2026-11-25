import html, sys, os, io, base64
from PIL import Image
OUT_MD, OUT_HTML, IMG = sys.argv[1], sys.argv[2], sys.argv[3]
def U(k): return ("https://www.aliexpress.com/item/%s.html" if k.startswith("1005") else "https://www.aliexpress.us/item/%s.html") % k
def P(n,img,fresh,tags,s,what,pot,cost,sold,rating,sell,links,concepts,risks):
    return dict(n=n,img=img,fresh=fresh,tags=tags,s=s,score=sum(s),what=what,pot=pot,cost=cost,sold=sold,rating=rating,sell=sell,links=links,concepts=concepts,risks=risks)
def NP(custom,niches,p):
    p["custom"]=custom; p["niches"]=niches; return p
D=[
# ---------- fresh waves ----------
P("Christmas Sleigh Pet Bed","2.jpg","wave",["xmas","pets"],[9,8,9,9,9],
 "Plush pet bed shaped like Santa's sleigh, for cats and small dogs. Washable cover, non-slip base.",
 "A ready-made Christmas photo that pet owners share. 11 listings, almost all fresh, each with only 3 to 21 orders: the wave is just starting.",
 "$11.09 to $36.59","about 120 across 11 listings","5.0 on the few rated","$39.99 to $49.99",
 [("21 sold, 5.0","3256810366894861"),("17 sold, 5.0","3256813037054703"),("Larger sled bed","3256812984784938")],
 [("Do NOT let… see this","Do NOT show this to a dog mom before Christmas","Dog sits in the sleigh with reindeer antlers, owner covers her mouth. Same hook action as our Grinch reel, then B-roll: set the bed by the tree, dog climbs in, cozy night shot."),
  ("Gifting reaction","He thinks he is delivering the presents this year","Owner unwraps the sleigh, dog jumps in before she finishes. Gift boxes stacked behind him.")],
 "Little order proof yet. Walmart sellers list similar beds at $13 to $35 and T.J. Maxx carried one. Only small pets fit, which the video must show."),
P("Electric Cat Whack-a-Mole Toy","whack.jpg","wave",["pets"],[8,7,10,9,8],
 "Rechargeable box with 6 holes. Feather tassels pop up at random and the cat smacks them.",
 "The cat's reaction is the whole video and needs no words. 5 fresh listings, about 990 orders in total, top one rated 4.9.",
 "$8.33 to $12.45","365, 269, 238, 60, 59","4.9, 4.7, 4.6","$39.99 with spare feather set",
 [("365 sold, 4.9","1005013410725504"),("238 sold, 4.6","3256812887305081"),("3 in 1 version","3256812835738470")],
 [("Pattern interrupt","My cat has not blinked in 11 minutes","Top-down shot of the cat frozen over the box, then a burst of smacking. B-roll: unbox, charge, three cats around it."),
  ("Problem → solution","3 a.m. zoomies vs. 3 a.m. now","Cat sprinting over the bed at night, cut to the cat busy with the toy in the hallway while the owner sleeps.")],
 "Cheap item, so $39.99 needs a bundle. Two listings are rated under 4.5. Not Christmas, which helps after December."),
P("Pet Christmas Tree Costume","treecostume.jpg","wave",["xmas","pets"],[8,7,9,10,8],
 "Green hooded cape with pom-poms and a star on the hood that turns a cat or small dog into a little Christmas tree. A red Santa version exists.",
 "Cute in one second and made for sharing. 5 fresh listings with about 275 orders, plus a Santa cape with 172.",
 "real price not shown (promo prices only)","86, 56, 54, 44, 35","4.8 to 5.0","$39.99 for a 2-cape set",
 [("86 sold, 5.0","1005013302319394"),("54 sold, 4.8","3256812969871752"),("Santa cape, 172 sold","1005013301283764")],
 [("3-2-1 reveal","3… 2… 1… we got a second tree this year","Owner holds a towel in front of the dog and counts, drops it: the dog is the tree, star on its head."),
  ("Do NOT let… see this","Do NOT let a dog mom see this before the family photo","Family lined up by the tree, the dog walks in dressed as the tree, everyone loses it.")],
 "Very cheap item and pet costumes are an old category; only this design is fresh. Sizes cause returns. Works only as a set."),
P("Lying Santa Roof Inflatable (8 to 12 ft)","lying.jpg","wave",["xmas"],[7,9,7,10,8],
 "Giant LED inflatable Santa lying on his side with sunglasses and a drink, for the garage roof or lawn. Up to 3.6 m.",
 "A funny instant read from the street. 7 fresh listings and the biggest sizes sell at $77 to $103, so the price holds.",
 "$28.31 to $102.70","about 172 across 7 listings","4.4 on the one rated listing","$79 to $129",
 [("71 sold","3256813129656712"),("38 sold, $48.09","3256813208791359"),("38 sold, $56.18","3256813138537877")],
 [("Pattern interrupt","Santa clocked out early at our house","Slow push-in from the street to Santa lounging on the garage roof at dusk, lights coming on. B-roll: unroll, inflate in real time, kids pointing."),
  ("Product vs product","The neighbours: 4,000 lights. Us:","Their house covered in lights, then ours with one huge lazy Santa. Deadpan.")],
 "The only rating shown is 4.4, under our 4.5 rule. Low orders so far. Bulky to ship and needs a blower and a US plug. Hard for Kling to keep a huge inflatable identical between shots."),
P("Stacked Santa, Reindeer and Snowman Inflatable (7.8 ft)","stacked.jpg","wave",["xmas"],[7,8,7,10,7],
 "2.4 m LED yard inflatable: Santa sitting on a reindeer sitting on an upside-down snowman.",
 "A character tower nobody has seen before, readable at a glance. Two fresh listings with 265 and 260 orders, both rated 5.0.",
 "$32.74 to $49.57","265 and 260","5.0 and 5.0","$79 to $89",
 [("265 sold, 5.0","3256813138260495"),("260 sold, 5.0","3256812792229083")],
 [("3-2-1 reveal","3… 2… 1… dad said he only bought one decoration","Flat fabric on the lawn, blower on, the tower rises in real time while the kids scream."),
  ("Store find","Found this and I am not leaving without it","Generic store aisle, she spots the box, hugs it. Cut to the tower lit up at night. No store names or logos.")],
 "Bulky. Shipping cost and days not verified. Inflatables as a category are sold everywhere; only this design is fresh."),
P("Christmas Magic Trail Wall Light","1.jpg","wave",["xmas"],[8,7,6,9,7],
 "Glowing winding track that hangs on the wall with a small Christmas train on it. Some versions show Santa's sleigh and reindeer.",
 "The only find with a wave of fresh listings and big order counts already: about 10 sellers appeared at once, top two at 2,000+ and 1,000+.",
 "$12.50 to $18.93","2,000+ and 1,000+","4.9 and 4.9","$39.99",
 [("2,000+ sold, 4.9","3256813237585599"),("1,000+ sold, 4.9","3256813406056769")],
 [("3-2-1 reveal","POV: you turn the lights off and Christmas runs up your wall","Dark room, kid flips the switch, the trail lights up from bottom to top."),
  ("Pattern interrupt","My husband said no more Christmas decorations. So I used the wall.","She hangs it in one move, he walks in and stops. B-roll: unbox, hang, room at night.")],
 "Clone listings at $6 to $9 are rated 1 to 3 stars, so the supplier must be one of the 4.9 ones. Some versions need assembly. A larger size or 2-pack helps defend $39.99."),
P("Santa in a Hot Cocoa Mug Inflatable (6 ft)","cocoa.png","wave",["xmas"],[7,7,6,9,6],
 "LED yard inflatable of a Santa-face cocoa mug with a gingerbread man and a marshmallow on top.",
 "Cozy and cute together, and a sibling of the gingerbread man below. Two fresh listings, 212 and 45 orders, 4.9.",
 "$35.66 to $46.98","212 and 45","4.9","$89 to $99",
 [("212 sold, 4.9","3256813364391020"),("45 sold","3256813140649062")],
 [("Day 1 vs now","Day 1 of December vs. after mom found this","Empty lawn, then the giant mug glowing in the snow with the kids holding real cocoa next to it."),
  ("Gifting reaction","We surprised grandma's front yard while she was at church","Family inflates it fast, she pulls into the driveway and laughs.")],
 "Bulky, shipping not verified. Second listing has no rating."),
P("Christmas Squishy Surprise Box","dumpling.jpg","wave",["xmas"],[7,6,7,8,7],
 "Display box of soft squeeze toys with Santa, snowman and elk faces. Titles call them dumpling squishies in a steamer box; the photo shows a surprise box.",
 "Satisfying to squeeze on camera and a cheap stocking filler. 12 fresh listings, about 900 orders in total.",
 "$1.09 to $21","137, 100, 97, 97, 88 and more","mixed: 2 to 5","$39.99 for a full gift box",
 [("97 sold, $21","3256813306161558"),("137 sold, 5.0","3256812828703822")],
 [("Unboxing + reaction","Do not open the Christmas steamer before the 25th","Hands lift the lid, squeeze each face slowly, kid tries to steal one."),
  ("Store find","Found the squishies everyone is hiding from their kids","Generic aisle, she grabs the last box. Cut to the kids on Christmas morning.")],
 "Ratings are mixed, so quality varies by seller. Tiny unit price. The audience skews young, which our rules avoid. The plain dumpling squishy is already huge; only the Christmas edition is new."),
P("LED Starburst Christmas Ball (30 or 50 cm)","ball.jpg","wave",["xmas"],[7,6,6,9,6],
 "Large hanging ball that lights up like a frozen firework, with snowflakes inside.",
 "Big glowing object in a dark room is an easy wow. Two fresh listings with 411 and 193 orders.",
 "$8.55 to $13.12","411 and 193","not shown","$39.99 for the 50 cm or a set of 3",
 [("411 sold","3256813234431204"),("193 sold","3256813233429079")],
 [("3-2-1 reveal","3… 2… 1… the only ornament we bought this year","She holds it under a towel, counts, switches it on in the dark."),
  ("Product vs product","$400 of ornaments vs. three of these","Tree with boxes of ornaments on the floor, then a bare corner lit by three balls.")],
 "No rating shown on either listing. Similar starburst lights exist as garden lights; the Christmas ball is the fresh part."),
P("Lighted Musical Village House With Skaters","village.jpg","wave",["xmas"],[7,6,6,8,6],
 "Tabletop snow village house with lights, music and small figures skating in a circle.",
 "Nostalgia for parents and grandparents. Two fresh listings with 279 and 278 orders, both 4.9.",
 "$14.59 to $16.59","279 and 278","4.9 and 4.9","$39.99 to $49.99",
 [("279 sold, 4.9","1005013410597943"),("278 sold, 4.9","1005013197783413")],
 [("Gifting reaction","I found the village my grandma had in 1994","She unwraps it, switches it on, goes quiet. Close shot of the skaters turning."),
  ("Story","Every year my dad set this up alone. This year I did it for him.","Three shots: empty mantel, hands placing the house, dad watching the skaters.")],
 "Lighted villages are an old US category; only this model is fresh. Music means the sound in the video must be the real one."),
P("Recordable Christmas Tree Message Bottle","bottle.png","wave",["xmas"],[9,5,8,4,7],
 "Small bottle ornament with a snowy tree inside and a voice recorder: record a message, press to play it back.",
 "The strongest emotion of the list, a loved one's voice kept in an ornament. 11 fresh listings, about 714 orders.",
 "$5.82 to $19.99","215, 190, 84, 71 and more","5.0 on the best, 3.5 on the biggest","$39.99 for a set of 2",
 [("190 sold, 5.0","3256812794473128"),("215 sold, 3.5","3256812906816042")],
 [("Gifting reaction","She pressed the button and heard her mom's voice","Daughter hands grandma the bottle, grandma presses, hand to her chest. Voice by Kling, words fixed in the recipe."),
  ("Story","The last ornament we hang every year","Kid records a message for dad who is away, dad plays it on Christmas morning.")],
 "Needs sound to be understood. One title says glass, so breakage is a risk. Ratings vary a lot by seller. Voice keepsakes are already in our product finder."),
P("Glowing Crochet Door Strands","crochet.jpg","wave",["xmas"],[7,6,5,9,6],
 "Long lighted hanging strands topped with a crochet-look Santa, snowman, reindeer or gingerbread figure, for the front door or wall.",
 "Handmade look that lights up at dusk. 12 to 15 fresh listings; the top one has 1,000+ orders at 4.9.",
 "$1.09 to $12.85","1,000+ on the top listing","4.9 on the top, 1 to 3.2 on copies","$39.99 for a set of 3",
 [("1,000+ sold, 4.9","3256813138217055")],
 [("Day 1 vs now","My front door on December 1st vs. tonight","Plain door, then four strands glowing either side of it, neighbour stops to look."),
  ("Pattern interrupt","Everyone asks which grandma made these","Close on the crochet figures, then the lights switch on.")],
 "Copies are rated 1 to 3.2, which suggests they do not match the photo: only the exact top listing is usable. We must not say it is handmade. Batteries not included."),
P("Snowman Magic Fountain Light","fountain.jpg","wave",["xmas"],[6,6,5,9,5],
 "Snowman garden stake holding a glowing ball, with strands of light pouring down like a fountain. Solar.",
 "Looks like snow pouring out of a snowman, clear without sound. 12 fresh listings but only about 227 orders.",
 "$9.75 to $23.79","65, 43, 32 and more","mostly 5.0, one 1.0","$39.99 to $49.99 for a pair",
 [("65 sold, 5.0","3256812932483861")],
 [("3-2-1 reveal","3… 2… 1… the snowman that never melts","Dusk, hand on the switch, the light pours down."),
  ("Product vs product","Real snowman: gone by Tuesday. This one:","Melted snowman puddle, then the lit one in the same spot.")],
 "Low order counts. Solar brightness in winter is unknown. Weakest emotion of the fresh waves."),
# ---------- fresh, one seller ----------
P("Inflatable Gingerbread Man With Gift (8 ft)","ginger.jpg","single",["xmas"],[7,8,7,10,7],
 "2.4 m LED yard inflatable gingerbread man in a Santa hat holding a candy cane and a present.",
 "Strongest order count among the fresh listings: 5,000+ at 4.9 on a listing that is only weeks old.",
 "$44.89","5,000+","4.9","$99 to $119",
 [("5,000+ sold, 4.9","3256813196884680")],
 [("Pattern interrupt","The HOA has emailed us twice about the cookie","Gingerbread man towering over the garage, dad proud, mom facepalming. 8 ft is the real size."),
  ("3-2-1 reveal","3… 2… 1… the kids think we forgot to decorate","Kids at the window, blower on, he rises past the glass.")],
 "A fresh listing with 5,000+ orders can be an older product listed again, so newness is not certain. Bulky; shipping not verified."),
P("Pet Stairs With a Hidden Cave","stairs.jpg","single",["pets"],[8,6,8,9,7],
 "Felt steps for small dogs and cats to reach the bed or sofa, with a hiding cave inside.",
 "An old or small dog finally reaching the bed alone is a strong, honest moment. Two fresh listings, 115 and 48 orders, 4.9.",
 "$8.68 to $13.57","115 and 48","4.9","$39.99 to $49.99",
 [("115 sold, 4.9","3256813008812524"),("Felt version, 48 sold","3256813164692404")],
 [("Problem → solution","He is 13 and he could not jump on the bed anymore","Old dog looking up at the bed, then walking up the steps on his own. Owner tears up."),
  ("Pattern interrupt","Wait for the second cat","Dog climbs the stairs, a paw shoots out of the cave underneath.")],
 "Plain pet stairs are an old category; the cave is the fresh part. Felt may not hold a heavier dog, and the weight limit is not shown."),
P("Roller-Coaster Santa Train Music Box","coaster.png","single",["xmas"],[7,7,7,9,6],
 "32 cm tabletop loop track with a mini Santa train that runs the loop, with lights and 8 songs.",
 "A moving object that keeps eyes on the screen, and the supplier price already supports a premium price.",
 "$60.99","17","5.0","$119 to $129",
 [("17 sold, 5.0","3256812944689489")],
 [("Pattern interrupt","My dad has been watching this for an hour and will not say why","Dad's eyes following the train round the loop. Then the kids doing the same."),
  ("Gifting reaction","The one gift nobody put down on Christmas morning","Unwrap, switch on, whole family leaning in.")],
 "One seller and 17 orders: no proof yet. High supplier cost means a failed test is expensive."),
P("Santa Sleigh Flying Over a Snow Village (34 cm)","sleighvillage.png","single",["xmas"],[8,6,6,8,6],
 "Musical tabletop village with a Santa sleigh and reindeer that fly in a circle above the houses.",
 "Cozy wow piece for the mantel. Already priced above our minimum on the supplier side.",
 "$48.30","37","4.5","$99 to $119",
 [("37 sold, 4.5","3256812947785868")],
 [("3-2-1 reveal","3… 2… 1… watch above the rooftops","Lights off, towel off, the sleigh starts circling over the lit village."),
  ("Story","My son checks every night that Santa is still practising","Kid in pyjamas kneeling in front of it, chin on the table.")],
 "One seller, 37 orders. Moving parts can arrive broken."),
P("Cat Window Hammock With Wooden Frame","hammock.jpg","single",["pets"],[7,5,8,8,6],
 "Plush cat bed on a wooden frame that mounts at the window or beside the bed.",
 "Cozy cat-in-the-window shot, and the price level fits without a bundle. 291 orders at 4.9.",
 "$21.67 to $27.38","291","4.9","$49.99",
 [("291 sold, 4.9","3256813102561562")],
 [("Day 1 vs now","Where my cat watched the snow last year vs. now","Cat balancing on a cold sill, then stretched out on the hammock with snow falling outside."),
  ("Problem → solution","She used to wake me at 5 a.m. Now she has a job.","Cat on the owner's face, cut to the cat watching birds from the hammock.")],
 "Window perches are sold everywhere; only this frame design is fresh. How it mounts is unclear from the listing."),
P("LED Ferris Wheel Christmas Scene","ferris.jpg","single",["xmas"],[7,6,6,8,6],
 "Tabletop Christmas fairground with a lit ferris wheel, carousel and tiny stalls.",
 "More detail than the usual village piece, good for slow close-ups. 138 orders on a fresh listing.",
 "$21.89","138","not shown","$59.99",
 [("138 sold","3256813332679561")],
 [("Gifting reaction","I told her it was just a candle","She opens the box, the wheel lights up, she calls the kids."),
  ("3-2-1 reveal","3… 2… 1… the smallest Christmas market in the world","Dark table, switch on, slow push-in.")],
 "No rating shown. Unclear whether the wheel really turns: the video may only show what it does."),
P("5 ft Snowman Inflatable With Rotating Lights","snowman.png","single",["xmas"],[6,6,6,9,5],
 "Indoor or outdoor inflatable snowman with coloured lights that turn inside it.",
 "511 orders at 4.9 on a fresh listing and a very low supplier price.",
 "$9.25","511","4.9","$39.99 to $49.99",
 [("511 sold, 4.9","3256813045744155")],
 [("Day 1 vs now","No snow this year. So we made our own snowman.","Kids at the window looking at green grass, then dancing around the glowing snowman in the living room."),
  ("Gifting reaction","It was supposed to go outside","Toddler hugging it and refusing to let go.")],
 "The $9.25 may be a promo price. Snowman inflatables are common; the rotating light is the only fresh part."),
P("Ceramic-Look Lit Tree With Train Base","ceramic.jpg","single",["xmas"],[7,5,6,8,6],
 "Tabletop lit Christmas tree with coloured bulbs and a small train turning around the base.",
 "Retro tree that many Americans remember from their grandparents. 229 orders at 4.9.",
 "$17.33","229","4.9","$49.99",
 [("229 sold, 4.9","3256813149867873")],
 [("Gifting reaction","Grandma had this exact tree. Hers did not have the train.","Mom opens the box and laughs, then cries a bit."),
  ("Store find","If you see this, do not walk past it","Generic shelf, hand grabs the last one. Cut to it glowing on the mantel.")],
 "Ceramic breaks in transit. Lighted ceramic trees are an old US category; only the train base is new."),
P("Musical Carousel Tree With Climbing Santa","carousel.jpg","single",["xmas"],[7,5,6,8,5],
 "Tabletop carousel with a lit tree on top, turning figures and a Santa climbing a ladder.",
 "Several moving parts in one piece. Fresh listing with 52 orders.",
 "$27.56","52","4.5","$59.99",
 [("52 sold, 4.5","3256813033220331")],
 [("Pattern interrupt","He has been climbing since Thanksgiving. Somebody help him.","Close on the tiny Santa on the ladder, carousel turning under him."),
  ("Gifting reaction","The gift my mother-in-law actually kept on the table","Unwrap, switch on, she moves the fruit bowl to make room.")],
 "Low orders and exactly 4.5. Close to the other village pieces, so test only one of them."),
# ---------- custom niche bases (round 4, 25 Nov; listed this week or in the last 2-3 weeks) ----------
NP("Dog collar (angel or dragon wings), horse tack, runners and cyclists, motorcycles: the same light already sold in four niches.",
 "Other wing shapes per group: eagle wings for hunters and bikers, butterfly for small dogs, breed-coloured sets; a horse-show version; a kids' scooter version.",
 P("Clip-On LED Wing Light","wingdog.jpg","niche",["pets"],[8,8,8,10,8],
 "Small light that clips to a dog collar, horse tack, a runner's belt or a bike and throws a pair of glowing wings on the ground behind.",
 "The strongest find so far: about 30 listings, all from the last 3 weeks, and 11 more dog listings appeared in the last 5 days alone. The biggest has about 247 orders. Reads instantly at night and is not seasonal.",
 "$10.19 to $36.89","about 247 on the biggest, then 95, 49, 41, 30 and less","none shown","$44.99 to $49.99",
 [("Dog, newest, $36.89","3256813509831358"),("Dog, about 247 sold","3256813447494385"),("Dog, 95 sold","3256813454540410"),("Horse version","3256813497935533"),("Runner version, 49 sold","3256813447514699")],
 [("Pattern interrupt","People keep stopping their cars to ask what my dog is","Night walk filmed from behind: plain dog, click, red wings spread on the road. Driver slows down."),
  ("Do NOT let… see this","Do NOT let a horse girl see this before the evening ride","Rider at dusk, wings glowing on the trail behind the horse.")],
 "Every listing photo is computer-made, and one carries an AI watermark: the real projection will be smaller and dimmer. A sample must be filmed before any video, and we show only what it really throws. Cheap versions at $6 to $11 suggest quality varies.")),
NP("Golden retriever now. Titles name the breed, so the breed is the part that changes.",
 "Dachshund, corgi and French bulldog versions; a horse; a tractor for farm families. Needs a supplier who makes custom inflatables.",
 P("Light-Up Inflatable Dog (5 ft)","infldog.png","niche",["xmas","pets"],[8,7,8,10,8],
 "LED yard inflatable of a sitting golden retriever in a Santa hat with a gift box.",
 "Breed owners buy anything with their breed on it, and an inflatable is filmed in one shot. 38 orders on a listing about two weeks old.",
 "$25.32 to $38.89","38 and 6","none shown","$69 to $79",
 [("38 sold, $25.32","3256813444222943"),("Older, 6 sold","3256813187163457")],
 [("Do NOT let… see this","Do NOT let a golden retriever mom see this","Real golden sits next to the glowing one, tilts its head. Owner gasps."),
  ("3-2-1 reveal","3… 2… 1… he has a twin now","Blower on, the inflatable rises beside the real dog.")],
 "Other sellers list a dachshund and a pug, so breeds do exist, but each is a separate supplier. A breed nobody makes means a custom order with a minimum quantity. Christmas-only as it stands.")),
NP("Golden retriever now. Dog figure on top, lit paw and icicles below.",
 "Any breed head on the same hanger; cat version; a horse head for stable doors; a name plate under the paw.",
 P("Dog Door Hanger With Lit Paw and Icicles","pawporch.png","niche",["xmas","pets"],[8,6,7,9,7],
 "Golden retriever figure in a Santa hat that hangs on the front door, with a glowing paw and lit icicles under it.",
 "Same idea as the snowman railing light, aimed at dog owners. One listing, about two weeks old, no orders shown.",
 "$10.79","none shown","none shown","$39.99 to $49.99",
 [("Only listing","3256813459522238")],
 [("Do NOT let… see this","Do NOT let a dog mom see this before she decorates the door","She hangs it, the paw lights up, the real dog looks up at it."),
  ("Day 1 vs now","Our front door last Christmas vs. this one","Plain wreath, then the dog hanger glowing at dusk.")],
 "One seller and no orders. The listing was described to me as a projector, but the photo shows a hanging figure with lights: what it really does needs a sample. Cheap, so the price needs a larger size or a set.")),
NP("Race car now; motorcycle version listed this week (separate card).",
 "Pickup truck, tractor, semi truck, muscle car, fire engine. This is the same move as the racing alarm clock in our playbook.",
 P("Car Alarm Clock With Engine Sound","caralarm.jpg","niche",[],[7,8,7,9,7],
 "Model car that is an alarm clock: display in the windscreen, engine sound, doors open, remote. Some versions spray mist.",
 "Already $40 to $57 at the supplier, so the price holds. About 8 listings in the last 2 to 3 weeks with 1 to 9 orders each.",
 "$39.32 to $57.19","9, 3, 1 and less","none shown","$89 to $99",
 [("Newest, $45.54","3256813446587334"),("9 sold, $40.67","3256813356740629")],
 [("Pattern interrupt","My husband has not been late once since I bought this","6 a.m., the car revs on the nightstand, he sits straight up."),
  ("Gifting reaction","He is 41. Look at his face.","He unwraps it, presses the remote, the doors lift.")],
 "The body in the photo copies a real sports car, so only a generic shape may be used. Novelty alarm clocks are already in our product finder. No custom words in the titles: re-theming is my inference.")),
NP("Red sport bike now, two listings this week.",
 "Cruiser, dirt bike, ATV, and the same clock as a tractor or truck.",
 P("Motorcycle Alarm Clock","motoalarm.jpg","niche",[],[6,6,6,9,6],
 "Battery alarm clock shaped like a red motorcycle, clock face in the rear wheel.",
 "Two listings from this week. Bikers buy bike-shaped gifts for themselves and get them from family.",
 "$24.59","none shown","none shown","$39.99 to $49.99",
 [("Newest","3256813498693750"),("Second listing","3256813479387936")],
 [("Gifting reaction","Dad said he did not want anything this year","He opens it, sets it next to his helmet."),
  ("Store find","If your dad rides, do not walk past this","Generic shelf, hand grabs it. Cut to it on his garage bench.")],
 "It only tells the time: nothing moves or lights up, so it is weak on screen. Older motorcycle clocks sell for $1 to $10, which makes $39.99 hard.")),
NP("Titles say 'Custom Music', 'Custom Engraving', 'Custom Picture Print', 'Custom Song'.",
 "Wedding or first-dance song with names and date; lullaby with the baby's name; a pet memorial with a photo on the lid.",
 P("Hand-Crank Music Box With Your Own Song","musicbox.jpg","niche",[],[8,5,8,4,7],
 "Wooden box with a brass movement that plays a song punched into a paper strip when you turn the handle. The song can be chosen.",
 "A gift that is different for every buyer, and $42 at the supplier already. The newest listing is about two weeks old.",
 "$42.49","none shown on the newest; 1,000+ on an older custom-print box","4.8 on the older one","$89 to $99",
 [("Newest, $42.49","3256813419323165"),("Older custom print, 1,000+ sold","3256810102531815")],
 [("Gifting reaction","She turned the handle and it was our wedding song","Wife cranks slowly, recognises it, looks up."),
  ("Story","The song my mom sang to me, for my daughter","Grandma, mother and baby, one box.")],
 "Needs sound to be understood. Custom songs mean a wait and a supplier who answers messages. Music boxes are an old category; the paper-strip custom song is the angle.")),
NP("Titles say 'Customized with Patterns, Names, and Dates', 'photo custom', and one is breed-specific.",
 "Per-breed silhouette; cat; horse; a larger headstone size to reach our price.",
 P("Personalised Pet Memorial Stone","memstone.png","niche",["pets"],[9,4,7,8,7],
 "Heart-shaped stone for the garden with the pet's photo, name, dates, angel wings and paw prints.",
 "The deepest emotion on the board, and every order is custom. Two listings in the last 2 to 3 weeks.",
 "$20.09 to $22.06","1","none shown","$49.99 to $59.99",
 [("Heart stone, $22.06","3256813459723988"),("Rectangular with photo","3256813446908283")],
 [("Story","Fourteen years. He still has his spot in the garden.","Empty dog bed, then hands placing the stone under a tree."),
  ("Gifting reaction","We gave this to my mom a month after Daisy","She reads the name, holds it to her chest.")],
 "Grief is the subject, so the tone must stay gentle and nothing is exaggerated here. Memorial stones have been sold for years; only these listings are new. Each order needs a photo from the buyer.")),
NP("Horse and foal now; a dog series exists in three breeds from another seller.",
 "Dog breeds, deer for hunters, cattle for farm families.",
 P("Glowing Animal Yard Statue","glowstatue.jpg","niche",["xmas"],[7,6,6,10,6],
 "Animal figure covered in warm lights for the yard. The photo shows a horse.",
 "A lit horse on the lawn is unusual and reads at night. About 7 listings; a dog series has 70 orders.",
 "$24.52 to $63.39","70 on the dog series; none shown on the newest","none shown","$99 to $119",
 [("Horse and foal, $54.19","3256813399585724"),("Dog series, 70 sold","3256810206041345")],
 [("Do NOT let… see this","Do NOT let a horse girl see this in December","Dark yard, switch on, the horse glows. She runs out in slippers."),
  ("Day 1 vs now","Everyone on our street has reindeer. We have this.","Row of lit reindeer, then our horse.")],
 "The newest listing is about three weeks old, not this week. No custom words in titles. Large and probably fragile to ship.")),
NP("Titles say 'Custom Text Neon Sign', 'Custom Personalized Garage Neon Signs'. Tractor, deer, dachshund and food shapes already exist.",
 "Fish for fishing dads, golf, pickleball, a breed outline with the dog's name.",
 P("LED Neon Shape Sign","neonmotif.jpg","niche",[],[6,5,5,10,5],
 "USB neon-style sign in the shape of an object. The newest one is a bowl of noodles.",
 "The most open base for custom: any shape and any name. One listing this week at $53.",
 "$15.62 to $56.99","up to 121 on older shapes","none shown","$79 to $89",
 [("Noodle sign, this week","3256813471630818"),("Custom garage sign","3256811709292369")],
 [("Gifting reaction","He has wanted a sign for the garage since 2015","Lights off, plug in, his name and a truck glow on the wall."),
  ("Day 1 vs now","The garage before vs. after one sign","Grey wall, then the lit sign over the workbench.")],
 "Neon signs are an old, crowded product; only the shapes are new. Weak emotion on its own. Several listings use real truck brand names, which we cannot.")),
NP("Titles say 'Custom Embroidered Name Text Logo', 'Monogrammed', 'Couples Robe'.",
 "A name on OUR heated robes as an add-on; nurse or vet-tech name; bridal party sets; golf-club style crest.",
 P("Embroidered Name Robe","namerobe.jpg","niche",[],[6,5,6,7,6],
 "Terry bathrobe with a name, text or logo embroidered on the chest or back. Sold as couples sets.",
 "Useful less as a new product than as proof that suppliers embroider names on robes: an upsell for the robes we already sell.",
 "$18.69","1 on the newest; 100 and 33 on older ones","none shown","add-on of $10 to $15 on our robes",
 [("Newest, $18.69","3256813402987680"),("Older, 100 sold","3256811853366368")],
 [("Gifting reaction","It has her name on it. She has not taken it off.","She opens the box, finds her name on the chest."),
  ("Unboxing + reaction","His and hers, and yes they are heated","Two robes, two names, same couch.")],
 "Plain robes are an old product. The idea here is the name on our own robe, which needs our supplier to agree and a longer delivery time.")),
NP("Every unit is custom: the photo shows two dogs, each with its own face and name on the ground. Titles say custom photo.",
 "Any breed and any name; a cat version; a memorial version with dates; a horse name for riders.",
 P("Name-and-Face Collar Projector","photocollar.jpg","niche",["pets"],[9,7,8,10,9],
 "Small light on the dog's collar that projects the dog's own face and name onto the pavement during a night walk.",
 "Listed in the last 5 days, two listings, no orders yet. Custom, tiny to ship, filmed in the dark, and aimed at people who buy anything with their dog on it.",
 "$23.39 to $25.29","1","none shown","$49.99 to $59.99",
 [("Newest, $25.29","3256813492939389"),("Second listing","3256813479870301")],
 [("Pattern interrupt","Strangers now know my dog's name before they know mine","Night walk past a cafe terrace, the dog's face and name glide over the pavement, people at the tables point and laugh."),
  ("Gifting reaction","I put his name on the street. She cried.","She clips it on, the name lights up on the ground, the dog sniffs its own face.")],
 "No orders and no ratings. The listing photo is computer-made, so the real projection will be smaller and blurrier: a sample is needed before filming. Every order needs a photo and a name from the buyer, which means messages and a longer wait.")),
NP("Highland cow now, listed in the last 5 days. Dog breeds exist from other sellers: golden retriever, dachshund, pug.",
 "Highland cow lovers, each dog breed, chicken and farm families. A custom shape needs a minimum order.",
 P("Highland Cow Light-Up Inflatable (5 ft)","cowinfl.jpg","niche",["xmas"],[8,7,7,10,8],
 "LED yard inflatable of a highland cow in a Santa hat holding a small tree and a candy cane.",
 "Highland cow fans buy the animal on everything, and this one is days old with nobody on it. Sits at $58 at the supplier.",
 "$57.79","none shown","none shown","$99 to $119",
 [("Only listing","3256813493161595")],
 [("Do NOT let… see this","Do NOT let a highland cow girl see this","She pulls into the driveway, the cow is glowing on the lawn, she stays in the car with her hands on her face."),
  ("3-2-1 reveal","3… 2… 1… he said no more cows in this house","Blower on, the cow rises outside the window. Technically not in the house.")],
 "One listing, no orders. Christmas-only as it stands, and the window closes in early December. Bulky to ship. Expensive to test.")),
# ---------- very new, almost no orders yet (round 2, 14 Nov) ----------
P("Tornado Vortex Lamp","vortex.jpg","early",[],[8,7,7,10,7],
 "Desk lamp with a column of water in which a spinning tornado is lit by colour-changing LEDs. About 35 cm, USB or battery.",
 "The only clear new wave outside Christmas: 12 recent listings, no big seller yet, and the real-size ones already cost $35 to $70, so the price holds. Not seasonal.",
 "$34.69 to $69.99 (small ones from $10.32)","about 22 across 12 listings","5.0 on five listings with 1 to 8 orders","$69 to $99",
 [("Main size, $34.69","3256813214453875"),("Larger, $67.79","3256813200555522"),("Small, 8 sold, 5.0","3256813086972932")],
 [("Pattern interrupt","There is a tornado on my nightstand and nobody warned me","Dark bedroom, hand presses the button, the vortex spins up and changes colour. B-roll: unbox, fill, kid's face lit blue."),
  ("Gifting reaction","I got my dad the one lamp he cannot stop staring at","Dad unwraps it, switches it on, pulls his chair closer.")],
 "Almost no orders, so no proof of demand. Unclear whether the tube is glass or acrylic; glass would rule it out. One cheap version is titled 'simulated' vortex, so only a version with a real water vortex may be filmed."),
P("Solar Santa Sleigh Light-Waterfall Stake","solarsleigh.jpg","early",["xmas"],[7,7,6,10,6],
 "Garden stake about 70 cm tall with Santa's sleigh on top and strands of warm star lights pouring down from it. Solar.",
 "About 19 listings appeared at once and none has volume yet: as early as it gets. Reads instantly at dusk.",
 "$13.01 to $39.69","about 29 across 19 listings","5.0 on the one rated","$49.99 for a pair",
 [("16 sold, 5.0","3256813245253925"),("70 cm resin and iron","3256813302857973"),("$39.69 version","3256813372324240")],
 [("3-2-1 reveal","3… 2… 1… Santa is dropping the presents early","Dusk lawn, the lights pour out of the sleigh as it gets dark. Kids run to it."),
  ("Day 1 vs now","Our front path on December 1st vs. tonight","Dark path, then a sleigh every few steps.")],
 "No proof yet. Solar brightness in winter is unknown and the listing photos look rendered, so the real glow may be weaker. Close to the Snowman Magic Fountain: test one, not both."),
P("Christmas Village Projection Centerpiece","projvillage.jpg","early",["xmas"],[8,7,7,9,6],
 "Tabletop gingerbread village in a tree shape with a light inside that throws gingerbread men, candy canes and stars onto the walls and ceiling.",
 "Lights off, switch on, the whole room fills with shapes: a strong kid reaction. About 12 fresh listings and 260 orders.",
 "$14.62 to $69.59","67 on the best-rated, 115 and 47 on cheap copies","5.0 on one, 1.5 and 2.0 on the best-selling cheap ones","$79 to $99 (the $42 to $70 version only)",
 [("67 sold, 5.0","3256813124222731"),("$42.89 version","3256813375389938"),("Rotating, $69.59","3256813172850638")],
 [("3-2-1 reveal","3… 2… 1… watch the ceiling","Family at the table, lights off, the room fills with gingerbread men. Kids point up."),
  ("Do NOT let… see this","Do NOT let a Christmas mom see this before December","She walks past it in a generic store aisle, stops, walks back.")],
 "The best-selling cheap copies are rated 1.5 and 2.0, which says the product does not match its photos. A sample is needed before any video: we may only show the projection it really makes. Room projectors are already crowded in our product finder."),
P("Rotating Santa Sleigh Tree Topper","topper.jpg","early",["xmas"],[7,7,7,9,6],
 "Lit star tree topper with Santa's sleigh and reindeer on an arm that circles the top of the tree, with music.",
 "The sleigh flying round the tree top makes kids look up. Fresh listings already sit at $45 to $47.",
 "$11.40 to $47.19","about 6 across 6 fresh listings; 45 and 40 on older ones","5.0 and 4.8 on the older ones","$59 to $69",
 [("Fresh, $45.29","3256813377840716"),("Older, 45 sold, 5.0","3256812751218674")],
 [("Pattern interrupt","My son has not looked at a single present. He is watching the roof of the tree.","Kid on the floor staring up, sleigh circling the star."),
  ("Product vs product","Every tree has a star. Ours has air traffic.","Normal star, then the sleigh doing laps.")],
 "Second-season product, not brand new, and still low volume after a year. Close in idea to the sleigh-over-village piece."),
P("Gingerbread House Music Box With Train","gingerhouse.jpg","early",["xmas"],[7,6,6,8,6],
 "Lit gingerbread candy-store house that plays music, with a small train or gingerbread man turning inside.",
 "Cozy and kid-friendly at a price that needs no bundle. 6 fresh listings.",
 "$15.25 to $85.09","none shown","none shown","$99 to $119",
 [("$65.89 version","3256813336763485"),("With rotating train, $63.99","3256813360511250")],
 [("Gifting reaction","She thought it was a cake box","Grandma lifts the lid, the house lights up and the train starts."),
  ("Story","The one decoration the kids are allowed to switch on themselves","Small hand on the switch every evening, three nights in a row.")],
 "Zero orders and no ratings. Resin or ceramic can break in transit. Very close to the village house and the ceramic tree already on the board."),
P("Infinity Cube Lamp","hypercube.jpg","early",[],[7,6,6,10,6],
 "Clear acrylic cube lamp with layered mirrors that looks like an endless tunnel of light.",
 "A small box that looks bottomless on camera. 6 fresh listings; an older listing of the same type has 276 orders at 4.9.",
 "$15.05 to $36.51","about 5 on fresh listings; 276, 234, 176 on older ones","4.6 to 5.0 on the older ones","$59 to $69",
 [("Fresh, $36.51","3256813276656536"),("Older, 276 sold, 4.9","3256810573323342")],
 [("Pattern interrupt","How deep is this box? Wrong.","Finger pointing into the cube, camera moves round to show it is 10 cm thick."),
  ("Gifting reaction","He asked for nothing. He has not left his desk since.","Husband unwraps it, turns the room light off.")],
 "The type has existed since earlier in 2026 and infinity mirrors are known in the West. Titles lean to gamer rooms, which is younger than our buyer."),
P("Valentine Squishy Box (24 pieces)","valsquish.jpg","early",["val"],[7,6,7,8,7],
 "Gift box of 24 small squeeze toys shaped like hearts, roses and sweets, sold as a Valentine countdown or surprise box.",
 "The Valentine version of the Christmas squishy box, listed early: 9 fresh listings and none has orders yet. The Christmas version on the same page shows 1,000+ orders at 4.9.",
 "$3.05 to $23.29","none shown","none shown","$39.99 for a large or double set",
 [("$23.29 set","3256813362914392")],
 [("Unboxing + reaction","A little squishy, a lot of love: she opened all 24 in one go","Hands open the lid, squeeze each heart, she steals the pink one."),
  ("Gifting reaction","He forgot the flowers. He did not forget this.","She frowns at the small box, opens it, cannot stop squeezing.")],
 "No orders at all yet. Cheap unit price. Several titles say 'for kids', which is outside our buyer. Avoid listings that use a toy brand's name."),
P("Remote-Control Blooming Rose Bouquet (building blocks)","rosebloom.jpg","early",["val"],[8,7,7,9,6],
 "Building-block rose bouquet in a pot whose flowers open and close by remote, with a glow.",
 "Roses that bloom on a button press is a clear 3-second wow for Valentine's, and the supplier price already supports a premium.",
 "$84.39","none shown","none shown","$149 to $169",
 [("Only listing","3256813373643371")],
 [("3-2-1 reveal","3… 2… 1… press it","He hands her the remote, the closed buds open and light up."),
  ("Product vs product","Real roses: dead by Friday. These:","Wilted bouquet in the bin, then the block roses opening.")],
 "One listing, no orders, no rating. The buyer has to build it. How the flowers move is unclear from the listing, so a sample is needed first. Expensive to test."),
P("Auto-Blooming Flower Lamp With Date","lotus.jpg","early",[],[7,6,6,9,5],
 "Flower-shaped lamp on a wood base whose petals open by themselves, with a warm glow and a date display in the centre.",
 "A calm wow gift for a mom or grandma. Not seasonal.",
 "$15.65","none shown","none shown","$49.99",
 [("Only listing","3256813328441235")],
 [("Gifting reaction","Mom, press the button","She presses, the petals open slowly, she looks up."),
  ("Day 1 vs now","What my mom's nightstand looked like before vs. now","Pile of chargers and a dead lamp, then the flower opening at dusk.")],
 "One listing, no orders. Petals are called 'crystal', which may mean glass."),
P("Giraffe Automatic Rope Cat Teaser","giraffe.png","wave",["pets"],[8,7,10,9,8],
 "Tall giraffe-shaped machine that sticks to a door and throws a rope out, then reels it back, over and over. Rechargeable.",
 "The only fresh pet find with real orders: two new listings with 468 and 258, rated 4.9 and 4.6. A fast action loop that needs no words.",
 "$7.33 to $10.19","468 and 258","4.9 and 4.6","$39.99 as a set with spare ropes",
 [("468 sold, 4.9","1005013423794603"),("258 sold, 4.6","1005013092548409")],
 [("Pattern interrupt","I work from home. This is my cat's new coworker.","Cat leaping at the rope again and again by the door while the owner types. B-roll: stick it on, charge, two cats queueing."),
  ("Problem → solution","My arm after 20 minutes with the feather wand vs. this","Owner's tired arm waving a wand, cut to the machine doing it while she drinks coffee.")],
 "Cheap, so a set is needed for $39.99. Older door-hanging string toys already have 10,000+ orders: the mechanism is known and only the launcher form is new."),
P("Clamp-On Desk Cat Bed","deskbed.jpg","early",["pets"],[8,6,8,9,7],
 "Plush cat bed on an arm that clamps to the edge of a desk, no drilling. Newer versions turn 360 degrees and adjust in height.",
 "The cat next to the laptop instead of on the keyboard: instant relief for anyone working from home. Price already near our minimum.",
 "$24.25 to $83.69","about 8 on fresh listings; 1,000+ and 700+ on older ones","4.8 and 4.9 on the older ones","$59 to $69",
 [("Fresh, $31.09","3256813222572738"),("Older, 1,000+ sold, 4.8","3256810180159848"),("Older 360°, 700+ sold","3256809871990131")],
 [("Problem → solution","Every meeting I have had this year vs. today","Cat walking across the keyboard on a video call, cut to the cat asleep on the bed beside the screen."),
  ("Do NOT let… see this","Do NOT show this to a cat mom who works from home","She clamps it on, the cat is in it before she lets go.")],
 "The type is not brand new: older listings have 1,000+ orders. Only the rotating, height-adjustable version is fresh. Weight limit not shown."),
P("Christmas Tree Cat Tower With Caves","sisaltree.jpg","early",["xmas","pets"],[8,7,8,9,8],
 "Cat tower shaped like a Christmas tree, with two round caves the cat sits in and a scratching trunk.",
 "The cat finally has its own tree to climb. Naturally priced above our minimum. 4 fresh listings.",
 "$20.19 to $131.49","none shown","none shown","$99 to $129",
 [("$56.29 version","3256813221163172"),("$29.29 version","3256813277609464")],
 [("Problem → solution","The only Christmas tree my cat is allowed to climb","Cat halfway up the real tree, ornaments falling. Cut to two cats looking out of their own tree."),
  ("3-2-1 reveal","3… 2… 1… which tree is hers?","Two trees side by side, a head pops out of the small one.")],
 "No orders shown on any listing. Size and weight unclear; the big version may be heavy to ship. Same idea as the felt tree cat house: test one of the two."),
P("Dog Tissue Box Snuffle Toy","tissue.jpg","early",["pets"],[7,7,9,9,7],
 "Fabric tissue box with cloth tissues that hide treats. The dog pulls them out one by one.",
 "A dog doing the naughty thing it is finally allowed to do. 5 fresh listings; slightly older ones have 269 and 191 orders at 4.9 and 4.6.",
 "$11.59 to $25.89","1 on fresh listings; 269, 191, 72 on older ones","4.6 to 5.0 on the older ones","$39.99 as a set of 2",
 [("Fresh, $25.89","3256813106529658"),("Older, 269 sold, 4.9","1005012619110494")],
 [("Pattern interrupt","He is allowed to do this. That is the whole point.","Dog yanking tissue after tissue, owner calmly watching. Then the real tissue box, untouched."),
  ("Problem → solution","What my living room looked like every time I left","Shredded tissues everywhere, cut to the dog busy with his own box.")],
 "Cheap item, around for several months already. Works only as a set."),
P("Duck Pedal Treat Dispenser","duckfeeder.jpg","early",["pets"],[7,6,9,9,7],
 "Duck-shaped feeder: the cat or dog presses the pedal and treats drop out.",
 "A pet that learned to pay itself is a funny, repeatable clip. 3 fresh listings.",
 "$19.55 to $32.99","none shown on the fresh listings","none shown","$39.99 to $49.99",
 [("Duck pedal, $19.55","3256813298325818"),("Press type, $32.99","3256813201729652")],
 [("Pattern interrupt","My cat has a job now and she is overpaid","Cat pressing the pedal again and again, staring at the owner between presses."),
  ("Story","Day 1: confused. Day 3: employed.","Three short shots of the same dog getting faster at it.")],
 "No orders shown. A similar duck dispenser with a new listing number shows 7,000+ orders, which usually means an older product listed again. Not every pet learns it, and the video must not promise that."),
P("Snowman Icicle Railing Light","icicle.jpg","early",["xmas"],[8,7,6,10,7],
 "Glowing snowman figure that sits on a porch or balcony railing with lit icicles hanging below it. About 1 m tall with the icicles.",
 "Made for the American front porch and clear in one second. About 15 listings, all from this season, and the most any of them has is 25 orders.",
 "$14.17 to $27.69","25, 20, 15, 14 and less","5.0 on the one rated","$59 to $69 for a set of 3",
 [("14 sold, $19.89","3256813159792452"),("25 sold, 5.0","3256813181193923"),("Newest, $18.99","3256813350369617")],
 [("Day 1 vs now","Our porch on December 1st vs. tonight","Bare railing in daylight, then three snowmen glowing along it at dusk with the icicles lit."),
  ("Do NOT let… see this","Do NOT let a Christmas mom see this before she finishes the porch","She clips one on, steps back, immediately orders two more.")],
 "Listing photos look rendered, so the real glow and size need a sample. Outdoor power or batteries are not stated. The set must be priced as three, since one is cheap."),
P("Campfire Friends Inflatable (8 to 10 ft)","warmtrio.jpg","early",["xmas"],[7,8,7,10,8],
 "LED yard inflatable of Santa, a polar bear, a reindeer and a dog sitting round a glowing campfire with mugs in hand.",
 "A whole funny scene instead of one figure, and it already sells for $74 to $90. Only 4 listings, all recent, none with orders.",
 "$73.79 to $90.09","none shown","none shown","$149 to $169",
 [("Newest, $90.09","3256813383620098"),("10 ft, $73.79","3256813342261625")],
 [("Pattern interrupt","Santa finished early and invited the boys over","Night shot of the lawn: the four of them round the fire, mugs up. Dad walks out with his own mug and sits next to them."),
  ("3-2-1 reveal","3… 2… 1… the neighbours are going to talk","Flat fabric on the snow, blower on, the campfire scene rises.")],
 "No orders and no ratings at all. Large and heavy to ship, and expensive to test. The mugs look like beer, which some buyers will not want in the yard."),
P("Christmas Tree With Legs","elftree.jpg","early",["xmas"],[8,7,6,10,7],
 "Small decorated tree with a curled top that stands on two legs in red boots. Sold as a DIY light-up piece in two sizes.",
 "A tree that looks like it could walk off is funny at a glance. The newest listing is days old; an earlier cheap one has 35 orders.",
 "$11.65 to $36.19","35 on the cheaper listing","none shown","$49.99",
 [("Newest, $36.19","3256813440357275"),("35 sold, $11.65","3256813330919792")],
 [("Pattern interrupt","I turned around and the tree had moved","Tree by the door, cut, tree by the fridge, cut, tree at the top of the stairs. Kid points."),
  ("Gifting reaction","She opened it and said 'it has BOOTS'","Mom lifts it out of the box by the boots and cannot stop laughing.")],
 "The curled-top tree style is close to a well-known Christmas film look, so no green character, no film words and no similar music in the video. Not confirmed that the two listings are the same object. Says DIY, so the buyer may have to assemble it."),
# ---------- already known ----------
P("Felt Christmas Tree Cat House","3.jpg","known",["xmas","pets"],[8,7,8,9,8],
 "Cone-shaped felt cat cave that looks like a small Christmas tree with pom-pom ornaments.",
 "A related product (a cat tree that turns into a Christmas tree) reportedly hit 34 million views on one video. That shows demand for the idea, not for this item.",
 "$24.79 to $36.08","90 and 39","4.8 and 4.9","$49.99",
 [("90 sold, 4.8","3256810025060388"),("39 sold, 4.9","3256810025048367")],
 [("Problem → solution","The only Christmas tree my cat is allowed to destroy","Cat knocks ornaments off the real tree, cut to the cat asleep inside its own."),
  ("3-2-1 reveal","3… 2… 1… find the cat","Two trees in the room, the small one moves, a paw comes out.")],
 "Sold by Walmart, Etsy (about $62) and Amazon ($49.88). Felt may arrive folded."),
P("Pop-Up Pre-Decorated Christmas Tree","4.png","known",["xmas"],[7,9,7,10,8],
 "Flat collapsed tree that pulls up into a full tree with lights and ornaments already on it. 4 to 7 ft.",
 "The pull-up moment is the strongest too-good-to-be-true shot here, and it is true.",
 "$48.76 to $98.47","391, 51, 27","4.4 on the biggest, 5.0 on the 51-sold","$129 to $149",
 [("391 sold, 4.4","3256809539423578"),("51 sold, 5.0","3256812712026934"),("Fresh, $48.76","3256813257048250")],
 [("Product vs product","Him: 3 hours and a ladder. Me:","Split screen: he untangles lights, she pulls the tree up in one move and sits down with cocoa."),
  ("Pattern interrupt","I decorated the whole tree during one commercial break","One continuous shot, timer on screen with the real time.")],
 "At least one brand already sells it with paid marketing and Walmart lists one. Bulky. Biggest listing is under our 4.5 rule. Late orders miss Christmas."),
P("Electric Climbing Santa (rope or ladder)","5.jpg","known",["xmas"],[7,6,8,9,6],
 "Small motorised Santa that climbs up and down a rope or a red ladder while music plays.",
 "Kids and cats stare at it. The rope version has 1,000+ orders; a fresh red-ladder listing has 52.",
 "$13.28 to $13.55","1,000+ and 52","4.6 and 5.0","$39.99 for a 2-pack",
 [("Rope, 1,000+ sold","3256809458469879"),("Red ladder, fresh","3256812871015807")],
 [("Pattern interrupt","My cat has been watching Santa climb for 40 minutes","Cat's head going up and down with Santa."),
  ("Pattern interrupt","Santa has been climbing since November 1st. Somebody help him.","Close on the little Santa struggling up the rope.")],
 "An old product. Thin margin, small motors break."),
P("AI Talking Plush Pet","8.jpg","known",[],[8,6,8,5,8],
 "Soft plush robot that listens and answers by voice over Wi-Fi. Several characters.",
 "A 2026 category: branded versions cost $140 to $429, AliExpress starts at $31. Many brands are launching it at once.",
 "$31.27 to $92.99","1,000+ on each main listing","4.9 and 4.5","$79 to $129",
 [("1,000+ sold, 4.9","3256809773989740"),("Fresh cat version","3256813236086469")],
 [("Unboxing + reaction","I asked it one question and my 6-year-old has not put it down since","Kid whispers to the plush, it answers, jaw drops."),
  ("Product vs product","This is the $40 version of the $400 AI pet","Side by side with a generic expensive robot pet.")],
 "Hardest to film honestly: only answers the toy really gives. Needs Wi-Fi and an app. Press already warns parents about AI toys."),
P("Santa Riding the Dog Costume","9.jpg","known",["xmas","pets"],[8,8,9,10,9],
 "Dog outfit with a small Santa figure on the dog's back, so Santa rides when the dog runs.",
 "Instant laugh with no words needed.",
 "$15.99 to $21.65","361, 218, 41","4.9 to 5.0","$39.99 only as a set",
 [("41 sold, 5.0","3256809604491122"),("Fresh fleece version","3256813146098508")],
 [("Pattern interrupt","Santa came early and he is NOT in control","Dog sprints through the house, Santa bouncing on his back."),
  ("Do NOT let… see this","Do NOT buy this if you want a calm Christmas","Kids screaming with laughter as the dog runs past the tree.")],
 "Sold cheaply everywhere for years. Fails our price rule alone. Sizes cause returns."),
P("Inflatable Santa Climbing In Through the Window","6.jpg","known",["xmas"],[6,8,6,9,6],
 "LED inflatable Santa that hangs from a window or balcony so he looks like he is climbing in. 2 m and 3 m.",
 "A harmless prank on the whole street.",
 "$23.06 to $35.26","461 and 287","4.7 and 4.9","$49.99 to $59.99",
 [("461 sold, 4.7","3256809491538526"),("Fresh, 287 sold","3256812724136778")],
 [("Pattern interrupt","The neighbours called to say someone is breaking into our house","Night shot from the street, phone buzzing, then Santa lit up at the window."),
  ("Pattern interrupt","He is stuck. He has been stuck since Thanksgiving.","Kids waving at him from inside.")],
 "Lowe's, Target and Costway sell it for about $25 to $70."),
P("10 ft Sitting Santa Inflatable With Reindeer","7.jpg","known",["xmas"],[6,9,6,9,6],
 "3 m LED inflatable Santa sitting with a reindeer and gift box, for roof or yard.",
 "Scale does the work: the biggest Santa on the street.",
 "$83.96","1,000+","4.9","$149 to $169",
 [("1,000+ sold, 4.9","3256809969009521")],
 [("Pattern interrupt","We bought the 10 ft Santa. The HOA has emailed twice.","Santa towering over the garage, dad proud."),
  ("Day 1 vs now","Day 1 vs. after my husband saw the neighbour's Santa","Small yard Santa, then the 10 ft one inflating.")],
 "Older listing, big-box stores sell similar ones. Heavy to ship."),
P("Plush Smart Hand Warmer","10.jpg","known",[],[7,6,6,6,6],
 "Small rechargeable hand warmer in a soft plush cover with a temperature display.",
 "A small thinking-of-you gift for someone who is always cold. 3,000+ orders at 4.9.",
 "$10.79","3,000+","4.9","$39.99 for a 2-pack",
 [("3,000+ sold, 4.9","3256810253089535")],
 [("Gifting reaction","My girlfriend's hands are always freezing. So I got her this.","She grabs it, hugs it, refuses to give it back."),
  ("Day 1 vs now","Day 1 of winter vs. now","Blowing on cold hands at the bus stop, then holding the plush warmer.")],
 "Battery product. Heated items are already crowded in our product finder. Weakest on screen."),
]
N=len(D)
order={"niche":0,"wave":1,"early":2,"single":3,"known":4}
D.sort(key=lambda p:(order[p["fresh"]],-p["score"]))
def lno(p):
    m=max(int(k)+(2251799813685248 if k.startswith("1005") else 0) for _,k in p["links"])
    return str(m)[:11]+"…"
BETS=[
("Clip-On LED Wing Light","Dog owners who walk at night, big-dog owners first; then horse riders.","New wave growing this week, tiny to ship, $10 to $22 cost, a dark-street wow that needs no words."),
("Name-and-Face Collar Projector","Breed owners: frenchie, dachshund, golden, corgi.","Days old, custom for every dog, same night-walk video as the wing light. Unproven: sample first."),
("Tornado Vortex Lamp","Gift for him: dads, husbands, desk and nightstand.","Already $35 to $70 at the supplier, a silent wow in a dark room, 12 recent listings with about 22 orders."),
("Electric Cat Whack-a-Mole Toy","Cat owners.","About 990 orders at 4.9. The cat's reaction is the whole video. Sell as a set."),
("Car Alarm Clock With Engine Sound","Car guys and the wives who buy for them.","A gift that holds an $89 price: $40 to $57 at the supplier. The base can move to trucks and tractors."),
("Giraffe Automatic Rope Cat Teaser","Cat owners who work from home.","726 orders on two new listings. Pairs with the whack-a-mole as one set."),
("Personalised Pet Memorial Stone","People who lost a pet.","The deepest emotion on the board, custom per order, sells all year."),
("Clamp-On Desk Cat Bed","Cat owners who work from home.","The base has 1,000+ orders at 4.8; the rotating version is new. Price already near $40."),
("Hand-Crank Music Box With Your Own Song","Couples and new parents; Valentine's next.","Custom per buyer, $42 at the supplier. Needs sound, so it is harder to film."),
("Infinity Cube Lamp","Gift for him; desk and gaming room.","A small box that looks bottomless on camera. An older listing of the type has 276 orders at 4.9."),
("Pet Stairs With a Hidden Cave","Owners of old or small dogs.","An honest problem-and-solution video. 163 orders at 4.9 on two new listings."),
("Dog Tissue Box Snuffle Toy","Dog owners.","Funny to watch, about 270 orders at 4.9 on a slightly older listing. Sell as a set."),
("Christmas Magic Trail Wall Light","Christmas moms. Short window: about two weeks.","The only one with proven demand (3,000+ orders). Our Christmas hooks fit as they are."),
("Snowman Icicle Railing Light","Christmas moms with a porch. Short window.","About 15 new listings, none above 25 orders. Sold as a set of three."),
("Christmas Village Projection Centerpiece","Christmas moms. Short window.","Closest thing to the projector that made $25,817 in six days in our archive. Only the $42 to $70 version, and only after a sample.")]
def datauri(name):
    im=Image.open(os.path.join(IMG,name)).convert("RGB").resize((360,360),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,"WEBP",quality=72); return "data:image/webp;base64,"+base64.b64encode(b.getvalue()).decode()
DATE="25 Nov 2026"
FR={"niche":"Custom niche base","wave":"Fresh wave","early":"Very new, no proof yet","single":"Fresh, one seller","known":"Already known"}
FRRO={"niche":"bază de nișat custom","wave":"val nou de listări","early":"foarte nou, aproape fără comenzi","single":"listare nouă, un singur vânzător","known":"deja cunoscut"}
# ---------- markdown ----------
md=[f"# Research AliExpress — {N} de produse, mai ales de Crăciun ({DATE})\n",
"Board cu poze: https://claude.ai/artifact/8XheU6FkHoaHgTLPfzZ32N\n",
"Cifrele (preț, comenzi, rating) sunt din paginile de căutare AliExpress, 13 nov 2026. Toate produsele sunt **ipoteze** până la cifrele noastre (pilot → `rezultate`).\n",
"**Neverificat:** livrarea în SUA (cost, zile), concurența pe Instagram/TikTok (trebuie Apify, cu acord pe cost), $/1M vizualizări. „Nou” = estimare după numărul listării și câte listări noi au apărut deodată; nou pe AliExpress NU înseamnă automat nesaturat pe Instagram.\n",
"Sus: baze de nișat custom (12, rundele 4–5 din 25 nov; listate săptămâna asta sau în ultimele 2–3 săptămâni). Apoi: valuri noi (14), apoi foarte noi aproape fără comenzi (16, rundele 2–3 din 14 nov), apoi listări noi cu un singur vânzător (9), apoi deja cunoscute (8); fiecare grup după scor.\n",
"| # | Produs | Cât de nou | Scor | Preț furnizor | Comenzi | Rating | Preț propus |","|---|---|---|---|---|---|---|---|"]
for i,p in enumerate(D,1): md.append(f"| {i} | {p['n']} | {FRRO[p['fresh']]} | {p['score']}/50 | {p['cost']} | {p['sold']} | {p['rating']} | {p['sell']} |")
for i,p in enumerate(D,1):
    md.append(f"\n## {i}. {p['n']} — scor {p['score']}/50 — {FRRO[p['fresh']]}\n")
    md.append(f"Ce e: {p['what']}\n\nPotențial: {p['pot']}\n")
    md.append("Link AliExpress: "+" · ".join(f"[{t}]({U(k)})" for t,k in p['links'])+"\n")
    if p.get("niches"): md.append(f"Dovadă de custom: {p['custom']}\n\nVersiuni de nișă: {p['niches']}\n")
    for j,(f,h,v) in enumerate(p['concepts'],1): md.append(f"Concept {j} ({f}), hook EN: \"{h}\" — {v}\n")
    md.append(f"Riscuri: {p['risks']}\n")
    md.append("Scor (emoție / exagerare / reacție / fără sunet / comentarii): "+" / ".join(map(str,p['s']))+"\n")
open(OUT_MD,"w").write("\n".join(md))
# ---------- html ----------
e=html.escape
TAG={"xmas":"Christmas","pets":"Pets","val":"Valentine"}
cards=[]
for i,p in enumerate(D,1):
    tags=f'<span class="tag f-{p["fresh"]}">{FR[p["fresh"]]}</span>'+"".join(f'<span class="tag">{TAG[t]}</span>' for t in p['tags'])
    links="".join(f'<a href="{U(k)}" target="_blank" rel="noopener">{e(t)}</a>' for t,k in p['links'])
    con="".join(f'<li><span class="fam">{e(f)}</span><q>{e(h)}</q><span class="see">{e(v)}</span></li>' for f,h,v in p['concepts'])
    cards.append(f'''<article class="card" data-tags="{p['fresh']} {' '.join(p['tags'])}">
<div class="top"><img src="{datauri(p['img'])}" alt="{e(p['n'])}, supplier photo" width="360" height="360" loading="lazy">
<div class="hd"><div class="line"><span class="rank">{i}</span><div class="score"><strong>{p['score']}</strong><span>/50</span></div></div><h2>{e(p['n'])}</h2><div class="tags">{tags}</div><p class="what">{e(p['what'])}</p></div></div>
<p class="row pot"><span class="lab">Potential</span>{e(p['pot'])}</p>
<dl class="nums"><div><dt>Supplier price</dt><dd>{e(p['cost'])}</dd></div><div><dt>Orders</dt><dd>{e(p['sold'])}</dd></div><div><dt>Rating</dt><dd>{e(p['rating'])}</dd></div><div><dt>Our price</dt><dd>{e(p['sell'])}</dd></div><div><dt>Newest listing no.</dt><dd>{lno(p)}</dd></div></dl>
{('<p class="row nv"><span class="lab">Custom evidence</span>'+e(p["custom"])+'</p><p class="row nv"><span class="lab">Niche versions</span>'+e(p["niches"])+'</p>') if p.get("niches") else ''}
<div class="hooks"><span class="lab">Concept ideas</span><ol>{con}</ol></div>
<p class="row"><span class="lab">Risks</span>{e(p['risks'])}</p>
<div class="links"><span class="lab">AliExpress listings</span>{links}</div>
</article>''')
ne=sum(p['fresh']=="early" for p in D); nn=sum(p['fresh']=="niche" for p in D); nw=sum(p['fresh']=="wave" for p in D); ns=sum(p['fresh']=="single" for p in D); nk=sum(p['fresh']=="known" for p in D)
page=f'''<title>AliExpress Christmas Board</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>
/* layout: verdict header, how-to-read notes, filter chips, then a 2-column board of product cards: photo + name on top, potential, numbers, concept ideas, risks */
:root{{--bg:#f2f5f3;--surface:#ffffff;--ink:#14261f;--muted:#5a6b64;--line:#d6dfda;--pine:#1d6a4e;--berry:#b0233a;--gold:#96700f;--soft:#e7eeea;
--display:"Space Grotesk",system-ui,sans-serif;--body:"Inter",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0e1613;--surface:#16211d;--ink:#e6efea;--muted:#9aaea5;--line:#2a3a34;--pine:#5cc49a;--berry:#f0788a;--gold:#e0b84e;--soft:#1d2b26;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0e1613;--surface:#16211d;--ink:#e6efea;--muted:#9aaea5;--line:#2a3a34;--pine:#5cc49a;--berry:#f0788a;--gold:#e0b84e;--soft:#1d2b26;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.5}}
.wrap{{max-width:1240px;margin:0 auto;padding-block:28px 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:20px}}
h1{{font-family:var(--display);font-size:clamp(26px,4vw,38px);line-height:1.1;margin:0;text-wrap:balance}}
.kicker{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--berry);font-weight:600}}
.lede{{max-width:70ch;color:var(--muted);margin:0}}
.guide{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin:0;padding:0;list-style:none}}
.guide li{{background:var(--soft);border-radius:10px;padding:12px 14px;min-width:0;font-size:13.5px;color:var(--muted)}}
.guide b{{font-family:var(--display);font-size:15px;display:block;color:var(--ink)}}
.note{{border-left:3px solid var(--gold);padding:2px 0 2px 12px;color:var(--muted);font-size:13.5px;max-width:86ch;margin:0}}
.note b{{color:var(--ink)}}
.bets{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px}}
.bh{{font:700 18px/1.25 var(--display);margin:0 0 10px}}
.bets ol{{margin:0;padding-left:22px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:8px 28px}}
.bets li{{font-size:13.5px;color:var(--muted);min-width:0}} .bets li b{{display:block;color:var(--ink);font-size:14.5px}} .bets li em{{display:block;font-style:normal;color:var(--pine);font-weight:600;font-size:13px}} .bets li span{{display:block}}
.bn{{font-size:13px;color:var(--muted);margin-top:10px;max-width:86ch}}
.chips{{display:flex;flex-wrap:wrap;gap:8px}}
.chips button{{font:500 13.5px var(--body);color:var(--ink);background:transparent;border:1px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer}}
.chips button[aria-pressed="true"]{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
.chips button:focus-visible,a:focus-visible{{outline:2px solid var(--berry);outline-offset:2px}}
.board{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,500px),1fr));gap:16px;align-items:start}}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:12px;min-width:0}}
.top{{display:flex;gap:14px;align-items:flex-start}}
.top img{{width:150px;height:150px;flex:none;border-radius:8px;object-fit:cover;background:var(--soft)}}
.hd{{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}}
.line{{display:flex;justify-content:space-between;align-items:center}}
.rank{{font:700 14px var(--display);color:var(--muted);border:1px solid var(--line);border-radius:6px;min-width:28px;height:26px;display:grid;place-items:center;font-variant-numeric:tabular-nums}}
h2{{font:700 18px/1.2 var(--display);margin:0;text-wrap:balance}}
.tags{{display:flex;flex-wrap:wrap;gap:6px}}
.tag{{font-size:11.5px;font-weight:600;letter-spacing:.03em;padding:2px 8px;border-radius:4px;background:var(--soft);color:var(--muted)}}
.f-wave{{color:var(--bg);background:var(--pine)}} .f-niche{{color:var(--bg);background:var(--berry)}} .nv{{background:var(--soft);border-radius:8px;padding:8px 10px}} .f-early{{color:var(--bg);background:var(--gold)}} .f-single{{color:var(--pine)}} .f-known{{color:var(--berry)}}
.score{{white-space:nowrap;font-variant-numeric:tabular-nums}}
.score strong{{font:700 24px/1 var(--display);color:var(--gold)}} .score span{{color:var(--muted);font-size:12px}}
p{{margin:0}} .what{{color:var(--muted);font-size:13.5px}}
.lab{{display:block;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:2px}}
.row{{font-size:13.5px}} .pot{{font-size:14.5px;font-weight:500}}
.nums{{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:10px 14px;margin:0;padding:10px 0;border-block:1px solid var(--line)}}
.nums dt{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.nums dd{{margin:0;font-weight:600;font-size:13.5px;font-variant-numeric:tabular-nums}}
.hooks ol{{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}}
.fam{{display:inline-block;font-size:11.5px;font-weight:600;color:var(--pine);border:1px solid var(--line);border-radius:4px;padding:1px 7px;margin-bottom:3px}}
.hooks q{{display:block;font:500 15.5px/1.35 var(--display);quotes:"\\201C" "\\201D"}}
.see{{font-size:13px;color:var(--muted)}}
.links{{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13.5px}} .links .lab{{flex-basis:100%}}
a{{color:var(--pine);text-underline-offset:2px}}
footer{{color:var(--muted);font-size:13px;max-width:86ch}}
@media (max-width:480px){{.top img{{width:104px;height:104px}}}}
</style>
<div class="wrap">
<div><div class="kicker">Product research · AliExpress · {DATE}</div><h1>{N} new products to test</h1></div>
<p class="lede">Sorted by how new they are, then by score. Each card has the supplier photo, why it could work, and two concept ideas built on our method: a hook copied from a proven viral, then B-roll, then “Comment X for the link”. Every product is a hypothesis until our own pilot numbers come in.</p>
<ul class="guide">
<li><b>Custom niche base · {nn} products</b>Added 25 Nov. Listed this week or in the last 2 to 3 weeks, and the same item can be re-themed for a passionate group.</li>
<li><b>Fresh wave · {nw} products</b>Several sellers listed the same product in the last weeks. The best sign we have that a product is new.</li>
<li><b>Very new, no proof yet · {ne} products</b>Listed in the weeks before 14 Nov with almost no orders. Earliest, and the least proven.</li>
<li><b>Fresh, one seller · {ns} products</b>A new listing with orders, but only one seller found. Newer, less proven.</li>
<li><b>Already known · {nk} products</b>Older listings or already in US stores. Kept from the first board; expect competition.</li>
</ul>
<section class="bets"><h2 class="bh">Top 15: what I would run to reach $10k fast, and who to aim it at</h2><ol>{''.join(f'<li><b>{e(n)}</b><em>{e(ni)}</em><span>{e(t)}</span></li>' for n,ni,t in BETS)}</ol><p class="bn">Ranked the way our playbooks rank a product: a wow you can see without sound, small and light, a price above $39, a passionate group to aim at, and new on AliExpress by listing number and order count. The first twelve sell all year; the last three are Christmas and have about two weeks left. Nothing here has our own sales numbers yet, so every line is a bet.</p></section>
<p class="note"><b>Not verified yet:</b> shipping cost and delivery days to the US, and dollars per 1M views. AliExpress shows no listing date, so how new a product is comes from its listing number and its order count. Prices, orders and ratings were read from AliExpress search pages on 13, 14 and 25 Nov 2026. Listing numbers grow by about 5 million a day, so a number above 32568134650… means listed in the week of 25 Nov. Christmas items must reach buyers before Dec 25, so the selling window closes in early December; the Valentine and non-seasonal items are there for what comes after.</p>
<div class="chips" role="group" aria-label="Filter products">
<button id="f-all" data-f="" aria-pressed="true">All {N}</button><button id="f-niche" data-f="niche" aria-pressed="false">Custom niche</button><button id="f-wave" data-f="wave" aria-pressed="false">Fresh wave</button><button id="f-early" data-f="early" aria-pressed="false">Very new</button><button id="f-single" data-f="single" aria-pressed="false">Fresh, one seller</button><button id="f-known" data-f="known" aria-pressed="false">Already known</button><button id="f-xmas" data-f="xmas" aria-pressed="false">Christmas</button><button id="f-pets" data-f="pets" aria-pressed="false">Pets</button><button id="f-val" data-f="val" aria-pressed="false">Valentine</button>
</div>
<div class="board">{''.join(cards)}</div>
<footer>Score is the sum of five 0 to 10 marks: emotion in 3 seconds, can be exaggerated, filmable reaction, clear without sound, comments and shares. Exaggeration applies to the scene and the reaction, never to what the product does. Photos are the suppliers' own listing photos.</footer>
</div>
<script>
document.querySelectorAll('.chips button').forEach(b=>b.addEventListener('click',()=>{{
 document.querySelectorAll('.chips button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 const f=b.dataset.f;document.querySelectorAll('.card').forEach(c=>{{c.hidden=!!f&&!c.dataset.tags.split(' ').includes(f)}});
}}));
</script>'''
open(OUT_HTML,"w").write(page)
print(len(page)//1024,"KB",nw,ns,nk)
