from crewai import Crew
from agents import (
    project_planner_agent,
    tech_stack_selector_agent,
    software_architect_agent,
    database_designer_agent
)
from tasks import ProjectPlanningTask
from llm_wrapper import CrewAIOllamaWrapper  # Use the patched wrapper

# Initialize LLM with `.call()` and stop-word compatibility
llm = CrewAIOllamaWrapper(model="codellama", verbose=True)

# Step 2: Get User Input
def multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)

project_idea = multiline_input("💡 What project do you want to build? (Press Enter twice to finish)")
project_goal = multiline_input("🎯 What's your main goal? (Press Enter twice to finish)")


# Step 3: Inject LLM into Agents
planner = project_planner_agent(); planner.llm = llm
tech_selector = tech_stack_selector_agent(); tech_selector.llm = llm
architect = software_architect_agent(); architect.llm = llm
db_designer = database_designer_agent(); db_designer.llm = llm

# Step 4: Create Tasks
tasks = ProjectPlanningTask()
planning_task = tasks.planning_task(planner, project_idea, project_goal)
tech_task = tasks.tech_selection_task(tech_selector, f"Based on project idea: {project_idea}")
arch_task = tasks.architecture_task(architect, f"Based on: {project_idea}", f"Based on: codellama stack")
db_task = tasks.database_design_task(db_designer, f"Based on: previous architecture")

# Step 5: Crew Setup
crew = Crew(
    agents=[planner, tech_selector, architect, db_designer],
    tasks=[planning_task, tech_task, arch_task, db_task],
    verbose=True
)

# Step 6: Run Crew (this is what triggers `.run()` on tasks internally)
result = crew.kickoff()

# Step 7: Print Final Result
print("\n🚀 Final Result from all tasks:\n")
print(result)
