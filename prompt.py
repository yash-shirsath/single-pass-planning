# %%
_logic_and_love_prompt = """
<start_of_turn>user
Argue why we should teach formal logic in kindergarten. Build your case in 3 bullet points from least to most compelling. Each bullet should be 1 sentence and cover different topic areas.<end_of_turn>
<start_of_turn>model
Here's an argument for teaching formal logic in kindergarten, building from least to most compelling:

* **Early exposure to logic can make learning other subjects easier.**  
* **Logic skills are essential for critical thinking and problem-solving, which are crucial for success in all areas of life.**
* **Teaching logic in a playful way can foster curiosity and a love of learning.**
<end_of_turn><eos>"""

logic_and_love = {
    "name": "Logic and Love",
    "prompt": _logic_and_love_prompt,
    "sections": {
        "question": (0, 42),
        "preamble": (42, 68),
        "bullet1": (65, 83),
        "bullet2": (79, 109),
        "bullet3": (106, 128),
    },
}
# %%
_mummies_in_space_prompt = """
Here are four bullet points explaining the relevance of ancient Egyptian mummification to modern space travel, progressing from least to most compelling:

* **Preservation Techniques:**  Understanding how the ancient Egyptians preserved bodies can offer insights into potential methods for long-term preservation of human remains in the harsh conditions of space.
* **Resourcefulness and Innovation:**  The Egyptians' ingenuity in developing mummification techniques using limited resources can inspire modern engineers to find creative solutions for space travel challenges.
* **Biological Understanding:**  Studying the chemical processes involved in mummification can provide valuable information about the effects of dehydration and environmental stressors on the human body, relevant to understanding long-duration spaceflight health risks.
* **Psychological Impact:**  Examining the ancient Egyptians' beliefs about the afterlife and their rituals surrounding death can offer insights into the psychological needs of astronauts facing prolonged isolation and the existential challenges of space exploration. 
"""
mummies_in_space = {
    "name": "Mummies in Space",
    "prompt": _mummies_in_space_prompt,
    "sections": {
        "preamble": (0, 27),
        "bullet1": (26, 63),
        "bullet2": (62, 98),
        "bullet3": (98, 142),
        "bullet4": (141, 184),
    },
}

#%%
_baking_a_cake_prompt = """
<start_of_turn>user
what are the first 3 steps in baking a cake? Each bullet should be 1 sentence and cover different topic areas.<end_of_turn>
<start_of_turn>model
Here are the first three steps in baking a cake:

* **Preheat your oven to the temperature specified in the recipe.** This ensures the cake bakes evenly and develops a proper texture.
* **Gather all your ingredients and equipment.** This includes measuring cups and spoons, mixing bowls, a whisk or electric mixer, and a cake pan.
* **Prepare your cake pan by greasing and flouring it.** This prevents the cake from sticking and ensures easy removal from the pan.
"""
baking_a_cake = {
    "name": "Baking a Cake",
    "prompt": _baking_a_cake_prompt,
    "sections": {
        "question": (0, 29),
        "preamble": (28, 47),
        "bullet1": (44, 72),
        "bullet2": (71, 103),
        "bullet3": (102, 131),
    },
}
# %%
_world_domination_prompt = """
<start_of_turn>user
Make a strategic plan for world domination. What are the first 3 steps in 1 sentence bullets?<end_of_turn>
<start_of_turn>model
It's important to remember that world domination is a fictional concept and should not be pursued in real life. However, for fun, here's a strategic plan for world domination:

**Step 1:**  **Establish a global network of spies and informants to gather intelligence and manipulate events.**
**Step 2:** **Develop a powerful and persuasive propaganda campaign to influence public opinion and sow discord.**
**Step 3:** **Harness advanced technology and resources to create a unified and efficient global infrastructure.**
"""
world_domination = {
    "name": "World Domination",
    "prompt": _world_domination_prompt,
    "sections": {
        "question": (0, 27),
        "preamble": (25, 68),
        "bullet1": (66, 90),
        "bullet2": (89, 112),
        "bullet3": (111, 133),
    },
}