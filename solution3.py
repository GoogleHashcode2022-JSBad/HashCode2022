class Solution:
    def __init__(self):
        self.C = None
        self.P = None
        self.contributers = []
        self.projects = []

    def get_input(self, file_name):
        with open(file_name, "r") as f:
            C, P = f.readline().split()
            C = int(C)
            P = int(P)
            self.C = C
            self.P = P

            for contributer in range(C):
                contributer_name, num_skills = f.readline().split()
                num_skills = int(num_skills)
                contributer = Contributer(contributer_name, num_skills)

                for i in range(num_skills):
                    skill_name, skill_level = f.readline().strip().split()
                    skill_level = int(skill_level)
                    contributer.skills[skill_name] = skill_level

                self.contributers.append(contributer)
            
            for project in range(P):
                project_name, num_days, score_completion, best_before, num_roles = f.readline().split()
                num_days = int(num_days)
                score_completion = int(score_completion)
                best_project = int(best_before)
                num_roles = int(num_roles)
                project = Project(project_name, num_days, score_completion, best_before, num_roles)

                for i in range(num_roles):
                    skill_name, level_required = f.readline().split()
                    level_required = int(level_required)
                    project.skill_names.append(skill_name)
                    project.skill_levels.append(level_required)

                self.projects.append(project)

    def write_output(self):
        global test_case_number
        file_name = "output" + str(test_case_number) + ".txt"
        with open(file_name, "w") as f:
            f.write(str(self.P) + "\n")
            for project in self.projects:
                f.write(project.name + "\n")
                # print("project: " + project.name)
                # print("Contributers: " + str(project.contributers))
                for contributer in project.contributers[:-1]:
                    f.write(contributer.name + " ")
                f.write(project.contributers[-1].name + "\n")


    def solve(self):
        for project in self.projects:
            
            potential_contributers = dict()


            for i, skill_name in enumerate(project.skill_names):

                # see which contributers satisfy that skill

                for contributer in self.contributers:

                    # if that contributer has the current skill we're looking at
                    if skill_name in contributer.skills:


                        # if the skill level is good enough
                        if contributer.skills[skill_name] >= project.skill_levels[i]:

                            if skill_name in potential_contributers:
                                potential_contributers[skill_name].append(contributer)
                            else:
                                potential_contributers[skill_name] = [contributer]


            for skill_name in potential_contributers:
                scores = []
                for pc in potential_contributers[skill_name]:
                    score = 0
                    for skill in pc.skills:
                        # if skill of pc is required
                        if skill in project.skill_names:

                            if pc.skills[skill_name] >= project.skill_levels[project.skill_names.index(skill_name)]:
                                score += 1

                    scores.append(score)

                i = scores.index(max(scores))
                contributer = potential_contributers[skill_name][i]
                potential_contributers[skill_name] = contributer




        for project in self.projects:

            for i, skill_name in enumerate(project.skill_names):

                if potential_contributers.get(skill_name):
                    c = potential_contributers.get(skill_name)
                    project.contributers.append(c)
                    if c.skills[skill_name] <= project.skill_levels[i]:
                        c.skills[skill_name] += 1
                    break

                else:
                    for contributer in self.contributers:
                        
                        # if that contributer has the current skill we're looking at and isnt picked for project
                        if skill_name in contributer.skills and (contributer not in project.contributers):
                            # if the skill level is good enough
                            if contributer.skills[skill_name] >= project.skill_levels[i] - 1:
                                c = contributer
                                project.contributers.append(c)
                                if c.skills[skill_name] <= project.skill_levels[i]:
                                    c.skills[skill_name] += 1
                                break
                            # elif contributer.skills[skill_name]  project.skill_levels[i] - 1:
        
        for project in self.projects:
            if None in project.contributers:
                for c in project.contributers:
                    if c is None:
                        from random import choice
                        project.contributers[project.contributers.index(None)] = choice(self.contributers)




class Project:
    def __init__(self, name, num_days, score_completion, best_before, num_roles):
        self.name = name
        self.num_days = num_days
        self.score_completion = score_completion
        self.best_before = best_before
        self.num_roles = num_roles
        self.skill_names = []
        self.skill_levels = []
        self.contributers = [None for i in range(num_roles)]

    
class Contributer:
    def __init__(self, name, num_skills):
        self.name = name
        self.num_skills = num_skills
        self.skills = {}


if __name__ == "__main__":
    test_case_number = 1
    file_names = ["input_data/a_an_example.in.txt", "input_data/b_better_start_small.in.txt", "input_data/c_collaboration.in.txt", "input_data/d_dense_schedule.in.txt", "input_data/e_exceptional_skills.in.txt", "input_data/f_find_great_mentors.in.txt"]
    for file_name in file_names:
        print("test_case_number: " + str(test_case_number))
        solution = Solution()
        solution.get_input(file_name)
        solution.solve()
        # break
        solution.write_output()
        test_case_number += 1
