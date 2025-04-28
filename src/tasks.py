from textwrap import dedent
from crewai import Task

class ProjectPlanningTask():
    def project_planning_task(self, agent, project_requirements, project_goals):
        return Task(
            description=dedent(f"""
            Develop a structured project plan by analyzing requirements, defining key features, 
            and outlining milestones. Identify dependencies and estimate timelines to ensure an 
            efficient workflow. The plan should be clear, actionable, and aligned with the project goals.

            Project Requirements: {project_requirements}
            Project Goals: {project_goals}

            The planning should include:
            - A **list of core features** required in the project.
            - A **detailed breakdown of tasks** and their dependencies.
            - A **timeline with estimated completion dates** for each milestone.
            - A **technology stack recommendation** based on project needs.
            - A **list of potential risks** and mitigation strategies.
            """),
            expected_output=dedent(f"""
            A well-structured project plan containing:
            - A **documented list of features** with descriptions.
            - A **workflow breakdown** outlining individual tasks and dependencies.
            - A **roadmap with milestone deadlines** and expected completion times.
            - A **recommended technology stack** suitable for implementation.
            - A **risk analysis report** highlighting potential challenges and solutions.
            """),
            agent=agent,
            async_execution=True
        )
   
    def planning_task(self, agent, project_requirements, project_goals):
        return Task(
            description=dedent(f"""
            Develop a structured project plan by analyzing requirements, defining key features, 
            and outlining milestones. Identify dependencies and estimate timelines to ensure an 
            efficient workflow. The plan should be clear, actionable, and aligned with the project goals.

            Project Requirements: {project_requirements}
            Project Goals: {project_goals}

            The planning should include:
            - A **list of core features** required in the project.
            - A **detailed breakdown of tasks** and their dependencies.
            - A **timeline with estimated completion dates** for each milestone.
            - A **technology stack recommendation** based on project needs.
            - A **list of potential risks** and mitigation strategies.
            """),
            expected_output=dedent(f"""
            A well-structured project plan containing:
            - A **documented list of features** with descriptions.
            - A **workflow breakdown** outlining individual tasks and dependencies.
            - A **roadmap with milestone deadlines** and expected completion times.
            - A **recommended technology stack** suitable for implementation.
            - A **risk analysis report** highlighting potential challenges and solutions.
            """),
            agent=agent,
        )

    def tech_selection_task(self, agent, project_plan):
        return Task(
            description=dedent(f"""
            Analyze the project plan and recommend the best technology stack based on project 
            requirements, scalability, and efficiency.

            Project Plan: {project_plan}

            The technology selection should include:
            - **Programming languages** best suited for the project.
            - **Frameworks and libraries** needed for front-end, back-end, and data management.
            - **Database selection** based on storage needs and access patterns.
            - **Deployment and DevOps tools** for CI/CD and scalability.
            """),
            expected_output=dedent(f"""
            A comprehensive technology stack report, including:
            - A **list of selected programming languages** with justification.
            - Recommended **frameworks and libraries**.
            - Database selection with reasoning.
            - Proposed DevOps and deployment strategy.
            """),
            agent=agent,
        )

    def architecture_task(self, agent, project_plan, tech_stack):
        return Task(
            description=dedent(f"""
            Design the system architecture by defining key components, modules, and their 
            interactions. Ensure scalability, security, and performance.

            Project Plan: {project_plan}
            Technology Stack: {tech_stack}

            The system architecture should include:
            - **High-level architectural diagram** showcasing components.
            - **Module breakdown** with responsibilities.
            - **Communication and data flow** between services.
            - **Security measures** and best practices.
            """),
            expected_output=dedent(f"""
            A well-defined system architecture including:
            - A **detailed architecture diagram**.
            - Breakdown of key modules and their interactions.
            - A **documented data flow model**.
            - Security guidelines and best practices.
            """),
            agent=agent,
        )

    def database_design_task(self, agent, system_architecture):
        return Task(
            description=dedent(f"""
            Design an optimized database schema based on the system architecture, 
            ensuring efficiency and scalability.

            System Architecture: {system_architecture}

            The database design should include:
            - **Entity-relationship model** for database structure.
            - **Table definitions** with primary and foreign keys.
            - **Indexing and optimization techniques** for performance.
            - **Backup and recovery strategies**.
            """),
            expected_output=dedent(f"""
            A well-structured database design with:
            - A **detailed ER diagram**.
            - Table schemas with relationships.
            - Optimization techniques for performance.
            - A documented backup and recovery plan.
            """),
            agent=agent,
        )

    def ui_ux_design_task(self, agent, project_plan):
        return Task(
            description=dedent(f"""
            Create wireframes and user interface designs to ensure a seamless user experience.

            Project Plan: {project_plan}

            The UI/UX design should include:
            - **Wireframes** for key screens.
            - **User experience flow** and navigation design.
            - **Color schemes and typography recommendations**.
            - **Accessibility considerations**.
            """),
            expected_output=dedent(f"""
            A complete UI/UX design package including:
            - Wireframes for key screens.
            - User journey flow and navigation structure.
            - Design system with colors and typography.
            - Accessibility guidelines.
            """),
            agent=agent,
        )

    def coding_task(self, agent, system_architecture, database_schema, ui_design):
        return Task(
            description=dedent(f"""
            Implement the project by writing clean, modular, and maintainable code 
            based on the system architecture and UI designs.

            System Architecture: {system_architecture}
            Database Schema: {database_schema}
            UI Design: {ui_design}

            The implementation should include:
            - **Backend development** with API endpoints.
            - **Frontend development** following the UI design.
            - **Integration of database** with backend services.
            - **Unit tests** to ensure code reliability.
            """),
            expected_output=dedent(f"""
            A functional software application with:
            - Complete backend and frontend implementation.
            - Well-structured codebase following best practices.
            - Integrated database connections.
            - A set of unit tests for validation.
            """),
            agent=agent,
        )

    def debugging_task(self, agent, codebase):
        return Task(
            description=dedent(f"""
            Analyze and debug the code to identify performance bottlenecks, 
            fix bugs, and optimize execution.

            Codebase: {codebase}

            The debugging should include:
            - **Bug identification and resolution**.
            - **Performance optimizations** for efficiency.
            - **Code refactoring** for maintainability.
            - **Security vulnerability checks**.
            """),
            expected_output=dedent(f"""
            An optimized and bug-free codebase with:
            - Resolved bugs and improved performance.
            - Cleaner, refactored code for maintainability.
            - Security vulnerabilities addressed.
            """),
            agent=agent,
        )

    def deployment_task(self, agent, codebase):
        return Task(
            description=dedent(f"""
            Deploy the application to a production environment, ensuring minimal downtime.

            Codebase: {codebase}

            The deployment should include:
            - **Setup of hosting and servers**.
            - **CI/CD pipeline configuration**.
            - **Performance monitoring tools**.
            - **Rollback and backup strategy**.
            """),
            expected_output=dedent(f"""
            A deployed application with:
            - Hosting and server configuration.
            - Automated CI/CD pipelines.
            - Active monitoring and logging tools.
            - A rollback plan in case of failures.
            """),
            agent=agent,
        )

    def documentation_task(self, agent, system_architecture, codebase):
        return Task(
            description=dedent(f"""
            Write detailed technical documentation covering system design, APIs, 
            and deployment procedures.

            System Architecture: {system_architecture}
            Codebase: {codebase}

            The documentation should include:
            - **System overview and architecture description**.
            - **API documentation** with usage examples.
            - **Deployment and setup instructions**.
            - **User manual for ease of understanding**.
            """),
            expected_output=dedent(f"""
            A well-documented project with:
            - System overview and architecture breakdown.
            - API documentation with endpoints and responses.
            - Deployment and setup guide.
            - User manual and FAQs.
            """),
            agent=agent,
        )
