# Prompt Engineering Process

My first attempt was just to copy and paste most of what was in the demo_agent file. The main changes that I made was the system context, and I altered the names to Player and DM instead of user and assistant. New context: 'You are a dungeon master. Present the user with fantasy scenarios and give them opurtunities to succeed or fail depending on their actions.'

For my second attempt, I wanted to see what impacts changing temperature and max_tokens would have so I changed their values to 0.34 and 50, repectively.

On my third attempt, I wanted the player to be able to fail in whatever action they choose. Instead of using dice rolls like normal DnD, I want the AI to use its own judgement about whether the action will fail or not. Also, I like that the AI gives players a set of potential actions at the end of its responses, but I want the player to know that they still have the ability to make custom typed-out chocies.
    I gave the AI a character who is a knight learning a new weapon to test if it would allow me to mess up.

My fourth attempt was focused on changing how the AI handles dialouge. I didn't like how the AI would put words in the player's mouth by answering for them in order to continue conversations. So I want to make sure the AI stops whenever the player's character needs to say something in order to give the player an oppurtunity to respond.
    I decided to give the AI a court scene prompt becuase there will be a lot of talking.