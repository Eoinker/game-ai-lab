# Prompt Engineering Process

My first attempt was just to copy and paste most of what was in the demo_agent file. The main changes that I made was the system context, and I altered the names to Player and DM instead of user and assistant. New context: 'You are a dungeon master. Present the user with fantasy scenarios and give them opurtunities to succeed or fail depending on their actions.'

For my second attempt, I wanted to see what impacts changing temperature and max_tokens would have so I changed their values to 0.34 and 50, repectively.

On my third attempt, I wanted the player to be able to fail in whatever action they choose. Instead of using dice rolls like normal DnD, I want the AI to use its own judgement about whether the action will fail or not. Also, I like that the AI gives players a set of potential actions at the end of its responses, but I want the player to know that they still have the ability to make custom typed-out chocies,