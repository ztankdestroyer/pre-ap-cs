print("MAD LIB GAME")
print("Enter answers to the following prompts\n")

noun1 = input("Any noun ")
noun2 = input("Any noun ")
noun3 = input("Any noun ")
occupation = input("An occupation ")
verb = input("Any verb ")
place = input("Place ")
verb1 = input("Verb ending in ed ")	
noun4 = input("Any noun ")
verb2 = input("Verb ending in ING ")	
noun5 = input("A plural noun ")	
noun6 = input("Any noun ")
emotion = input("Any emotion ")

story = "It was during the battle of NOUN1 when I was running through a \n" +\
        "NOUN2 when a NOUN3 went off right next to my \n" +\
        "platoon. Our OCCUPATION yelled for us to VERB to \n" +\
        "the nearest PLACE we could find. When we got to the \n" +\
        "PLACE we VERB1 to start a fire. As we were starting the fire \n"+\
        "the enemy saw the NOUN4 from the fire and started \n" +\
        "VERB2 NOUN5 at us. we all quickly ducked behind the \n" +\
        "NOUN6 at the PLACE and returned fire. we quickly \n" +\
        "eliminated the enemy and were EMOTION that we had won the battle."

story = story.replace("NOUN1", noun1)
story = story.replace("NOUN2", noun2)
story = story.replace("NOUN3", noun3)
story = story.replace("NOUN4", noun4)
story = story.replace("OCCUPATION", occupation)
story = story.replace("VERB", verb)
story = story.replace("PLACE", place)
story = story.replace("VERB1", verb1)
story = story.replace("VERB2", verb2)
story = story.replace("NOUN5", noun5)
story = story.replace("NOUN6", noun6)
story = story.replace("EMOTION", emotion)
print(story)