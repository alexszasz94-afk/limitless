import sys
robe, v = sys.argv[1], sys.argv[2]
P = robe == "princess"
head = ("Edit the input video. Keep {ex} the same {n} shots, the same cuts, the same camera position and framing, the same body movements and the same timing as the input video, second by second; the output has exactly the same length as the input. Change only the person, the room, the robe, the cable connector and the remote. "
        "PERSON: exactly the woman of Image 1, same face and hair; under the robe she wears {outfit}, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2{sd}; {roomnote}. ")
robe_p = "ROBE: the hooded robe of Image 3 (front) and Image 4 (back): REPRODUCE IT ONE TO ONE from Images 3-4 in every frame, every colour, every trim, the white sherpa lining and the hood with its tiara. The foot pockets are exactly like Image 5 and Image 6."
robe_s = "ROBE: exactly the robe of Images 3-6, REPRODUCE IT ONE TO ONE in every frame: the same fabric, colours, embroidered motifs, white fluffy sherpa lining and white fluffy trims as Images 3-6. HOOD: exactly Image 6 (front) and Image 5 (back), a real 3D sewn hood."
back_img = "Image 4" if P else "Image 5"
hoodup = "the blue hood with its gold tiara exactly like Images 3-4" if P else "the dog-face hood exactly like Image 6"
pockets_p = 'THE HEM COVERS HER FEET AT ALL TIMES: the robe is extra long, its white hem lies flat on the floor all around her and touches the floor, there is NO gap between the hem and the floor, so her feet are always hidden behind the hem and inside the pockets - never visible on the floor, before, during and after she steps in, also when the robe is still closed. She slides each foot from behind the hem straight down into its pocket, so the pocket fills up and rests full on the floor; only the yellow fabric and the white fluffy band are seen on the floor, never a sock, a foot or a heel. FEET STAY IN THE POCKETS UNTIL THE END: once both feet are inside the foot pockets they never come out again.'
pockets_s = ("THE FOOT POUCH: one wide pouch across the whole width at the inside of the hem, open only at the top, the robe fabric outside, white fluffy trim on top. Both her feet start OUTSIDE the pouch on the floor; she lifts her right foot over the white top edge into the right half of the pouch, then her left foot over the top edge into the left half; no foot is ever inside before she puts it in, and once a foot is in it never comes out again; the filled pouch rests on the floor with her feet inside it.")
pocket_word = ("a foot pocket", "the other foot pocket") if P else ("the foot pouch", "the pouch")
conn = ("SHOT {k} ({a} to {b} s): extreme close-up of her two hands in front of the robe fabric: one hand holds one half of OUR cable connector and pushes it into the other half until it is fully joined, no gap. The connector is EXACTLY the one of Image 7, reproduced one to one: the same {c} colour, the same shape of the two halves, the same ribs and the same {c} cable. Never a white plug.")
rem_p = "pink, the gold and crystal crown on top, the numbers 5, 4, 3, 2, 1 from top to bottom with a small crystal light next to each, the round pearl button at the bottom. Her thumb presses the round button and the light next to 1 glows pink"
rem_s = "a white oval remote with the numbers 5, 4, 3, 2, 1 from top to bottom with a small dot light next to each and a round grey button at the bottom. Her thumb presses the round button and the light next to 1 glows green"
remote = ("SHOT {k} ({a} to {b} s): close-up of her hand holding OUR remote against the robe fabric, EXACTLY the remote of Image 8 reproduced one to one: " + (rem_p if P else rem_s) +
          " and stays on, then only the light next to 2, then only 3, one light at a time going up; each light stays steadily on until the next one comes, never blinking, never two lights at once. No digital screen, no digits display, no other remote.")
legs = "her legs are completely covered by the closed robe down to the feet" + (", the hem closed over them" if P else "") + "; no pajama pants, no knee and no foot visible"
front = ("SHOT {k} ({a} to {b} s{jc}): full body, she stands on the floor in the FOREGROUND facing the camera, nothing between her and the camera, the hood DOWN on her back in this and every following shot, her whole face visible. Exactly like the input: {act} " + (pockets_p if P else pockets_s))
outfit = "a <colour> long pajama set" if P else "<outfit, long pajamas or long lounge pants, e.g. red buffalo-plaid long pajamas>"
if v == "3":
    S = [f"SHOT 1 (0 to 1.0 s): close, seen from behind, the robe is already on her shoulders and she settles it, the hood hangs down on her back exactly like {back_img}; her face is not seen.",
         front.format(k=2, a="1.0", b="6.7", jc=", with the same small jump cuts at 2.0 s and 3.9 s", act=f"the robe is closed, she opens one side and holds it out, she {'slides one foot down behind the hem into' if P else 'lifts one foot into'} {pocket_word[0]}, then she holds the robe wide open with both arms showing the white {'sherpa ' if P else ''}lining, she {'slides the other foot down behind the hem into' if P else 'lifts the other foot into'} {pocket_word[1]}, then she wraps the robe closed and stands wrapped in it."),
         conn.format(k=3, a="6.7", b="7.5", c="lilac" if P else "grey"), remote.format(k=4, a="7.5", b="10.0"),
         f"SHOT 5 (10.0 to 12.0 s): she sits on the sofa of Image 2, wrapped in the closed robe, hood down, and pulls the white {'sherpa' if P else 'fluffy'} collar up to her face, smiling; " + legs + "."]
    roomnote = "the last shot is on its sofa"
elif v == "4":
    S = [f"SHOT 1 (0 to 1.7 s): close, seen from behind, the robe is already on her shoulders, she lifts the hood with both hands and pulls it up over her head, then we see the back of the hood up on her head exactly like {back_img}; her face is not seen.",
         front.format(k=2, a="1.7", b="5.8", jc="", act=f"the robe is open, she holds one side out and {'slides one foot down behind the hem into' if P else 'lifts one foot into'} {pocket_word[0]}, then she holds the robe wide open with both arms showing the white {'sherpa ' if P else ''}lining, she {'slides the other foot down behind the hem into' if P else 'lifts the other foot into'} {pocket_word[1]}, then she wraps the robe closed and stands wrapped in it."),
         conn.format(k=3, a="5.8", b="7.3", c="lilac" if P else "grey"), remote.format(k=4, a="7.3", b="9.3"),
         f"SHOT 5 (9.3 to 12.0 s): she sits on the sofa of Image 2, wrapped in the closed robe, hood down, and pulls the white {'sherpa' if P else 'fluffy'} collar up to her face with both hands and closes her eyes, smiling; " + legs + "."]
    roomnote = "the last shot is on its sofa"
else:
    S = [f"SHOT 1 (0 to 1.8 s, with the same small jump cut at 1.0 s): close, from the side, she slides her arm into the long sleeve of the robe and pulls the robe onto her shoulder; her face is mostly out of the frame.",
         f"SHOT 2 (1.8 to 2.5 s): close, seen from behind, the robe is on her shoulders, the hood hangs down on her back exactly like {back_img}.",
         f"SHOT 3 (2.5 to 4.2 s): she lies stretched out on her back on the sofa of Image 2, her head on a cushion, relaxed, wrapped in the closed robe, hood down, her face visible; " + legs + ".",
         conn.format(k=4, a="4.2", b="5.0", c="lilac" if P else "grey"), remote.format(k=5, a="5.0", b="7.1"),
         f"SHOT 6 (7.1 to 9.1 s): she lies curled up on her side on the sofa of Image 2, completely wrapped in the closed robe, the hood UP on her head ({hoodup}), eyes closed, cozy; " + legs + ".",
         f"SHOT 7 (9.1 to 11.0 s): she sits on the sofa of Image 2 facing the camera, wrapped in the closed robe, and pulls the hood up over her head with both hands ({hoodup}), then holds the collar closed under her chin; " + legs + "."]
    roomnote = "the lying shots and the last shot are on its sofa"
n = {"3": "five", "4": "five", "5": "seven"}[v]
tail = open("tail.txt").read().strip()
print(head.format(ex="exactly" if P else "EXACTLY", sd="" if P else ", soft daylight", n=n, outfit=outfit, roomnote=roomnote) + (robe_p if P else robe_s) + "\n" + "\n".join(S) + "\n" + tail)
