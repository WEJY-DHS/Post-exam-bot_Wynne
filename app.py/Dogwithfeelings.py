print("Welcome to #TheDogWithFeelings! I am Bumble, here and ready to help you :D")
print()
while True:
  description = input("Could you describe how you feel in a sentence, hooman? (Honestly though, I only understand a few feelings. Oops!)")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append(". Ah yes, hoomans do indeed face a lot of challenges in life. Although I do not understand what it is like, I can imagine how taxing it is on oneself. However, do remember that tomorrow will be a better day and to count your blessings. All the best! Hope you are feeling better now! ;)")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy" or "joyful")
      encouragement_list.append(". Yes, that's the spirit! I'm super glad that you are feeling this way, hooman. I do not know you, but I wish for your happiness to continue on. Do be sure to keep smiling!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired" or "exhausted")
      encouragement_list.append(". I understand how you feel hooman. I feel tired ALL the time (or maybe I am just lazy hehe.) Anyways, do remember to take care of yourself I'm sure that you have a reason for feeling this way. Despite all the challenges you are facing, do not forget that you are stronger than you think. Wishing you all the best! (Hope you get many yummy treats as a reward once this is all over.)")
      counter += 1
    if each_word == "curious":
      feelings_list.append("curious")
      encouragement_list.append(". Ah yes, many hoomans ask me this question. How did I manage to sneak up on to this computer, you say? Well, it all started when my hooman left me by myself in my home all alone. You see, I was feeling bored and so I... Oh! I'm not supposed to tell you this. My owner will punish me with the 'Ground'. (She doesn't take me out for walks when that happens.)")
      counter += 1
    if each_word == "nervous" or "anxious":
      feelings_list.append("nervous")
      encouragement_list.append(". Meow? Oh, Bumble's having a meal now...I guess I'll step in! By the way, I'm Moo the cat! I don't really feel nervous often but my friend Fancy does. She thinks hoomans are unpredictable! Anyways, I always tell her that once she faces the hoomans she'll realise that there's nothing to be nervous about!)")
      counter += 1    
    if each_word == "neutral":
      feelings_list.append("neutral")
      encouragement_list.append("...Meow? Umm, Bumble's asleep now, so I, Tiger, will attend to you. So...umm...I feel neutral a lot. I just like staring into the distance and watching the hoomans pass by. I guess you could, umm, smile more so you can turn that neutrality into joy!)")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. You see, hooman language isn't my expertise so I'm still learning :( Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
